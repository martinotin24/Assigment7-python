#!/usr/bin/env python3
import sys
import argparse

def parse_input(numbers_str):
    try:
        # Convert comma-separated values to a list of integers
        numbers = [int(n.strip()) for n in numbers_str.split(',')]
    except ValueError:
        print("Error: All inputs must be integers.")
        sys.exit(1)
    return numbers

def bitwise_operations(numbers):
    if not numbers:
        return None, None, None
    # Initialize with the first number
    bitwise_and = numbers[0]
    bitwise_or = numbers[0]
    bitwise_xor = numbers[0]
    
    # Perform operations on the rest of the numbers
    for num in numbers[1:]:
        bitwise_and &= num
        bitwise_or |= num
        bitwise_xor ^= num
    return bitwise_and, bitwise_or, bitwise_xor

def filter_numbers(numbers, threshold):
    # Return numbers greater than the threshold
    return [num for num in numbers if num > threshold]

def main():
    parser = argparse.ArgumentParser(description="Perform bitwise operations and filtering on a list of integers.")
    parser.add_argument('--numbers', type=str, required=True, help='Comma-separated list of integers')
    parser.add_argument('--threshold', type=int, default=0, help='Threshold for filtering numbers')
    args = parser.parse_args()

    numbers = parse_input(args.numbers)
    and_result, or_result, xor_result = bitwise_operations(numbers)
    filtered_numbers = filter_numbers(numbers, args.threshold)

    print("Bitwise AND:", and_result)
    print("Bitwise OR:", or_result)
    print("Bitwise XOR:", xor_result)
    print("Numbers greater than threshold:", filtered_numbers)

if __name__ == "__main__":
    main()
