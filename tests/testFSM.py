import unittest
import pyfsm.state_machine as fsm


class TestCreateFSM(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
