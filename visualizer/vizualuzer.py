import matplotlib.pyplot as plt
def plot_results(times, true_angles, accel_angles, gyro_rates, filtered_angles):

    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    
    #График истинного угла (зеленый, сплошная линия)
    plt.plot(times, true_angles, 'g-', label='Истинный угол')
    
    #График угла по акселерометру (красный, пунктирная линия)
    plt.plot(times, accel_angles, 'r--', label='Акселерометр')
    
    #График отфильтрованного угла (синий, сплошная линия)
    plt.plot(times, filtered_angles, 'b-', label='Фильтр (комплементарный/Kalman)')
    
    plt.title('Сравнение углов наклона')
    plt.ylabel('Угол (рад)')
    plt.grid(True)
    plt.legend()
    
    plt.subplot(2, 1, 2)
    
    #График скорости вращения (фиолетовый, сплошная линия)
    plt.plot(times, gyro_rates, 'm-', label='Гироскоп')
    
    plt.title('Скорость вращения по гироскопу')
    plt.xlabel('Время (с)')
    plt.ylabel('Скорость (рад/с)')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
