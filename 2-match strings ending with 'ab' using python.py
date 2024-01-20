2.	Implement a basic finite state automaton that recognizes a specific language or pattern. In this example,
we'll create a simple automaton to match strings ending with 'ab' using python.

PROGRAM :-

class StateMachine:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}  
        self.alphabet = {'a', 'b'}         
        self.transitions = {
            'q0': {'a': 'q0', 'b': 'q1'},
            'q1': {'a': 'q2', 'b': 'q1'},
            'q2': {'a': 'q2', 'b': 'q2'}
        }  
        self.start_state = 'q0'
        self.accept_states = {'q2'}        
    def process_input(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                print(f"Invalid symbol '{symbol}' encountered.")
                return False
            current_state = self.transitions[current_state][symbol]
        if current_state in self.accept_states:
            return True
        else:
            return False
if __name__ == "__main__":
    fsm = StateMachine()
    test_strings = ['aaaab', 'ab', 'bab', 'aabb', 'abcab']
    for test_string in test_strings:
        result = fsm.process_input(test_string)
        if result:
            print(f"Accepted: '{test_string}' ends with 'ab'")
        else:
            print(f"Rejected: '{test_string}' does not end with 'ab'")
