import matplotlib.pyplot as plt

# Sample data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 120, 90, 130, 150]

# Create a line plot with customizations
plt.plot(months, sales, color="blue", marker="o", linestyle="--", linewidth=2, markersize=8)
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.title("Monthly Sales Trend")
plt.grid(True)
plt.show()
