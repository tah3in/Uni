import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, dim):
        self.position = np.random.rand(dim)
        self.velocity = np.random.rand(dim)
        self.best_position = self.position
        self.best_fitness = float('inf')

def objective_function(x):
    return x[0]**2 + x[1]**2

def update_velocity(particle, global_best_position, inertia_weight, c1, c2):
    inertia_term = inertia_weight * particle.velocity
    cognitive_term = c1 * np.random.rand() * (particle.best_position - particle.position)
    social_term = c2 * np.random.rand() * (global_best_position - particle.position)
    new_velocity = inertia_term + cognitive_term + social_term
    return new_velocity

def update_position(particle):
    new_position = particle.position + particle.velocity
    return new_position

def particle_swarm_optimization(objective_function, dim, num_particles, num_iterations, c1, c2, inertia_weight):
    particles = [Particle(dim) for _ in range(num_particles)]
    global_best_position = None
    global_best_fitness = float('inf')

    fitness_history = []  # To store fitness values over iterations

    for iteration in range(num_iterations):
        for particle in particles:
            fitness = objective_function(particle.position)
            if fitness < particle.best_fitness:
                particle.best_fitness = fitness
                particle.best_position = particle.position

            if fitness < global_best_fitness:
                global_best_fitness = fitness
                global_best_position = particle.position

        for particle in particles:
            particle.velocity = update_velocity(particle, global_best_position, inertia_weight, c1, c2)
            particle.position = update_position(particle)

        fitness_history.append(global_best_fitness)

    return global_best_position, global_best_fitness, fitness_history

# Example usage:
dim = 2  # Dimension of the search space
num_particles = 30
num_iterations = 100
c1 = 2.0  # Cognitive parameter
c2 = 2.0  # Social parameter
inertia_weight = 0.9

best_position, best_fitness, fitness_history = particle_swarm_optimization(objective_function, dim, num_particles, num_iterations, c1, c2, inertia_weight)

print("Best Position:", best_position)
print("Best Fitness:", best_fitness)

# Plotting fitness over iterations
plt.plot(range(1, num_iterations + 1), fitness_history, marker='o')
plt.title('Fitness Over Iterations')
plt.xlabel('Iteration')
plt.ylabel('Fitness')
plt.show()
