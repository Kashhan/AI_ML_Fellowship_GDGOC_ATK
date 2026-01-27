numbers = [5, 2, 8, 2, 5, 9, 1]

unique_numbers = list(set(numbers))
sorted_numbers = sorted(unique_numbers)
maximum = max(sorted_numbers)
minimum = min(sorted_numbers)
average = sum(sorted_numbers) / len(sorted_numbers)

print("Original:", numbers)
print("Unique:", unique_numbers)
print("Sorted:", sorted_numbers)
print("Max:", maximum)
print("Min:", minimum)
print("Average:", average)
