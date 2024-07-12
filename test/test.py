import os
import sys

# モジュールのインポートのためにパスを追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import calculate_plagiarism_score

# テストに使うjava_fileたちを取得
def get_java_files(root):
    java_files = {} # テストに使うjava_fileたちを格納する辞書型変数
    for dir, _, files in os.walk(root):
        for file in files:
            if file.endswith('.java'):
                path_parts = dir.split('/')
                case_num = -1
                file_type = ''

                for part in path_parts:
                    if part.startswith('case-'): # ディレクトリ名が'case-1', 'case-2', ...の形式であることを仮定
                        case_num = int(part[5:])
                    elif part in ['non-plagiarized', 'original', 'plagiarized']: # ファイルが'non-plagiarized', 'original', 'plagiarized'のどれかのディレクトリにあることを仮定
                        file_type = part

                # ディレクトリに対する仮定が違ったらエラーを出力
                if case_num == -1 or file_type == '':
                    print('error occured')

                # java_fileを辞書型変数に格納
                if case_num not in java_files:
                    java_files[case_num] = {'non-plagiarized': [], 'original': [], 'plagiarized': []}
                
                with open(os.path.join(dir, file), 'r') as f:
                    java_files[case_num][file_type].append(f.read())

    return java_files

# テストを実行
def do_test(java_files):
    file_num = 0 # テストに使うファイルの数(original除く)
    wrong_count = 0 # 間違った結果の数
    for case_num in java_files:
        assert(len(java_files[case_num]['original']) == 1)
        original = java_files[case_num]['original'][0]

        # originalとplagiarizedの組み合わせに対してテスト
        for plagiarized in java_files[case_num]['plagiarized']:
            score = calculate_plagiarism_score(original, plagiarized)
            print(f'Plagiarized Case {case_num}: {score}%')
            if score < 40: # 剽窃スコア40%未満の場合はエラーを出力
                print('[ERROR]: Plagiaried score is less than 40%')
                wrong_count += 1
            file_num += 1
        
        # originalとnon-plagiarizedの組み合わせに対してテスト
        for non_plagiarized in java_files[case_num]['non-plagiarized']:
            score = calculate_plagiarism_score(original, non_plagiarized)
            print(f'Non-Plagiarized Case {case_num}: {score}%')
            if score >= 40: # 剽窃スコア40%以上の場合はエラーを出力
                print('[ERROR]: Non-Plagiarized score is greater than or equal to 40%')
                wrong_count += 1
            file_num += 1
    
    # テスト結果を出力
    print(f'Number of files tested: {file_num}')
    print(f'Number of wrong results: {wrong_count}')
    print(f'Accuracy: {(file_num - wrong_count) / file_num * 100}%')

# テスト結果をoutput.txtに出力(任意に変更可能)
output_file = 'output.txt'

with open('output.txt', 'w') as f:
    sys.stdout = f # 標準出力先をoutput.txtに変更

    root = './IR-Plag-Dataset' # テストに使うデータセットのルートディレクトリ
    java_files = get_java_files(root)
    do_test(java_files)

sys.stdout = sys.__stdout__
