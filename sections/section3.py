# 3.1.1 Numbers.
print(f"2 + 2 = {2 + 2}")
print(f"50 - 5*6 = {50 - 5*6}")
print(f"(50 - 5*6) / 4 = {(50 - 5*6) / 4}")
print(f"8 / 5 = {8 / 5}")

print(f"17 / 3 = {17 / 3}")
print(f"17 / 3 = {17 // 3} (floor division)")
print(f"17 / 3 = {17 % 3} (remainder)")

print(f"5 ** 2 = {5 ** 2}")

width = 20
height = 5 * 9
area = width * height
print("width * height = {area}")

print(f"round(5.1234, 2) = {round(5.1234, 2)}")

# 3.1.2 Strings
print('doesn\'t (using a backslash to "escape" the quotes)')
print("doesn't (using single and double quotes)")
print(r"C:\some\name (using a raw string to avoid backslash problems)")
print(
    """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
     (This is a multi-line string.)
"""
)
print(3 * "un" + "ium (using maths with strings)")
text = "Put seveal strings within parentheses " "to have them joined together"
print(text)
word = "Python"
print(f"word = {word}")
print(f"word[0] = {word[0]}")
print(f"word[-6:-4] = {word[-6:-4]}")
print(f"word[-2:] = {word[-2:]}")
print(f"len(word) = {len(word)}")

# 3.1.3 Lists
squares = [1, 4, 9, 16, 25]
print(f"squares[-3:] = {squares[-3:]}")
print(f"squares + [36, 49, 64, 81, 100] = {squares + [36, 49, 64, 81, 100]}")
cubes = [1, 8, 27, 65, 125]
print(f"Cubes with a typo: {cubes}")
cubes[3] = 64
cubes.append(216)
print(f"Cubes corrected and extended: {cubes}")
cubes[:] = []
print(f"Cubes list cleared: {cubes}")
nested_list = [["a", "b", "c"], ["0", "1", "2"]]
print(f"nested_list[0]: {nested_list[0]}")
print(f"nested_list[1]: {nested_list[1]}")
print(f"nested_list[0][1]: {nested_list[0][1]}")

# 3.2 First Steps Towards Programming
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b
