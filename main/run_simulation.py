def run_simulation(duration=10.0):
    # 1. Создаёт экземпляры MEMSSimulator и KalmanFilter
    # 2. Генерирует «истинное» движение (угол и скорость)
    # 3. В цикле по времени:
    #       - Получает данные с эмулятора (gyro и accel)
    #       - Передаёт их в фильтр Калмана (predict + update)
    #        - Сохраняет: t, true_angle, gyro_meas, accel_meas, filtered_angle
    # 4. Сохраняет всё в CSV или возвращает списки


