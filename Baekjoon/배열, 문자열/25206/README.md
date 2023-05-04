### 문제

[https://www.acmicpc.net/problem/25206](https://www.acmicpc.net/problem/25206)

<br>

### 문제 요약

학점 계산하기

전공 평점 = (학점 * 과목 평점)의 합  / (학점의 총합)

<br>

### 배운 점

딕셔너리로 등급별 과목 평점 저장하기

```python
dic = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5,
       "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
```

dic[key]로 접근 가능

소수점 6자리까지 표시하기

```python
print("%.6f" % (result / t_total))
```