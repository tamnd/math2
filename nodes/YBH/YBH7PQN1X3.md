---
tag: YBH7PQN1X3
kind: proof
name: Proof of the kernel and image of the adjoint
msc: ["15A04", "47A05"]
topics: [3YM9EK6VMB]
audience: ug1
proves: YPP8XT6B7Y
uses: [0VGSYBWHV2, 0ST8QF9T3T, TPP76FP659, 079D68S3AW, 0PXN9G4MX1, 0E2NYPVSP9, 0W4FSW1TVB]
methods: [MKHVRNW68H, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_adjoint
    locator: Properties
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Proof

We prove part 1 by a chain of equivalences.
The other parts follow from part 1, the rule $T^{**} = T$, and the facts on orthogonal complements in finite dimension.

1. A vector $u$ of an inner product space with $\ip{x}{u} = 0$ for all $x$ is $0$. The reason: $x = u$ gives $\ip{u}{u} = 0$, and positivity of the [[inner product|0VGSYBWHV2]] gives $u = 0$.
2. Part 1. Let $w \in W$. By step 1, $T^* w = 0$ holds if and only if $\ip{v}{T^* w} = 0$ for all $v \in V$.
3. By the [[definition of the adjoint|0ST8QF9T3T]], $\ip{v}{T^* w} = \ip{Tv}{w}$. So $T^* w = 0$ if and only if $\ip{Tv}{w} = 0$ for all $v \in V$.
4. The vectors $Tv$ with $v \in V$ are exactly the vectors of $\im T$. So the last condition says $\ip{x}{w} = 0$ for all $x \in \im T$.
5. By conjugate symmetry, $\ip{x}{w} = 0$ if and only if $\ip{w}{x} = 0$. So the condition says $w \in (\im T)^\perp$, by the definition of the [[orthogonal complement|079D68S3AW]]. Hence $\ker T^* = (\im T)^\perp$.
6. Part 3, first equality. Apply part 1 to the linear map $T^* \colon W \to V$. It gives $\ker (T^*)^* = (\im T^*)^\perp$.
7. By the [[algebraic properties|TPP76FP659]], $(T^*)^* = T$. So $\ker T = (\im T^*)^\perp$.
8. Part 2. Take the orthogonal complement of both sides of step 7: $(\ker T)^\perp = ((\im T^*)^\perp)^\perp$.
9. The space $V$ is finite-dimensional, so [[the double complement|0PXN9G4MX1]] gives $((\im T^*)^\perp)^\perp = \im T^*$. Hence $\im T^* = (\ker T)^\perp$.
10. Part 3, second equality. Take the orthogonal complement of both sides of part 1, in $W$. The double complement in $W$ gives $(\ker T^*)^\perp = \im T$.
11. Part 4. By part 2 and the [[dimension of the complement|0E2NYPVSP9]], $\dim \im T^* = \dim V - \dim \ker T$.
12. By the [[rank-nullity theorem|0W4FSW1TVB]] for $T$, $\dim V - \dim \ker T = \dim \im T$. So $\rank T^* = \rank T$.
13. Part 5. The map $T$ is injective if and only if $\ker T = 0$. By part 2, this holds if and only if $\im T^* = 0^\perp = V$, that is, $T^*$ is surjective.
14. Apply step 13 to $T^*$ in place of $T$, and use $(T^*)^* = T$. Then $T^*$ is injective if and only if $T$ is surjective. This proves all five parts.

## Idea

The kernel of $T^*$ consists of the vectors that $T^*$ kills, and by the definition these are the vectors orthogonal to every output of $T$.
The other identities follow by applying this to $T^*$ and by taking orthogonal complements twice.
Dimensions then follow from rank-nullity.

## Variants

With orthonormal bases, the statement becomes the statement about the four fundamental subspaces of the matrix $A$ of $T$ and of $A^*$.
The proof by matrices uses the rows of $A$: $A x = 0$ means that $x$ is orthogonal to the conjugates of all rows of $A$, which are the columns of $A^*$.
