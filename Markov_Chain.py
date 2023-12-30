import random
import numpy as np
import pandas as pd
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        # Initialize the Markov Chain class
        self.transition_matrix = {}

    def add_transition(self, current_state, next_state):
        # Add a transition from the current state to the next state
        if current_state not in self.transition_matrix:
            self.transition_matrix[current_state] = defaultdict(int)
        self.transition_matrix[current_state][next_state] += 1

    def generate_states(self, initial_state, num_states):
        # Generate a sequence of states starting from the initial state
        generated_sequence = [initial_state]
        for _ in range(num_states - 1):
            next_state = self._get_next_state(generated_sequence[-1])
            if next_state is None:
                break
            generated_sequence.append(next_state)
        return generated_sequence

    def _get_next_state(self, current_state):
        # Get the next state based on the current state
        if current_state not in self.transition_matrix:
            return None
        total_transitions = sum(self.transition_matrix[current_state].values())
        random_value = random.uniform(0, total_transitions)
        accumulated_sum = 0.0
        for next_state, count in self.transition_matrix[current_state].items():
            accumulated_sum += count
            if accumulated_sum >= random_value:
                return next_state
        return None

    def print_transition_matrix(self):
        # Print the transition matrix
        for current_state, next_states in self.transition_matrix.items():
            print(f"{current_state}: {', '.join([f'{state}: {count}' for state, count in next_states.items()])}")

def print_matrix(matrix):
    # Determine the number of characters for formatting
    col_width = max(len(str(item)) for sublist in matrix for item in sublist)

    # Create a format string based on the calculated widths
    fmt = f"{{:{col_width}d}}" * len(matrix[0])

    # Print the matrix with the formatted values
    print("\n".join(" ".join(fmt.format(item) for item in sublist) for sublist in matrix))
    format_str = '{:>' + str(col_width) + '}'
    format_str = ' '.join([format_str] * len(matrix[0]))

    # Print the matrix in tabular form
    for row in matrix:
        print(format_str.format(*row))

# Example usage

if __name__ == "__main__":
    # Create a Markov Chain instance
    markov_chain = MarkovChain()

    # Add transitions based on the text
    text = "In a land far away, there lived a wise old owl. The owl loved to share stories. These stories were not just any tales; they were reflections of the wisdom the owl had gained over the years. Every evening, creatures from all around the land would gather to listen to the owl's tales. The tales spoke of adventures, lessons, and the mysteries of the land. Among the listeners were a curious rabbit, a brave fox, and a cautious deer. The rabbit, known for its endless curiosity, would always ask questions about the tales. The fox, brave and cunning, would ponder how to use the lessons in life. The deer, cautious and gentle, would reflect on the morals of the stories. Together, they learned much from the wise old owl and looked forward to each new tale with great anticipation."
    words = text.split()
    for i in range(len(words) - 1):
        markov_chain.add_transition(words[i], words[i + 1])

    # Print the transition matrix
    markov_chain.print_transition_matrix()

    # Convert the transition matrix to a numpy array and pandas DataFrame
    transition_matrix_df = pd.DataFrame.from_dict(markov_chain.transition_matrix, orient='index')
    transition_matrix_array = transition_matrix_df.to_numpy()

    # Normalize the transition matrix
    normalized_transition_matrix = transition_matrix_array / transition_matrix_array.sum(axis=1, keepdims=True)

    # Generate a sequence of states (words)
    initial_state = "In"
    num_states = 50 # length of the generated text
    generated_sequence = markov_chain.generate_states(initial_state, num_states)
    print("Generated Text:", " ".join(generated_sequence))