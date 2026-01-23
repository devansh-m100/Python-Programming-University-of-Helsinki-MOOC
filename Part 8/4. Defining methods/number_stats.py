# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.total = 0

    def add_number(self, number: int):
        self.numbers += 1
        self.total += number

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        if self.numbers == 0:
            return 0
        return self.total

    def average(self):
        if self.numbers == 0:
            return 0
        return self.total / self.numbers
    
stats_all = NumberStats()
stats_even = NumberStats()
stats_odd = NumberStats()
print("Please type in integer numbers:")
while True:
    input_num = int(input())
    if input_num == -1:
        break
    stats_all.add_number(input_num)

    if input_num % 2 == 0:
        stats_even.add_number(input_num)
    else:
        stats_odd.add_number(input_num)

print("Sum of numbers:", stats_all.get_sum())
print("Mean of numbers:", stats_all.average())
print("Sum of even numbers:", stats_even.get_sum())
print("Sum of odd numbers:", stats_odd.get_sum())
