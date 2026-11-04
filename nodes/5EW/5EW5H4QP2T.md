---
tag: 5EW5H4QP2T
kind: proof
name: Proof of the dimension formula for a tensor product
msc: [15A69, 15A03]
proves: 0R84PF4JV7
uses: [0SH5VT8QYA, 05G2G0P224, 0VTQTPQGAV, 0EVHJFTG9Z, 018W3V3TCT]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/tensorprod.pdf
    locator: Theorem 4.9 and Example 4.10
---

## Proof

1. Let $m = \dim V$ and $n = \dim W$. By the definition of [[dimension|05G2G0P224]], $V$ has a [[basis|0VTQTPQGAV]] $e_1, \dots, e_m$ and $W$ has a basis $f_1, \dots, f_n$.
2. By the [[basis of a tensor product|0SH5VT8QYA]], the family $(e_i \otimes f_j)$ with $1 \le i \le m$ and $1 \le j \le n$ is a basis of $V \otimes W$.
3. This family has $mn$ indices. Its vectors are pairwise distinct, because a [[linearly independent|0EVHJFTG9Z]] family has no repeated vector. A repeat $x = y$ would give the nontrivial relation $1 \cdot x - 1 \cdot y = 0$.
4. So $V \otimes W$ has a basis of $mn$ vectors. Hence it is [[finite-dimensional|018W3V3TCT]], and $\dim(V \otimes W) = mn = \dim V \cdot \dim W$.

## Idea

The products $e_i \otimes f_j$ of basis vectors form a basis of $V \otimes W$. There is one such product for each pair $(i, j)$, which gives $\dim V \cdot \dim W$ vectors.
