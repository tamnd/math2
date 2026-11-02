---
tag: HB0MJCV482
kind: statement
role: theorem
name: Christoffel–Darboux formula
msc: [42C05, 33C45]
uses: [DYR1QFNGNJ, 0NB0AWGJBW]
about: [0NB0AWGJBW]
sources:
  - url: https://en.wikipedia.org/wiki/Christoffel%E2%80%93Darboux_formula
same_as:
  wikidata: Q5111650
  wikipedia: Christoffel–Darboux formula
---

## Statement

Let $\mu$ be a positive [[Borel measure|DYR1QFNGNJ]] on $\R$ with infinite support and all moments finite.
Let $(p_n)_{n \ge 0}$ be the orthonormal polynomials for $\mu$, with $\deg p_n = n$ and leading coefficient $k_n > 0$.
So $\int_\R p_m p_n\, d\mu$ is $1$ if $m = n$ and $0$ otherwise.
Then for every $n \ge 0$ and all real $x \ne y$,
$$\sum_{j=0}^{n} p_j(x)\, p_j(y) = \frac{k_n}{k_{n+1}} \cdot \frac{p_{n+1}(x)\, p_n(y) - p_n(x)\, p_{n+1}(y)}{x - y},$$
and for every real $x$,
$$\sum_{j=0}^{n} p_j(x)^2 = \frac{k_n}{k_{n+1}} \left( p_{n+1}'(x)\, p_n(x) - p_n'(x)\, p_{n+1}(x) \right).$$

## Remarks

For orthonormal polynomials the three-term recurrence reads $x p_j = \alpha_{j+1} p_{j+1} + \beta_j p_j + \alpha_j p_{j-1}$ with $\alpha_j = \frac{k_{j-1}}{k_j}$.
Multiplying it at $x$ by $p_j(y)$, subtracting the same with $x$ and $y$ exchanged, and summing over $j$ makes the sum telescope to the right-hand side.
The second formula is the limit $y \to x$ of the first.
Example: let $n = 0$ and let $\mu$ be a probability measure with mean $m$ and variance $s^2$.
Then $p_0 = 1$ and $p_1 = \frac{x - m}{s}$, and the right-hand side is $\frac{1}{1/s} \cdot \frac{(x - m)/s - (y - m)/s}{x - y} = 1$, which matches the left-hand side.
The left-hand side $K_n(x, y)$ is the reproducing kernel of the polynomials of degree at most $n$ for the [[inner product|0NB0AWGJBW]] $\int f g\, d\mu$.

## Explanations

### L1 human

Adding up the products $p_j(x) p_j(y)$ for all degrees up to $n$ looks like a long computation.
The formula says that the sum collapses to an expression in only the last two polynomials.
This is the polynomial analogue of the closed form for the Dirichlet kernel in Fourier series.

### L2 human

The kernel $K_n(x, y)$ gives the orthogonal projection onto polynomials of degree at most $n$, so the formula controls partial sums of orthogonal expansions.
The diagonal form shows $p_{n+1}' p_n - p_n' p_{n+1} > 0$, which implies that the zeros of $p_n$ and $p_{n+1}$ are real, simple and interlace.
The numbers $\frac{1}{K_n(x, x)}$ are the Christoffel function, whose values at the zeros of $p_{n+1}$ are the Gaussian quadrature weights.
In random matrix theory the kernel $K_n$ describes the correlations of eigenvalues of unitary invariant ensembles.
