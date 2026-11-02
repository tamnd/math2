---
tag: TWANGP59RB
kind: statement
role: theorem
name: Measurable solutions of Cauchy's equation
msc: [39B22, 28A20]
uses: [KF719SZD5T, YYNCJSR0PJ, 2Z2QVWZ262]
about: [KF719SZD5T]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_functional_equation
---

## Statement

Let $f \colon \R \to \R$ be an [[additive function|KF719SZD5T]], that is, $f(x + y) = f(x) + f(y)$ for all $x, y \in \R$.
Assume that $f$ is [[measurable|YYNCJSR0PJ]] with respect to [[Lebesgue measure|2Z2QVWZ262]].
Then there is a constant $c \in \R$ such that $f(x) = cx$ for all $x \in \R$, and in fact $c = f(1)$.

## Remarks

The proof reduces the claim to boundedness on an interval.
By Lusin's theorem, $f$ is bounded on some compact set $K$ of positive measure.
By the Steinhaus theorem, the difference set $K - K$ contains an open interval around $0$.
Each point $x = a - b$ of that interval with $a, b \in K$ has $f(x) = f(a) - f(b)$, so $f$ is bounded on this interval.
Then [[Darboux's theorem on additive functions|2F30ZHN1RT]] gives $f(x) = cx$.
Measurability cannot be dropped: [[a Hamel basis gives additive functions that are not linear|FFTNS66XG6]], and such functions are not Lebesgue measurable.
This is one of the regularity conditions that settle [[Cauchy's functional equation|ZBMEVWN100]].

## Explanations

### L1 human

An additive function turns sums into sums.
The only additive functions one can draw are the lines $f(x) = cx$ through the origin.
This theorem says that already a very weak regularity, measurability, forces an additive function to be such a line.
So the strange additive functions can never be measured or integrated.

### L2 human

Measurability is weaker than continuity, monotonicity or local boundedness, so this result contains the other classical criteria.
In practice, any additive function that comes from an explicit formula, a limit of continuous functions or a probability model is measurable, so it is linear.
The same argument works for additive maps between $\R^n$ and $\R^m$.
More generally, a Haar measurable homomorphism between second countable locally compact groups is continuous.
The key tools, Lusin's theorem and the Steinhaus theorem, are standard in measure theory.
