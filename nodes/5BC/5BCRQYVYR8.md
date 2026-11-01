---
tag: 5BCRQYVYR8
kind: statement
role: theorem
name: Perron's irreducibility criterion
msc: ["12E05", 11R09, 11C08]
uses: [00X2A9G9W3, 0BDX4MBKT4, 0QFV5Y1Z5X, 0D430QR02W]
about: [00X2A9G9W3]
sources:
  - url: https://en.wikipedia.org/wiki/Perron%27s_irreducibility_criterion
same_as:
  wikidata: Q104857583
  wikipedia: Perron's irreducibility criterion
---

## Statement

Let $n \ge 1$ and let $f = x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$ be a [[monic polynomial|0BDX4MBKT4]] with integer coefficients and $a_0 \ne 0$.
If
$$\abs{a_{n-1}} > 1 + \abs{a_{n-2}} + \dots + \abs{a_1} + \abs{a_0},$$
then $f$ is [[irreducible|00X2A9G9W3]] in $\Z[x]$ and in $\Q[x]$.

## Remarks

Proof idea: by [[Rouché's theorem|0D430QR02W]], comparing $f$ with $a_{n-1} x^{n-1}$ on the unit circle, $f$ has exactly $n - 1$ roots in the open unit disc and one root outside it.
If $f = g h$ with monic $g, h \in \Z[x]$ of positive degree, one factor has all its roots in the open unit disc.
Its constant term is then a nonzero integer of absolute value less than $1$, which is impossible.
Irreducibility over $\Q$ follows by [[Gauss's lemma|0QFV5Y1Z5X]].
Example: $x^3 + 5x^2 + 2x + 1$ is irreducible, since $5 > 1 + 2 + 1$.
The hypothesis $a_0 \ne 0$ is necessary: $x^2 + 3x = x(x + 3)$ satisfies the inequality $3 > 1 + 0$.
A second form of the criterion allows equality in the inequality, provided that $f(1) \ne 0$ and $f(-1) \ne 0$.

## Explanations

### L1 human

If the second coefficient of a monic integer polynomial is larger than all the other coefficients together, plus one, the polynomial cannot be factored.
The check needs only additions of absolute values.

### L2 human

The criterion is a typical analytic proof of irreducibility.
One locates the complex roots, then uses that the constant term of an integer factor is a nonzero integer.
It complements algebraic tests such as [[Eisenstein's criterion|02BPKD7TMD]] and [[reduction modulo a prime|0KWWEXW0RN]].
For example, it shows at once that $x^n + 3x^{n-1} + 1$ is irreducible for every $n \ge 2$.
