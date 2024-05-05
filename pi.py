# TODO
#問 2. 文字列
text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

a=text.strip()
b=a.replace(",","")
c=b.replace(".","")
print(list(map(len,c.split(" "))))
#314159265358979323846264
##

