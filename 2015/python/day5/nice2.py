"""
Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
"""

if __name__ == "__main__":

    file_name = "input.txt"

    try:
        nice_strings = 0
        strings = 0

        with open(file_name, 'r') as file:
            for line in file:
                strings += 1
                rule1, rule2 = False, False
                charlist = [x for x in line.strip()]
                # character-pair -> index of second letter
                char_pairs = {}
                for i in range(len(charlist) - 1):
                    if not rule1:
                        cp = charlist[i] + charlist[i+1]
                        if cp in char_pairs and i > char_pairs[cp]:
                            rule1 = True
                        elif cp not in char_pairs:
                            char_pairs[cp] = i+1

                    if not rule2 and i < len(charlist) - 2:
                        if charlist[i] == charlist[i+2]:
                            rule2 = True

                if rule1 and rule2:
                    nice_strings += 1

            print(f'out of {strings} strings, found {nice_strings} nice strings')
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except IOError:
        print("An error occurred while reading the file.")