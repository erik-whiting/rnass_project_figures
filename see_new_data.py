import json

with open("chem_map_data_with_predictions/with_scores/C014I_with_predictions.json") as fh:
    data = json.load(fh)

print("Outer keys")
for k in data[0].keys():
    print(f"- {k}")

print("Prediction keys")
for k in data[0]["predictions"].keys():
    print(f"- {k}")

print("See predictions plus sampled structure and RNA strucutre")
for model, pred in data[0]["predictions"].items():
    print(f"{pred} - {model}")
print(f"{data[0]['structure']} - RNAStructure w/ DMS constraints")
print(f"{data[0]['best_sample']} - Best sample from EternaFold")

# Running this script gives you:
"""
Outer keys
- name
- sequence
- structure
- data
- reads
- predictions
- best_sample
- score
Prediction keys
- RNAFold
- EternaFold
- RNAStructure
- MXFold
- Simfold
- IPKnot
- NeuralFold
- ContextFold
- SPOT-RNA
- NUPACK
- MXFold2
- ContraFold
- pKnots
See predictions plus sampled structure and RNA strucutre
.((((((....)))))).....((((((.....)))))).(.(((((((.....))))))).).. - RNAFold
.((((((....))))))...(.((((((.....)))))))..(((((((.....))))))).... - EternaFold
.((((((....)))))).....((((((.....))))))...(((((((.....))))))).... - RNAStructure
.((((((....)))))).....((((((.....)))))).(.(((((((.....))))))).).. - MXFold
.((((((....)))))).....((((((.....)))))).(.(((((((.....))))))).).. - Simfold
.((((((....)))))).....((((((.....))))))...(((((((.....))))))).... - IPKnot
(((((((....))))))(..(((((((((...))))))....)))).)(((.......))).... - NeuralFold
.((((((....)))))).(..(((((((.....)))))).)..).......(((.......))). - ContextFold
.((((((....)))))).....(((((((...)))))))...(((((((.....))))))).... - SPOT-RNA
.((((((....)))))).....((((((.....)))))).(.(((((((.....))))))).).. - NUPACK
.((((((....)))))).....(((((((...))))))).(.(((((((.....))))))).).. - MXFold2
.((((((....)))))).....(((((((...))))))).(.(((((((.....))))))).).. - ContraFold
.((((((....)))))).....((((((.....))))))...(((((((.....))))))).... - pKnots
.((((((....)))))).....((((((.....))))))...(((((((.....))))))).... - RNAStructure w/ DMS constraints
.((((((....)))))).....((((((.....))))))...(((((((.....))))))).... - Best sample from EternaFold
"""
