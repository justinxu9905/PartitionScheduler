from abc import ABC, abstractmethod


class Algorithm(ABC):
    @abstractmethod
    def __call__(self, cluster, clock):
        pass


class ThresholdFirstFitAlgorithm(Algorithm):
    def __call__(self, cluster, clock, cpu_threshold=0.75, memory_threshold=0.75, disk_threshold=0.75):
        instances_to_reschedule = [inst for machine in cluster.machines_to_schedule for inst in machine.instances.values()]
        machines = cluster.machines.values()
        for inst in instances_to_reschedule:
            if inst.machine.to_schedule:
                inst.machine.to_schedule = False
                cluster.machines_to_schedule.remove(inst.machine)
            inst.machine.pop(inst.id)
        for inst in instances_to_reschedule:
            for machine in machines:
                if machine.accommodate_w(inst):
                    machine.push(inst)
