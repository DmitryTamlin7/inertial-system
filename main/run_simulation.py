import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import csv
import os

from emulator.mems_simulator import MEMSSimulator
from kalman_filter.kalman import KalmanFilter
from visualizer.vizualuzer import plot_results


def run_simulation(duration=10.0, dt=0.01, save_to_csv=True, filename='simulation_output.csv'):
    sim = MEMSSimulator(dt=dt)
    kf = KalmanFilter(dt=dt)

    time_steps = int(duration / dt)
    true_angle = 0.0
    true_rate = 1.0

    data = []

    for step in range(time_steps):
        t = step * dt
        true_angle += true_rate * dt

        gyro_meas = sim.get_gyro(true_rate)
        accel_meas = sim.get_accel(true_angle)

        kf.predict(gyro_meas)
        kf.update(accel_meas)

        filtered_angle = kf.get_angle()

        data.append((t, true_angle, gyro_meas, accel_meas, filtered_angle))

    if save_to_csv:
        output_dir = os.path.join(os.path.dirname(__file__), "..", "output")
        os.makedirs(output_dir, exist_ok=True)
        full_path = os.path.join(output_dir, filename)

        print(f"[INFO] Сохраняем результат в: {os.path.abspath(full_path)}")

        with open(full_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['time', 'true_angle', 'gyro_meas', 'accel_meas', 'filtered_angle'])
            writer.writerows(data)

    return data


if __name__ == "__main__":
    data = run_simulation()

    times = [row[0] for row in data]
    true_angles = [row[1] for row in data]
    gyro_rates = [row[2] for row in data]
    accel_angles = [row[3] for row in data]
    filtered_angles = [row[4] for row in data]

    plot_results(times, true_angles, accel_angles, gyro_rates, filtered_angles)

