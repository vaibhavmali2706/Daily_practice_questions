height = [1,8,6,2,5,4,8,3,7]
max_area = 0
i = 0
j = len(height) - 1 
while i < j:
    area = min(height[i], height[j]) * (j - i)
    print(f"i: {i}, j: {j}, height[i]: {height[i]}, height[j]: {height[j]}, area: {area}")
    max_area = max(max_area, area)
    if height[i] < height[j]:
        i += 1
    else:
        j -= 1
print(max_area)