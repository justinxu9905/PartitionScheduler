from abc import ABC, abstractmethod


class Trigger(ABC):
    @abstractmethod
    def __call__(self, cluster, clock):
        pass


class ThresholdTrigger(Trigger):
    def __call__(self, cluster, clock, cpu_threshold=0.75, memory_threshold=0.75, disk_threshold=0.75):
        for machine in cluster.machines.values():
            if machine.cpu / machine.cpu_capacity <= (1 - cpu_threshold) \
                    or machine.memory / machine.memory_capacity <= (1 - memory_threshold) \
                    or machine.disk / machine.disk_capacity <= (1 - disk_threshold):
                machine.to_schedule = True
                cluster.machines_to_schedule.add(machine)
