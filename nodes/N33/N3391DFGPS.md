---
tag: N3391DFGPS
kind: proof
name: Proof of the dimension of the dual space by the dual basis
msc: [15A03, 15A04]
proves: 00889YD15K
uses: [07JBSZE0V4, 0ZD2CF6ZS0, 0R8X9XA83A, 0KCQ9Y3QKA, 0CRMGPAH83, 088RYKAWK9, 03GSZ8RTZJ, 0ZHWKQMVX5, 07YQ1C78G0]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Finite-dimensional case
---

## Proof

We show that the dual basis is a basis of $V^*$.

1. Let $n = \dim V$ and let $(b_1, \dots, b_n)$ be a [[basis|0KCQ9Y3QKA]] of $V$. Write $\delta_{ij} = 1$ if $i = j$ and $\delta_{ij} = 0$ if $i \ne j$.
2. For each $i$, [[the extension of values on a basis|0R8X9XA83A]] gives a [[linear form|07YQ1C78G0]] $b_i^* \colon V \to F$ with $b_i^*(b_j) = \delta_{ij}$ for all $j$. These form the [[dual basis|0ZD2CF6ZS0]] $(b_1^*, \dots, b_n^*)$ in the [[dual space|07JBSZE0V4]] $V^*$.
3. The family $(b_1^*, \dots, b_n^*)$ is [[linearly independent|0CRMGPAH83]]. Suppose $\sum_{i=1}^n \lambda_i b_i^* = 0$ with $\lambda_i \in F$.
4. The operations of $V^*$ are pointwise. Evaluating at $b_j$ gives $0 = \sum_{i=1}^n \lambda_i b_i^*(b_j) = \sum_{i=1}^n \lambda_i \delta_{ij} = \lambda_j$. This holds for each $j$.
5. The family $(b_1^*, \dots, b_n^*)$ [[spans|088RYKAWK9]] $V^*$. Let $g \in V^*$, and let $h = \sum_{i=1}^n g(b_i)\, b_i^*$.
6. For each $j$, $h(b_j) = \sum_{i=1}^n g(b_i) \delta_{ij} = g(b_j)$. So $g$ and $h$ are linear maps $V \to F$ that agree on a basis.
7. By the uniqueness part of [[the same result|0R8X9XA83A]], $g = h$. So $g$ lies in the span of the $b_i^*$.
8. By steps 3 to 7, $(b_1^*, \dots, b_n^*)$ is a basis of $V^*$ with $n$ elements.
9. So $V^*$ is [[finite-dimensional|0ZHWKQMVX5]], and its [[dimension|03GSZ8RTZJ]] is $n = \dim V$.

## Idea

The dual basis vector $b_i^*$ reads off the $i$-th coordinate. A linear form is fixed by its values on the basis, so it is the combination of the coordinate functions with those values as coefficients. This gives exactly $n$ basis vectors for $V^*$.
