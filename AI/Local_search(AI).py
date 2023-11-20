import random
import time
import os
# shape
map = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]
]

time_sec = 0

num_colors = 3

# الگوریتم تبرید شبیه سازی شده
def simulated_annealing_algorithm():
    num_vertices = len(map) #5 count city 
    colors = generate_random_colors(num_vertices)
    temperature = 1000
    cooling_rate = 0.95
    
    while temperature > 0.1:
        time.sleep(time_sec)
        new_colors = colors.copy()
        # print(new_colors)
        # time.sleep(0.5)
        # os.system('cls')

        # تعیین یک رنگ جدید برای یک راس تصادفی
        vertex = random.randint(0, num_vertices - 1)
        color = random.randint(1, num_colors)
        new_colors[vertex] = color
        
        old_cost = calculate_cost(colors)
        new_cost = calculate_cost(new_colors)
        
        if accept_move(old_cost, new_cost, temperature):
            colors = new_colors
        
        temperature *= cooling_rate
    
    return colors


# الگوریتم جستجوی ممنوعه
def tabu_search_algorithm():
    num_vertices = len(map)
    colors = generate_random_colors(num_vertices)
    tabu_list = []
    tabu_tenure = 5
    best_solution = colors.copy()
    best_cost = calculate_cost(colors)
    
    num_iterations = 100
    
    for _ in range(num_iterations):
        best_neighbor = None
        best_neighbor_cost = float('inf')
        for vertex in range(num_vertices):
            time.sleep(time_sec)
            for color in range(1, num_colors + 1):
                neighbor = colors.copy()
                neighbor[vertex] = color
                neighbor_cost = calculate_cost(neighbor)
                
                if (neighbor_cost < best_neighbor_cost) and (neighbor not in tabu_list):
                    best_neighbor = neighbor
                    best_neighbor_cost = neighbor_cost
        
        colors = best_neighbor
        # print('append : ',colors)
        tabu_list.append(best_neighbor)
        
        if len(tabu_list) > tabu_tenure:
            # print('delete : ',tabu_list.pop(0))
            tabu_list.pop(0)
        
        if best_neighbor_cost < best_cost:
            best_solution = best_neighbor
            best_cost = best_neighbor_cost
    
    return best_solution


# الگوریتم تپه‌نوردی
def hill_climbing_algorithm():
    num_vertices = len(map)
    colors = generate_random_colors(num_vertices)
    
    while True:
        best_neighbor = None
        best_cost = calculate_cost(colors)
        
        for vertex in range(num_vertices):
            time.sleep(time_sec)
            for color in range(1, num_colors + 1):
                neighbor = colors.copy()
                neighbor[vertex] = color
                neighbor_cost = calculate_cost(neighbor)
                
                if neighbor_cost < best_cost:
                    best_neighbor = neighbor
                    best_cost = neighbor_cost
        
        if best_neighbor is None:
            break
        
        colors = best_neighbor
    
    return colors

# توابع کمکی
def generate_random_colors(num_vertices):
    return [random.randint(1, num_colors) for _ in range(num_vertices)]

def calculate_cost(colors):
    cost = 0
    
    for i in range(len(map)):
        time.sleep(time_sec)
        for j in range(i + 1, len(map)):
            if map[i][j] == 1 and colors[i] == colors[j]:
                cost += 1
    
    return cost

def accept_move(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return True
    
    probability = 2.71828 ** ((old_cost - new_cost) / temperature)
    return random.random() < probability



# اجرای الگوریتم‌ها
start_time = time.time()
sa_solution = simulated_annealing_algorithm()
sa_time = time.time() - start_time

start_time = time.time()
hill_climbing_solution = hill_climbing_algorithm()
hill_climbing_time = time.time() - start_time

start_time = time.time()
tabu_search_solution = tabu_search_algorithm()
execution_time = time.time() - start_time


print("Simulated Annealing Solution:", sa_solution)
print("Simulated Annealing Time:", sa_time)
print("___________________________________________________")
print("tabu search solution:", tabu_search_solution)
print("tabu search Time:", execution_time)
print("___________________________________________________")
print("Hill Climbing Solution:", hill_climbing_solution)
print("Hill Climbing Time:", hill_climbing_time)
print("___________________________________________________")