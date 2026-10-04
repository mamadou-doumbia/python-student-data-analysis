import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["Mamadou", "Ahmed", "Sarah", "Youssef", "Fatima"],
    "Math": [15, 12, 18, 11, 16],
    "Python": [17, 14, 19, 13, 15],
    "Statistics": [14, 11, 18, 12, 17]
}

df = pd.DataFrame(data)

df["Average"] = df[["Math", "Python", "Statistics"]].mean(axis=1)

print("=== Student Data ===")
print(df)

print("\n=== Class Statistics ===")
print(f"Class average: {df['Average'].mean():.2f}")
print(f"Highest average: {df['Average'].max():.2f}")
print(f"Lowest average: {df['Average'].min():.2f}")

plt.bar(df["Student"], df["Average"])

plt.title("Student Average Grades")
plt.xlabel("Students")
plt.ylabel("Average")

plt.ylim(0, 20)
plt.show()
