txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")  # output: Yes, 'free' is present.

txt = """Lorem 1 ipsum 2 dolor 3 sit 4 amet 5,
consectetur 6 adipiscing 7 elit 8"""
print("Current 'txt' variable length is " + str(len(txt)) + " symbols")
# output: Current 'txt' variable length is 71 symbols

s1 = 'this line is a'
s2 = 'spam'

s1 += ' ' + s2

print(s1)  # output: this line is a spam
print(s2 * 3)  # output: spamspamspam
print(len(s1))  # output: 19
print(s1[0])  # output: t
print(s1[2])  # output: i
print(s1[-2])  # output: a
print(s1[5:9])  # output: line
print(s1[5:-2])  # output: line is a sp
print(s1[5:])  # output: line is a spam
print(s1[:9])  # output: this line

txt_lst = [s * 2 for s in txt if s.isdigit()]  # txt is a list now
print(txt_lst)  # output: ['11', '22', '33', '44', '55', '66', '77', '88']

txt = {int(s) * 2 for s in txt if s.isdigit()}  # txt is a set now
print(txt)  # output: {2, 4, 6, 8, 10, 12, 14, 16}

txt = '\t'.join(map(str, txt))
print(txt)  # output:   2   4	6	8	10	12	14	16

txt = '{}{: >6}{}'.format('hello', 'world', '!')
print(txt)  # output: hello world!

s = '"'
z = 'PerfLab'
txt = '{0}{1:-^20}{0}'.format(s, z)
print(txt)  # output: "------PerfLab-------"

print('{quote}{text:*>20}{quote}'.format(quote="'", text="PerfLab"))  # output: '*************PerfLab'

print('{quote}{0:.4}{quote}'.format("PerfLab", quote='"'))  # output: "Perf"

print(f'"{z: ^20}"')  # output: "      PerfLab       "
