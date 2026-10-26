---
tag: ~c5fc6c0d
kind: definition
name: Power sum symmetric polynomials
msc: ["05E05"]
defines: ~4d7f9e8a
uses: [~9753c486]
sources:
  - url: https://en.wikipedia.org/wiki/Power_sum_symmetric_polynomial
    locator: Definition
---

## Definition

Let $R$ be a [[commutative ring|~79bc52c4]] and let $n \ge 1$.
For $k \ge 1$, the $k$-th power sum in $x_1, \dots, x_n$ is
$$p_k = x_1^k + x_2^k + \dots + x_n^k \in R[x_1, \dots, x_n].$$

## Remarks

Each $p_k$ is [[symmetric|~9753c486]] and homogeneous of degree $k$.
[[Newton's identities|~eab00ef7]] relate the power sums to the [[elementary symmetric polynomials|~71a32e63]].
If $R$ contains $\mathbb{Q}$, then every symmetric polynomial in $R[x_1, \dots, x_n]$ is a polynomial in $p_1, \dots, p_n$.
This fails over $\mathbb{Z}$: $e_2 = \tfrac{1}{2}(p_1^2 - p_2)$ needs the coefficient $\tfrac{1}{2}$.

## Explanations

### L1 human

The power sums add up the same power of every variable.
They are symmetric, and over the rationals they can replace the elementary symmetric polynomials as generators.
