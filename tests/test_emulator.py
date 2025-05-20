import numpy as np
from emulator.mems_simulator import MEMSSimulator


def test_get_gyro_noise_present():
    sim = MEMSSimulator()
    true_rate = 0.0
    values = [sim.get_gyro(true_rate) for _ in range(100)]
    assert len(set(np.round(values, 4))) > 1


def test_get_accel_noise_present():
    sim = MEMSSimulator()
    true_angle = 0.0
    values = [sim.get_accel(true_angle) for _ in range(100)]
    assert len(set(np.round(values, 4))) > 1


def test_gyro_drift_accumulates():
    sim = MEMSSimulator(dt=0.1, gyro_drift=1.0)
    base = sim.get_gyro(0.0)
    for _ in range(500):
        sim.get_gyro(0.0)
    after = sim.get_gyro(0.0)
    assert abs(after - base) > 0.1
