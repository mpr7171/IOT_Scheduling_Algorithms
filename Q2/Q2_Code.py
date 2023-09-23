import queue

patients = [
    {"name": "A", "arrival_time": 0, "treatment_time": 30, "urgency_level": 3},
    {"name": "B", "arrival_time": 10, "treatment_time": 20, "urgency_level": 5},
    {"name": "C", "arrival_time": 15, "treatment_time": 40, "urgency_level": 2},
    {"name": "D", "arrival_time": 20, "treatment_time": 15, "urgency_level": 4},
]

def print_schedule(schedule):
    print("Patient Schedule:")
    for i, patient in enumerate(schedule):
        print(f"{i + 1}. Patient {patient['name']} (Urgency: {patient['urgency_level']})")

# FCFS Scheduling
def fcfs_scheduling(patients):
    return sorted(patients, key=lambda x: x['arrival_time'])

# SJF Scheduling
def sjf_scheduling(patients):
    return sorted(patients, key=lambda x: x['treatment_time'])

# Priority Scheduling
def ps_scheduling(patients):
    return sorted(patients, key=lambda x: x['urgency_level'], reverse=True)  # Higher urgency is higher priority

# Round Robin Scheduling
def rr_scheduling(patients, time_quantum):
    queue_rr = queue.Queue()
    for patient in patients:
        queue_rr.put(patient)

    schedule = []
    current_time = 0

    while not queue_rr.empty():
        patient = queue_rr.get()
        if patient['treatment_time'] <= time_quantum:
            schedule.append(patient)
            current_time += patient['treatment_time']
        else:
            schedule.append({"name": patient['name'], "arrival_time": current_time, "treatment_time": time_quantum, "urgency_level": patient['urgency_level']})
            current_time += time_quantum
            patient['treatment_time'] -= time_quantum
            queue_rr.put(patient)

    return schedule

if __name__ == "__main__":
    print("FCFS Scheduling:")
    fcfs_schedule = fcfs_scheduling(patients)
    print_schedule(fcfs_schedule)

    print("\nSJF Scheduling:")
    sjf_schedule = sjf_scheduling(patients)
    print_schedule(sjf_schedule)

    print("\nPriority Scheduling:")
    ps_schedule = ps_scheduling(patients)
    print_schedule(ps_schedule)

    print("\nRound Robin Scheduling:")
    time_quantum = 10
    rr_schedule = rr_scheduling(patients, time_quantum)
    print_schedule(rr_schedule)