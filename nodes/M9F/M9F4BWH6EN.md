---
tag: M9F4BWH6EN
kind: example
name: A right coset of {e, (1 2)} in S3 that is not a left coset of it
msc: ["20B30"]
topics: [1VHQWXC64D]
audience: ug1
instance_of: [0NE1DK7H4T]
not_instance_of:
  - target: 03DEH43F4H
    note: the set {(1 3), (1 3 2)} is a right coset of H = {e, (1 2)} but not a left coset of H
uses: [0515A6D2Y1, 09H9Y0Q11W, 0X1JXT47GA, 03DEH43F4H, 0NE1DK7H4T, 0CB0DX5BVV]
sources:
  - url: https://en.wikipedia.org/wiki/Coset
    locator: First example
  - book: isbn:9780471433347
    locator: Section 3.2
---

## Example

Let $G = S_3$ be the [[symmetric group|0515A6D2Y1]] on $\{1, 2, 3\}$, with permutations composed from right to left.
Let $H = \{e, (1\,2)\}$.
This is a [[subgroup|0X1JXT47GA]], because $(1\,2)(1\,2) = e$.
Let $C = H(1\,3)$.

1. By the definition of a [[right coset|0NE1DK7H4T]], $C = \{e(1\,3), (1\,2)(1\,3)\}$.
2. We compute $(1\,2)(1\,3)$. The map $(1\,3)$ acts first. It sends $1 \mapsto 3$, and then $(1\,2)$ fixes $3$. So $1 \mapsto 3$. Next, $3 \mapsto 1 \mapsto 2$ and $2 \mapsto 2 \mapsto 1$. Thus $(1\,2)(1\,3) = (1\,3\,2)$.
3. So $C = \{(1\,3), (1\,3\,2)\}$.
4. The [[left cosets|03DEH43F4H]] of $H$ are $H = \{e, (1\,2)\}$, $(1\,3)H = \{(1\,3), (1\,2\,3)\}$ and $(2\,3)H = \{(2\,3), (1\,3\,2)\}$. Here $(1\,3)(1\,2) = (1\,2\,3)$ and $(2\,3)(1\,2) = (1\,3\,2)$, by the same method as step 2.
5. The set $C$ is not equal to any of these three sets. Thus $C$ is a right coset of $H$ but not a left coset of $H$.

## Remarks

The example shows that the left and the right cosets of a subgroup can be different partitions of $G$.
This happens here because $H$ is not [[normal|0CB0DX5BVV]] in $S_3$.
If we replace $H$ by the normal subgroup $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$, then each right coset is also a left coset.

The set $C$ is a left coset of a different subgroup.
Let $K = (1\,3)H(1\,3) = \{e, (2\,3)\}$.
Then $(1\,3)K = \{(1\,3), (1\,3)(2\,3)\} = \{(1\,3), (1\,3\,2)\} = C$.
In general, $Hg = g(g^{-1}Hg)$, so each right coset of $H$ is a left coset of the conjugate subgroup $g^{-1}Hg$.

## Explanations

### L1 human

Take the six ways to arrange three objects.
The subgroup $H$ has two of them: do nothing, or swap the objects $1$ and $2$.
If you do the swap after a move $g$, you get the right coset $Hg$.
If you do the swap before $g$, you get the left coset $gH$.
For $g = (1\,3)$ the two orders give different results.

### L2 human

We compare the two cosets of $H$ that contain $g = (1\,3)$.

1. The left coset is $gH = \{(1\,3), (1\,3)(1\,2)\} = \{(1\,3), (1\,2\,3)\}$.
2. The right coset is $Hg = \{(1\,3), (1\,2)(1\,3)\} = \{(1\,3), (1\,3\,2)\}$.
3. The two sets both contain $g$, but they are different.

The typical use is to check whether a subgroup is normal: $H$ is normal if and only if $gH = Hg$ for each $g$.
A trap is to compose permutations in the wrong order.
If you compose from left to right, the names of the two cosets change places.
