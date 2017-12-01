import unittest
import state_machine as fsm


class TestCreateFSM(unittest.TestCase):
    def test_create_state_machine(self):
        states = ["READY", "RUNNING", "IDLE"]
        initial_state = "IDLE"
        events = ["initialized","start","finish"]
        transitions=[]
        transitions.append(["IDLE","initialized","READY"])
        transitions.append(["READY", "start", "RUNNING"])
        transitions.append(["RUNNING", "finish", "IDLE"])
        self.state_machine = fsm.StateMachine(states,initial_state, events, transitions)

        self.assertEqual(self.state_machine.getCurrentState().name, "IDLE")
        self.assertEqual(len(self.state_machine._states), 3)
        self.assertEqual(len(self.state_machine._events), 3)


if __name__ == '__main__':
    unittest.main()
