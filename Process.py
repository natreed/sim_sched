import enum

DEFAULT_BUDGET = 50

#States that a
class P_State(enum.Enum):
    CREATED = 0
    READY = 1
    RUNNING = 2
    BLOCKED = 3
    ZOMBIE = 4
    FINISHED = 5

class P_Priority(enum.Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3

#TODO: Did not include blocking conditions to keep it simple
#starting with only required cpu time.
#The process is just the state of the process. The scheduler
#will make changes as necessary to the process state
class Process(object):
    def __init__(self, _required_cpu_time, _instantiation_time, _pid):
        self.pid = _pid
        self.time_slice = 0
        self.p_state = P_State.CREATED
        self.next_state = P_State.RUNNING
        self.required_cpu_time = _required_cpu_time
        self.cpu_time_remaining = _required_cpu_time
        #time process is scheduled first
        self.start_time = 0
        #updated every time process is fetched
        self.cpu_arrival = []
        # Queue length and fetch count will be aggregated across all processes
        # in the simulation and used to calculate avg queue length.
        # queue lengths are taken each time process is scheduled.
        self.queue_lens = []
        #number of times scheduled
        self.fetch_count = 0
        self.instantiation_time = _instantiation_time
        self.finish_time = 0
        self.total_runtime = 0
        self.p_priority = P_Priority.ZERO
        self.p_budget = DEFAULT_BUDGET
