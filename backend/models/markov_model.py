import numpy as np

states = ['Study', 'Instagram', 'YouTube', 'Idle']

transition_matrix = np.array([
    [0.6, 0.2, 0.1, 0.1],
    [0.2, 0.5, 0.2, 0.1],
    [0.3, 0.4, 0.2, 0.1],
    [0.4, 0.2, 0.2, 0.2]
])


def predict_next_state(current_state_index):
    return np.random.choice(
        states,
        p=transition_matrix[current_state_index]
    )


print(predict_next_state(0))