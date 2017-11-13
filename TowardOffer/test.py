sequence = [7,4,6,5]
left_tree = []
right_tree = []
for i in range(len(sequence)):
    if sequence[i] < sequence[-1]:    # left tree
        left_tree.append(sequence[i])
    else:
        right_tree.extend(sequence[i:-1])
        break

print left_tree
print right_tree