sentence = "Hey my name is {1} and I am from {0}"

name = "Shiv"
college = "RGIT"

print(sentence.format(name,college))

# f-string
print(f" We use f-strings like this: Hey my name is {{name}} and I am from {{college}}")

price = 99.09999
txt = f"For only {price: .2f} dollars!"
print(txt)
