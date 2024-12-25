letter ="Hey My Name is {} and i am from {}"

county = "India"
name ="Santosh"
print(letter.format(name,county))
print(letter.format(county,name))


print(f"Hey My Name is {name} and i am from {county}")

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# to show curly bracket 
print(f"Hey My Name is {{name}} and i am from {{county}}")