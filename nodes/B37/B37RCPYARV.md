---
tag: B37RCPYARV
kind: statement
role: theorem
name: Malmquist's theorem
msc: [34M05, 30D35]
uses: [0NT64JV96A, 0ZZ7ZYDR8W, 0XDK9CGYKJ, 0VT2QK6X6Q, 9KAQ1REPE8]
about: [0VT2QK6X6Q, 0ZZ7ZYDR8W]
sources:
  - url: https://en.wikipedia.org/wiki/Malmquist%27s_theorem
same_as:
  wikidata: Q17056925
  wikipedia: Malmquist's theorem
---

## Statement

Let $R(z, w)$ be a [[rational function|0XDK9CGYKJ]] of two complex variables.
Suppose the [[ordinary differential equation|0NT64JV96A]]
$$w'(z) = R\big(z, w(z)\big)$$
has a transcendental [[meromorphic|0ZZ7ZYDR8W]] solution on $\C$.
Here transcendental means that the solution is not a rational function.
Then there are rational functions $a_0, a_1, a_2$ of $z$ such that
$$R(z, w) = a_0(z) + a_1(z) w + a_2(z) w^2.$$
So the equation is a [[Riccati equation|0VT2QK6X6Q]] or a linear equation.

## Remarks

A proof with Nevanlinna theory compares the growth of both sides: if $R$ had degree $d$ in $w$, then $T(r, R(z, w)) = d\,T(r, w) + O(\log r)$, while $T(r, w')$ is at most $2T(r, w)$ plus a small error.
This bounds the degree, and a study of the poles of $w$ excludes nonpolynomial dependence on $w$.
Example: $w' = 1 + w^2$ has the transcendental meromorphic solution $w = \tan z$, and its right side is a polynomial of degree $2$ in $w$, as the theorem requires.
In contrast, the solutions of $w' = w^3$ are $w = \pm (c - 2z)^{-1/2}$ and $w = 0$; they have branch points, as the theorem predicts, so no transcendental meromorphic solution exists.
The hypothesis that the solution is transcendental is needed: $w = z$ solves $w' = 1 + (w - z)^3$, whose right side has degree $3$ in $w$.

## Explanations

### L1 human

Most first-order differential equations have solutions with branch points, which are not single-valued in the whole plane.
Take a first-order equation whose right side is rational.
Malmquist's theorem says that if it has a non-rational solution that is single-valued with only poles, then it must be a Riccati equation.
So, apart from Riccati equations, nonlinear first-order equations with rational right side have no such nice global solutions.

### L2 human

The theorem is the first-order prototype of the classification behind the Painlevé equations, where the same question is asked for second-order equations.
It also has an analogue for difference equations $w(z + 1) = R(z, w(z))$, studied in [[Nevanlinna theory of difference equations|9KAQ1REPE8]]: transcendental meromorphic solutions of finite order force strong restrictions on $R$.
Results of this kind are called Malmquist-type theorems.
