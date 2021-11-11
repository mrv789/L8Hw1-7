class Math:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num


    def division_by_zero(first_num, second_num):
        if second_num != 0:
            return (first_num / second_num)
        else:
            return (f"Делить на ноль нельзя")


print(Math.division_by_zero(10, 0))
print(Math.division_by_zero(10, 0.1))
