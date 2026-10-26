---
tag: ~ebbd8e12
kind: definition
name: Characteristic polynomial
msc: [15A15, 15A18]
defines: ~14b846dc
uses: [~0dd14763, ~c4555ee3]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Formal definition
---

## Definition

Let $K$ be a commutative ring, let $n \ge 1$, and let $A$ be an $n \times n$ matrix over $K$.
The *characteristic polynomial* of $A$ is the polynomial
$$p_A(t) = \det(t I_n - A) \in K[t],$$
where $\det$ is the [[determinant|~362fc72a]] of a matrix with entries in the polynomial ring $K[t]$.

## Remarks

The polynomial $p_A$ is monic of degree $n$.
For $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $p_A(t) = t^2 - (a + d) t + (ad - bc)$.
Some authors use $\det(A - t I_n)$, which equals $(-1)^n p_A(t)$.
Over a field, the roots of $p_A$ are the [[eigenvalues|~13fe038c]] of $A$.

## Explanations

### L1 human

The number $\lambda$ is an eigenvalue exactly when $A - \lambda I$ is singular, that is, when $\det(\lambda I - A) = 0$.
If we replace $\lambda$ by a variable $t$, then we get a polynomial.
Its roots are the eigenvalues.
