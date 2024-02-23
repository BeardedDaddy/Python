def bubble_sort(data: list) -> None:
    """Sorts a list in place."""
    n = len(data)
    comparison_count = 0
    
    for i in range(n -1):
        for i in range(n - 1):
            comparison_count += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                
                
x = 1
y = 2
print(x, y)

x, y = y, x
print(x, y)
