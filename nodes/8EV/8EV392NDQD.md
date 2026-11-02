---
tag: 8EV392NDQD
kind: definition
name: Central polynomial
msc: [16R10, 16R20]
defines: 667YZTHE96
uses: [04C5ZBG1WT, 2P3Y2FRCSZ, 0JXZKX526R, C0EDT81EGH, MVT64B3B6H, 0F765KFC2J]
sources:
  - url: https://en.wikipedia.org/wiki/Central_polynomial
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]], let $n \ge 1$, and let $M_n(k)$ be the ring of $n \times n$ [[matrices|0JXZKX526R]] over $k$.
Let $f \in k\langle x_1, \ldots, x_m \rangle$ be an element of the [[free algebra|2P3Y2FRCSZ]] with zero constant term.
The polynomial $f$ is a *central polynomial* for $M_n(k)$ if:

1. $f(a_1, \ldots, a_m)$ is a scalar matrix $\lambda I$, with $\lambda \in k$, for all $a_1, \ldots, a_m \in M_n(k)$;
2. $f$ is not a [[polynomial identity|C0EDT81EGH]] of $M_n(k)$: $f(a_1, \ldots, a_m) \ne 0$ for some $a_1, \ldots, a_m \in M_n(k)$.

## Remarks

Clause 1 says that all values of $f$ lie in the [[center|MVT64B3B6H]] $k I$ of $M_n(k)$.

Example: $f = (x_1 x_2 - x_2 x_1)^2$ is a central polynomial for $M_2(k)$.
For $a, b \in M_2(k)$ the matrix $c = ab - ba$ has trace $0$, so the [[Cayley–Hamilton theorem|0F765KFC2J]] gives $c^2 = -\det(c) \, I$, a scalar matrix.
For $a = e_{12}$ and $b = e_{21}$ one has $c = e_{11} - e_{22}$ and $c^2 = I \ne 0$, so clause 2 holds.

Non-example: $g = x_1 x_2 - x_2 x_1$ fails clause 1 for $M_2(k)$, since $g(e_{12}, e_{21}) = e_{11} - e_{22}$ is not scalar.
Non-example: $s_4$, the standard polynomial of degree $4$, satisfies clause 1 for $M_2(k)$ only because all its values are $0$, so it fails clause 2.

For $n = 1$ every polynomial with a nonzero value on $k$ is central, so the notion is of interest for $n \ge 2$.
Central polynomials exist for every $n \ge 1$, a result of Formanek and of Razmyslov.
