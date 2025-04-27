# exception -> an event that interrupts the flow of a program
# ZeroDivisionError, TypeError, ValueError
# Try -> Except -> Finally

try:
    number = int(input("Enter a number: "))
    print(123/number)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Enter only numbers.")
except Exception:
    print("Sth went wroong.")
finally:
    print("Do some cleanup here.")