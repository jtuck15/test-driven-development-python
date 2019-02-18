def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count
    
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One uppercase letter"
assert count_upper_case("AB") == 2, "Two uppercase letters"
assert count_upper_case("a") == 0, "One lowercase letter"
assert count_upper_case("aBcDeFgHiJkL") == 6, "Mix of upper and lowercase letters"
assert count_upper_case("£@$%^") == 0, "Special characters"
assert count_upper_case("aBcD$%&328&Jf") == 3, "Mix of numbers, special, upper and lower case"

print("All test passed!")