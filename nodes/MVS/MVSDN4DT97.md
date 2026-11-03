---
tag: MVSDN4DT97
kind: statement
role: theorem
name: Lamé's theorem
msc: [11A05, 11Y16, 68W40]
uses: [0TRNT4X7J0, 0GA9K57A39, 0SC8T7548D]
about: [0TRNT4X7J0]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_algorithm
---

## Statement

Let $(F_n)$ be the [[Fibonacci numbers|0GA9K57A39]], with $F_1 = F_2 = 1$ and $F_{n+2} = F_{n+1} + F_n$.
Let $a > b \ge 1$ be integers, and suppose the [[Euclidean algorithm|0TRNT4X7J0]] on $(a, b)$ performs exactly $N \ge 1$ divisions with remainder before reaching remainder $0$.
Then $b \ge F_{N+1}$ and $a \ge F_{N+2}$.
Consequently, $N$ is at most $5$ times the number of decimal digits of $b$.

## Remarks

The proof is by induction on $N$.
The last division has quotient at least $2$, because its dividend exceeds its divisor, and every earlier quotient is at least $1$.
Read backwards, each number in the chain of remainders is at least the sum of the next two, so the chain dominates the Fibonacci numbers.
For the digit bound, $F_{N+1} \ge \varphi^{N-1}$ with $\varphi = (1 + \sqrt 5)/2$ the [[golden ratio|0SC8T7548D]], so $N - 1 \le \log_\varphi b < 4.79 \log_{10} b$; if $b$ has $d$ digits this gives $N < 1 + 4.79\, d$, hence $N \le 5d$ since $N$ is an integer.

The bound is sharp: the pair $(F_{N+2}, F_{N+1})$ needs exactly $N$ divisions.
For example, $(13, 8)$ gives $13 = 1 \cdot 8 + 5$, $8 = 1 \cdot 5 + 3$, $5 = 1 \cdot 3 + 2$, $3 = 1 \cdot 2 + 1$, $2 = 2 \cdot 1 + 0$, which is $N = 5$ divisions with $b = 8 = F_6$.

## Explanations

### L1 human

The Euclidean algorithm is fast: the number of steps grows only with the number of digits, not with the size of the numbers.
Lamé's theorem makes this exact: at most five steps per decimal digit of the smaller number.
The slowest inputs are pairs of consecutive Fibonacci numbers, where every quotient is $1$.

### L2 human

The theorem is one of the first results of the [[analysis of algorithms|2TSJFYVFS8]].
It shows that computing $\gcd(a, b)$ takes $O(\log b)$ division steps, so the Euclidean algorithm runs in time polynomial in the length of the input.
The same bound holds for the [[extended Euclidean algorithm|0964YQFSA8]], which performs the same divisions.
