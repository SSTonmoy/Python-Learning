# Add a static method in problem 2, to greet the user with hello.
class Calculator:

    @staticmethod
    def greet():
        print('Hello, User.')

    def square(self, num):
        result = num*num
        return result

    def cube(self, num):
        result = num*num*num
        return result

    def squareroot(self, num):
        result = num**0.5
        return result


Calculator.greet()
num = int(input('Enter the number: '))
answer = Calculator()
print(f'The square of {num} is :{answer.square(num)}\nThe cube of {num} is : {answer.cube(num)}\nThe squareroot of {num} is : {answer.squareroot(num)}\n')
