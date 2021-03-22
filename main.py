from data.loader import InstanceConfigLoader, MachineConfigLoader
from framework.algorithm import ThresholdFirstFitAlgorithm
from framework.instance import InstanceConfig
from framework.machine import MachineConfig
from framework.simulation import Simulation
from framework.trigger import ThresholdTrigger

if __name__ == '__main__':
    machine_configs = [
        MachineConfig(0, 12, 20, 20),
        MachineConfig(1, 21, 25, 25)
    ]  # MachineConfigLoader('./data/machine_resources.a.csv')

    instance_configs = [
        InstanceConfig(0, 0, 3, 5, 5, [3, 6, 5], [5, 5, 5]),
        InstanceConfig(1, 0, 3, 5, 5, [3, 2, 1], [5, 5, 5]),
        InstanceConfig(2, 1, 5, 5, 5, [5, 5, 5], [5, 5, 5]),
        InstanceConfig(3, 1, 5, 5, 5, [5, 5, 5], [5, 5, 5]),
        InstanceConfig(4, 1, 5, 5, 5, [5, 5, 5], [5, 5, 5])
    ]  # InstanceConfigLoader('./data/output_instance_deployed_a.csv')

    sim = Simulation(machine_configs, instance_configs, ThresholdTrigger(), ThresholdFirstFitAlgorithm())
    sim.run()
    print(sim.cluster.structure)
