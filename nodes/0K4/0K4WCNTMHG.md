---
tag: 0K4WCNTMHG
kind: definition
name: Rayleigh quotient
msc: [15A18, 15A42]
defines: 06WHP8SE98
uses: [0EKZCX4K3P, 0ZND7NQ970]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_quotient
    locator: Bounds for Hermitian M
---

## Definition

Let $A$ be a [[Hermitian|0P17NGQQMQ]] $n \times n$ complex matrix, and let $x \in \C^n$ with $x \ne 0$.
The *Rayleigh quotient* of $A$ and $x$ is the real number
$$R(A, x) = \frac{x^* A x}{x^* x}.$$

## Remarks

For each $x \ne 0$, $\lambda_{\min} \le R(A, x) \le \lambda_{\max}$, where $\lambda_{\min}$ and $\lambda_{\max}$ are the least and the greatest [[eigenvalues|0BQAA2BK3Q]] of $A$.
If $x$ is an eigenvector for $\lambda$, then $R(A, x) = \lambda$.
So $\lambda_{\max} = \max_{x \ne 0} R(A, x)$ and $\lambda_{\min} = \min_{x \ne 0} R(A, x)$.

## Explanations

### L1 human

The Rayleigh quotient measures how much a symmetric matrix stretches a given direction, on average.
Its largest value over all directions is the largest eigenvalue.
This gives a way to estimate eigenvalues without solving the characteristic equation.
