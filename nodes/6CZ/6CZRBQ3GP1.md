---
tag: 6CZRBQ3GP1
kind: proof
name: Proof of the dimension formula for the space of linear maps
msc: ["15A03", "15A04"]
topics: [9080WQTZ3M]
audience: ug1
proves: 0Z9N1ER0W0
methods: [01XM7JEKHY, 0NTF6DMVAP]
uses: [0X9MBPP2Z3, 0VPCJWGMP9, ~dbc9db14, 0R8X9XA83A, 0KCQ9Y3QKA, 0CRMGPAH83, 088RYKAWK9, 03GSZ8RTZJ, 0ZHWKQMVX5]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/linear_algebra_thm_proof.pdf
    locator: Section 2.2
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Proof

We write down an explicit basis of $\Hom_F(V, W)$ with $\dim V \cdot \dim W$ elements.

1. Let $n = \dim V$ and $m = \dim W$. Let $(b_1, \dots, b_n)$ be a [[basis|0KCQ9Y3QKA]] of $V$ and $(c_1, \dots, c_m)$ a basis of $W$.
2. Write $\delta_{jk} = 1$ if $j = k$, and $\delta_{jk} = 0$ if $j \ne k$.
3. Fix $i \le m$ and $j \le n$. By the [[theorem on bases|0R8X9XA83A]], there is a linear map $E_{ij} \colon V \to W$ with $E_{ij}(b_k) = \delta_{jk} c_i$.
4. These $mn$ maps lie in [[$\Hom_F(V, W)$|0VPCJWGMP9]]. By the [[vector space theorem|~dbc9db14]], this set is a vector space with pointwise operations.
5. (Spanning.) Let $T \in \Hom_F(V, W)$. For each $k$, write $T(b_k) = \sum_{i=1}^m a_{ik} c_i$ with $a_{ik} \in F$.
6. Let $S = \sum_{i,j} a_{ij} E_{ij}$. The operations are pointwise, so $S(b_k) = \sum_{i,j} a_{ij} \delta_{jk} c_i$.
7. Only the terms with $j = k$ remain. So $S(b_k) = \sum_{i=1}^m a_{ik} c_i = T(b_k)$ for each $k$.
8. $S$ and $T$ are linear and agree on a basis. By uniqueness in the theorem on bases, $T = S$.
9. So the maps $E_{ij}$ [[span|088RYKAWK9]] $\Hom_F(V, W)$.
10. (Independence.) Suppose $\sum_{i,j} a_{ij} E_{ij} = 0$, the zero map, with $a_{ij} \in F$.
11. Evaluate at $b_k$, as in steps 6 and 7. This gives $\sum_{i=1}^m a_{ik} c_i = 0$.
12. The family $(c_i)$ is [[linearly independent|0CRMGPAH83]]. So $a_{ik} = 0$ for each $i$, and this holds for each $k$.
13. By steps 9 and 12, $(E_{ij})$ is a basis of $\Hom_F(V, W)$ with $mn$ elements.
14. So $\Hom_F(V, W)$ is [[finite-dimensional|0ZHWKQMVX5]], and its [[dimension|03GSZ8RTZJ]] is $mn = \dim V \cdot \dim W$.

## Idea

A linear map is fixed by the images of the $n$ basis vectors of $V$.
Each image has $m$ coordinates in $W$.
So a linear map is described by $mn$ free scalars, the entries of its matrix.
The map $E_{ij}$ is the map whose matrix has entry $1$ at place $(i, j)$ and $0$ elsewhere.

## Variants

- The map $\Hom(V, W) \to W^n$, $T \mapsto (T(b_1), \dots, T(b_n))$, is linear. By the theorem on bases, it is bijective. So $\dim \Hom(V, W) = \dim W^n = nm$.
- After the matrix isomorphism $\Hom(V, W) \cong M_{m \times n}(F)$ is known, the result follows from the basis of matrix units of $M_{m \times n}(F)$.
