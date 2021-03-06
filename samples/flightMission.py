import pyfsmlib.state_machine as fsm


def idle():
    print("STATE IDLE")
    print("STATE IDLE::Waiting for initialization parameters")


def ready():
    print("STATE READY")
    print("STATE READY::Initialization done. Waiting for START")


def takeOff():
    print("STATE TAKING_OFF")
    print("STATE TAKING_OFF::Going to take off point")


def point1():
    print("STATE POINT1")
    print("STATE POINT1::Going to point1")

def point2():
    print("STATE POINT2")
    print("STATE POINT2::Going to point2")

def point3():
    print("STATE POINT3")
    print("STATE POINT3::Going to point3")

def point4():
    print("STATE POINT4")
    print("STATE POINT4::Going to point4")

def point5():
    print("STATE POINT5")
    print("STATE POINT5::Going to point5")

def land():
    print("STATE LANDING")
    print("STATE LANDING::Going to landing position")

def abort():
    print("STATE ABORTING")
    print("STATE ABORTING::Going to default position")


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

    # bind functions
    state_machine._states[0].run = idle
    state_machine._states[1].run = ready
    state_machine._states[2].run = takeOff
    state_machine._states[3].run = point1
    state_machine._states[4].run = point2
    state_machine._states[5].run = point3
    state_machine._states[6].run = point4
    state_machine._states[7].run = point5
    state_machine._states[8].run = land
    state_machine._states[9].run = abort

    state_machine.startFSM()

    state_machine.propagateEvent("initialized")

    state_machine.propagateEvent("start_mission")
    state = ""
    while state != "IDLE":
        state_machine.propagateEvent("position_reached")
        state = state_machine.currentState.name

    print("Starting mission again")
    state_machine.propagateEvent("initialized")
    state_machine.propagateEvent("start_mission")
    state_machine.propagateEvent("position_reached")
    state_machine.propagateEvent("abort")
    state_machine.propagateEvent("position_reached")

# Call main application
runFlightMission()
