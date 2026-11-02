---
tag: SB8PFJCJBC
kind: statement
role: theorem
name: Weyl–von Neumann theorem
msc: [47A55, 47B15]
uses: [HM2HHE3J51, 0Z2P41SVDP, 6HSJBJ8TTQ, 0S9GGTR0EX, M2NEP1K5AE, 153N5DW55Z]
about: [M2NEP1K5AE]
sources:
  - url: https://en.wikipedia.org/wiki/Weyl%E2%80%93von_Neumann_theorem
same_as:
  wikidata: Q7990342
  wikipedia: Weyl–von Neumann theorem
---

## Statement

Let $H$ be a [[separable|0Z2P41SVDP]] complex [[Hilbert space|HM2HHE3J51]], and let $\varepsilon > 0$.
Let $A$ be a bounded operator on $H$ with $A = A^*$, where $A^*$ is the [[adjoint|6HSJBJ8TTQ]] of $A$.
Then there are an [[orthonormal basis|0S9GGTR0EX]] $(e_n)$ of $H$, real numbers $(\lambda_n)$ and a [[compact operator|M2NEP1K5AE]] $K$ on $H$ such that:

1. $K = K^*$ and $\norm{K} < \varepsilon$;
2. $(A + K) e_n = \lambda_n e_n$ for every $n$.

## Remarks

In words, every bounded self-adjoint operator is the sum of a diagonal operator and a compact self-adjoint operator of arbitrarily small norm.
Weyl proved the version with $K$ compact, and von Neumann showed that $K$ can be chosen in the Hilbert–Schmidt class, the [[Schatten class|153N5DW55Z]] $S_2$, with Hilbert–Schmidt norm less than $\varepsilon$.
The idea of the proof is to use spectral projections of $A$ for small intervals.
They give finite-dimensional subspaces that are almost invariant under $A$, and $A$ is diagonalized up to a small error on each of them.
Example: the multiplication operator $(Af)(x) = x f(x)$ on $L^2([0,1])$ has no eigenvalues at all, yet by the theorem a compact perturbation of small norm has an orthonormal basis of eigenvectors.
The theorem does not extend to trace class perturbations.
By the Kato–Rosenblum theorem, if $A$ has a nonzero absolutely continuous part, then so does $A + K$ for every trace class self-adjoint $K$.
Then $A + K$ is not diagonal.

## Explanations

### L1 human

A self-adjoint matrix can be diagonalized exactly, but a self-adjoint operator on an infinite-dimensional space may have no eigenvectors at all.
The theorem says that this failure is small: after adding a tiny compact correction, there is a full orthonormal basis of eigenvectors.
So, up to compact errors, every self-adjoint operator is diagonal.

### L2 human

The theorem shows that the point spectrum and the continuous spectrum of a self-adjoint operator are not stable under compact perturbations, while the essential spectrum is, by Weyl's theorem.
It is a starting point of the theory of unitary equivalence modulo compact operators, which later led to the Brown–Douglas–Fillmore theory of extensions of C*-algebras.
