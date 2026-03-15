import heapq

priority_map = {
    "Red": 1,
    "Yellow": 2,
    "Green": 3
}

class PatientQueue:

    def __init__(self):
        self.queue = []

    def add_patient(self, patient, triage):

        priority = priority_map[triage]

        heapq.heappush(self.queue, (priority, patient))

    def get_next_patient(self):

        if not self.queue:
            return None

        return heapq.heappop(self.queue)[1]