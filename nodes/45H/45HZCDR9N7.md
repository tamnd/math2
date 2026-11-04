---
tag: 45HZCDR9N7
kind: proof
name: Proof that the projections of a product are continuous
msc: [54B10]
proves: 0PM88Z9W4M
uses: [0Z57EC6YX3, 06EX0FHBTF, 0SY9ECQ19Q, 0FGCFY1AZX, 0CNQXVBHCX]
sources:
  - url: https://en.wikipedia.org/wiki/Product_topology
    locator: Definition
---

## Proof

We compute preimages of open sets.

1. Let $U$ be open in $X$. The [[preimage|0FGCFY1AZX]] is $\pi_1^{-1}(U) = \set{(x, y) \in X \times Y : x \in U} = U \times Y$.
2. The set $Y$ is open in $Y$ by the axioms of a [[topology|0CNQXVBHCX]]. So $U \times Y$ is one of the sets $U \times V$ of the [[product topology|0Z57EC6YX3]] basis.
3. By the definition of a [[basis|06EX0FHBTF]], its members are open. So $\pi_1^{-1}(U)$ is open in $X \times Y$, and $\pi_1$ is [[continuous|0SY9ECQ19Q]].
4. Let $V$ be open in $Y$. In the same way, $\pi_2^{-1}(V) = X \times V$, and $X$ is open in $X$.
5. So $X \times V$ is a basic open set, and $\pi_2$ is continuous.

## Idea

The preimage of an open set under a projection is a box whose other side is the whole factor. Such a box is one of the basic open sets of the product topology.
