---
tag: MMEX2JZWGR
kind: definition
name: Kovacic's algorithm
msc: [34M15, 12H05, 68W30]
defines: XC4245C9E5
uses: [R80FA7993W, RW8DQQYJMR, H5P06V330V]
sources:
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Vessiot_theory
---

## Definition

Let $r \in \C(x)$ be a rational function and consider the equation $y'' = r\, y$ over the differential field $\C(x)$.
Let $G$ be its [[differential Galois group|RW8DQQYJMR]], the group of differential automorphisms of a [[Picard–Vessiot extension|H5P06V330V]].
Then $G$ is an algebraic subgroup of $\mathrm{SL}_2(\C)$, and exactly one of the following holds.

1. $G$ is conjugate to a group of upper triangular matrices; then there is a solution $y = e^{\int \omega}$ with $\omega \in \C(x)$.
2. Case 1 fails and $G$ is conjugate to a group of matrices that are diagonal or anti-diagonal. Then some solution is $y = e^{\int \omega}$ with $\omega$ algebraic of degree $2$ over $\C(x)$.
3. Cases 1 and 2 fail and $G$ is finite. Then all solutions are algebraic, and some solution is $y = e^{\int \omega}$ with $\omega$ algebraic of degree $4$, $6$ or $12$.
4. $G = \mathrm{SL}_2(\C)$; then the equation has no nonzero [[Liouvillian|R80FA7993W]] solution.

*Kovacic's algorithm* tests cases 1, 2 and 3 in turn.
In each case it builds finitely many candidate exponents from the expansions of $r$ at its poles and at infinity.
Then it searches for $\omega$ by solving for a polynomial of bounded degree.
It returns a Liouvillian solution, or the answer that none exists.

## Remarks

Every equation $y'' + a(x)\, y' + b(x)\, y = 0$ with $a, b \in \C(x)$ can be brought to the reduced form: $z = y\, e^{\frac12 \int a}$ satisfies $z'' = r z$ with $r = \tfrac14 a^2 + \tfrac12 a' - b$.
Example: for $r = 1$, the solution $y = e^{x}$ has $\omega = y'/y = 1 \in \C(x)$, so the equation falls in case 1.
Non-example: for the Airy equation, $r = x$, the algorithm finds no candidate in cases 1 to 3, so $G = \mathrm{SL}_2(\C)$ and no nonzero solution is Liouvillian.
In case 3 the group modulo $\pm 1$ is the tetrahedral, octahedral or icosahedral group, and these correspond to the degrees $4$, $6$ and $12$.
Jerald Kovacic published the algorithm in 1986.
