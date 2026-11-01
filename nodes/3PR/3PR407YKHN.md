---
tag: 3PR407YKHN
kind: definition
name: Spectral radius
msc: [15A18, 15A60]
defines: 9V7YQA85PC
uses: [0JXZKX526R, 0BQAA2BK3Q, 0XPX5NC67E]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_radius
---

## Definition

Let $A$ be an $n \times n$ complex [[square matrix|0JXZKX526R]], and let $\sigma(A) \subset \C$ be its [[spectrum|0XPX5NC67E]], the set of its [[eigenvalues|0BQAA2BK3Q]].
The *spectral radius* of $A$ is
$$\rho(A) = \max \set{\abs{\lambda} : \lambda \in \sigma(A)}.$$

## Remarks

Example: $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has characteristic polynomial $x^2 + 1$, so $\sigma(A) = \set{i, -i}$ and $\rho(A) = 1$.

The spectral radius is not a norm on matrices.
For $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, the only eigenvalue is $0$, so $\rho(N) = 0$ although $N \ne 0$.

For every [[operator norm|06EKW1AKXF]] $\norm{\cdot}$, $\rho(A) \le \norm{A}$, and [[Gelfand's formula|3KX0KQ7V05]] gives $\rho(A) = \lim_{k \to \infty} \norm{A^k}^{1/k}$.
The powers $A^k$ tend to $0$ if and only if $\rho(A) < 1$.
For a [[normal matrix|0MR0BYF0K2]], $\rho(A)$ equals the operator norm induced by the Euclidean norm.
The same definition applies to a linear map of a finite-dimensional complex vector space.

## Explanations

### L1 human

The spectral radius is the size of the largest eigenvalue.
It says how fast repeated application of the matrix makes vectors grow or shrink in the long run.
