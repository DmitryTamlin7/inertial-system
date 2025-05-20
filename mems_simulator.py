import numpy as np

class MEMSSimulator:
    def __init__(self, dt=0.01, gyro_drift=0.05, noise_std=0.1):

        self.dt = dt
        self.gyro_drift = gyro_drift
        self.noise_std = noise_std
        self.gyro_bias = 0.0

    def get_gyro(self, true_rate: float) -> float:

        self.gyro_bias += np.random.randn() * self.gyro_drift * self.dt
        noise = np.random.randn() * self.noise_std
        return true_rate + self.gyro_bias + noise

    def get_accel(self, true_angle: float) -> float:

        noise = np.random.randn() * self.noise_std
        return true_angle + noise
