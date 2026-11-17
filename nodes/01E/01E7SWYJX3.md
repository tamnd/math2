---
tag: 01E7SWYJX3
kind: statement
role: theorem
name: Normality via cosets
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
about: [0CB0DX5BVV, 564VVAQTNR]
uses: [0CB0DX5BVV, 03DEH43F4H, 0NE1DK7H4T]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Equivalent conditions
  - url: https://en.wikipedia.org/wiki/Coset
    locator: Normal subgroups
---

## Statement

Let $G$ be a [[group|G5S1M9]] and let $N$ be a [[subgroup|0X1JXT47GA]] of $G$.
The following three conditions are equivalent.

1. $N$ is [[normal|0CB0DX5BVV]] in $G$, that is, $gng^{-1} \in N$ for each $g \in G$ and each $n \in N$.
2. $gN = Ng$ for each $g \in G$, that is, each [[left coset|03DEH43F4H]] of $N$ is equal to the [[right coset|0NE1DK7H4T]] with the same representative.
3. The product of left cosets is well defined: if $aN = a'N$ and $bN = b'N$, then $abN = a'b'N$.

## Remarks

Condition 3 says that the rule $(aN)(bN) = abN$ does not depend on the choice of the representatives $a$ and $b$.
So it defines an operation on the set $G/N$ of left cosets, and this operation makes $G/N$ the [[quotient group|0KYX2N69J0]].
The proof uses the fact that $xN = yN$ exactly when $y^{-1}x \in N$, for all $x, y \in G$.

### Why each hypothesis is needed

- Condition 2 must hold for each $g \in G$, not only for some $g$. Let $H = \{e, (1\,2)\}$ in $S_3$, with composition from right to left. Then $gH = Hg$ for $g = (1\,2)$, but $(1\,2\,3)H = \{(1\,2\,3), (1\,3)\}$ and $H(1\,2\,3) = \{(1\,2\,3), (2\,3)\}$.
- For this $H$, condition 3 also fails. We have $(1\,3)H = (1\,2\,3)H$, but $(1\,3)(1\,3)H = H$ and $(1\,2\,3)(1\,3)H = (2\,3)H \ne H$.
- The theorem needs $N$ to be a subgroup. Then the left cosets of $N$ partition $G$, and the test $xN = yN \iff y^{-1}x \in N$ holds.

### Consequences

- The [[quotient group|0KYX2N69J0]] $G/N$ exists exactly when $N$ is normal.
- For a normal subgroup, the left cosets and the right cosets are the same sets, so we can say "the cosets of $N$" without "left" or "right".
- A subgroup of [[index|0DTXBQPA2S]] $2$ is normal, because its left and right cosets are both $N$ and $G \setminus N$ ([[subgroups of index two are normal|0V547YQRMV]]).

### Converse

The statement is a list of equivalent conditions, so each converse is part of it.

### Generalizations

- For a single $g \in G$, the proof shows that $gN = Ng$ exactly when $gNg^{-1} = N$, that is, when $g$ is in the [[normaliser|0YGN3VAA0D]] of $N$.
- For rings, the same argument shows that the product $(a + I)(b + I) = ab + I$ of additive cosets of an additive subgroup $I$ is well defined exactly when $I$ is a two-sided ideal.

## History

Galois used normal subgroups in his letter of 1832 to Auguste Chevalier.
Hölder defined quotient groups in 1889.
Condition 3 is the condition that the definition of a quotient group needs.

## Explanations

### L1 human

A subgroup cuts the group into pieces called cosets, in two ways: by multiplication on the left and by multiplication on the right.
For most subgroups, the two ways give different pieces.
For a normal subgroup, they give the same pieces.
Then we can multiply two pieces: take one element from each piece, multiply them, and take the piece of the product.
The answer does not depend on which elements we took.
This is how the pieces become a new group.

### L2 human

Condition 3 is the one we use in practice, because it builds the quotient group.
We check it for $N = A_3$ in $S_3$, with composition from right to left.
The cosets are $A_3$ and $T = \{(1\,2), (1\,3), (2\,3)\}$.
The product of two transpositions is even, so it is in $A_3$.
The product of a transposition and an element of $A_3$ is odd, so it is in $T$.
So the product of two cosets is the same for each choice of representatives: $TT = A_3$, $TA_3 = A_3T = T$ and $A_3A_3 = A_3$.

A common error is to think that $gN = Ng$ means that $g$ commutes with each element of $N$.
The equation compares two sets.
For $g = (1\,2)$ and $N = A_3$, both sides are $T$, but $(1\,2)(1\,2\,3) = (2\,3)$ and $(1\,2\,3)(1\,2) = (1\,3)$.

### L3 human

Condition 3 says that the equivalence relation $a \sim a' \iff aN = a'N$ is compatible with the group operation.
An equivalence relation on an algebraic structure that is compatible with all its operations is a congruence.
So the normal subgroups of $G$ correspond to the congruences on $G$.
Each congruence on $G$ is the relation $aN = a'N$, where $N$ is the class of $e$.
This is the group case of a general pattern of universal algebra.
For rings, the congruences correspond to two-sided ideals, and for modules they correspond to submodules.
