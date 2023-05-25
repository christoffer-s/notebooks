from matplotlib import pyplot as plt
import pandas as pd


data = pd.read_csv("co2.csv")

plt.plot(data)