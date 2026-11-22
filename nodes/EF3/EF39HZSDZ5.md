---
tag: EF39HZSDZ5
kind: proof
name: Proof that the kernel of a linear map is a subspace
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
proves: REWYZ8N7EN
methods: [0NTF6DMVAP, 41JZ39GE3F]
uses: [02YFME3RGW, 0EPTJA5QV4, STYEWH8R4E]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: Properties
  - book: isbn:9780134860244
    locator: Section 2.1
---

## Proof

We check the three conditions in the [[definition of a subspace|0EPTJA5QV4]], and then we rewrite $T(u) = T(v)$ as an equation for $u - v$.

1. By the [[lemma on zero|STYEWH8R4E]], $T(0) = 0$, so $0 \in \ker T$.
2. Let $u, v \in \ker T$, so that $T(u) = 0$ and $T(v) = 0$.
3. Additivity gives $T(u + v) = T(u) + T(v) = 0 + 0 = 0$, so $u + v \in \ker T$.
4. Let $a \in F$ and $v \in \ker T$; homogeneity gives $T(av) = a\,T(v) = a \cdot 0 = 0$, so $av \in \ker T$.
5. Steps 1, 3 and 4 show that $\ker T$ is a subspace of $V$.
6. For the second claim, let $u, v \in V$; linearity gives $T(u - v) = T(u) - T(v)$.
7. So $T(u) = T(v)$ holds if and only if $T(u - v) = 0$, which means $u - v \in \ker T$.

## Idea

The kernel is defined by the equation $T(v) = 0$.
The right side is $0$, and $0$ is kept by sums and scalar multiples, so the set of solutions is kept by them as well.
The second claim moves everything to one side, so that a question about two vectors becomes a question about one.

## Variants

The kernel is the preimage $T^{-1}(\{0\})$ of the subspace $\{0\}$ of $W$.
The preimage of any subspace of $W$ under a linear map is a subspace of $V$, with the same proof, and the lemma is the case of the smallest subspace.
The closure checks can also be done in one step: if $u, v \in \ker T$ and $a \in F$, then $T(au + v) = a\,T(u) + T(v) = 0$.
