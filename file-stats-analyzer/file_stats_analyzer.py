import math

def main():
    filename = input("Please enter the filename: ")
    
    try:
        with open(filename, "r") as file:
            numbers = [float(line.strip()) for line in file if line.strip()]

        count = len(numbers)
        minimum = min(numbers)
        maximum = max(numbers)
        average = sum(numbers) / count
        
        variance = sum((x - average) ** 2 for x in numbers) / (count - 1)
        
        std_dev = math.sqrt(variance)
        
        print("\nStats:")
        print(f"Number of Values: {count}")
        print(f"Minimum: {int(minimum) if minimum.is_integer() else minimum}")
        print(f"Maximum: {int(maximum) if maximum.is_integer() else maximum}")
        print(f"Average: {average:.2f}")
        print(f"Variance: {variance:.2f}")
        print(f"Standard Deviation: {std_dev:.2f}")
        
    except FileNotFoundError:
            print("Error: File not found. Please check the filename and try again.")
    except ValueError:
            print("Error: File contains nun-numeric data.")
            
if __name__ == "__main__":
    main()
