import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load a dataset
penguins = sns.load_dataset('penguins')
print(type(penguins))
print(penguins)