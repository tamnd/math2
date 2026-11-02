---
tag: YB35R7F7RZ
kind: statement
role: theorem
name: Euler's continued fraction formula
msc: [40A15, 11A55]
uses: [0BK6JBK58W, 0SRWNR42BQ, 0JH4MN4K1C, 0NB643K60Q]
about: [04P2RJ4WPS]
sources:
  - url: https://en.wikipedia.org/wiki/Euler's_continued_fraction_formula
same_as:
  wikidata: Q5361532
  wikipedia: Euler's continued fraction formula
---

## Statement

Let $n \ge 1$ and let $a_0, a_1, \dots, a_n$ be complex numbers such that no division by zero occurs on the right-hand side below.
Then
$$a_0 + a_0 a_1 + a_0 a_1 a_2 + \cdots + a_0 a_1 \cdots a_n = \cfrac{a_0}{1 - \cfrac{a_1}{1 + a_1 - \cfrac{a_2}{1 + a_2 - \cfrac{\cdots}{\cdots + a_{n-1} - \cfrac{a_n}{1 + a_n}}}}}.$$
Consequently, let $(a_k)$ be an infinite sequence, and consider the infinite [[continued fraction|0BK6JBK58W]] of the same shape.
Its $n$-th [[convergent|0SRWNR42BQ]] equals the $n$-th [[partial sum|0NB643K60Q]] of the [[series|0JH4MN4K1C]] $\sum_{k \ge 0} a_0 a_1 \cdots a_k$.
So the continued fraction converges exactly when the series does, and to the same value.

## Remarks

Proof idea: by induction on $n$.
Replacing $a_n$ by $a_n(1 + a_{n+1})$ turns the left side for $n$ into the left side for $n + 1$.
On the right side the same replacement turns the last fraction $\frac{a_n}{1 + a_n}$ into $\frac{a_n}{1 + a_n - \frac{a_{n+1}}{1 + a_{n+1}}}$, because both equal $\frac{a_n(1 + a_{n+1})}{1 + a_n + a_n a_{n+1}}$.
Check for $n = 1$: $\cfrac{a_0}{1 - \frac{a_1}{1 + a_1}} = a_0(1 + a_1)$.
Example: with $a_0 = 1$ and $a_k = x$ for $k \ge 1$, the series is the [[geometric series|01X5CVV1Q5]], and for $\abs{x} < 1$
$$\frac{1}{1 - x} = \cfrac{1}{1 - \cfrac{x}{1 + x - \cfrac{x}{1 + x - \cdots}}}.$$

## Explanations

### L1 human

Any series whose terms are running products $a_0$, $a_0 a_1$, $a_0 a_1 a_2$, and so on, can be rewritten as a continued fraction with the same partial values.
So results about series transfer directly to continued fractions of this shape, and back.

### L2 human

Power series have this form with $a_k = c_k x / c_{k-1}$ when the coefficients $c_k$ are nonzero.
In this way the formula turns the series of $e^x$, $\log(1 + x)$ or $\arctan x$ into continued fractions.
These continued fractions converge at the same rate as the series; other transformations are needed to obtain faster convergence.
