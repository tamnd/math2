---
tag: 6CZRBQ3GP1
kind: proof
name: Proof of the dimension formula for the space of linear maps
msc: [15A03, 15A04]
proves: 0Z9N1ER0W0
uses: [0X9MBPP2Z3, 0R8X9XA83A, 0KCQ9Y3QKA, 0CRMGPAH83, 088RYKAWK9, 03GSZ8RTZJ, 0ZHWKQMVX5]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/linear_algebra_thm_proof.pdf
    locator: Section 2.2
---

## Proof

We write down an explicit basis of $\Hom_F(V, W)$ with $\dim V \cdot \dim W$ elements.

1. Let $n = \dim V$ and $m = \dim W$. Let $(b_1, \dots, b_n)$ be a [[basis|0KCQ9Y3QKA]] of $V$ and $(c_1, \dots, c_m)$ a basis of $W$.
2. Write $\delta_{jk} = 1$ if $j = k$ and $\delta_{jk} = 0$ if $j \ne k$.
3. For $1 \le i \le m$ and $1 \le j \le n$, [[the extension of values on a basis|0R8X9XA83A]] gives a linear map $E_{ij} \colon V \to W$ with $E_{ij}(b_k) = \delta_{jk} c_i$ for $1 \le k \le n$.
4. These $mn$ maps lie in the [[space of linear maps|0X9MBPP2Z3]] $\Hom_F(V, W)$. Its operations are pointwise.
5. The maps $E_{ij}$ [[span|088RYKAWK9]] $\Hom_F(V, W)$. Let $T \in \Hom_F(V, W)$. For each $k$, write $T(b_k) = \sum_{i=1}^m a_{ik} c_i$ with $a_{ik} \in F$.
6. Let $S = \sum_{i=1}^m \sum_{j=1}^n a_{ij} E_{ij}$. By the pointwise operations, $S(b_k) = \sum_{i,j} a_{ij} \delta_{jk} c_i = \sum_{i=1}^m a_{ik} c_i = T(b_k)$ for each $k$.
7. So $S$ and $T$ are linear maps that agree on a basis. By the uniqueness part of [[the same result|0R8X9XA83A]], $T = S$.
8. The maps $E_{ij}$ are [[linearly independent|0CRMGPAH83]]. Suppose $\sum_{i,j} a_{ij} E_{ij} = 0$, the zero map, with $a_{ij} \in F$.
9. Evaluating at $b_k$, as in step 6, gives $\sum_{i=1}^m a_{ik} c_i = 0$. Since $(c_i)$ is linearly independent, $a_{ik} = 0$ for all $i$. This holds for each $k$.
10. By steps 5 to 9, $(E_{ij})_{1 \le i \le m,\, 1 \le j \le n}$ is a basis of $\Hom_F(V, W)$ with $mn$ elements.
11. So $\Hom_F(V, W)$ is [[finite-dimensional|0ZHWKQMVX5]], and its [[dimension|03GSZ8RTZJ]] is $mn = \dim V \cdot \dim W$.

## Idea

A linear map is fixed by the images of the basis vectors of $V$, and each image has $m$ coordinates. So a linear map is described by $mn$ free scalars, the entries of its matrix. The maps $E_{ij}$ are the maps whose matrix has a single entry $1$.
