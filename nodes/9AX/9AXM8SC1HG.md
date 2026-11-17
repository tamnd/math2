---
tag: 9AXM8SC1HG
kind: proof
name: Proof of the third isomorphism theorem
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
proves: 0TJ1V9DDPC
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0CB0DX5BVV, 0KYX2N69J0, 03DEH43F4H, 0GJ83E78A5, 0C9ZKYSPYR, 0CXXJNG5B6]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem C (groups)
---

## Proof

We apply the universal property of the quotient to the projection $G \to G/M$, and then the first isomorphism theorem.

1. Let $G$ be a group with identity $e$, and let $N$ and $M$ be [[normal subgroups|0CB0DX5BVV]] of $G$ with $N \subseteq M$. Because $N$ and $M$ are normal, the [[quotient groups|0KYX2N69J0]] $G/N$ and $G/M$ exist. This step uses the hypothesis that $M$ is normal.
2. For $a \in G$, the [[left coset|03DEH43F4H]] $aM$ equals $M$ if and only if $a \in M$. If $aM = M$, then $a = ae \in aM = M$. If $a \in M$, then $aM \subseteq M$ by closure, and each $m \in M$ equals $a(a^{-1}m)$ with $a^{-1}m \in M$, so $M \subseteq aM$.
3. Let $\pi_M \colon G \to G/M$ be the projection $\pi_M(g) = gM$. It is a surjective homomorphism, and by step 2 its kernel is $M$, because $M$ is the identity of $G/M$.
4. By the hypothesis $N \subseteq M$, we get $N \subseteq \ker \pi_M$. This step uses the hypothesis that $N \subseteq M$.
5. We apply the [[universal property of the quotient group|0GJ83E78A5]] to $\pi_M$ and $N$. Part 1 gives a homomorphism $f \colon G/N \to G/M$ with $f(gN) = gM$ for each $g \in G$.
6. Part 2 gives $\operatorname{im} f = \operatorname{im} \pi_M = G/M$. So $f$ is surjective.
7. Part 3 gives $\ker f = (\ker \pi_M)/N = M/N$.
8. The kernel of a homomorphism is a normal subgroup ([[this statement|0C9ZKYSPYR]]). So $M/N$ is a normal subgroup of $G/N$. This proves part 1.
9. By the [[first isomorphism theorem|0CXXJNG5B6]] applied to $f$, the formula $(gN)(M/N) \mapsto f(gN) = gM$ gives a well defined isomorphism from $(G/N)/(M/N)$ onto $\operatorname{im} f = G/M$. This proves part 2.

This proves the theorem.

## Idea

Each coset of $N$ is inside one coset of $M$, because $N \subseteq M$.
So the projection $G \to G/M$ factors through $G/N$, as the map $gN \mapsto gM$.
This map is surjective, and its kernel is $M/N$, so the first isomorphism theorem gives the result.

## Variants

A direct proof checks the properties of $f(gN) = gM$ by hand.
If $gN = g'N$, then $g' = gn$ with $n \in N \subseteq M$, so $g'M = gnM = gM$, and $f$ is well defined.
The map is a homomorphism, because $f((aN)(bN)) = (ab)M = (aM)(bM)$.
It is surjective, and by step 2 its kernel is the set of cosets $gN$ with $g \in M$, which is $M/N$.
