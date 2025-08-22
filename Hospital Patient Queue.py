import heapq
from collections import deque
import time

class Patient:
    def __init__(self, name, is_emergency=False):
        self.name = name
        self.is_emergency = is_emergency
        self.arrival_time = time.time()

class HospitalQueue:
    def __init__(self, avg_time_per_patient=10):
        self.emergency_queue = []
        self.regular_queue = deque()
        self.avg_time = avg_time_per_patient
        self.counter = 0

    def add_patient(self, name, is_emergency=False):
        patient = Patient(name, is_emergency)
        if is_emergency:
            heapq.heappush(self.emergency_queue, (self.counter, patient))
            self.counter += 1
        else:
            self.regular_queue.append(patient)

    def next_patient(self):
        if self.emergency_queue:
            return heapq.heappop(self.emergency_queue)[1]
        elif self.regular_queue:
            return self.regular_queue.popleft()
        return None

    def estimated_wait_time(self, name):
        pos = 0
        for _, p in self.emergency_queue:
            pos += 1
            if p.name == name:
                return pos * self.avg_time
        for i, p in enumerate(self.regular_queue):
            if p.name == name:
                return (len(self.emergency_queue) + i + 1) * self.avg_time
        return None

hospital = HospitalQueue()
hospital.add_patient("Alice", True)
hospital.add_patient("Bob", False)
hospital.add_patient("Charlie", False)
hospital.add_patient("David", True)

print(hospital.estimated_wait_time("Bob"))
print(hospital.next_patient().name)
print(hospital.next_patient().name)
print(hospital.estimated_wait_time("Charlie"))
