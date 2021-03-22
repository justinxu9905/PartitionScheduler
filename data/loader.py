import csv

from framework.instance import InstanceConfig
from framework.machine import MachineConfig


def MachineConfigLoader(filename):  # id, cpu_capacity, memory_capacity, disk_capacity...
    machine_configs = []
    with open(filename) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            machine_id, cpu_capacity, memory_capacity, disk_capacity = row[0], float(row[1]), float(row[2]), float(row[3])
            machine_configs.append(MachineConfig(machine_id, cpu_capacity, memory_capacity, disk_capacity))
    return machine_configs


def InstanceConfigLoader(filename):
    instance_configs = []
    with open(filename) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            inst_id, machine_id, cpu_curve, memory_curve, disk = row[0], row[2], [float(cpu) for cpu in row[3].split('|')], [float(memory) for memory in row[4].split('|')], float(row[5])
            instance_configs.append(InstanceConfig(inst_id, machine_id, cpu_curve[0], memory_curve[0], disk, cpu_curve, memory_curve))
    return instance_configs
