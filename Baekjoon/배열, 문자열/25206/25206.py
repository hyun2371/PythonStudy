import sys

result = 0
t_total = 0
dic = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5,
       "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for _ in range (20):

    s, t, score = sys.stdin.readline().split()
    if score == "P":
        continue
    t = float(t)
    t_total += t
    result = result + dic[score] * t
    print(result)


print("%.6f" % (result / t_total))