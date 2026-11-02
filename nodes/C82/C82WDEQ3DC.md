---
tag: C82WDEQ3DC
kind: statement
role: theorem
name: Asymptotic behavior of solutions of renewal equations
msc: [45M05, 60K05, "45E10"]
uses: [45V0W838BQ, 0H8H7ZTHW2, FK3QBZAZH7, DND8CBEVXT]
about: [45V0W838BQ]
sources:
  - url: https://en.wikipedia.org/wiki/Renewal_theory
---

## Statement

Let $F$ be a [[cumulative distribution function|0H8H7ZTHW2]] with $F(0) = 0$, so that $F$ is the law of a positive random variable.
Assume that $F$ is not arithmetic, that is, $F$ is not concentrated on a set $\set{0, h, 2h, \dots}$ for any $h > 0$.
Let $\mu = \int_{[0, \infty)} t \, dF(t)$ be its mean, with $0 < \mu \le \infty$.
Let $g \colon [0, \infty) \to \R$ be directly Riemann integrable.
This means that, for the partition of $[0, \infty)$ into intervals of length $h$, the upper and lower Riemann sums of $g$ are finite.
It also means that they tend to the same limit as $h \to 0$.
Consider the renewal equation
$$u(t) = g(t) + \int_{[0, t]} u(t - s) \, dF(s), \qquad t \ge 0,$$
where the integral is a [[Lebesgue–Stieltjes integral|FK3QBZAZH7]].
Then:

1. The equation has exactly one solution $u$ that is bounded on bounded intervals, namely $u(t) = \int_{[0, t]} g(t - s) \, dU(s)$. Here $U = \sum_{n \ge 0} F^{*n}$, where $F^{*n}$ is the $n$-fold convolution power of $F$ and $F^{*0}$ is the unit mass at $0$.
2. As $t \to \infty$,
$$u(t) \to \frac{1}{\mu} \int_0^\infty g(s) \, ds,$$
where $1/\mu$ is read as $0$ when $\mu = \infty$.

## Remarks

Part 1 follows by iterating the equation: the series of convolution powers converges because $F^{*n}(t) \to 0$ fast for each fixed $t$.
Part 2 is the key renewal theorem.
Its proof first treats $g$ equal to the indicator function of $[0, h)$, which is Blackwell's renewal theorem.
It then approximates a directly Riemann integrable $g$ from above and below by step functions.
A nonnegative, nonincreasing, Lebesgue integrable function on $[0, \infty)$ is directly Riemann integrable.

Example: for $g = 1 - F$, the constant $u = 1$ solves the equation, since $1 - F(t) + F(t) = 1$.
The limit in part 2 is $\frac{1}{\mu} \int_0^\infty (1 - F(s)) \, ds = \mu / \mu = 1$, as it must be.

The hypothesis that $F$ is not arithmetic is needed.
If $F$ is the unit mass at $1$, then $U$ puts mass $1$ on each integer $n \ge 0$.
For $g$ the indicator function of $[0, 1/2)$, the solution is $u(t) = 1$ when the fractional part of $t$ is less than $1/2$ and $u(t) = 0$ otherwise, so $u(t)$ has no limit.

## Explanations

### L1 human

A renewal equation describes a quantity that is fed by a source $g$ and by its own past, where the past is weighted by a waiting time law $F$.
The theorem says that after a long time the quantity settles down to a constant.
The constant is the total size of the source divided by the mean waiting time $\mu$.
For example, the expected number of light bulb replacements in a time window of length $h$ tends to $h / \mu$.

### L2 human

In [[renewal theory|45V0W838BQ]], $U(t)$ is the expected number of renewals in $[0, t]$, counting the start.
Many quantities of a renewal process, such as the law of the residual waiting time at time $t$, satisfy a renewal equation with an explicit $g$.
The theorem then gives their limits as $t \to \infty$.
The same method describes the long-time behaviour of age-structured populations through the [[renewal equation|EWVVH3EKMR]] and the [[Euler–Lotka equation|E0YVMBPK7A]], after a change of variable that makes $F$ a probability distribution.
From the point of view of [[Volterra integral equations|DND8CBEVXT]], it is a statement about the [[Volterra equation of convolution type|SNFYTC1TTA]] whose kernel is a probability measure.
