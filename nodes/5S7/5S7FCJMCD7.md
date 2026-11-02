---
tag: 5S7FCJMCD7
kind: definition
name: Tensor product of Hilbert spaces
msc: [46M05, 46C05]
defines: EY0X2NKA3S
uses: [HM2HHE3J51, 0BF2DE2SYK, 0S9GGTR0EX]
sources:
  - url: https://en.wikipedia.org/wiki/Tensor_product_of_Hilbert_spaces
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $H_1$ and $H_2$ be [[Hilbert spaces|HM2HHE3J51]] over $\mathbb{K}$.
Let $H_1 \otimes H_2$ be their algebraic [[tensor product|0BF2DE2SYK]] over $\mathbb{K}$.
There is exactly one inner product on $H_1 \otimes H_2$ such that
$$\ip{x_1 \otimes x_2}{y_1 \otimes y_2} = \ip{x_1}{y_1} \ip{x_2}{y_2}$$
for all $x_1, y_1 \in H_1$ and $x_2, y_2 \in H_2$.
The *tensor product of Hilbert spaces* $H_1 \mathbin{\widehat{\otimes}} H_2$ is the completion of $H_1 \otimes H_2$ for this inner product.

## Remarks

If $(e_i)_{i \in I}$ and $(f_j)_{j \in J}$ are [[orthonormal bases|0S9GGTR0EX]] of $H_1$ and $H_2$, then $(e_i \otimes f_j)_{(i, j) \in I \times J}$ is an orthonormal basis of $H_1 \mathbin{\widehat{\otimes}} H_2$.

Example: $\ell^2(I) \mathbin{\widehat{\otimes}} \ell^2(J)$ is unitarily equivalent to $\ell^2(I \times J)$, by $e_i \otimes f_j \mapsto e_{(i, j)}$.
Both sides have orthonormal bases indexed by $I \times J$, and the map sends one onto the other.
Similarly, for $\sigma$-finite measure spaces, $L^2(X) \mathbin{\widehat{\otimes}} L^2(Y)$ is $L^2(X \times Y)$, with $f \otimes g$ sent to $(x, y) \mapsto f(x) g(y)$.

Non-example: if $H_1$ and $H_2$ are infinite-dimensional, the algebraic tensor product $H_1 \otimes H_2$ with the inner product above is not complete.
For instance, $\sum_{n \ge 1} 2^{-n} e_n \otimes f_n$ converges in the completion but is not a finite sum of elementary tensors.
In finite dimension no completion is needed, and $H_1 \mathbin{\widehat{\otimes}} H_2 = H_1 \otimes H_2$.

Other completions of $H_1 \otimes H_2$, for instance the projective tensor product, are Banach spaces with different norms.
