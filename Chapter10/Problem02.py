# Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:
    def square(self, num):
        result = num*num
        return result

    def cube(self, num):
        result = num*num*num
        return result

    def squareroot(self, num):
        result = num**0.5
        return result


num = int(input('Enter the number: '))
answer = Calculator()
print(
    f'''The square of {num} is :{answer.square(num)}\n
    The cube of {num} is : {answer.cube(num)}\n
    The squareroot of {num} is : {answer.squareroot(num)}\n'''
      )
