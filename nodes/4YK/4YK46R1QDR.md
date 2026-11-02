---
tag: 4YK46R1QDR
kind: statement
role: theorem
name: Chu–Vandermonde identity
msc: ["33C05", "05A19"]
uses: [0GBZM0MT0F, YZHM3HSM0F, 428M453CR2]
about: [428M453CR2]
sources:
  - url: https://en.wikipedia.org/wiki/Vandermonde%27s_identity
---

## Statement

Let $n \ge 0$ be an integer.

1. For all $x, y \in \C$,
$$\binom{x + y}{n} = \sum_{k=0}^{n} \binom{x}{k} \binom{y}{n - k},$$
where $\binom{x}{k} = \frac{x(x-1)\cdots(x-k+1)}{k!}$ is the [[binomial coefficient|0GBZM0MT0F]].
2. Equivalently, for all $b, c \in \C$ with $c \notin \set{0, -1, -2, \ldots}$,
$${}_2F_1(-n, b; c; 1) = \frac{(c - b)_n}{(c)_n},$$
where ${}_2F_1$ is the terminating [[hypergeometric series|428M453CR2]] and $(x)_n$ is the [[Pochhammer symbol|YZHM3HSM0F]].

## Remarks

Both sides of part 1 are polynomials in $x$ and $y$.
For natural numbers $x = m$ and $y = p$ the identity is [[Vandermonde's identity|01JADB9VW5]], proved by counting $n$-element subsets of a union of an $m$-set and a $p$-set.
A polynomial in two variables that vanishes on $\N \times \N$ is zero, so part 1 holds for all $x, y$.
Part 2 is also the case $a = -n$ of [[Gauss's hypergeometric theorem|1FC0T0GCCX]], since $\frac{\Gamma(c) \Gamma(c + n - b)}{\Gamma(c + n) \Gamma(c - b)} = \frac{(c - b)_n}{(c)_n}$.

Example: with $x = y = \frac12$ and $n = 2$, the left side is $\binom{1}{2} = 0$, and the right side is $\binom{1/2}{2} + \binom{1/2}{1}^2 + \binom{1/2}{2} = -\frac18 + \frac14 - \frac18 = 0$.

The name records that the identity was known to Zhu Shijie long before Vandermonde.

## Explanations

### L1 human

Vandermonde's identity counts the ways to choose $n$ people from two groups: choose $k$ from the first and $n - k$ from the second.
The Chu–Vandermonde identity says that the same formula stays true when the group sizes are replaced by arbitrary numbers, even fractions or complex numbers.
This works because both sides are polynomials that agree at all whole numbers.

### L2 human

In hypergeometric language it is the summation of a terminating ${}_2F_1$ at $z = 1$.
It is the simplest case of a whole hierarchy of terminating summations, followed by the Pfaff–Saalschütz formula for ${}_3F_2$ and Dougall's formula.
Its $q$-analogue is the [[q-Vandermonde identity|MBRSCQRGGH]].
