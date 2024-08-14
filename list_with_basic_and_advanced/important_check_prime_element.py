def check_prime_list(list_of_elements):
    def is_prime(n):
        if n <= 1:
            return False
        for num in range(2, int(n**0.5) + 1):
            if n % num == 0:
                return False
        return True

    return all(is_prime(element) for element in list_of_elements)


list_1 = [0, 3, 4, 7, 9]
list_2 = [3, 5, 7, 13]
list_3 = [1, 5, 3]

print(check_prime_list(list_1))  # Should return False
print(check_prime_list(list_2))  # Should return True
print(check_prime_list(list_3))  # Should return False
