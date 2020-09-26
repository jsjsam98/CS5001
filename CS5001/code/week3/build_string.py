def build_string(s, a, b, c):
    line1 = str(s)*int(a)
    line2 = str(s)*int(b)
    line3 = str(s)*int(c)
    print('{}\n{}\n{}'.format(line1, line2, line3))
