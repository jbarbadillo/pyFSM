class State:
    def __init__(self, name):
        self.name = name
        self._transitions = {}

    @classmethod
    def run(cls):
        pass


class StateMachine:
    currentState = None
    initialState = None

    def __init__(self, states, initial_state, events, transitions):
        self._states = []
        self.addStates(states)  # possible states
        self._events = events   # allowed events
        self.initialState = initial_state

        if not self.addTransitions(transitions):
            raise ValueError

        self.started = False
        print("pyFSM created!")
        #TODO print a summary of states and transitions

    def propagateEvent(self, event):
        if self.started:
            currentState = self.getCurrentState()
            if event in currentState._transitions:
                self.currentState = self.getStateByName(currentState._transitions[event])
                self.currentState.run()
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
            if not self.addTransition(transition):
                return False

        return True

    def addTransition(self, transition):
        if self.validateTransition(transition):
            pass
        else:
            # TODO explain why is invalid
            print("Invalid transition")
            return False

        # transition[origin,event, destiny]
        state = self.getStateByName(transition[0])
        state._transitions[transition[1]] = transition[2]
        return True

    def validateTransition(self, transition):
        if not transition[1] in self._events:
            print("Invalid transition: Event '%s' is not registered" % transition[1])
            return False
        if not transition[0] in (state.name for state in self._states):
            print("Invalid transition: Origin '%s' is not registered as a state" % transition[0])
            return False
        if not transition[2] in (state.name for state in self._states):
            print("Invalid transition: Target '%s' is not registered as a state" % transition[2])
            return False

        # check that transition does not overlap other transition
        state = self.getStateByName(transition[0])
        if transition[1] in state._transitions:
            print("A transition exists already for this event '%s' !" % transition[1])
            return False
        return True

    def getStateByName(self, name):
        for state in self._states:
            if state.name == name:
                break
        else:
            print("Not found state %s" % name)
            return False

        return state

    def getCurrentState(self):
        return self.currentState

    def checkValidStates(self):
        # checks that all states have valid transitions and a function bound
        for state in self._states:
            if len(state.transitions) < 1 and self.isEmptyFunction(state.run()):
                return False

        return True

    @staticmethod
    def isEmptyFunction(func):
        def empty_func():
            pass

        return func.__code__.co_code == empty_func.__code__.co_code

    def startFSM(self):
        if self.initialState != None and self.checkValidStates:
            if self.currentState == None:
                self.currentState = self.getStateByName(self.initialState)

            self.started = True
            self.currentState.run()
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

    def updateFSM(self):
        if self.started and self.currentState:
            self.currentState.run()
            return True
        else:
            return False
