import pandas as pd
import numpy as np

np.random.seed(42)  # Setting seed for reproducibility
data = np.random.randn(10, 4)  # Generate random values from a normal distribution
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])

def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return 'color: {}'.format(color)

styled_df = df.style.apply(lambda x: x.map(color_negative_red), subset=pd.IndexSlice[:, :])

styled_df
