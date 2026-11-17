---
tag: 0NE1DK7H4T
kind: concept
name: Right coset
msc: ["20A05"]
topics: [1VHQWXC64D]
audience: ug1
specializes: [564VVAQTNR]
uses: [G5S1M9, 0X1JXT47GA, 564VVAQTNR, 03DEH43F4H]
sources:
  - url: https://en.wikipedia.org/wiki/Coset
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Coset
    locator: First example
  - book: isbn:9780471433347
    locator: Section 3.2
---

## Summary

Let $G$ be a [[group|G5S1M9]], let $H$ be a [[subgroup|0X1JXT47GA]] of $G$, and let $g \in G$.
The right coset of $H$ with representative $g$ is the set $Hg = \{hg : h \in H\}$.
For $a, b \in G$, the right cosets $Ha$ and $Hb$ are equal if and only if $ab^{-1} \in H$, and they are disjoint otherwise.
The inversion $x \mapsto x^{-1}$ maps each [[left coset|03DEH43F4H]] $gH$ onto the right coset $Hg^{-1}$.
Right cosets matter because the comparison of $gH$ with $Hg$ detects whether $H$ is a [[normal subgroup|0CB0DX5BVV]].

## Motivation

In a group that is not abelian, $gh$ and $hg$ can differ.
So the copies $gH$ of $H$ moved on the left can differ from the copies $Hg$ moved on the right.
Right cosets are the second way to sort $G$ into copies of $H$.
The two sortings agree exactly for the normal subgroups.

## Notation

The [[right coset|060Z37VVB6]] of $g$ is written $Hg$, and in additive notation $H + g$.
The set of all right cosets of $H$ in $G$ is written $H \backslash G$.
Some books, for example those of Marshall Hall and Derek Robinson, use right cosets as the standard cosets.
This site uses left cosets as the standard.

## Remarks

### Examples

- In an [[abelian group|082GHNPJ53]], $Hg = gH$ for each $g$. Thus the cosets of $3\mathbb{Z}$ in $\mathbb{Z}$ in [[this example|BM4VXG92DT]] are right cosets too.
- In $(\mathbb{R}^2, +)$, the right cosets of a line through the origin are the parallel lines, as [[this example|3WTCVF5RP8]] shows.
- In $S_3$ with $H = \{e, (1\,2)\}$, the right cosets are $H$, $\{(1\,3), (1\,3\,2)\}$ and $\{(2\,3), (1\,2\,3)\}$, as [[this example|4DWC4XFS34]] shows.
- In $S_3$, the subgroup $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$ has the right cosets $A_3$ and $\{(1\,2), (1\,3), (2\,3)\}$. These are also its left cosets.

### Non-examples

- In $S_3$, the left coset $(1\,3)H = \{(1\,3), (1\,2\,3)\}$ of $H = \{e, (1\,2)\}$ is not a right coset of $H$, as [[this example|BPVNZ5VNND]] shows.
- In $\mathbb{Z}/4\mathbb{Z}$, the set $\{1, 2\}$ is a translate of $\{0, 1\}$, but it is not a right coset of any subgroup. The only subgroup of order $2$ is $\{0, 2\}$, with the cosets $\{0, 2\}$ and $\{1, 3\}$. [[This example|94SNG0EQQZ]] gives the details.

### Basic properties

Let $a, b, g \in G$.

- The element $g$ is in $Hg$, because $g = eg$ and $e \in H$.
- Criterion: $Ha = Hb$ if and only if $ab^{-1} \in H$. The proof is the proof for left cosets with the sides exchanged.
- The right cosets form a [[partition|08QMKTWF9T]] of $G$, and [[each right coset has $|H|$ elements|0DKMBWTD7P]].
- Inversion: $(gH)^{-1} = \{(gh)^{-1} : h \in H\} = \{h^{-1}g^{-1} : h \in H\} = Hg^{-1}$, because $h \mapsto h^{-1}$ is a bijection of $H$.
- Thus $C \mapsto C^{-1}$ is a bijection from the set $G/H$ of left cosets to the set $H \backslash G$ of right cosets. Its inverse is again $C \mapsto C^{-1}$.
- Consequence: the number of left cosets equals the number of right cosets. This number is the [[index|0DTXBQPA2S]] $[G : H]$, also when it is infinite.
- The equality $gH = Hg$ holds for all $g \in G$ if and only if $H$ is normal, by [[this result|01E7SWYJX3]].

### History

Right cosets and left cosets are two versions of the same idea, which is present in the work of Galois around 1830.
The choice of the standard side differs between authors and between periods.

### Common errors

- The map $gH \mapsto Hg$ is not well defined in general. In $S_3$, $(1\,3)H = (1\,2\,3)H$, but $H(1\,3) = \{(1\,3), (1\,3\,2)\}$ and $H(1\,2\,3) = \{(1\,2\,3), (2\,3)\}$ differ. The correct bijection is $gH \mapsto Hg^{-1}$.
- The criterion for right cosets is $ab^{-1} \in H$, not $a^{-1}b \in H$.

## Explanations

### L1 human

A left coset multiplies each element of the subgroup by a fixed element on the left.
A right coset multiplies on the right.
When the order of multiplication does not matter, as for numbers, the two give the same sets.
For the symmetries of a triangle, the order matters, and the two can give different sets.
Still, the left cosets and the right cosets always come in the same number.

### L2 human

We compare the left and the right cosets of $H = \{e, (1\,2)\}$ in $S_3$, with permutations composed from right to left.

1. The products with $(1\,3)$ are $(1\,3)(1\,2) = (1\,2\,3)$ and $(1\,2)(1\,3) = (1\,3\,2)$.
2. Thus the left coset is $(1\,3)H = \{(1\,3), (1\,2\,3)\}$, and the right coset is $H(1\,3) = \{(1\,3), (1\,3\,2)\}$.
3. The products with $(2\,3)$ are $(2\,3)(1\,2) = (1\,3\,2)$ and $(1\,2)(2\,3) = (1\,2\,3)$.
4. Thus $(2\,3)H = \{(2\,3), (1\,3\,2)\}$ and $H(2\,3) = \{(2\,3), (1\,2\,3)\}$.
5. The left cosets are $H$, $(1\,3)H$, $(2\,3)H$. The right cosets are $H$, $H(1\,3)$, $H(2\,3)$.
6. Only $H$ is in both lists. Thus $H$ is not normal in $S_3$.
7. Inversion maps $(1\,3)H$ to $\{(1\,3), (1\,3\,2)\} = H(1\,3)^{-1}$, because $(1\,2\,3)^{-1} = (1\,3\,2)$.

The typical use is a test for normality: compare $gH$ and $Hg$ for the generators $g$ of $G$.

A trap is to think that $H$ is not normal as soon as $gh \neq hg$ for some $g$ and $h$.
For $A_3$ in $S_3$, the products $(1\,2)(1\,2\,3)$ and $(1\,2\,3)(1\,2)$ differ, but $(1\,2)A_3 = A_3(1\,2)$.

### L3 human

The right cosets of $H$ are the orbits of the left action of $H$ on $G$, $g \mapsto hg$.
Inversion is an anti-automorphism of $G$, so it exchanges each statement about left cosets with the same statement about right cosets.
In the same way, the [[opposite group|D33V8HE0KY]] turns left cosets into right cosets.
Both kinds of cosets are special cases of the [[double cosets|DSBE321XMS]] $HgK$, with $K = \{e\}$ or $H = \{e\}$.
