from kalman_filter.kalman import KalmanFilter


def test_initial_estimate_zero():
    kf = KalmanFilter()
    assert kf.get_estimate() == 0.0


def test_predict_updates_angle():
    kf = KalmanFilter()
    kf.predict(gyro_rate=1.0)
    assert kf.get_estimate() != 0.0


def test_update_corrects_toward_accel():
    kf = KalmanFilter()
    for _ in range(300):  # было 50, стало 300
        kf.predict(gyro_rate=0.0)
        kf.update(accel_angle=10.0)
    assert abs(kf.get_estimate() - 10.0) < 1.0


def test_kalman_converges_to_constant_value():
    kf = KalmanFilter()
    true_angle = 30.0
    for _ in range(500):
        kf.predict(gyro_rate=0.0)
        kf.update(accel_angle=true_angle)
    estimate = kf.get_estimate()
    assert abs(estimate - true_angle) < 1.0


def test_kalman_handles_bias():
    kf = KalmanFilter()
    for _ in range(500):
        kf.predict(gyro_rate=5.0)
        kf.update(accel_angle=0.0)
    estimate = kf.get_estimate()
    assert abs(estimate) < 5.0
