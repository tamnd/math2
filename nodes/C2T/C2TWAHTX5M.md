---
tag: C2TWAHTX5M
kind: proof
name: Proof of the rank–nullity theorem by the first isomorphism theorem
msc: ["15A03", "15A04"]
topics: [9080WQTZ3M]
audience: ug1
proves: 0W4FSW1TVB
methods: [0NTF6DMVAP]
uses: [0MTBGVZ4XJ, 0SXDQ6TN00, 0VJBSK15SN, REWYZ8N7EN, B6KFVB1H5F, 0BR3FY5Q8M, 03GSZ8RTZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Rank–nullity_theorem
    locator: Second proof
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Modules
---

## Proof

Let $n = \dim V$ and let $K = \ker T$.

1. By the [[lemma on the kernel|REWYZ8N7EN]], $K$ is a subspace of $V$. So the [[quotient space|0BR3FY5Q8M]] $V / K$ is defined.
2. By the [[dimension of a quotient space|0SXDQ6TN00]], $V / K$ is finite-dimensional, and $\dim(V / K) + \dim K = n$.
3. By the [[first isomorphism theorem|0MTBGVZ4XJ]], the map $v + K \mapsto T(v)$ is a linear isomorphism $V / K \to \im T$.
4. By the [[theorem on the image|B6KFVB1H5F]], $\im T$ is spanned by the images of a basis of $V / K$. So $\im T$ is finite-dimensional.
5. By the [[classification by dimension|0VJBSK15SN]], $\dim \im T = \dim(V / K)$.
6. Steps 2 and 5 give $\dim \im T + \dim \ker T = n = \dim V$.

## Idea

The first isomorphism theorem identifies the image with the quotient $V / \ker T$.
The dimension of a quotient is the dimension of the whole space minus the dimension of the subspace.
So the image has dimension $\dim V - \dim \ker T$.

## Variants

- The proof moves the counting into the formula $\dim(V / K) = \dim V - \dim K$, which is proved by extending a basis of $K$. So this proof and the [[first proof|XNC3VQ11SH]] use the same idea, split into two lemmas.
- In infinite dimension, steps 1 and 3 still hold, and $V \cong K \oplus V/K$ by choosing a [[complement|0P9T8WHNMH]] of $K$. This gives the cardinal form $\dim V = \dim \ker T + \dim \im T$.
