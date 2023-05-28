import sys

def tsp_dp(graph):
    n = len(graph)
    start = 0
    # Создаем таблицу для хранения подзадач
    memo = [[None] * (1 << n) for _ in range(n)]
    
    # Рекурсивная функция для вычисления минимального пути
    def tsp_mask(curr, mask):
        if mask == (1 << n) - 1:
            return graph[curr][start], None
        
        if memo[curr][mask] is not None:
            return memo[curr][mask]
        
        ans = sys.maxsize
        best_next = None
        
        for next_node in range(n):
            if mask & (1 << next_node) == 0:
                new_mask = mask | (1 << next_node)
                distance, _ = tsp_mask(next_node, new_mask)
                if graph[curr][next_node] + distance < ans:
                    ans = graph[curr][next_node] + distance
                    best_next = next_node
        
        memo[curr][mask] = ans, best_next
        return ans, best_next
    
    # Вызываем рекурсивную функцию для начальной вершины
    min_distance, best_next = tsp_mask(start, 1)
    
    # Восстановление пути
    path = [start]
    mask = 1 << start
    
    while len(path) < n:
        path.append(best_next)
        mask |= (1 << best_next)
        _, best_next = tsp_mask(best_next, mask)
    
    path.append(path[0])
    for i in range(len(path)):
        path[i] = path[i] + 1
    
    return min_distance, path

