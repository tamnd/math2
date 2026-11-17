---
tag: N5NTPAR2KT
kind: example
name: The cosets of a subgroup that is not normal do not form a group
msc: ["20B30"]
topics: [E1506A5A55]
audience: ug1
not_instance_of:
  - target: 0KYX2N69J0
    note: the product of cosets depends on the choice of representatives
uses: [0515A6D2Y1, 03DEH43F4H, 0CB0DX5BVV, 01E7SWYJX3]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_group
    locator: Definition
---

## Example

In the [[symmetric group|0515A6D2Y1]] $S_3$, let $H = \{e, (1\,2)\}$.
Compose permutations from right to left.
The rule $(aH)(bH) = abH$ does not define a product on the left cosets of $H$.
So the cosets of $H$ do not form a [[quotient group|0KYX2N69J0]].

1. Two of the [[left cosets|03DEH43F4H]] are $(1\,3)H = \{(1\,3), (1\,2\,3)\}$ and $(2\,3)H = \{(2\,3), (1\,3\,2)\}$. Here $(1\,3)(1\,2) = (1\,2\,3)$ and $(2\,3)(1\,2) = (1\,3\,2)$.
2. Take $a = (1\,3)$ and $b = (2\,3)$. Then $ab = (1\,3)(2\,3) = (1\,3\,2)$, which is in $(2\,3)H$.
3. Take $a' = (1\,2\,3)$, which is in the same coset as $a$, and the same $b$. Then $a'b = (1\,2\,3)(2\,3) = (1\,2)$, which is in $H$.
4. The cosets $(2\,3)H$ and $H$ are different. So the rule gives two different answers for the product of $(1\,3)H$ and $(2\,3)H$.

## Remarks

$H$ is not a [[normal subgroup|0CB0DX5BVV]] of $S_3$, because $(1\,3)(1\,2)(1\,3)^{-1} = (2\,3) \notin H$.
For a normal subgroup the product of cosets is always well defined, and for a subgroup that is not normal it is never well defined.
The failure shows up also in the cosets: $(1\,3)H = \{(1\,3), (1\,2\,3)\}$, but $H(1\,3) = \{(1\,3), (1\,3\,2)\}$, so $(1\,3)H \ne H(1\,3)$ ([[normality via cosets|01E7SWYJX3]]).
Compare $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$, which is normal: its two cosets form a group of order $2$.

## Explanations

### L1 human

We try to multiply two bags of permutations by taking one permutation from each bag.
For a good product, the bag of the answer must not depend on the choices.
Here two choices from the same bags give answers in different bags.
So there is no sensible product of these bags.

### L2 human

The check of well-definedness is the first step in the construction of a quotient group.
Here it fails, and one counterexample is enough to show it.
To find a counterexample, change one representative and keep the other, as in steps 2 and 3.
In the proof for a normal subgroup $N$, the key step is $b^{-1}nb \in N$.
Here this step fails: with $b = (2\,3)$ and $n = (1\,2)$, we get $b^{-1}nb = (1\,3) \notin H$.
