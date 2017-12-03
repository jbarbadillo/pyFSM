import unittest
import pyfsm.state_machine as fsm


class TestCreateFSM(unittest.TestCase):
    # Creates a valid state machine
    def test_create_FSM(self):
        states = ["READY", "RUNNING", "IDLE"]
        initial_state = "IDLE"
        events = ["initialized", "start", "finish"]
        transitions = [["IDLE", "initialized", "READY"], ["READY", "start", "RUNNING"], ["RUNNING", "finish", "IDLE"]]
        self.state_machine = fsm.StateMachine(states, initial_state, events, transitions)

        self.assertEqual(self.state_machine.initialState, "IDLE")
        self.assertEqual(len(self.state_machine._states), 3)
        self.assertEqual(len(self.state_machine._events), 3)
        self.assertEqual(self.state_machine.currentState, None)

    # Creates a state machine with invalid transitions
    def test_create_bad_transitions(self):
        states = ["READY", "RUNNING", "IDLE"]
        initial_state = "IDLE"
        events = ["initialized", "start", "finish"]
        transitions = [["IDLE", "initialized", "READY"], ["ABORTED", "start", "RUNNING"], ["RUNNING", "finish", "IDLE"]]

        # Exception on invalid transitions due to invalid origin state ABORTED
        with self.assertRaises(ValueError):
            self.state_machine = fsm.StateMachine(states, initial_state, events, transitions)





    def test_start_FSM(self):
        states = ["READY", "RUNNING", "IDLE"]
        initial_state = "IDLE"
        events = ["initialized", "start", "finish"]
        transitions = [["IDLE", "initialized", "READY"], ["READY", "start", "RUNNING"], ["RUNNING", "finish", "IDLE"]]
        self.state_machine = fsm.StateMachine(states, initial_state, events, transitions)

        self.assertEqual(self.state_machine.started, False)
        # TODO test return values on start
        self.state_machine.startFSM()
        self.assertEqual(self.state_machine.currentState.name, "IDLE")
        self.assertEqual(self.state_machine.started, True)

    def test_propagate_event(self):
        states = ["READY", "RUNNING", "IDLE"]
        initial_state = "IDLE"
        events = ["initialized", "start", "finish"]
        transitions = [["IDLE", "initialized", "READY"], ["READY", "start", "RUNNING"], ["RUNNING", "finish", "IDLE"]]
        self.state_machine = fsm.StateMachine(states, initial_state, events, transitions)

        self.state_machine.startFSM()
        response = self.state_machine.propagateEvent("initialized")
        self.assertEqual(response, True)
        self.assertEqual(self.state_machine.currentState.name, "READY")

    def test_stop_FSM(self):
        states = ["READY", "RUNNING", "IDLE"]
        initial_state = "IDLE"
        events = ["initialized", "start", "finish"]
        transitions = [["IDLE", "initialized", "READY"], ["READY", "start", "RUNNING"], ["RUNNING", "finish", "IDLE"]]
        self.state_machine = fsm.StateMachine(states, initial_state, events, transitions)

        #Try to stop without starting
        response = self.state_machine.stopFSM()
        self.assertEqual(response, False)

        #Start and stop
        response = self.state_machine.startFSM()
        self.assertEqual(response, True)
        response = self.state_machine.stopFSM()
        self.assertEqual(response, True)

    def test_bind_methods(self):
        print("---------   TEST BIND METHODS -------------")
        def ready():
            print("STATE READY")

        def running():
            print("STATE RUNNING")

        def idle():
            print("STATE IDLE")

        states = ["READY", "RUNNING", "IDLE"]
        initial_state = "IDLE"
        events = ["initialized", "start", "finish"]
        transitions = [["IDLE", "initialized", "READY"], ["READY", "start", "RUNNING"], ["RUNNING", "finish", "IDLE"]]
        self.state_machine = fsm.StateMachine(states, initial_state, events, transitions)

        #bind functions
        self.state_machine._states[0].run = ready
        self.state_machine._states[1].run = running
        self.state_machine._states[2].run = idle

        self.state_machine.startFSM()
        self.state_machine.updateFSM()

        self.state_machine.propagateEvent("initialized")
        response = self.state_machine.updateFSM()
        self.assertEqual(response, True)

        self.state_machine.propagateEvent("start")
        response = self.state_machine.updateFSM()
        self.assertEqual(response, True)

        self.state_machine.propagateEvent("finish")
        response = self.state_machine.updateFSM()
        self.assertEqual(response, True)
        print("---------------------------------------------")

if __name__ == '__main__':
    unittest.main()
