# python3


def max_pairwise_product(numbers):
    lenght = len(numbers)
    list = sorted(numbers)
    max_product = list[lenght - 1] * list[lenght - 2]
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
