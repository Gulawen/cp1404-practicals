# Find the error in the following program.
def main():
    # Get a value from the user.
    value = int(input("Enter a value."))
    # Get 10 percent of the value.
    ten_percent(value)
    # Display 10 percent of the value.

    print("10 percent of ", value, " is ",ten_percent(value))

# The ten_percent function returns 10 percent
# of the argument passed to the function.
def ten_percent(num):
    return num * 0.1

main()
