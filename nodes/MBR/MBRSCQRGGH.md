---
tag: MBRSCQRGGH
kind: statement
role: theorem
name: q-Vandermonde identity
msc: [33D15, 05A30]
uses: [EB4N9RQR51, Y1X8ZZQ7VM]
about: [EB4N9RQR51]
sources:
  - url: https://en.wikipedia.org/wiki/Basic_hypergeometric_series
---

## Statement

Let $n \ge 0$ be an integer, let $q \in \C \setminus \set{0}$ with $q^k \ne 1$ for $1 \le k \le n$, and let $a, c \in \C$ with $a \ne 0$ and $(c; q)_n \ne 0$.
Then the terminating [[basic hypergeometric series|EB4N9RQR51]] satisfy
$${}_2\phi_1 \left( \begin{matrix} a, q^{-n} \\ c \end{matrix} ; q, q \right) = \frac{(c/a; q)_n}{(c; q)_n}\, a^n$$
and
$${}_2\phi_1 \left( \begin{matrix} a, q^{-n} \\ c \end{matrix} ; q, \frac{c q^n}{a} \right) = \frac{(c/a; q)_n}{(c; q)_n},$$
where $(\cdot\,; q)_n$ is the [[q-Pochhammer symbol|Y1X8ZZQ7VM]].

## Remarks

Both sides are rational functions, and the series stop at index $n$ since $(q^{-n}; q)_k = 0$ for $k > n$.
Proof idea: the second form is the case $b = q^{-n}$ of the $q$-Gauss sum, which follows from [[Heine's transformation|A93A5VATSD]].
The first form is the second one with the order of summation reversed.
Example: $n = 1$.
The first sum is $1 + \frac{(1 - a)(1 - q^{-1})}{(1 - c)(1 - q)}\, q = 1 - \frac{1 - a}{1 - c} = \frac{a - c}{1 - c}$, and the right side is $\frac{(1 - c/a)\, a}{1 - c} = \frac{a - c}{1 - c}$.
In terms of [[Gaussian binomial coefficients|YS09Z1YNEK]] it reads $\binom{m+n}{k}_q = \sum_{j} \binom{m}{j}_q \binom{n}{k-j}_q\, q^{(m-j)(k-j)}$.
At $q = 1$ this becomes [[Vandermonde's identity|01JADB9VW5]].

## Explanations

### L1 human

Vandermonde's identity counts the ways to choose $n$ people from a group of men and women by splitting according to the number of men.
The $q$-Vandermonde identity is the same sum with each binomial coefficient replaced by its $q$-analogue and suitable powers of $q$.
It is the simplest closed-form sum of a terminating basic hypergeometric series.

### L2 human

Its Gaussian binomial form can also be proved, for $q$ a prime power, by counting subspaces of $\F_q^{m+n}$.
It is the $q$-analogue of the [[Chu–Vandermonde identity|4YK46R1QDR]] for ${}_2F_1$, and it is a terminating case of the $q$-Gauss sum.
It is used to evaluate connection coefficients between $q$-orthogonal polynomials.
