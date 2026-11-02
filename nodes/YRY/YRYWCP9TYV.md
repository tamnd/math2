---
tag: YRYWCP9TYV
kind: statement
role: theorem
name: Three-term recurrence for orthogonal polynomials
msc: [42C05, 33C45]
uses: [DYR1QFNGNJ, 0NB0AWGJBW, 0VT6P0GNQR, 0FYX44GP92]
about: [0FYX44GP92]
sources:
  - url: https://en.wikipedia.org/wiki/Favard%27s_theorem
---

## Statement

Let $\mu$ be a positive [[Borel measure|DYR1QFNGNJ]] on $\R$ with infinite support and with $\int_\R \abs{x}^k\, d\mu(x) < \infty$ for every $k \ge 0$.
Let $\ip{f}{g} = \int_\R f g\, d\mu$, and let $(p_n)_{n \ge 0}$ be the monic orthogonal polynomials for $\mu$, so that $\deg p_n = n$, $p_n$ has leading coefficient $1$, and $\ip{p_m}{p_n} = 0$ for $m \ne n$.
Set $p_{-1} = 0$.
Then there are real numbers $a_n$ for $n \ge 0$ and $b_n > 0$ for $n \ge 1$ such that, for every $n \ge 0$,
$$p_{n+1}(x) = (x - a_n)\, p_n(x) - b_n\, p_{n-1}(x),$$
namely $a_n = \frac{\ip{x p_n}{p_n}}{\ip{p_n}{p_n}}$ and $b_n = \frac{\ip{p_n}{p_n}}{\ip{p_{n-1}}{p_{n-1}}}$.

## Remarks

Infinite support makes $\ip{\cdot}{\cdot}$ an [[inner product|0NB0AWGJBW]] on all polynomials, so the [[Gram–Schmidt process|0VT6P0GNQR]] applied to $1, x, x^2, \dots$ gives the $p_n$.
The polynomial $x p_n - p_{n+1}$ has degree at most $n$, so it is a combination of $p_0, \dots, p_n$.
Its coefficient on $p_k$ is $\frac{\ip{x p_n}{p_k}}{\ip{p_k}{p_k}} = \frac{\ip{p_n}{x p_k}}{\ip{p_k}{p_k}}$, which is $0$ for $k \le n - 2$ because $x p_k$ has degree less than $n$.
This key step uses that multiplication by $x$ is symmetric for $\ip{\cdot}{\cdot}$.
The same symmetry gives $\ip{x p_n}{p_{n-1}} = \ip{p_n}{x p_{n-1}} = \ip{p_n}{p_n}$, which yields the formula for $b_n$.
Example: for the [[Hermite polynomials|MGACY98E9H]] made monic, $a_n = 0$ and $b_n = \frac{n}{2}$, so $p_2 = x^2 - \frac{1}{2}$.

## Explanations

### L1 human

Orthogonal polynomials are not just any list of polynomials: each one is built from the previous two by a short rule.
To get the next one, multiply the current one by $x$, shift by a multiple of it, and subtract a multiple of the one before.
This makes them cheap to compute and gives them many special properties.

### L2 human

The recurrence coefficients encode the measure: they form a symmetric tridiagonal Jacobi matrix whose spectral measure is $\mu$, normalised to mass $1$, when $\mu$ is determined by its moments.
The converse, that any such recurrence with $b_n > 0$ comes from a measure, is Favard's theorem.
The zeros of $p_n$ are the eigenvalues of the $n \times n$ truncated Jacobi matrix, which is the basis of the Golub–Welsch method for Gaussian quadrature.
The Christoffel–Darboux formula is a direct consequence of the recurrence.
