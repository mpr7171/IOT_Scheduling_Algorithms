from queue import Queue

processes = [
    {"name": "P1", "arrival_time": 0, "burst_time": 24, "priority": 3},
    {"name": "P2", "arrival_time": 4, "burst_time": 3, "priority": 1},
    {"name": "P3", "arrival_time": 5, "burst_time": 3, "priority": 4},
    {"name": "P4", "arrival_time": 6, "burst_time": 12, "priority": 2},
]

def calculate_times(schedule):
    waiting_time = [0] * len(schedule)
    turnaround_time = [0] * len(schedule)

    waiting_time[0] = 0

    for i in range(1, len(schedule)):
        waiting_time[i] = schedule[i - 1]["burst_time"] + waiting_time[i - 1] - schedule[i]["arrival_time"]
        if waiting_time[i] < 0:
            waiting_time[i] = 0

    for i in range(len(schedule)):
        turnaround_time[i] = schedule[i]["burst_time"] + waiting_time[i]

    return waiting_time, turnaround_time

# FCFS Scheduling
def fcfs_scheduling(processes):
    return sorted(processes, key=lambda x: x['arrival_time'])

# SJF Scheduling
def sjf_scheduling(processes):
    return sorted(processes, key=lambda x: (x['burst_time'], x['arrival_time']))

# Priority Scheduling
def ps_scheduling(processes):
    return sorted(processes, key=lambda x: x['priority'])

# Round Robin Scheduling
def rr_scheduling(processes, time_quantum):
    queue_rr = Queue()
    for process in processes:
        queue_rr.put(process)

    schedule = []
    current_time = 0

    while not queue_rr.empty():
        process = queue_rr.get()
        if process['burst_time'] <= time_quantum:
            schedule.append(process)
            current_time += process['burst_time']
        else:
            schedule.append({"name": process['name'], "arrival_time": current_time, "burst_time": time_quantum, "priority": process['priority']})
            current_time += time_quantum
            process['burst_time'] -= time_quantum
            queue_rr.put(process)

    return schedule

if __name__ == "__main__":
    print("FCFS Scheduling:")
    fcfs_schedule = fcfs_scheduling(processes)
    waiting_time, turnaround_time = calculate_times(fcfs_schedule)
    print("Process\tWaiting Time\tTurnaround Time")
    for i, process in enumerate(fcfs_schedule):
        print(f"{process['name']}\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print("\nSJF Scheduling:")
    sjf_schedule = sjf_scheduling(processes)
    waiting_time, turnaround_time = calculate_times(sjf_schedule)
    print("Process\tWaiting Time\tTurnaround Time")
    for i, process in enumerate(sjf_schedule):
        print(f"{process['name']}\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print("\nPriority Scheduling:")
    ps_schedule = ps_scheduling(processes)
    waiting_time, turnaround_time = calculate_times(ps_schedule)
    print("Process\tWaiting Time\tTurnaround Time")
    for i, process in enumerate(ps_schedule):
        print(f"{process['name']}\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print("\nRound Robin Scheduling:")
    time_quantum = 4
    rr_schedule = rr_scheduling(processes, time_quantum)
    waiting_time, turnaround_time = calculate_times(rr_schedule)
    print("Process\tWaiting Time\tTurnaround Time")
    for i, process in enumerate(rr_schedule):
        print(f"{process['name']}\t{waiting_time[i]}\t\t{turnaround_time[i]}")