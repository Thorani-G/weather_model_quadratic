# Quadratic Weather Model
a, b, c = -0.2, 1.5, 24

def quadratic_weather_model(time):
    return a * (time ** 2) + b * time + c

# === WATERFALL MODE ===
print("=== WATERFALL MODE ===")
for hour in range(0, 25, 6):
    print(f"Time: {hour} hrs -> {quadratic_weather_model(hour):.2f}°C")

# === ITERATIVE MODE ===
print("\n=== ITERATIVE MODE ===")
for iteration in range(1, 4):
    print(f"Iteration {iteration}:")
    for hour in range(0, 25, 12):
        print(f"Time: {hour} hrs -> {quadratic_weather_model(hour):.2f}°C")
    print("---")

# === AGILE MODE ===
print("\n=== AGILE MODE ===")
times = [0, 6, 12, 18, 24]
for sprint in range(1, 3):
    print(f"Sprint {sprint}:")
    for t in times:
        print(f"Time: {t} hrs -> {quadratic_weather_model(t):.2f}°C")
    print("---")
