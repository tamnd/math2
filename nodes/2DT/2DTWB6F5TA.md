---
tag: 2DTWB6F5TA
kind: example
name: Hilbert matrix
msc: [15B05, 15B48]
instance_of: [PQ1D8FQB3E, 95MTQMX59H, 0KX66CZMBB]
uses: [00SPJSDT3Z]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_matrix
same_as:
  wikidata: Q612991
  wikipedia: Hilbert matrix
---

## Example

For $n \ge 1$, the Hilbert matrix $H_n$ is the $n \times n$ real matrix with entries
$$(H_n)_{ij} = \frac{1}{i + j - 1} \qquad (1 \le i, j \le n).$$
For $n = 3$ it is
$$H_3 = \begin{pmatrix} 1 & \tfrac12 & \tfrac13 \\ \tfrac12 & \tfrac13 & \tfrac14 \\ \tfrac13 & \tfrac14 & \tfrac15 \end{pmatrix}.$$

It is a [[Hankel matrix|PQ1D8FQB3E]]: the entry depends only on $i + j$, with $h_k = 1/(k-1)$.

It is a [[Cauchy matrix|95MTQMX59H]]: with $x_i = i$ and $y_j = 1 - j$, the entry is $1/(x_i - y_j)$, and all $x_i - y_j = i + j - 1$ are nonzero.

It is a [[positive definite matrix|0KX66CZMBB]].
Indeed, $(H_n)_{ij} = \int_0^1 t^{i-1} t^{j-1} \, dt$, so $H_n$ is the [[Gram matrix|00SPJSDT3Z]] of the functions $1, t, \dots, t^{n-1}$ for the inner product $\ip{f}{g} = \int_0^1 f(t) g(t) \, dt$.
For $c \in \R^n$ and $p(t) = \sum_i c_i t^{i-1}$, this gives $c^T H_n c = \int_0^1 p(t)^2 \, dt$, which is positive when $c \ne 0$, because then $p$ is a nonzero polynomial.

## Remarks

The inverse of $H_n$ has integer entries; for example $\det H_2 = 1/12$ and $H_2^{-1} = \begin{pmatrix} 4 & -6 \\ -6 & 12 \end{pmatrix}$.
The Hilbert matrix is a standard test case in numerical analysis, because it is badly conditioned: its condition number grows very fast with $n$.

## Explanations

### L1 human

The Hilbert matrix is a simple square table of fractions, $1$, $\tfrac12$, $\tfrac13$, and so on, arranged so that each anti-diagonal holds one fraction.
It comes from fitting a polynomial to a function by least squares on the interval from $0$ to $1$.
It looks harmless, but it is extremely close to a singular matrix, so computers lose many digits when they solve systems with it.
