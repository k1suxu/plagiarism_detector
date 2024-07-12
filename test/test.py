import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import calculate_plagiarism_score

def get_java_files(root):
    java_files = {}
    for dir, _, files in os.walk(root):
        for file in files:
            if file.endswith('.java'):
                path_parts = dir.split('/')
                case_num = -1
                file_type = ''

                for part in path_parts:
                    if part.startswith('case-'):
                        case_num = int(part[5:])
                    elif part in ['non-plagiarized', 'original', 'plagiarized']:
                        file_type = part

                if case_num == -1 or file_type == '':
                    print('error occured')

                if case_num not in java_files:
                    java_files[case_num] = {'non-plagiarized': [], 'original': [], 'plagiarized': []}
                
                with open(os.path.join(dir, file), 'r') as f:
                    java_files[case_num][file_type].append(f.read())

    return java_files

def do_test(java_files):
    file_num = 0
    wrong_count = 0
    for case_num in java_files:
        assert(len(java_files[case_num]['original']) == 1)
        original = java_files[case_num]['original'][0]

        for plagiarized in java_files[case_num]['plagiarized']:
            score = calculate_plagiarism_score(original, plagiarized)
            print(f'Plagiarized Case {case_num}: {score}%')
            if score < 40:
                print('[ERROR]: Plagiaried score is less than 40%')
                wrong_count += 1
            file_num += 1
        
        for non_plagiarized in java_files[case_num]['non-plagiarized']:
            score = calculate_plagiarism_score(original, non_plagiarized)
            print(f'Non-Plagiarized Case {case_num}: {score}%')
            if score >= 40:
                print('[ERROR]: Non-Plagiarized score is greater than or equal to 40%')
                wrong_count += 1
            file_num += 1
    
    print(wrong_count, file_num, (file_num-wrong_count) / file_num * 100)


output_file = 'output.txt'

with open('output.txt', 'w') as f:
    sys.stdout = f

    root = './IR-Plag-Dataset'
    java_files = get_java_files(root)
    do_test(java_files)

sys.stdout = sys.__stdout__
