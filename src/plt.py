import matplotlib.pyplot as plt
import numpy as np

def visualize_tsp_solution(distance_matrix, order):
    num_points = len(distance_matrix)

    # Создаем списки координат для точек и соединяющих их линий
    points = np.array([(np.cos(2 * np.pi * i / num_points), np.sin(2 * np.pi * i / num_points)) for i in range(num_points)])
    lines_x = [points[order[i]][0] for i in range(num_points)]
    lines_y = [points[order[i]][1] for i in range(num_points)]

    # Добавляем начальную точку в конец, чтобы замкнуть путь
    lines_x.append(lines_x[0])
    lines_y.append(lines_y[0])

    # Создаем график и добавляем точки и линии
    plt.figure()
    plt.scatter(points[:, 0], points[:, 1], color='red', zorder=1)

    # Добавляем индексы точек рядом с ними
    for i in range(num_points):
        plt.text(points[i][0], points[i][1], str(i), color='black', ha='center', va='center')

    plt.plot(lines_x, lines_y, color='blue', linewidth=1, zorder=2)

    # Добавляем текст с расстояниями между точками
    for i in range(num_points):
        for j in range(i + 1, num_points):
            distance = distance_matrix[order[i]][order[j]]
            plt.text((points[i][0] + points[j][0]) / 2, (points[i][1] + points[j][1]) / 2, str(distance), color='black', ha='center', va='center')

    # Настраиваем оси и отображаем график
    plt.axis('equal')
    plt.show()

    