import pathlib
import numpy as np
import pandas as pd

path = pathlib.Path(__file__).resolve().parent.joinpath("data")
if not path.exists():
    path.mkdir()

columns = columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
for i in range(100):
    df = pd.DataFrame(
        np.random.randint(low=0, high=100, size=(int(1e4), 10)),
        columns=columns
    )
    df.to_csv(path.joinpath(f"data_{i}"), index=False)
