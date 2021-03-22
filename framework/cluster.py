from framework.machine import Machine


class Cluster(object):
    def __init__(self):
        self.machines = {}
        self.machines_to_schedule = set()

    def configure_machines(self, machine_configs):
        for machine_config in machine_configs:
            machine = Machine(machine_config)
            self.machines[machine.id] = machine
            machine.attach(self)

    def configure_instances(self, instance_configs):
        for instance_config in instance_configs:
            machine_id = instance_config.machine_id
            machine = self.machines.get(machine_id, None)
            assert machine is not None
            machine.add_instance(instance_config)

    @property
    def structure(self):
        return {
            i: {
                    'cpu_capacity': m.cpu_capacity,
                    'memory_capacity': m.memory_capacity,
                    'disk_capacity': m.disk_capacity,
                    'cpu': m.cpu,
                    'memory': m.memory,
                    'disk': m.disk,
                    'instances': {
                        j: {
                            'cpu': inst.cpu,
                            'memory': inst.memory,
                            'disk': inst.disk
                        } for j, inst in m.instances.items()
                    }
                }
            for i, m in self.machines.items()
        }