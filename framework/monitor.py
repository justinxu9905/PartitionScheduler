class Monitor(object):
    def __init__(self, env, trigger):
        self.env = env
        self.trigger = trigger
        self.simulation = None
        self.cluster = None

    def attach(self, simulation):
        self.simulation = simulation
        self.cluster = simulation.cluster

    def sample(self):
        for instance, instance_cpu_curve in self.simulation.instance_cpu_curves.items():
            instance.cpu = instance_cpu_curve.pop(0)
        for instance, instance_memory_curve in self.simulation.instance_memory_curves.items():
            instance.memory = instance_memory_curve.pop(0)
        return True

    def run(self):
        while not self.simulation.finished:
            self.sample()
            self.trigger(self.cluster, self.env.now)
            if self.cluster.machines_to_schedule:
                print('At', self.env.now, 'scheduler was triggered!')
                self.simulation.scheduler.run()
            yield self.env.timeout(15)
