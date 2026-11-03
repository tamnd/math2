---
tag: T1KQ3DPYZF
kind: statement
role: theorem
name: Liénard–Chipart criterion
msc: [26C10, 93D20, 30C15]
uses: [Y631JTMMT5, 0BT9BYWVRY, KJF8Y19BNV]
about: [Y631JTMMT5]
sources:
  - url: https://en.wikipedia.org/wiki/Li%C3%A9nard%E2%80%93Chipart_criterion
same_as:
  wikidata: Q17098836
  wikipedia: Liénard–Chipart criterion
---

## Statement

Let $p(s) = a_0 s^n + a_1 s^{n-1} + \cdots + a_n$ be a real polynomial of degree $n \ge 1$ with $a_0 > 0$, and put $a_k = 0$ for $k < 0$ and $k > n$.
Let $\Delta_1, \ldots, \Delta_n$ be the leading principal [[minors|0BT9BYWVRY]] of the $n \times n$ Hurwitz matrix $H = (a_{2j - i})_{1 \le i, j \le n}$.
Then $p$ is a [[Hurwitz polynomial|Y631JTMMT5]] if and only if any one of the following four conditions holds:

1. $a_n > 0$, $a_{n-2} > 0$, $a_{n-4} > 0$, $\ldots$ and $\Delta_1 > 0$, $\Delta_3 > 0$, $\Delta_5 > 0$, $\ldots$;
2. $a_n > 0$, $a_{n-2} > 0$, $a_{n-4} > 0$, $\ldots$ and $\Delta_2 > 0$, $\Delta_4 > 0$, $\Delta_6 > 0$, $\ldots$;
3. $a_n > 0$, $a_{n-1} > 0$, $a_{n-3} > 0$, $\ldots$ and $\Delta_1 > 0$, $\Delta_3 > 0$, $\Delta_5 > 0$, $\ldots$;
4. $a_n > 0$, $a_{n-1} > 0$, $a_{n-3} > 0$, $\ldots$ and $\Delta_2 > 0$, $\Delta_4 > 0$, $\Delta_6 > 0$, $\ldots$.

In each list, the indices run over all values between $1$ and $n$, and the coefficient indices over all values between $0$ and $n$.

## Remarks

The [[Routh–Hurwitz stability criterion|KJF8Y19BNV]] asks for all $n$ minors $\Delta_1, \ldots, \Delta_n$ to be positive.
The Liénard–Chipart criterion replaces about half of these determinants by sign conditions on coefficients, which are much cheaper to check.
This is possible because positive coefficients are necessary for a Hurwitz polynomial.
Under these sign conditions, half of the minor conditions follow from the others.

Example: for $n = 3$, condition 2 reads $a_3 > 0$, $a_1 > 0$ and $\Delta_2 = a_1 a_2 - a_0 a_3 > 0$.
For $p(s) = s^3 + 2s^2 + 2s + 1$ these are $1 > 0$, $2 > 0$ and $4 - 1 = 3 > 0$, so $p$ is Hurwitz; indeed $p(s) = (s + 1)(s^2 + s + 1)$.

The coefficient conditions cannot be dropped.
For $p(s) = s^3 - s^2 - s - 2$ one has $\Delta_2 = a_1 a_2 - a_0 a_3 = 1 + 2 = 3 > 0$, but $a_1 < 0$, and $p$ has the root $2$.

## Explanations

### L1 human

To check that a polynomial has all its roots in the left half-plane, the Routh–Hurwitz test computes $n$ determinants.
Liénard and Chipart showed that about half of them suffice, if one also checks that some coefficients are positive.
Checking a coefficient is free, so the test becomes cheaper.

### L2 human

The criterion is used in the same way as the Routh–Hurwitz criterion, to find the parameter values for which a linear system is stable.
Since fewer determinant inequalities appear, the stability region is described by fewer polynomial inequalities in the parameters.
