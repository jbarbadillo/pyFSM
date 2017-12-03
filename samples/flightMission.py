import pyfsm.state_machine as fsm


def idle():
    print("STATE IDLE")


def ready():
    print("STATE READY")


def takeOff():
    print("STATE TAKING_OFF")


def point1():
    print("STATE POINT1")


def point2():
    print("STATE POINT2")


def point3():
    print("STATE POINT3")


def point4():
    print("STATE POINT4")


def point5():
    print("STATE POINT5")


def land():
    print("STATE LANDING")


def abort():
    print("STATE ABORTING")



def runFlightMission():
    print("---------Sample Flight Mission using FSM-------------")

    states = ["IDLE", "READY", "TAKING_OFF", "POINT1", "POINT2", "POINT3", "POINT4", "POINT5", "LANDING", "ABORTING"]
    initial_state = "IDLE"
    events = ["initialized", "start_mission", "position_reached", "abort"]
    transitions = [["IDLE", "initialized", "READY"],
                   ["READY", "start_mission", "TAKING_OFF"],
                   ["TAKING_OFF", "position_reached", "POINT1"],
                   ["TAKING_OFF", "abort", "ABORTING"],
                   ["POINT1", "position_reached", "POINT2"],
                   ["POINT1", "abort", "ABORTING"],
                   ["POINT2", "position_reached", "POINT3"],
                   ["POINT2", "abort", "ABORTING"],
                   ["POINT3", "position_reached", "POINT4"],
                   ["POINT3", "abort", "ABORTING"],
                   ["POINT4", "position_reached", "POINT5"],
                   ["POINT4", "abort", "ABORTING"],
                   ["POINT5", "position_reached", "LANDING"],
                   ["POINT5", "abort", "ABORTING"],
                   ["LANDING", "position_reached", "IDLE"],
                   ["ABORTING", "position_reached", "IDLE"]]

    try:
        state_machine = fsm.StateMachine(states, initial_state, events, transitions)
    except ValueError:
        print("Could not create FSM!")
        return False

    state_machine.startFSM()

# Call main application
runFlightMission()
