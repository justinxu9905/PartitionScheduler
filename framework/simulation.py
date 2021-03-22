import simpy

from framework.cluster import Cluster
from framework.monitor import Monitor
from framework.scheduler import Scheduler


class Simulation(object):
    def __init__(self, machine_configs, instance_configs, trigger, algorithm):
        self.env = simpy.Environment()

        self.cluster = Cluster()
        self.cluster.configure_machines(machine_configs)
        self.cluster.configure_instances(instance_configs)

        self.instance_cpu_curves = {
            self.cluster.machines[instance_config.machine_id].instances[instance_config.id]:
                instance_config.cpu_curve for instance_config in instance_configs
        }
        self.instance_memory_curves = {
            self.cluster.machines[instance_config.machine_id].instances[instance_config.id]:
                instance_config.memory_curve for instance_config in instance_configs
        }

        self.monitor = Monitor(self.env, trigger)
        self.scheduler = Scheduler(self.env, algorithm)

        self.monitor.attach(self)
        self.scheduler.attach(self)

    def run(self):
        self.env.process(self.monitor.run())
        # self.env.process(self.scheduler.run())
        self.env.run()

    @property
    def finished(self):
        for instance_cpu_curve in self.instance_cpu_curves.values():
            if not instance_cpu_curve:
                return True
        for instance_memory_curve in self.instance_memory_curves.items():
            if not instance_memory_curve:
                return True
        return False
