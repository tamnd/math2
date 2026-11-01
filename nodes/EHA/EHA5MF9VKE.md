---
tag: EHA5MF9VKE
kind: statement
role: theorem
name: Markov brothers' inequality
msc: [41A17, 26C05, 26D05]
uses: [MAM9H3SY3Y, 0DPF6WRZW6, 084NGSTWM7]
about: [1G0B73WPX8]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_brothers%27_inequality
same_as:
  wikidata: Q176674
  wikipedia: Markov brothers' inequality
---

## Statement

Let $n \ge 1$ and let $P$ be a real [[polynomial function|MAM9H3SY3Y]] of [[degree|0DPF6WRZW6]] at most $n$.
Write $\norm{Q} = \max_{-1 \le x \le 1} \abs{Q(x)}$ for a function $Q$ continuous on $[-1, 1]$.

1. $\norm{P'} \le n^2 \norm{P}$.
2. More generally, for $1 \le k \le n$, the $k$-th [[derivative|084NGSTWM7]] satisfies
$$\norm{P^{(k)}} \le \frac{n^2 (n^2 - 1^2)(n^2 - 2^2) \cdots (n^2 - (k-1)^2)}{1 \cdot 3 \cdot 5 \cdots (2k - 1)} \, \norm{P}.$$

## Remarks

Both bounds are attained by the [[Chebyshev polynomial|M6EAR1JHPP]] $T_n$, defined by $T_n(\cos \theta) = \cos(n \theta)$.
The constant in the second bound equals $T_n^{(k)}(1)$; for $k = 1$ it is $n^2$.

Example: $P(x) = T_2(x) = 2x^2 - 1$ has $\norm{P} = 1$ and $P'(x) = 4x$, so $\norm{P'} = 4 = 2^2 \norm{P}$.

In the interior, [[Bernstein's inequality for polynomials|F0YGC89S9R]] gives the stronger pointwise bound $\abs{P'(x)} \le \frac{n}{\sqrt{1 - x^2}} \norm{P}$ for $-1 < x < 1$.
The factor $n^2$ in the first bound is caused by the endpoints $\pm 1$, where this pointwise bound degenerates.

## Explanations

### L1 human

A polynomial of degree $n$ that stays between $-1$ and $1$ on the interval $[-1, 1]$ cannot be too steep there.
Its slope is at most $n^2$ in absolute value.
The Chebyshev polynomials, which oscillate as much as possible, are the steepest ones.

### L2 human

Markov-type inequalities bound the derivative of a polynomial by its size, with a constant depending only on the degree.
They are used in approximation theory to prove inverse theorems: if a function is well approximated by polynomials, then it is smooth.
The first inequality is due to A. A. Markov and the general one to his brother V. A. Markov.
