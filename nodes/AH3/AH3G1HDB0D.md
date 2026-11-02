---
tag: AH3G1HDB0D
kind: statement
role: theorem
name: Kneser's construction of real analytic tetration
msc: [39B12, 30D05, 26A18]
uses: [0J0FCWV32D, 081WKEDK6C, NT65WHM5VV, E7890PHMGP, 68SHB7Z721]
about: [NT65WHM5VV, E7890PHMGP]
sources:
  - url: https://en.wikipedia.org/wiki/Tetration
---

## Statement

Let $\exp$ be the [[exponential function|0J0FCWV32D]].
There is a [[real-analytic|081WKEDK6C]], strictly increasing function $F \colon (-2, \infty) \to \R$ such that
$$F(0) = 1 \quad \text{and} \quad F(x + 1) = \exp(F(x)) \quad \text{for all } x > -2.$$
So $F$ extends [[tetration|NT65WHM5VV]] to base $e$ from integer heights to real heights: $F(n) = {}^{n}e$ for all integers $n \ge 1$.

## Remarks

Kneser's construction starts at a non-real fixed point $L$ of $\exp$ in $\C$, with $L \approx 0.318 + 1.337i$.
There $\exp'(L) = L$ has modulus greater than $1$, so $\exp$ has a holomorphic Schröder function near $L$, and this gives a complex solution of the [[Abel equation|68SHB7Z721]].
This solution is not real on the real axis, and Kneser corrects it by a conformal change of variables, built with the Riemann mapping theorem, to obtain a real-analytic one.
From $F$ one gets a real-analytic [[functional square root|E7890PHMGP]] of $\exp$ on $\R$: $g(x) = F\big(F^{-1}(x) + \tfrac12\big)$ satisfies $g(g(x)) = \exp(x)$.
The values at integers are forced: $F(-1) = \log F(0) = 0$, $F(1) = e$, $F(2) = e^e$, and $F(x) \to -\infty$ as $x \to -2$ from the right.
The equation $F(x + 1) = \exp(F(x))$ with $F(0) = 1$ has many solutions, even smooth ones, so extra conditions are needed to single out Kneser's solution.

## Explanations

### L1 human

Tetration ${}^{n}e$ is a tower of $n$ copies of $e$, and it is easy to define when $n$ is a whole number.
Kneser showed that one can fill in the values between the whole numbers by a smooth curve, in fact an analytic one.
The curve still obeys the rule "one more floor means one more exponential".
This also gives a function that, applied twice, is the exponential function.

### L2 human

The equation $F(x + 1) = \exp(F(x))$ is an Abel-type equation for the inverse of $F$, and its solutions are easy to build piece by piece on intervals of length $1$.
Such solutions are usually not analytic, and the difficulty is to find a solution that is analytic everywhere.
Kneser's method combines the theory of linearization near a repelling fixed point, the Schröder and Koenigs theory, with the Riemann mapping theorem.
It is the standard reference point for later work on tetration to other bases and on uniqueness of analytic solutions.
