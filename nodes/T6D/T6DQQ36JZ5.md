---
tag: T6DQQ36JZ5
kind: statement
role: theorem
name: Descartes' rule of signs
msc: [26C10, "12D10"]
uses: [0Q9EZS90GY, 00EHX6FWC0, 03XVP8Q4GY, 0194DY35BG, 7THS519D4A]
about: [019MA1VTR2]
sources:
  - url: https://en.wikipedia.org/wiki/Descartes%27s_rule_of_signs
same_as:
  wikidata: Q1379344
  wikipedia: Descartes's rule of signs
---

## Statement

Let $f = a_n x^n + \cdots + a_1 x + a_0$ be a nonzero polynomial with real coefficients.
Let $V$ be the number of sign changes in the sequence of nonzero coefficients of $f$, taken in order of degree.
Let $P$ be the number of positive [[roots|00EHX6FWC0]] of $f$, counted with [[multiplicity|03XVP8Q4GY]].
Then $P \le V$, and $V - P$ is even.

## Remarks

The parity part follows by comparing the sign of the leading coefficient with the sign of the lowest nonzero coefficient.
Both $V$ and $P$ are even exactly when these signs agree.
The bound $P \le V$ can be proved by induction on the degree, using [[Rolle's theorem|0194DY35BG]] to compare the positive roots of $f$ with those of $f'$.
Example: $f = x^3 - x^2 - x + 1$ has signs $+, -, -, +$, so $V = 2$; indeed $f = (x - 1)^2 (x + 1)$ has the double positive root $1$, so $P = 2$.
The number of negative roots is bounded in the same way by the sign changes of $f(-x)$.
The bound need not be reached: $x^2 - x + 1$ has $V = 2$ and no real root, so $P = 0$.

## Explanations

### L1 human

Reading the signs of the coefficients of a polynomial gives an upper bound for the number of its positive roots.
Each change from plus to minus, or from minus to plus, allows at most one positive root.
The count can only be too high by an even number.

### L2 human

The rule is a quick first test before one locates roots more precisely.
If all roots of $f$ are real, then the bound is exact: $P = V$.
[[Budan's theorem|7THS519D4A]] extends the rule from the half-line $(0, \infty)$ to any interval, and [[Sturm's theorem|R44CV0KD9T]] gives the exact number of distinct real roots in an interval.
