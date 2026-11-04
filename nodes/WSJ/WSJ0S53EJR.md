---
tag: WSJ0S53EJR
kind: proof
name: Proof that distinct eigenvalues imply diagonalisable
msc: [15A20]
proves: 0Y95Z7MT02
uses: [0ZND7NQ970, 0B5H4208Z9, 0HNMFG8F8K, 096V7H13H9, 0QK7FPE6VE, 056SW1E0AC, 0Y17PEKF24]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/minpolyandappns.pdf
    locator: Theorem 3.2
---

## Proof

We build a basis of eigenvectors.

1. Let $\lambda_1, \dots, \lambda_n \in F$ be pairwise distinct [[eigenvalues|0ZND7NQ970]] of $A$, that is, of the map $x \mapsto A x$ on $F^n$.
2. For each $i$, choose an [[eigenvector|0B5H4208Z9]] $v_i \in F^n$ for $\lambda_i$. So $v_i \ne 0$ and $A v_i = \lambda_i v_i$.
3. The eigenvalues are pairwise distinct. So $v_1, \dots, v_n$ are linearly independent, because [[eigenvectors with distinct eigenvalues are linearly independent|0HNMFG8F8K]].
4. The space $F^n$ has [[dimension $n$|0QK7FPE6VE]]. So the $n$ independent vectors $v_1, \dots, v_n$ form a [[basis|096V7H13H9]] of $F^n$.
5. Thus $F^n$ has a basis of eigenvectors of $A$. By the [[characterisation of diagonalisable matrices|056SW1E0AC]], $A$ is [[diagonalisable|0Y17PEKF24]] over $F$.

## Idea

One eigenvector for each of the $n$ distinct eigenvalues already gives $n$ independent vectors. In an $n$-dimensional space, that is a basis. A basis of eigenvectors is exactly what diagonalisation needs.
