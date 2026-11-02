---
tag: RKFB6AHPBE
kind: definition
name: Matrix summability method
msc: [40C05]
defines: M6311DWJ1E
uses: [X80DZEXQDQ, 0QE8STGJH2, 0JH4MN4K1C]
sources:
  - url: https://en.wikipedia.org/wiki/Silverman–Toeplitz_theorem
---

## Definition

Let $A = (a_{nk})_{n, k \ge 0}$ be an infinite matrix of complex numbers.
For a complex [[sequence|0QE8STGJH2]] $s = (s_k)_{k \ge 0}$, the *$A$-transform* of $s$ is the sequence
$$(As)_n = \sum_{k=0}^{\infty} a_{nk} s_k \qquad (n \ge 0),$$
defined when each of these [[series|0JH4MN4K1C]] converges.
The sequence $s$ is *$A$-summable to $L$* if $(As)_n$ is defined for every $n$ and $(As)_n \to L$ as $n \to \infty$.
The resulting [[summability method|X80DZEXQDQ]], with $D_A$ the set of $A$-summable sequences and $A(s) = \lim_n (As)_n$, is the *matrix method* given by $A$.

## Remarks

Example: the Cesàro matrix has $a_{nk} = \frac{1}{n+1}$ for $k \le n$ and $a_{nk} = 0$ for $k > n$.
For $s = (1, 0, 1, 0, \dots)$ one has $(As)_n = \frac{\lceil (n+1)/2 \rceil}{n+1} \to \frac12$, so $s$ is $A$-summable to $\frac12$.
Non-example: for $a_{nk} = 2^{-k-1}$ and $s_k = 2^k$, the series $\sum_k a_{nk} s_k = \sum_k \frac12$ diverges, so $(As)_n$ is not defined and $s$ is not $A$-summable.
The identity matrix gives ordinary convergence.
Every matrix method is linear, because $A(\lambda s + \mu t) = \lambda As + \mu At$.

## Explanations

### L1 human

Multiply the infinite matrix by the sequence, viewed as an infinite column, and take the limit of the result.
