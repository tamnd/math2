---
tag: 7QFW771QMA
kind: statement
role: theorem
name: Kummer's 24 solutions
msc: ["33C05", "34M03"]
uses: [W8VE25R5A7, 463X5V31D9, KAAJ0JJ2GF, 0SG74WBFA2]
about: [W8VE25R5A7]
sources:
  - url: https://en.wikipedia.org/wiki/Hypergeometric_function
---

## Statement

Let $a, b, c \in \C$ be such that none of $c$, $c - a - b$, $a - b$ is an integer, and consider the [[hypergeometric differential equation|W8VE25R5A7]] with these parameters.
Let ${}_2F_1$ be the [[hypergeometric function|463X5V31D9]].

1. The following six functions are solutions, each on a suitable simply connected domain:
$$\begin{aligned} w_1 &= {}_2F_1(a, b; c; z), & w_2 &= z^{1-c} \, {}_2F_1(a - c + 1, b - c + 1; 2 - c; z), \\ w_3 &= {}_2F_1(a, b; a + b - c + 1; 1 - z), & w_4 &= (1 - z)^{c-a-b} \, {}_2F_1(c - a, c - b; c - a - b + 1; 1 - z), \\ w_5 &= z^{-a} \, {}_2F_1(a, a - c + 1; a - b + 1; 1/z), & w_6 &= z^{-b} \, {}_2F_1(b, b - c + 1; b - a + 1; 1/z). \end{aligned}$$
2. Applying the [[Pfaff and Euler transformations|KAAJ0JJ2GF]] to each $w_i$ gives four expressions $z^{\lambda} (1 - z)^{\mu} \, {}_2F_1(a', b'; c'; \xi)$.
In each, $\xi$ is one of $z$, $1 - z$, $1/z$, $1/(1 - z)$, $z/(z - 1)$, $(z - 1)/z$.
This gives $24$ expressions of solutions, falling into six groups of four equal functions.

## Remarks

The six variables are the images of $z$ under the six [[Möbius transformations|0SG74WBFA2]] that permute $\set{0, 1, \infty}$.
Each such map carries the equation to a hypergeometric equation with permuted local exponents.
The solutions $w_1, \ldots, w_6$ are the pairs of local solutions at $0$, $1$ and $\infty$, each with a pure power behaviour there.
The hypothesis that $c$, $c - a - b$ and $a - b$ are not integers makes the two exponents at each singular point differ by a non-integer, so each pair is a basis.
Without it, some of the six formulas are undefined or coincide, and logarithmic solutions appear.

Example: the group of $w_1$ consists of
$${}_2F_1(a, b; c; z) = (1 - z)^{-a} \, {}_2F_1\left(a, c - b; c; \tfrac{z}{z - 1}\right) = (1 - z)^{-b} \, {}_2F_1\left(c - a, b; c; \tfrac{z}{z - 1}\right) = (1 - z)^{c - a - b} \, {}_2F_1(c - a, c - b; c; z).$$

Since the solution space is two-dimensional, any three of the $w_i$ are linearly dependent.
For instance, on $\C \setminus \big((-\infty, 0] \cup [1, \infty)\big)$,
$$w_1 = \frac{\Gamma(c) \Gamma(c - a - b)}{\Gamma(c - a) \Gamma(c - b)} \, w_3 + \frac{\Gamma(c) \Gamma(a + b - c)}{\Gamma(a) \Gamma(b)} \, w_4,$$
and the first coefficient is the value given by [[Gauss's hypergeometric theorem|1FC0T0GCCX]].

## Explanations

### L1 human

The hypergeometric equation has three special points, $0$, $1$ and $\infty$, and near each of them there are two natural solutions that behave like powers.
Each of these six solutions can be written as a hypergeometric function in four different ways.
That gives Kummer's list of $24$ formulas.

### L2 human

The list is the tool for continuing ${}_2F_1$ from one singular point to another.
Linear relations between solutions at different points, the connection formulas, follow from Gauss's theorem and give the monodromy explicitly.
