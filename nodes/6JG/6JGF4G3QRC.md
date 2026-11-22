---
tag: 6JGF4G3QRC
kind: proof
name: Proof of the dimension formula for a quotient space
msc: [15A03]
topics: [QHKTJ89V6S]
audience: ug1
proves: 0SXDQ6TN00
uses: [0QW084460E, 0M4SXE5WW3, 0WK0Y8RH1M, 0BR3FY5Q8M, 0KCQ9Y3QKA, 0CRMGPAH83, 088RYKAWK9, 03GSZ8RTZJ, 0ZHWKQMVX5]
sources:
  - url: https://pi.math.cornell.edu/~dcollins/math4310/IsomorphismTheorems.pdf
    locator: Proposition 1
---

## Proof

We extend a basis of $W$ to a basis of $V$ and show that the cosets of the new vectors form a basis of $V / W$.

1. Let $n = \dim V$.
   By the [[dimension of a subspace|0QW084460E]], $W$ is finite-dimensional.
   Let $m = \dim W$ and let $(w_1, \dots, w_m)$ be a [[basis|0KCQ9Y3QKA]] of $W$.
2. The family $(w_1, \dots, w_m)$ is [[linearly independent|0CRMGPAH83]] in $V$.
   By the [[extension to a basis|0M4SXE5WW3]], it is part of a basis of $V$.
3. By the [[dimension theorem|0WK0Y8RH1M]], this basis has $n$ vectors.
   We write it as $(w_1, \dots, w_m, v_{m+1}, \dots, v_n)$.
4. For $x \in V$, we have $x + W = W$ if and only if $x \in W$.
   If $x + W = W$, then $x = x + 0$ lies in $W$.
   If $x \in W$, then $x + w \in W$ for each $w \in W$, and each $w \in W$ equals $x + (w - x)$ with $w - x \in W$, so $x + W = W$.
5. In the [[quotient space|0BR3FY5Q8M]] $V / W$, the zero vector is $0 + W = W$.
   So by step 4, a coset $x + W$ is zero exactly when $x \in W$.
6. We show that the cosets $v_{m+1} + W, \dots, v_n + W$ [[span|088RYKAWK9]] $V / W$.
   Let $v + W \in V / W$, and write $v$ in the basis of step 3:
   $$v = \sum_{i=1}^{m} a_i w_i + \sum_{k=m+1}^{n} a_k v_k.$$
7. By the definition of the operations of $V / W$,
   $$v + W = \sum_{i=1}^{m} a_i (w_i + W) + \sum_{k=m+1}^{n} a_k (v_k + W).$$
8. Each $w_i$ lies in $W$, so $w_i + W$ is the zero vector by step 5.
   Hence $v + W = \sum_{k=m+1}^{n} a_k (v_k + W)$.
9. We show that the cosets $v_{m+1} + W, \dots, v_n + W$ are linearly independent.
   Suppose $\sum_{k=m+1}^{n} b_k (v_k + W) = W$ with $b_k \in F$.
10. The left side equals $x + W$ with $x = \sum_{k=m+1}^{n} b_k v_k$.
    By step 5, $x \in W$.
11. Since $(w_1, \dots, w_m)$ spans $W$, we have $x = \sum_{i=1}^{m} d_i w_i$ for some $d_1, \dots, d_m \in F$.
12. Then
    $$\sum_{i=1}^{m} d_i w_i - \sum_{k=m+1}^{n} b_k v_k = 0.$$
    The basis of step 3 is linearly independent, so all $b_k = 0$.
13. By steps 6 to 12, $(v_{m+1} + W, \dots, v_n + W)$ is a basis of $V / W$ with $n - m$ vectors.
14. So $V / W$ is [[finite-dimensional|0ZHWKQMVX5]] of [[dimension|03GSZ8RTZJ]] $n - m$, and
    $$\dim(V / W) + \dim W = (n - m) + m = \dim V.$$

## Idea

Choose a basis of $V$ that starts with a basis of $W$.
Passing to the quotient turns the vectors of $W$ into zero.
The remaining basis vectors survive as cosets: they still span, because the $W$ part of every vector disappears, and they stay independent, because a combination that falls into $W$ must be trivial.
So exactly $\dim W$ dimensions are lost.

## Variants

The quotient map $\pi \colon V \to V / W$ is linear and surjective with kernel $W$.
So the rank-nullity theorem for $\pi$ gives $\dim V = \dim W + \dim(V / W)$ at once.
This proof is shorter, but it moves the work into the proof of rank-nullity, which itself extends a basis of the kernel in the same way.

A second variant uses a complement $C$ of $W$, which exists by extending a basis.
The map $C \to V / W$, $c \mapsto c + W$, is an isomorphism, so $\dim(V / W) = \dim C = \dim V - \dim W$, where the last equality holds because $V = W \oplus C$.
