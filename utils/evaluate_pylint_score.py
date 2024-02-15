# evaluate_pylint_score.py

import sys

def evaluate_pylint_score(output_file):
    with open(output_file, 'r') as f:
        lines = f.readlines()
    
    score_line = next((line for line in lines if 'Your code has been rated at' in line), None)
    if score_line:
        score = float(score_line.split(' ')[-2])
        if score >= 6:
            print("Pylint score is acceptable. Proceeding with the push.")
            sys.exit(0)
        else:
            print("Pylint score is below 6. Skipping the push.")
            sys.exit(1)
    else:
        print("Pylint score not found in output. Skipping the push.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python evaluate_pylint_score.py <pylint_output_file>")
        sys.exit(1)
    output_file = sys.argv[1]
    evaluate_pylint_score(output_file)
