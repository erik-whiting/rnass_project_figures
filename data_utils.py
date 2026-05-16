models = [
    "ContextFold",
    "ContraFold",
    "EternaFold",
    "IPKnot",
    "MXFold",
    "MXFold2",
    "NeuralFold",
    "NUPACK",
    "pKnots",
    "RNAFold",
    "RNAStructure",
    "Simfold",
    "SPOT-RNA"
]

def model_type_map(model):
    physics_models =    ["ContextFold", "ContraFold", "EternaFold", "IPKnot", "NeuralFold"]
    empirical_models =  ["NUPACK", "RNAFold", "RNAStructure", "pKnots", "Simfold"]
    ml_models =         ["MXFold", "MXFold2", "SPOT-RNA"]
    if model in physics_models:
        return "physics"
    if model in empirical_models:
        return "empirical"
    if model in ml_models:
        return "ML"

def get_model_color(model):
    mtype = model_type_map(model)
    color_map = {"physics": "green", "empirical": "red", "ML": "blue"}
    return color_map[mtype]


pretty_attr_map = {
    'sequence_length': 'Sequence Length',
    'gc_content': 'GC-Content',
    'sequence_entropy': 'Sequence Entropy',
    'average_longest_gc_helix': 'Longest GC Helix',
    'mfe': 'MFE',
    'ens_def': 'Ensemble Defect',
    'longest_consecutive_A': 'Longest Conesecutive A',
    'longest_consecutive_C': 'Longest Conesecutive C',
    'longest_consecutive_G': 'Longest Conesecutive G',
    'longest_consecutive_U': 'Longest Conesecutive U',
    'avg_gu_pairs': 'GU Pairs',
    'averge_bps_predicted': 'Average Basepairs Predicted',
    'hairpin_count': 'Hairpin Count',
    'helix_count': 'Helix Count',
    'single_strand_count': 'Single Strand Count',
    'junction_count': 'Junction Count',
    'average_mway_count': 'Multiway Junction Count',
    'longest_singlestrand': 'Longest Single Strand',
    'average_singlestrand_size': 'Average Single Strand Size',
    'longest_helix': 'Longest Helix',
    'average_helix_size': 'Average Helix Size',
    'average_hamming_distance_of_preds': 'Average Hamming Distance Between Predictions',
    'average_au_pairs_of_helices': 'Average AU Pairs in Helices',
    'helices_with_reverse_compliment': 'Helices with Reverse Complements',
    'rate_of_gt_4_unpaired_nt_in_hairpin': 'Rate of >4 Unpaired Nucleotides in Hairpin'
}

chemical_mapping_datasets = {
    "EternaData",
    "Ribonanza",
    "RNAndria mRNA",
    "RNAndria miRNA",
    "YesselmanLab"
}
