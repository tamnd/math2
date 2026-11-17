---
tag: S6XAS4GBV8
kind: example
name: A left coset in S3 that is not a double coset
msc: ["20A05"]
topics: [1VHQWXC64D]
audience: grad
not_instance_of:
  - target: DSBE321XMS
    note: "the left coset (1 3)H is a proper subset of the double coset H(1 3)H, so it is not an (H, H) double coset"
uses: [0515A6D2Y1, 0X1JXT47GA, 03DEH43F4H, DSBE321XMS, 08QMKTWF9T, 0CB0DX5BVV]
sources:
  - url: https://en.wikipedia.org/wiki/Double_coset
    locator: Definition
---

## Example

Let $G = S_3$ be the [[symmetric group|0515A6D2Y1]], and compose permutations from right to left.
Let $H = \{e, (1\,2)\}$, a [[subgroup|0X1JXT47GA]] of order $2$.
Let $C = (1\,3)H$ be the [[left coset|03DEH43F4H]] of $(1\,3)$.
We show that $C$ is not an $(H, H)$ [[double coset|DSBE321XMS]].

1. We have $C = \{(1\,3), (1\,3)(1\,2)\} = \{(1\,3), (1\,2\,3)\}$.
2. Suppose that $C = HgH$ for some $g \in S_3$.
3. Then $(1\,3) \in HgH$. The double cosets form a [[partition|08QMKTWF9T]] of $G$, so $HgH = H(1\,3)H$.
4. The double coset $H(1\,3)H$ contains $(1\,2)(1\,3) = (1\,3\,2)$.
5. But $(1\,3\,2) \notin C$, by step 1. This contradicts step 2.

Thus $C$ is a left coset of $H$, but it is not an $(H, H)$ double coset.

## Remarks

The double coset of $(1\,3)$ is $H(1\,3)H = \{(1\,3), (2\,3), (1\,2\,3), (1\,3\,2)\}$.
It is the union of the two left cosets $(1\,3)H$ and $(2\,3)H$.
So the left coset $C$ is one half of a double coset.

The only left coset of $H$ that is also an $(H, H)$ double coset is $H$ itself.
In general, a left coset $gH$ is an $(H, H)$ double coset exactly when $HgH = gH$, that is, when $g^{-1}Hg \subseteq H$.
For a finite group, this holds exactly when $g$ normalises $H$.
If $H$ is [[normal|0CB0DX5BVV]], then each left coset is a double coset.

## Explanations

### L1 human

A left coset uses moves of the subgroup on one side only.
A double coset uses them on both sides, so it can be larger.
Here the left coset has $2$ elements, and the double coset around it has $4$ elements.
So the left coset is only a part of a double coset.

### L2 human

We test the criterion $g^{-1}Hg \subseteq H$ for $g = (1\,3)$.

1. We have $(1\,3)^{-1} = (1\,3)$.
2. We compute $(1\,3)(1\,2)(1\,3) = (2\,3)$.
3. Thus $g^{-1}Hg = \{e, (2\,3)\}$, and this set is not contained in $H$.
4. So $(1\,3)H$ is not a double coset, as we found above.

The typical use is to see that double cosets are coarser than cosets.
A trap is to think that each double coset is a coset of some subgroup.
The double coset $H(1\,3)H$ has $4$ elements, and $4$ does not divide $6$.
