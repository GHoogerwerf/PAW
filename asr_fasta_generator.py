import numpy as np
import pandas as pd

df = pd.read_table("__________name of input file________", error_bad_lines=False)

with open("_________name of output file__________", "w") as out:
    node_n = ""
    state_n = ""
    for index, row in df.iterrows():
        if row["Node"] != node_n:
            out.write("\n" + ">" + row["Node"] + "\n")
            if row["State"] != "-":
                out.write(row["State"])
            else:
                next
            node = row["Node"]
        elif row["Node"] != node:
            if row["State"] != "-":
                out.write(row["State"] + "\n")
            else:
                next
        elif row["Node"] == node:
            if row["State"] != "-":
                out.write(row["State"])
            else:
                next
            node_n = row["Node"]
