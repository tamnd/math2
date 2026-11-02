---
tag: RFA8HAEW9D
kind: statement
role: theorem
name: Gauss–Jacobi quadrature
msc: [65D32, 41A55, 33C45]
uses: [FP37BTP93K, TRD7DSF2KR, ZYT1JNT1Y0, Y7KSGE97GK]
about: [FP37BTP93K]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%E2%80%93Jacobi_quadrature
same_as:
  wikidata: Q5527851
  wikipedia: Gauss–Jacobi quadrature
---

## Statement

Let $\alpha, \beta > -1$ and let $\omega(x) = (1 - x)^{\alpha} (1 + x)^{\beta}$ on $(-1, 1)$.
Let $n \ge 1$ and let $x_1, \ldots, x_n$ be the zeros of the [[Jacobi polynomial|TRD7DSF2KR]] $P_n^{(\alpha, \beta)}$; they are real, simple and lie in $(-1, 1)$.
Let $\ell_1, \ldots, \ell_n$ be the [[Lagrange basis polynomials|Y7KSGE97GK]] of these nodes, and set $w_i = \int_{-1}^{1} \omega(x) \ell_i(x) \, dx$.
Then $w_i = \int_{-1}^{1} \omega(x) \ell_i(x)^2 \, dx > 0$ for each $i$, and for every polynomial $p$ of degree at most $2n - 1$,
$$\int_{-1}^{1} (1 - x)^{\alpha} (1 + x)^{\beta} p(x) \, dx = \sum_{i=1}^{n} w_i \, p(x_i).$$

## Remarks

The proof is the general argument for [[Gaussian quadrature|FP37BTP93K]].
Divide $p$ by $P_n^{(\alpha,\beta)}$ and use the orthogonality of $P_n^{(\alpha,\beta)}$ to all polynomials of lower degree for the weight $\omega$.
Then integrate the remainder, of degree at most $n - 1$, by interpolation.
Applying the exactness to $\ell_i^2$, of degree $2n - 2$, gives $w_i = \int \omega \ell_i^2 > 0$.
Example: $\alpha = \beta = 0$ gives Gauss–Legendre quadrature.
Example: $\alpha = \beta = -\tfrac12$ gives Gauss–Chebyshev quadrature, with nodes $x_i = \cos\frac{(2i - 1)\pi}{2n}$ and equal weights $w_i = \pi / n$; for $n = 1$ the rule is $\pi f(0)$, and indeed $\int_{-1}^1 (1 - x^2)^{-1/2} dx = \pi$.
The condition $\alpha, \beta > -1$ is needed for $\omega$ to be integrable; for $\alpha \le -1$ even $\int \omega$ diverges.

## Explanations

### L1 human

Some integrals on $[-1, 1]$ have a factor that blows up or vanishes at an endpoint, such as $1/\sqrt{1 - x}$.
Ordinary rules handle such endpoint behaviour badly.
Gauss–Jacobi quadrature builds the factor $(1-x)^\alpha (1+x)^\beta$ into the weights, so that only the smooth part of the integrand is sampled.
With $n$ points it is exact for that factor times any polynomial of degree up to $2n - 1$.

### L2 human

The family contains the Gauss–Legendre and Gauss–Chebyshev rules as special cases.
It is used for integrands with known algebraic endpoint singularities, for example in boundary integral methods and in spectral methods based on Jacobi polynomials.
The nodes and weights are computed in practice from the three-term recurrence of the Jacobi polynomials, as eigenvalues and eigenvector components of a symmetric tridiagonal matrix.
