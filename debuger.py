from matplotlib import pyplot as plt
import pandas as pd


data = pd.read_csv("ssbmedier.csv", index_col = 0, skiprows = (0, 1), sep =";", na_values=[".", ".."], encoding = "latin-1")

K = []   
startVerdi = 2010   
for i in range(0, 10):
    K.append(startVerdi + i)
data.columns = K  

plt.plot(data)
plt.show()




