n = eval(input("Enter number of rows to be added: "))

f = open("readme_cf.txt", "a")

for i in range(0, n):
    pb = input("Problem number: ")
    for j in range(len(pb)):
        if pb[j] >= 'A' and pb[j] <= 'Z':
            m = j
    pb_n = pb[:m]
    pb_c = pb[m:]

    s = "\n|{0}-{1}|[{0}-{1}](http://codeforces.com/problemset/problem/{0}/{1})| [C++](./{0}{1}.cpp)|".format(pb_n, pb_c)

    f.write(s)

f.close()
