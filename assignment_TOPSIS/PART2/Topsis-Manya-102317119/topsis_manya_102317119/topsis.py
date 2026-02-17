import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):

    data = pd.read_csv(input_file)

    if data.shape[1] < 3:
        raise Exception("Input file must have at least 3 columns")

    matrix = data.iloc[:, 1:].values.astype(float)

    weights = np.array(list(map(float, weights.split(','))))
    impacts = impacts.split(',')

    if len(weights) != matrix.shape[1]:
        raise Exception("Number of weights must match criteria")

    # Normalization
    norm = np.sqrt((matrix ** 2).sum(axis=0))
    matrix = matrix / norm

    # Apply weights
    matrix = matrix * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(matrix[:, i].max())
            ideal_worst.append(matrix[:, i].min())
        else:
            ideal_best.append(matrix[:, i].min())
            ideal_worst.append(matrix[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    d_plus = np.sqrt(((matrix - ideal_best) ** 2).sum(axis=1))
    d_minus = np.sqrt(((matrix - ideal_worst) ** 2).sum(axis=1))

    score = d_minus / (d_plus + d_minus)
    rank = score.argsort()[::-1].argsort() + 1

    data['Topsis Score'] = score
    data['Rank'] = rank

    data.to_csv(output_file, index=False)
    
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: topsis <input_file> <weights> <impacts> <output_file>")
        sys.exit(1)

    topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
import sys
import pandas as pd

def main():
    if len(sys.argv) != 5:
        print("Usage: topsis <input.csv> <weights> <impacts> <output.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    # call your existing topsis logic here
    # for example:
    # topsis(input_file, weights, impacts, output_file)

    print("TOPSIS executed successfully")

if __name__ == "__main__":
    main()
