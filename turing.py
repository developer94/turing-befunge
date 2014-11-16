class TM:
    right = 1
    left = -1


    def __init__(self, blank):
        self.states = {'halt': {},
                       'success': {},
                       'failure': {},
                       'init': {}}

        self.tail = 0
        self.current = 0

        self.track = [blank]
        self.state = 'init'
        self.blank = blank


    def addState(self, state):
        self.states[state] = {}


    def setTrack(self, newTrack):
        self.track = newTrack
        self.tail = len(newTrack) - 1


    def addTransitionFunction(self, state, symbol, next_state,
                                        new_symbol, direction):
        if(state in self.states):
            self.states[state][symbol] = {'state': next_state,
                                          'symbol': new_symbol,
                                          'direction': direction}
        else:
            raise "State not defined!"


    def print_track(self):
        print('State: ' + self.state)

        for symbol in self.track:
            print(symbol + ' ', end="", flush=True)

        print()

        for i in range(0, self.tail + 1):
            mark = '^' if self.current == i else ' '
            print(mark + ' ', end="", flush=True)

        print()


    def run(self):
        while(True):
            self.print_track()

            # execute the state change
            if(self.track[self.current] in self.states[self.state]):
                transition = self.states[self.state][self.track[self.current]]
                self.track[self.current] = transition['symbol']
                self.state = transition['state']

                new_current = self.current + transition['direction']

                if(new_current < 0): # hit the left side
                    self.tail += 1
                    self.track.insert(0, self.blank)
                elif(new_current > self.tail): # hit the right side
                    self.tail += 1
                    self.track.append(self.blank)
                    self.current = new_current
                else: # moving freely
                    self.current = new_current
            else:
                break



if __name__=="__main__":
    InstructionMachine = TM('b')

    InstructionMachine.setTrack(['1', '0', '1', '1'])
    InstructionMachine.addState('A')

    InstructionMachine.addTransitionFunction('init', '0', 'init', '0', TM.right)
    InstructionMachine.addTransitionFunction('init', '1', 'init', '1', TM.right)
    InstructionMachine.addTransitionFunction('init', 'b', 'A', 'b', TM.left)
    InstructionMachine.addTransitionFunction('A', '0', 'success', '0', TM.right)
    InstructionMachine.addTransitionFunction('A', '1', 'failure', '1', TM.right)

    InstructionMachine.run()