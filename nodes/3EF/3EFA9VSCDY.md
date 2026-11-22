---
tag: 3EFA9VSCDY
kind: proof
name: Proof that the quotient space is a vector space
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
proves: YYH67TQ9GV
methods: [41JZ39GE3F, 0NTF6DMVAP]
uses: [0SVR29SV1V, 0J0SK5FF4M, 0EPTJA5QV4, 05EGHEQZAW, 02YFME3RGW]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 3E
---

## Proof

We show that the cosets are the classes of an equivalence relation, then that the operations respect it, and then we check the axioms and the quotient map.

1. Define $v \sim w$ when $v - w \in U$.
   It is reflexive, since $v - v = 0 \in U$.
   It is symmetric, since $w - v = (-1)(v - w) \in U$.
   It is transitive, since $v - x = (v - w) + (w - x) \in U$.
   Each of these uses that $U$ is a [[subspace|0EPTJA5QV4]].
2. The class of $v$ is $\{w : w - v \in U\}$.
   Writing $w = v + u$ with $u = w - v$ shows that this class equals $v + U$, so the cosets are the equivalence classes.
3. Two equivalence classes are equal or disjoint, and each element lies in its own class.
   Hence $v + U = w + U$ holds if and only if $v \sim w$, that is, $v - w \in U$.
   This proves part 1.
4. Addition is well defined.
   Let $v + U = v' + U$ and $w + U = w' + U$, so that $v - v' \in U$ and $w - w' \in U$ by step 3.
   Then $(v + w) - (v' + w') = (v - v') + (w - w') \in U$, so $(v + w) + U = (v' + w') + U$.
5. Scalar multiplication is well defined.
   With $v - v' \in U$ and $a \in F$, we get $av - av' = a(v - v') \in U$, so $av + U = av' + U$.
   This proves part 2.
6. Each vector space axiom for $V / U$ follows from the same axiom in $V$, applied to representatives.
   For example, associativity of addition reads
   $$\bigl((v + U) + (w + U)\bigr) + (x + U) = \bigl((v + w) + x\bigr) + U = \bigl(v + (w + x)\bigr) + U = (v + U) + \bigl((w + U) + (x + U)\bigr).$$
7. The zero is $0 + U$, since $(v + U) + (0 + U) = (v + 0) + U = v + U$.
   The negative of $v + U$ is $(-v) + U$, since their sum is $(v - v) + U = 0 + U$.
   This proves part 3, so $V / U$ is a [[vector space|05EGHEQZAW]].
8. The [[quotient map|0J0SK5FF4M]] $\pi$ is linear, by the definition of the operations:
   $$\pi(v + w) = (v + w) + U = \pi(v) + \pi(w), \qquad \pi(av) = av + U = a\, \pi(v).$$
9. Every coset $v + U$ equals $\pi(v)$, so $\pi$ is surjective.
10. By step 3, $\pi(v) = 0 + U$ holds if and only if $v - 0 \in U$.
    So the [[kernel|02YFME3RGW]] of $\pi$ is $U$, which proves part 4.

## Idea

The three closure properties of a subspace are exactly what the construction needs.
The zero vector gives reflexivity, negatives give symmetry, and sums give transitivity.
The same closure under sums and scalars then makes the operations independent of the representatives.
After that, every axiom is inherited from $V$, because the operations on cosets are the operations on representatives.

## Variants

One can define $V / U$ directly as the set of equivalence classes of $\sim$ and never mention cosets; step 2 shows that the two descriptions agree.
The same proof works for a submodule of a module over any ring.
For a normal subgroup of a group only the group operation is present, and normality replaces commutativity in the check of step 4.
