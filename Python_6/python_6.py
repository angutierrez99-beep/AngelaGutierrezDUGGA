import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

penguins = sns.load_dataset("penguins")
penguins = penguins.dropna()

