---
tag: 3RDB8B5GFA
kind: statement
role: theorem
name: Hurwitz's theorem (number theory)
msc: [11J04, 11J70]
uses: [0DZXAXEJQ9, 0NCJ5WXN6Z, 04VA28F3HB, 0SC8T7548D]
about: [0DZXAXEJQ9]
sources:
  - url: https://en.wikipedia.org/wiki/Hurwitz%27s_theorem_(number_theory)
same_as:
  wikidata: Q1630588
  wikipedia: Hurwitz's theorem (number theory)
---

## Statement

Let $\xi$ be an [[irrational number|0DZXAXEJQ9]].
Then there are infinitely many [[rational numbers|0NCJ5WXN6Z]] $p/q$, with $p, q \in \Z$ and $q \ge 1$, such that
$$\abs{\xi - \frac{p}{q}} < \frac{1}{\sqrt{5}\, q^2}.$$
The constant $\sqrt{5}$ is best possible.
That is, for each real $A > \sqrt{5}$ there is an irrational $\xi$ with only finitely many rationals $p/q$ that satisfy $\abs{\xi - p/q} < 1/(A q^2)$.

## Remarks

The proof uses the [[continued fraction expansion|04VA28F3HB]] of $\xi$.
Among any three consecutive convergents $p_n/q_n$ of $\xi$, at least one satisfies the inequality, and there are infinitely many convergents.
For the second part, take the [[golden ratio|0SC8T7548D]] $\varphi = (1 + \sqrt{5})/2$, whose continued fraction is $[1; 1, 1, 1, \dots]$.
Its convergents are quotients of consecutive Fibonacci numbers, and $q^2 \abs{\varphi - p/q}$ tends to $1/\sqrt{5}$ along them.
The theorem improves the constant $1$ of [[Dirichlet's approximation theorem|04JAY9DGB7]].
If one removes $\varphi$ and all numbers equivalent to it under the action of $\mathrm{GL}_2(\Z)$, the best constant becomes $\sqrt{8}$.

## Explanations

### L1 human

Each irrational number can be approached by fractions $p/q$ with an error much smaller than $1/q^2$.
Hurwitz's theorem gives the exact best factor: the error can be made smaller than $1/(\sqrt{5} q^2)$ infinitely often.
The golden ratio is the hardest number to approximate, and it shows that $\sqrt{5}$ cannot be improved.

### L2 human

The theorem belongs to the theory of the Lagrange spectrum, which records the best constants for each irrational number.
Continued fractions are the main tool: the convergents give the best approximations.
Numbers with bounded partial quotients, such as quadratic irrationals, are badly approximable, and the golden ratio is the extreme case.
