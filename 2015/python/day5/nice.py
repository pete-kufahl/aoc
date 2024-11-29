"""
A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
"""

if __name__ == "__main__":

    file_name = "input.txt"
    disqual = { 'ab', 'cd', 'pq', 'xy' }
    vowels = { 'a', 'e', 'i', 'o', 'u' }
    try:
        nice_strings = 0
        strings = 0
        with open(file_name, 'r') as file:
            for line in file:
                strings += 1
                charlist = [x for x in line.strip()]
                num_vowels = 1 if charlist[0] in vowels else 0
                doubleletter = False
                disqualified = False
                for i in range(1, len(charlist), 1):
                    # print((charlist[i-1], charlist[i]), charlist[i-1] + charlist[i], 'True' if charlist[i-1] + charlist[i] in disqual else 'False')
                    if charlist[i-1] + charlist[i] in disqual:
                        disqualified = True
                        break
                    if charlist[i-1] == charlist[i]:
                        doubleletter = True
                    if charlist[i] in vowels:
                        num_vowels += 1
                if (not disqualified) and doubleletter and num_vowels > 2:
                    nice_strings += 1
        print(f'out of {strings} strings, found {nice_strings} nice strings')
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except IOError:
        print("An error occurred while reading the file.")