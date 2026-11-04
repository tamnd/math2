---
tag: TVXBJQR31R
kind: proof
name: Proof that consecutive Fibonacci numbers are coprime
msc: [11B39]
proves: 0D3PFXEAKF
uses: [0GFKP8F8AG, 02WF878BH1, 0ASJVEFA9J]
methods: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Fibonacci_sequence
    locator: Divisibility properties
---

## Proof

We argue by [[induction|0ASJVEFA9J]] on $n$.

1. Base case $n = 0$. We have $F_0 = 0$ and $F_1 = 1$. The only positive divisor of $1$ is $1$, so $\gcd(F_0, F_1) = 1$.
2. Induction step. Let $n \ge 0$ and assume $\gcd(F_n, F_{n+1}) = 1$.
3. Let $e$ be a positive integer that divides $F_{n+1}$ and $F_{n+2}$.
4. By the recurrence, $F_n = F_{n+2} - F_{n+1}$. A common divisor of two integers divides their difference, so $e \mid F_n$.
5. So $e$ is a positive common divisor of $F_n$ and $F_{n+1}$. By the induction hypothesis, the greatest such divisor is $1$. So $e \le 1$, and $e = 1$.
6. Thus the only positive common divisor of $F_{n+1}$ and $F_{n+2}$ is $1$. So their [[greatest common divisor|02WF878BH1]] is $1$.
7. By induction, $F_n$ and $F_{n+1}$ are [[coprime|0GFKP8F8AG]] for each $n \ge 0$.

## Idea

A common divisor of two neighbours in the sequence also divides the term before them, because that term is their difference.
Walking down the sequence, it divides $F_1 = 1$, so it is $1$.
