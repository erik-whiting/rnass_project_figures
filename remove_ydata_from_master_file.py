old_path = "data/chemical_mapping_master_file.txt"
new_path = "data/chemical_mapping_master_file_filtered.txt"

with open(old_path) as fh:
    data = fh.readlines()


with open(new_path, "w") as fh:
    for d in data:
        if d.startswith("YesselmanLab"):
            continue
        fh.write(d)

print("Done")
