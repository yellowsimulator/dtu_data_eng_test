import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("processing_times.csv")

y_non_para = df["non_parallel_time"]
y_para = df["parallel_time"]
record_size = df["size"]

plt.plot(record_size, y_non_para)
plt.plot(record_size, y_para)
plt.legend(["Non Parallel time (s)", "Parallel time (s)"])
plt.title("Comparing parallel and non parallel execution time")
plt.xlabel("Record size")
plt.ylabel("Execution time (s)")
plt.show()

