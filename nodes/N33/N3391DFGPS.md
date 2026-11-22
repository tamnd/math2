---
tag: N3391DFGPS
kind: proof
name: Proof of the dimension of the dual space by the dual basis
msc: ["15A03", "15A04"]
topics: [9K7FFF26QR]
audience: ug1
proves: 00889YD15K
methods: [0NTF6DMVAP]
uses: [07JBSZE0V4, 0ZD2CF6ZS0, 0R8X9XA83A, 0KCQ9Y3QKA, 0CRMGPAH83, 088RYKAWK9, 03GSZ8RTZJ, 0ZHWKQMVX5, 07YQ1C78G0]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Finite-dimensional case
---

## Proof

We show that the dual basis is independent and spans $V^*$, by evaluating forms on the basis vectors.

1. Let $n = \dim V$, let $(b_1, \dots, b_n)$ be a [[basis|0KCQ9Y3QKA]] of $V$, and write $\delta_{ij} = 1$ if $i = j$ and $\delta_{ij} = 0$ if $i \ne j$.
2. For each $i$, the theorem that [[linear maps are determined by a basis|0R8X9XA83A]] gives a [[linear form|07YQ1C78G0]] $b_i^*$ on $V$ with $b_i^*(b_j) = \delta_{ij}$ for all $j$.
3. These forms make up the [[dual basis|0ZD2CF6ZS0]] $(b_1^*, \dots, b_n^*)$ in the [[dual space|07JBSZE0V4]] $V^*$.
4. To show that the family is [[linearly independent|0CRMGPAH83]], suppose that $\sum_{i=1}^n \lambda_i b_i^* = 0$ with $\lambda_i \in F$.
5. The operations of $V^*$ are pointwise, so evaluation at $b_j$ gives $0 = \sum_{i=1}^n \lambda_i\, b_i^*(b_j) = \sum_{i=1}^n \lambda_i \delta_{ij} = \lambda_j$ for each $j$.
6. To show that the family [[spans|088RYKAWK9]] $V^*$, let $g \in V^*$ and put $h = \sum_{i=1}^n g(b_i)\, b_i^*$.
7. For each $j$, evaluation at $b_j$ gives $h(b_j) = \sum_{i=1}^n g(b_i)\, \delta_{ij} = g(b_j)$, so $g$ and $h$ agree on a basis.
8. By the uniqueness part of the [[same theorem|0R8X9XA83A]], $g = h = \sum_i g(b_i)\, b_i^*$, which is part 2 and shows that $g$ lies in the span.
9. By steps 4 to 8, $(b_1^*, \dots, b_n^*)$ is a basis of $V^*$ with $n$ elements, which is part 1.
10. So $V^*$ is [[finite-dimensional|0ZHWKQMVX5]], and its [[dimension|03GSZ8RTZJ]] is $n = \dim V$, which is part 3.

## Idea

The form $b_i^*$ reads off coordinate $i$ of a vector.
A linear form is fixed by its values on the basis, so it must be the combination of the coordinate forms with those values as coefficients.
Evaluating at $b_j$ picks out one coefficient at a time, and that is what makes the dual basis independent.
The spanning step uses a finite sum, which is why the argument needs a finite basis.

## Variants

The theorem that linear maps are determined by a basis also gives a shorter route that never names the dual basis.
The map $V^* \to F^n$, $f \mapsto (f(b_1), \dots, f(b_n))$, is linear, and it is bijective because a form can take any values on the basis and is fixed by them.
So $V^* \cong F^n$, and $\dim V^* = n$.
The dual basis is the preimage of the standard basis of $F^n$ under this isomorphism.

Part 3 is also the case $W = F$ of the formula $\dim \Hom(V, W) = \dim V \cdot \dim W$ from the [[dimension of the space of linear maps|0Z9N1ER0W0]].
