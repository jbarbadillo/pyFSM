class State:
    transitions = {}

    def __init__(self, name):
        self.name = name


class StateMachine:
    currentState = None
    initialState = None

    def __init__(self, states, initial_state, events, transitions):
        self._states = []
        self.addStates(states)  # possible states
        self._events = events  # allowed events
        self.initialState = initial_state

        self.addTransitions(transitions)
        self.started = False
        print("pyFSM created!")

    def propagateEvent(self, event):
        if self.started:
            currentState = self.getCurrentState()
            if event in currentState.transitions:
                self.currentState = self.getStateByName(currentState.transitions[event])
                # TODO execute run method on state
            return True
        else:
            return False


    def addStates(self, states):
        for stateName in states:
            state = State(stateName)
            self._states.append(state)

    def addTransitions(self, transitions):
        for transition in transitions:
            self.addTransition(transition)

    def addTransition(self, transition):
        if self.validateTransition(transition) == True:
            print("Valid transition")
        else:
            print("Invalid transition")
            return

        # transition[origin,event, destiny]
        state = self.getStateByName(transition[0])
        state.transitions[transition[1]] = transition[2]
        print("Added transition %s + %s -> %s" % (transition[0], transition[1], transition[2]))

    def validateTransition(self, transition):
        if transition[1] in self._events:
            print("Valid event '%s'" % transition[1])
        else:
            return False
        if transition[0] in (state.name for state in self._states):
            print("Valid origin '%s'" % transition[0])
        else:
            return False
        if transition[2] in (state.name for state in self._states):
            print("Valid origin '%s'" % transition[2])
        else:
            return False

        # TODO check that transition does not overlap other transition
        return True

    def getStateByName(self, name):
        for state in self._states:
            if state.name == name:
                print("Found state '%s'" % name)
                break
        else:
            print("Not found")
            return False

        return state

    def getCurrentState(self):
        return self.currentState

    def startFSM(self):
        if self.initialState != None and self.currentState == None:
            self.currentState = self.getStateByName(self.initialState)
            self.started = True
            # TODO execute run on current state
            print("pyFSM::started")
            return True
        else:
            return False

    def stopFSM(self):
        if self.started:
            self.started = False
            print("pyFSM::stopped")
            return True
        else:
            return False
    # def updateFSM(self):
