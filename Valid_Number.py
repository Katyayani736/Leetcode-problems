class Solution:
    def isNumber(self, s: str) -> bool:
        """
        Checks if a string `s` represents a valid number.

        Args:
            s: The string to be evaluated.

        Returns:
            True if `s` is a valid number, False otherwise.
        """

        n, e, d, o = False, False, False, False
        for i in s:
            if i in "0123456789":
                n = True
            elif i in "+-":
                if n or d or o:
                    return False
                else:
                    o = True
            elif i in "eE":
                if e or not n:
                    return False
                else:
                    d = False  # Reset decimal flag
                    o = False  # Reset operator flag
                    e = True
                    n = False  # Allow digits after exponent
            elif i == ".":
                if e or d:
                    return False
                else:
                    d = True
            else:
                return False
        return n  # Return True if at least one digit present

# Main function for user input and function call
def main():
    solution = Solution()
    while True:
        user_input = input("Enter a string (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        result = solution.isNumber(user_input)
        if result:
            print(f"'{user_input}' is a valid number.")
        else:
            print(f"'{user_input}' is not a valid number.")

if __name__ == "__main__":
    main()
