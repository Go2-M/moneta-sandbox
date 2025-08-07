import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ダミー観測データ
data = pd.DataFrame({
    "x": np.linspace(0, 10, 50),
        "y": np.sin(np.linspace(0, 10, 50))
        })
print(data.head())

plt.plot(data["x"], data["y"])
plt.title("Sample Observation Data")
plt.show()