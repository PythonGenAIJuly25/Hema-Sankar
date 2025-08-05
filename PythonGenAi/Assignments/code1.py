from collections import defaultdict, deque

def get_task_schedule(task_list, dependencies_list):
    dependency_graph = defaultdict(list)
    prerequisite_counts = {task: 0 for task in task_list}
    for dependent_task, prerequisite in dependencies_list:
        dependency_graph[prerequisite].append(dependent_task)
        prerequisite_counts[dependent_task] += 1
    execution_queue = deque([task for task in task_list if prerequisite_counts[task] == 0])
    scheduled_order = []
    while execution_queue:
        current_task = execution_queue.popleft()
        scheduled_order.append(current_task)
        for dependent_task in dependency_graph[current_task]:
            prerequisite_counts[dependent_task] -= 1
            if prerequisite_counts[dependent_task] == 0:
                execution_queue.append(dependent_task)
    if len(scheduled_order) == len(task_list):
        return scheduled_order
    else:
        return None

tasks1 = ["A", "B", "C", "D"]
dependencies1 = [("B", "A"), ("C", "B"), ("D", "A")]
print("Test Case 1:", get_task_schedule(tasks1, dependencies1))

tasks2 = ["X", "Y", "Z"]
dependencies2 = [("Y", "X"), ("Z", "Y"), ("X", "Z")]
print("Test Case 2:", get_task_schedule(tasks2, dependencies2))

tasks3 = ["P", "Q", "R"]
dependencies3 = []
print("Test Case 3:", get_task_schedule(tasks3, dependencies3))

tasks4 = ["compile", "test", "deploy", "build", "package"]
dependencies4 = [
    ("test", "compile"),
    ("deploy", "package"),
    ("package", "build"),
    ("build", "compile")
]
print("Test Case 4:", get_task_schedule(tasks4, dependencies4))