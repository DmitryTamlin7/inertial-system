#Фильтр Калмана Фильтр предсказывает угол с гироскопа, и корректирует с помощью акселерометра.

class KalmanFilter:
    def __init__(self, dt=0.01, Q_angle=0.001, Q_gyro=0.003, R_angle=0.03):
        self.dt = dt
        self.Q_angle = Q_angle
        self.Q_gyro = Q_gyro
        self.R_angle = R_angle

        self.angle = 0.0
        self.bias = 0.0
        self.P = [[0.0, 0.0], [0.0, 0.0]]

    def predict(self, gyro_rate):
        self.angle += self.dt * (gyro_rate - self.bias)
        self.P[0][0] += self.dt * (self.dt*self.P[1][1] - self.P[1][0] - self.P[0][1] + self.Q_angle)
        self.P[0][1] -= self.dt * self.P[1][1]
        self.P[1][0] -= self.dt * self.P[1][1]
        self.P[1][1] += self.Q_gyro * self.dt

    def update(self, accel_angle):
        y = accel_angle - self.angle
        S = self.P[0][0] + self.R_angle
        K = [self.P[0][0]/S, self.P[1][0]/S]
        self.angle += K[0] * y
        self.bias += K[1] * y
        P00_temp = self.P[0][0]
        P01_temp = self.P[0][1]
        self.P[0][0] -= K[0] * P00_temp
        self.P[0][1] -= K[0] * P01_temp
        self.P[1][0] -= K[1] * P00_temp
        self.P[1][1] -= K[1] * P01_temp

    def get_estimate(self):
        return self.angle

    def get_angle(self):
        return self.angle
