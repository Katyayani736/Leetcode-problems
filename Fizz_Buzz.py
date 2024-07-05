class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        Generates a list containing "Fizz", "Buzz", "FizzBuzz", or the number itself 
        for each integer from 1 to n (inclusive).

        Args:
            n: The upper limit of the range (inclusive).

        Returns:
            A list of strings representing the FizzBuzz sequence.
        """

        result = []
        for i in range(1, n + 1):  # Iterate through numbers from 1 to n (inclusive)
            # Check for divisibility by both 3 and 5 (FizzBuzz)
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            # Check for divisibility by 3 only (Fizz)
            elif i % 3 == 0:
                result.append("Fizz")
            # Check for divisibility by 5 only (Buzz)
            elif i % 5 == 0:
                result.append("Buzz")
            # Otherwise, append the number as a string
            else:
                result.append(str(i))
        return result

# Main function for user input and function call
def main():
    solution = Solution()
    while True:
        try:
            user_input = int(input("Enter an upper limit (positive integer): "))
            if user_input <= 0:
                print("Please enter a positive integer.")
                continue
            result = solution.fizzBuzz(user_input)
            print(result)
            break  # Exit the loop after valid input
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
