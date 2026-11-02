---
tag: DANS1S61SX
kind: statement
role: proposition
name: Thiele's interpolation formula
msc: [41A05, 41A20, 65D05]
uses: [0XDK9CGYKJ, 04P2RJ4WPS, 0EPAT51DXQ]
about: [0XDK9CGYKJ, 04P2RJ4WPS]
sources:
  - url: https://en.wikipedia.org/wiki/Thiele%27s_interpolation_formula
same_as:
  wikidata: Q7783991
  wikipedia: Thiele's interpolation formula
---

## Statement

Let $n \ge 1$, let $x_1, \dots, x_{n+1} \in \R$ be pairwise distinct, and let $f$ be a real [[function|0EPAT51DXQ]] defined at these points.
The *reciprocal differences* $\rho_k$ of $f$ are defined by $\rho_0(x_i) = f(x_i)$,
$$\rho_1(x_i, x_{i+1}) = \frac{x_i - x_{i+1}}{f(x_i) - f(x_{i+1})},$$
and, for $k \ge 2$,
$$\rho_k(x_i, \dots, x_{i+k}) = \frac{x_i - x_{i+k}}{\rho_{k-1}(x_i, \dots, x_{i+k-1}) - \rho_{k-1}(x_{i+1}, \dots, x_{i+k})} + \rho_{k-2}(x_{i+1}, \dots, x_{i+k-1}).$$
Set $a_0 = f(x_1)$, $a_1 = \rho_1(x_1, x_2)$ and $a_k = \rho_k(x_1, \dots, x_{k+1}) - \rho_{k-2}(x_1, \dots, x_{k-1})$ for $2 \le k \le n$.
Assume that no denominator above is zero and that the finite [[continued fraction|04P2RJ4WPS]]
$$R(x) = a_0 + \cfrac{x - x_1}{a_1 + \cfrac{x - x_2}{a_2 + \cfrac{x - x_3}{\ddots + \cfrac{x - x_n}{a_n}}}}$$
can be evaluated at each node without division by zero.
Then $R$ is a [[rational function|0XDK9CGYKJ]] and $R(x_i) = f(x_i)$ for $i = 1, \dots, n + 1$.

## Remarks

Reciprocal differences play for rational interpolation the role that [[divided differences|N5ZHV4HWDC]] play for polynomial interpolation.
The proof is by induction on $n$: the tail of the continued fraction starting at $a_1$ interpolates the reciprocal data $(x - x_1)/(f(x) - f(x_1))$ at $x_2, \dots, x_{n+1}$.

Example: $n = 1$ gives $R(x) = f(x_1) + (x - x_1)\dfrac{f(x_2) - f(x_1)}{x_2 - x_1}$, the line through the two data points.

The non-degeneracy hypothesis is needed.
The formula can break down even when a simple interpolant exists.
For instance, for equal values $f(x_1) = f(x_2)$, interpolated by a constant, the first reciprocal difference already divides by $0$.

## Explanations

### L1 human

Polynomials are bad at imitating functions with poles or with horizontal asymptotes.
Thiele's formula fits a ratio of polynomials instead, written as a continued fraction.
Its coefficients come from a table of reciprocal differences, built much like a table of divided differences.

### L2 human

Thiele's formula is the rational analogue of the [[Newton polynomial|9W77FPTM9E]]: each new node adds one more level to the continued fraction and leaves the earlier levels unchanged.
Its truncations give rational interpolants whose numerator and denominator degrees grow alternately.
It is closely related to [[Padé approximants|1F16G4V64X]], which match derivatives at one point instead of values at many points.
