import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from aif360.datasets import BinaryLabelDataset
from aif360.metrics import BinaryLabelDatasetMetric
from aif360.algorithms.preprocessing import Reweighing

class EthicalAIValidator:
    def __init__(self):
        self.scaler = StandardScaler()
        self.reweighing = Reweighing('AGE', unprivileged_groups=[{'AGE': 0}], privileged_groups=[{'AGE': 1}])

    def preprocess_data(self, X, y, sensitive_feature):
        X_scaled = self.scaler.fit_transform(X)
        dataset = BinaryLabelDataset(df=np.column_stack((X_scaled, sensitive_feature)), 
                                     label_names=['outcome'], 
                                     protected_attribute_names=['AGE'])
        return dataset

    def measure_bias(self, dataset):
        metric = BinaryLabelDatasetMetric(dataset, unprivileged_groups=[{'AGE': 0}], privileged_groups=[{'AGE': 1}])
        print(f"Disparate Impact: {metric.disparate_impact()}")
        print(f"Statistical Parity Difference: {metric.statistical_parity_difference()}")

    def mitigate_bias(self, dataset):
        return self.reweighing.fit_transform(dataset)

    def validate_and_mitigate(self, X, y, sensitive_feature):
        dataset = self.preprocess_data(X, y, sensitive_feature)
        print("Before mitigation:")
        self.measure_bias(dataset)
        
        mitigated_dataset = self.mitigate_bias(dataset)
        print("\nAfter mitigation:")
        self.measure_bias(mitigated_dataset)
        
        return mitigated_dataset