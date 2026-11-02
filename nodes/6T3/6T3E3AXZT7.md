---
tag: 6T3E3AXZT7
kind: statement
role: theorem
name: Bertrand's test
msc: [40A05]
uses: [0CVVKY7GY2, 0NBRP6093V, 0044CPHJBV, 9JQEWK5405]
about: [FJKV01J9F1]
sources:
  - url: https://en.wikipedia.org/wiki/Ratio_test
---

## Statement

Let $(a_n)_{n \ge 2}$ be a sequence of positive real numbers, and put
$$B_n = \ln n \left( n \left( \frac{a_n}{a_{n+1}} - 1 \right) - 1 \right),$$
where $\ln$ is the [[natural logarithm|0044CPHJBV]].

1. If there are $r > 1$ and $N$ with $B_n \ge r$ for all $n \ge N$, then $\sum a_n$ [[converges|0CVVKY7GY2]].
2. If there is $N$ with $B_n \le 1$ for all $n \ge N$, then $\sum a_n$ [[diverges|0NBRP6093V]].

In particular, if $B_n \to B$, the series converges when $B > 1$ and diverges when $B < 1$.

## Remarks

This is [[Kummer's test|9JQEWK5405]] with $c_n = n \ln n$.
A short computation gives $\rho_n = B_n - (n+1) \ln(1 + 1/n)$.
The inequality $\ln(1 + x) \ge x/(1 + x)$ gives $(n+1)\ln(1 + 1/n) \ge 1$, and this quantity tends to $1$.
So $B_n \ge r > 1$ gives $\rho_n \ge (r - 1)/2$ for large $n$, and $B_n \le 1$ gives $\rho_n \le 0$; moreover $\sum 1/(n \ln n)$ diverges.
Example: if $a_n / a_{n+1} = 1 + 1/n + O(1/n^s)$ with $s > 1$, then $B_n = \ln n \cdot O(n^{1-s}) \to 0$, so the series diverges.
This is the case that [[Raabe's test|CD6CAQ6XDN]] leaves open in [[Gauss's test|A7MJXJERNY]].
For $a_n = 1/(n (\ln n)^p)$ one finds $B_n \to p$, so the test decides these series for $p \ne 1$.

## Explanations

### L1 human

Bertrand's test is the next step after Raabe's test.
It is used when Raabe's quantity tends to $1$.
It compares the series with the slowly converging or diverging series $\sum 1/(n (\ln n)^p)$.

### L2 human

The ratio test, Raabe's test and Bertrand's test form a scale of finer and finer tests, all special cases of Kummer's test.
Each one looks at the next term in the expansion of $a_n / a_{n+1}$.
One use of Bertrand's test is the proof of Gauss's test in the boundary case $h = 1$.
