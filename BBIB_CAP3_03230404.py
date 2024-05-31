################################
# https://github.com/Ugyen2003/03230404_BIA101_CAP3
# Ugyen Pem
# B 
# 03230404
################################
# REFERENCES
# Links that you referred while solving 
# the problem
# https://youtu.be/DCaKj3eIrro?si=G5m9idptKfF7y4v5 
################################
# SOLUTION
# Your Solution Score: 494730
################################

def process_line(line):
    """
    Process a line to find and perform operations on two-digit numbers.
    """
    left_pointer = 0
    right_pointer = len(line) - 1

    left_number = None
    right_number = None

    while left_pointer < len(line) and right_pointer >= 0:
        if left_number is None and line[left_pointer].isdigit():
            left_number = line[left_pointer]
        else:
            left_pointer += 1

        if right_number is None and line[right_pointer].isdigit():
            
            right_number = line[right_pointer]
        else:
            right_pointer -= 1

        if left_number is not None and right_number is not None:
            break

    if left_number is not None and right_number is not None:
        return int(left_number + right_number)  # Summing adjacent two-digit numbers
    elif left_number is not None:
        return int(left_number * 2)  # Doubling standalone two-digit numbers on the left
    elif right_number is not None:
        return int(right_number * 2)  # Doubling standalone two-digit numbers on the right
    else:
        return 0

def main():
    """
    Main function to read data from the text file and calculate the sum of processed numbers.
    """
    file_path = "404.txt"  # Adjusted to a relative path for simplicity

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        total_sum = 0

        for line in lines:
            line = line.strip()
            two_digit_number = process_line(line)
            total_sum += two_digit_number

        print("The sum of all processed numbers is:", total_sum)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    main()
    
    
    


