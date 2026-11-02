---
tag: CJCPD4DZ65
kind: statement
role: proposition
name: Positivity of Hankel matrices of moments
msc: [44A60, 15B05]
uses: [PR11BZQQPG, 01XAHPADBA, PQ1D8FQB3E, 01MMVW8CKC, 0KX66CZMBB, FQTXV6BQZG]
about: [PQ1D8FQB3E, 01XAHPADBA]
sources:
  - url: https://en.wikipedia.org/wiki/Hankel_matrix
  - url: https://en.wikipedia.org/wiki/Hamburger_moment_problem
---

## Statement

Let $\mu$ be a positive Borel [[measure|PR11BZQQPG]] on $\R$ such that every [[moment|01XAHPADBA]] $m_k = \int x^k \, d\mu(x)$, $k \ge 0$, is finite.
For $n \ge 0$, let $H_n = (m_{j+k})_{j,k=0}^{n}$ be the $(n+1) \times (n+1)$ [[Hankel matrix|PQ1D8FQB3E]] of the moments.
Then:

1. $H_n$ is [[positive semidefinite|01MMVW8CKC]] for every $n \ge 0$.
2. If the [[support|FQTXV6BQZG]] of $\mu$ is an infinite set, then $H_n$ is [[positive definite|0KX66CZMBB]] for every $n \ge 0$, so $\det H_n > 0$.

## Remarks

For real $c = (c_0, \ldots, c_n)$, let $p(x) = \sum_{j=0}^{n} c_j x^j$.
Then $c^{T} H_n c = \sum_{j,k} c_j c_k \int x^{j+k} \, d\mu = \int p(x)^2 \, d\mu(x) \ge 0$, which is clause 1.
If $c \ne 0$, then $p$ is a nonzero polynomial with at most $n$ real roots.
If the support is infinite, then $p^2 > 0$ on a set of positive measure, so the integral is positive, which is clause 2.
Example: for Lebesgue measure on $[0, 1]$, $m_k = 1/(k+1)$, and $H_n$ is the Hilbert matrix $(1/(j + k + 1))$, which is positive definite.
For $\mu = \delta_0$, the support is finite, $H_n$ has $m_0 = 1$ in one corner and zeros elsewhere, and it is only semidefinite for $n \ge 1$.
The converse of clause 1 is Hamburger's theorem, part of the [[Hamburger moment problem|TBNCFXTMMW]].
It says that a real sequence with all $H_n$ positive semidefinite is the moment sequence of a positive measure on $\R$.

## Explanations

### L1 human

From the moments of a mass distribution, build square tables whose entry in row $j$ and column $k$ is the moment of order $j + k$.
These tables always behave like sums of squares: they never give a negative value.
The reason is that each value is the average of the square of a polynomial.

### L2 human

This is the necessary condition in the Hamburger moment problem, and Hamburger showed that it is also sufficient.
For the Stieltjes problem on $[0, \infty)$ one adds the shifted Hankel matrices $(m_{j+k+1})$, whose positivity reflects $x \ge 0$.
The positive definite case gives an inner product $\ip{p}{q} = \int p q \, d\mu$ on polynomials, and Gram–Schmidt then yields the orthogonal polynomials of $\mu$.
