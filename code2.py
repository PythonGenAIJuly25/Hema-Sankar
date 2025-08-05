def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

test1 = [[1,3],[2,6],[8,10],[15,18]]
result1 = merge_intervals(test1)
print(f"Test Case 1: {test1} -> {result1}")

test2 = [[1,4],[4,5]]
result2 = merge_intervals(test2)
print(f"Test Case 2: {test2} -> {result2}")

test3 = [[1,4],[2,3]]
result3 = merge_intervals(test3)
print(f"Test Case 3: {test3} -> {result3}")

test4 = [[1,2],[3,4],[5,6]]
result4 = merge_intervals(test4)
print(f"Test Case 4: {test4} -> {result4}")

test5 = [[1,4],[2,5],[3,6]]
result5 = merge_intervals(test5)
print(f"Test Case 5: {test5} -> {result5}")

test6 = [[6,7],[2,4],[5,9]]
result6 = merge_intervals(test6)
print(f"Test Case 6: {[[6,7],[2,4],[5,9]]} -> {result6}")

test7 = [[1,4]]
result7 = merge_intervals(test7)
print(f"Test Case 7: {test7} -> {result7}")

test8 = [[2,3],[4,5],[6,7],[8,9],[1,10]]
result8 = merge_intervals(test8)
print(f"Test Case 8: {[[2,3],[4,5],[6,7],[8,9],[1,10]]} -> {result8}")