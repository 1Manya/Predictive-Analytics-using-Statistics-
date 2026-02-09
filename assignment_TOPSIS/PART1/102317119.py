import sys
import pandas as pd
import numpy as np
import os

def error(msg):
    print(f"Error: {msg}")
    sys.exit(1)

# ---------- STEP 1: Check number of arguments ----------
if len(sys.argv) != 5:
    error("Incorrect number of parameters.\nUsage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")

input_file = sys.argv[1]
weights = sys.argv[2]
impacts = sys.argv[3]
output_file = sys.argv[4]

# ---------- STEP 2: File existence ----------
if not os.path.isfile(input_file):
    error("Input file not found.")

# ---------- STEP 3: Read CSV ----------
try:
    data = pd.read_csv(input_file)
except Exception:
    error("Unable to read input file.")

# ---------- STEP 4: Minimum columns check ----------
if data.shape[1] < 3:
    error("Input file must contain three or more columns.")

# ---------- STEP 5: Convert weights & impacts ----------
try:
    weights = list(map(float, weights.split(',')))
except:
    error("Weights must be numeric and comma separated.")

impacts = impacts.split(',')

# ---------- STEP 6: Validate impacts ----------
for i in impacts:
    if i not in ['+', '-']:
        error("Impacts must be either '+' or '-'.")

# ---------- STEP 7: Match counts ----------
criteria_count = data.shape[1] - 1

if len(weights) != criteria_count or len(impacts) != criteria_count:
    error("Number of weights, impacts and criteria must be same.")

# ---------- STEP 8: Check numeric values ----------
for col in data.columns[1:]:
    if not pd.api.types.is_numeric_dtype(data[col]):
        error("From 2nd to last columns must contain numeric values only.")

# ---------- STEP 9: TOPSIS Calculation ----------
matrix = data.iloc[:, 1:].values.astype(float)

# Normalization
norm = np.sqrt((matrix ** 2).sum(axis=0))
normalized = matrix / norm

# Weighted matrix
weights = np.array(weights)
weighted = normalized * weights

# Ideal best & worst
ideal_best = []
ideal_worst = []

for j in range(criteria_count):
    if impacts[j] == '+':
        ideal_best.append(weighted[:, j].max())
        ideal_worst.append(weighted[:, j].min())
    else:
        ideal_best.append(weighted[:, j].min())
        ideal_worst.append(weighted[:, j].max())

ideal_best = np.array(ideal_best)
ideal_worst = np.array(ideal_worst)

# Distances
d_plus = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
d_minus = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

# Scores
scores = d_minus / (d_plus + d_minus)

# Ranking
rank = scores.argsort()[::-1].argsort() + 1

# ---------- STEP 10: Save Result ----------
result = data.copy()
result['TOPSIS Score'] = scores
result['Rank'] = rank

try:
    result.to_csv(output_file, index=False)
except:
    error("Unable to write output file.")

print("TOPSIS analysis completed successfully.")
