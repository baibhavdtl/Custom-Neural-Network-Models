import numpy as np
import pandas as pd

X = np.random.uniform(0,4*np.pi,10000)
y = np.sin(X)
df = pd.DataFrame({"X" : X , "y" : y})
df.to_csv("sin_data.csv", index = False)

