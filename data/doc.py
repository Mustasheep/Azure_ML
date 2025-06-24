# %%

import pandas as pd

# %%

df = pd.read_clipboard()
df.to_csv("german_credit.csv", index=False)