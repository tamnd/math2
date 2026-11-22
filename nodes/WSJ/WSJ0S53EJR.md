---
tag: WSJ0S53EJR
kind: proof
name: Proof that n distinct eigenvalues imply diagonalizable
msc: ["15A20"]
topics: [Z6S6PWMJPH]
audience: ug1
proves: 0Y95Z7MT02
methods: [0NTF6DMVAP]
uses: [0ZND7NQ970, 0B5H4208Z9, 0HNMFG8F8K, 096V7H13H9, 056SW1E0AC, 0Y17PEKF24]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/minpolyandappns.pdf
    locator: Theorem 3.2
---

## Proof

We choose one eigenvector for each eigenvalue and show that these vectors form a basis.

1. Let $\lambda_1, \dots, \lambda_n \in F$ be the pairwise distinct [[eigenvalues|0ZND7NQ970]] of $T$.
2. For each $i$, choose an [[eigenvector|0B5H4208Z9]] $v_i \in V$ for $\lambda_i$.
   So $v_i \ne 0$ and $T(v_i) = \lambda_i v_i$.
3. The eigenvalues are pairwise distinct, so $v_1, \dots, v_n$ are linearly independent, because [[eigenvectors with distinct eigenvalues are linearly independent|0HNMFG8F8K]].
4. The space $V$ has dimension $n$, so the $n$ independent vectors $v_1, \dots, v_n$ form a basis of $V$, by the [[right-size criterion|096V7H13H9]].
5. Thus $V$ has a basis of eigenvectors of $T$.
   By the [[characterization by eigenvectors|056SW1E0AC]], $T$ is [[diagonalizable|0Y17PEKF24]] over $F$.
6. For an $n \times n$ matrix $A$, the eigenvalues of the map $x \mapsto A x$ in $F$ are the roots of $p_A$ in $F$.
   So $n$ distinct roots give $n$ distinct eigenvalues, and steps 1 to 5 apply to this map.

## Idea

One eigenvector for each of the $n$ distinct eigenvalues already gives $n$ independent vectors.
In an $n$-dimensional space, $n$ independent vectors form a basis.
A basis of eigenvectors is exactly what diagonalization needs, so nothing else is left to check.

## Variants

The [[minimal polynomial criterion|0MPAJRB23T]] gives a second proof.
The minimal polynomial divides $p_T = (t - \lambda_1) \cdots (t - \lambda_n)$, so it is a product of distinct linear factors, and $T$ is diagonalizable.
