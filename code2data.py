f = open("code2data.txt", mode="w", encoding="utf-8")

relationship_set = ["+", "-", "*", "/"]

text_list__plus = ["what is {} plus {} ",
                   "I have {} apples. Peter has {} apples. How many do we have in total ?"]

for number1 in range(0, 10):
    for number2 in range(0, 10):
        for text in text_list__plus:
            one_data = []
            one_data.append(text.format(number1, number2))
            numbers = "{},{}".format(number1, number2)
            one_data.append(numbers)
            relationship = "+"
            one_data.append(relationship)
            one_data.append("compute2number")
            print(one_data)
            f.write(" # ".join(one_data) + "\n")
