import numpy as np

# -----------------------
# 1. Define Time Intervals (20-minute blocks from 7:00 AM to 7:00 PM)
# -----------------------
time_intervals = [
    ("07:00", "07:20"), ("07:20", "07:40"), ("07:40", "08:00"), ("08:00", "08:20"),
    ("08:20", "08:40"), ("08:40", "09:00"), ("09:00", "09:20"), ("09:20", "09:40"),
    ("09:40", "10:00"), ("10:00", "10:20"), ("10:20", "10:40"), ("10:40", "11:00"),
    ("11:00", "11:20"), ("11:20", "11:40"), ("11:40", "12:00"), ("12:00", "12:20"),
    ("12:20", "12:40"), ("12:40", "13:00"), ("13:00", "13:20"), ("13:20", "13:40"),
    ("13:40", "14:00"), ("14:00", "14:20"), ("14:20", "14:40"), ("14:40", "15:00"),
    ("15:00", "15:20"), ("15:20", "15:40"), ("15:40", "16:00"), ("16:00", "16:20"),
    ("16:20", "16:40"), ("16:40", "17:00"), ("17:00", "17:20"), ("17:20", "17:40"),
    ("17:40", "18:00"), ("18:00", "18:20"), ("18:20", "18:40"), ("18:40", "19:00"),
]

# Set of indices marking which blocks are peak hours
peak_block_indices = {7, 10, 14, 15, 16, 17, 18, 19, 20}

# -----------------------
# 2. Collect employee inputs for each time block
# -----------------------
time_blocks = []
print("=== Enter the number of employees per time block ===")
for i, (start, end) in enumerate(time_intervals):
    while True:
        try:
            # Ask user for number of employees (must be 2–4)
            e = int(input(f"Block {i+1:02d} ({start} - {end}): How many employees? (2-4) ➜ "))
            if e < 2 or e > 4:
                print("❌ Only 2, 3, or 4 employees are allowed.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid integer.")

    # Store block info with peak flag and employee count
    time_blocks.append({
        "start": start,
        "end": end,
        "is_peak": i in peak_block_indices,
        "employees": e
    })

# -----------------------
# 3. Set arrival rates and wait time lookups
# -----------------------
peak_lambda = 8       # Avg. number of arrivals during peak blocks
non_peak_lambda = 3   # Avg. number of arrivals during non-peak blocks

# Expected wait times based on employees and peak status
wait_time_lookup = {
    "peak": {
        2: 8.000,
        3: 7.461,
        4: 4.957
    },
    "non_peak": {
        2: 1.2828,
        3: 0.8316,
        4: 0.6052
    }
}

# -----------------------
# 4. Simulation Functions
# -----------------------

# Simulates customer wait times for one day
def simulate_day(schedule, peak_lambda, non_peak_lambda, wait_lookup):
    customer_waits = []
    for block in schedule:
        employees = block["employees"]
        # Select lambda and base mean wait time
        if block["is_peak"]:
            lam = peak_lambda
            base_mean = wait_lookup["peak"][employees]
        else:
            lam = non_peak_lambda
            base_mean = wait_lookup["non_peak"][employees]

        # Generate number of arrivals using Poisson distribution
        arrivals = np.random.poisson(lam)
        # For each arrival, simulate wait time using Exponential distribution
        for _ in range(arrivals):
            w = np.random.exponential(scale=base_mean)
            customer_waits.append(w)

    # Return average wait time for the day
    return np.mean(customer_waits) if customer_waits else 0.0

# Run the simulation over multiple days and get average wait time
def run_simulation(schedule, peak_lambda, non_peak_lambda, wait_lookup, days=1000):
    daily_averages = []
    for _ in range(days):
        avg_w = simulate_day(schedule, peak_lambda, non_peak_lambda, wait_lookup)
        daily_averages.append(avg_w)
    return np.mean(daily_averages)

# -----------------------
# 5. Final Output and Summary
# -----------------------
if __name__ == "__main__":
    # Count how many blocks have 2, 3, or 4 employees
    employee_counts = {}
    for block in time_blocks:
        e = block["employees"]
        employee_counts[e] = employee_counts.get(e, 0) + 1

    print("\n=== Number of Blocks by Employee Count ===")
    for count, total in sorted(employee_counts.items()):
        print(f"{count} employees: {total} blocks")

    # Calculate total employee-hours and daily labor cost
    total_employee_hours = sum(b["employees"] * (20 / 60.0) for b in time_blocks)
    daily_cost = total_employee_hours * 17.0

    print(f"\n=== Daily Employee Cost ===")
    print(f"Total employee-hours (7:00–19:00): {total_employee_hours:.2f}")
    print(f"Cost at $17/hour: ${daily_cost:.2f}")

    # Run 1000-day simulation and report average wait time
    num_days = 1000
    avg_wait = run_simulation(time_blocks, peak_lambda, non_peak_lambda, wait_time_lookup, days=num_days)
    print(f"\n=== Simulation Results Over {num_days} Days ===")
    print(f"Average Customer Wait Time: {avg_wait:.3f} minutes")
