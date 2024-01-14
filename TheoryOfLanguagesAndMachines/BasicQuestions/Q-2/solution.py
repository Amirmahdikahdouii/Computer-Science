class DFA:
    def __init__(self, quantities: list, alphabet: list, start_state: str, final_states: list, string: str = None):
        self.quantities = quantities
        self.alphabet = alphabet
        self.start_position = start_state
        self.final_states = final_states
        self.result = False
        self.string = string

    def delta(self, state: str, character: str):
        """
        This Function is looklike delta function in DFA (Deterministic Finite Accepter).
        And it will return the new state by given state and character or 
        raise exception if character or state was not found.
        """

        if character.lower() not in self.alphabet:
            raise ValueError("character is not in alphabet")
        elif state.upper() not in self.quantities:
            raise ValueError("given state is not in quantities")
        states = {
            "A-a": "D",
            "A-b": "B",
            "B-a": "C",
            "B-b": "A",
            "C-a": "B",
            "C-b": "D",
            "D-a": "A",
            "D-b": "C",
        }
        for key in states.keys():
            if key.startswith(state.upper()) and key.endswith(character.lower()):
                return states[key]
        raise ValueError("State with given character is not defined!")

    def check(self):
        position = self.start_position
        for i in self.string:
            position = self.delta(position, i)
        self.result = position in self.final_states
        return position in self.final_states

    def __str__(self):
        return str(self.check())


string = None
# Uncomment this line to input test case by yourself.
# string = input().lower()

quantities = ["A", "B", "C", "D"]
alphabet = ['a', 'b']
start_state = "A"
final_states = ["B"]

dfa = DFA(quantities, alphabet, start_state, final_states, string)
