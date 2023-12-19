def calculate_sum(input_pattern):
    rows = input_pattern.strip().split('\n')
    total_sum = 0

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            current_char = rows[i][j]
            
            if current_char.isdigit() or current_char == '-' and j + 1 < len(rows[i]) and rows[i][j+1].isdigit():
                # Handling negative numbers
                if current_char == '-':
                    current_char += rows[i][j+1]
                    j += 1
                
                current_sum = int(current_char)
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

                for ni, nj in neighbors:
                    if 0 <= ni < len(rows) and 0 <= nj < len(rows[ni]) and rows[ni][nj].isdigit():
                        current_sum += int(rows[ni][nj])

                total_sum += current_sum

    return total_sum

# Example usage with the provided input
input_pattern = "467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598.."

result = calculate_sum(input_pattern)
print("Sum of numbers adjacent to symbols:", result)
