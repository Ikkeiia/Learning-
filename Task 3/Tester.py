class TurnBase:
    def __init__(self, turn = 1):
        self.turn = turn

    def turn_update(self):
        return self.turn + 1

    def turn_reset(self):
        self.turn = 1

