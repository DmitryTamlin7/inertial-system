import numpy as np
import csv

from emulator.mems_simulator import MEMSSimulator
from kalman_filter.kalman import KalmanFilter

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
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['time', 'true_angle', 'gyro_meas', 'accel_meas', 'filtered_angle'])
            writer.writerows(data)

    return data
