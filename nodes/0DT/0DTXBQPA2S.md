---
tag: 0DTXBQPA2S
kind: concept
name: Index of a subgroup
msc: ["20A05"]
topics: [1VHQWXC64D]
audience: ug1
uses: [G5S1M9, 0X1JXT47GA, 03DEH43F4H, 0NE1DK7H4T, 0G0ASKNA6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: Properties
  - book: isbn:9780471433347
    locator: Section 3.2
same_as:
  wikidata: Q1464168
  wikipedia: Index of a subgroup
---

## Summary

Let $G$ be a [[group|G5S1M9]] and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
The index of $H$ in $G$, written $[G : H]$, is the [[cardinality|0G0ASKNA6Z]] of the set $G/H$ of [[left cosets|03DEH43F4H]] of $H$ in $G$.
It is equal to the number of [[right cosets|0NE1DK7H4T]] of $H$.
The subgroup $H$ has finite index when $[G : H]$ is a natural number, and infinite index otherwise.
For a finite group, $[G : H] = |G| / |H|$.
The index measures how large $H$ is inside $G$, also when $G$ and $H$ are both infinite.

## Motivation

The order $|H|$ says nothing useful when $H$ is infinite.
For example, $2\mathbb{Z}$ and $\mathbb{Z}$ have the same cardinality, but $2\mathbb{Z}$ is "half" of $\mathbb{Z}$.
The index captures this: $[\mathbb{Z} : 2\mathbb{Z}] = 2$, because there are two cosets, the even and the odd integers.
For finite groups, the index is the factor $|G| / |H|$ in [[Lagrange's theorem|3C53TD]].

## Notation

The index is written $[G : H]$ or $|G : H|$.
Both forms are common, and this site uses $[G : H]$.
Some books write $(G : H)$.
The [[definition|04QEBF8S49]] uses left cosets, and the choice does not change the value.

## Remarks

### Examples

- For each positive integer $n$, $[\mathbb{Z} : n\mathbb{Z}] = n$, as [[this example|JBQNPAZKWA]] shows. The cosets are the residue classes modulo $n$.
- In $S_3$, the subgroup $\{e, (1\,2)\}$ has index $3$, and $A_3$ has index $2$, as [[this example|4DWC4XFS34]] shows.
- The subgroup $\mathbb{Z}$ has infinite index in $(\mathbb{Q}, +)$, as [[this example|BF4EBR7D8C]] shows.
- Each group has $[G : G] = 1$ and $[G : \{e\}] = |G|$.
- In the group $\mathbb{R}^\times$ of nonzero real numbers, the positive numbers have index $2$. The cosets are the positive and the negative numbers.

### Non-examples

- A subset that is not a subgroup has no index. In $\mathbb{Z}/4\mathbb{Z}$, the subset $S = \{0, 1\}$ has four different translates, but $|G| / |S| = 2$, as [[this example|94SNG0EQQZ]] shows.
- The index is not the order of a quotient group in general. The set $G/H$ is a group only when $H$ is [[normal|0CB0DX5BVV]], but the index is defined for each subgroup.

### Basic properties

- The number of left cosets equals the number of right cosets. The map $gH \mapsto Hg^{-1}$ is a bijection, because $(gH)^{-1} = Hg^{-1}$, as shown in [[right coset|0NE1DK7H4T]].
- If $G$ is finite, then $|G| = [G : H] \cdot |H|$, by [[this theorem|04DC0SRN2K]].
- [[Tower law|0ZQJ7KEFQ5]]: if $K \le H \le G$, then $[G : K] = [G : H] \cdot [H : K]$.
- If $H$ and $K$ have finite index, then $H \cap K$ has finite index, and $[G : H \cap K] \le [G : H] \cdot [G : K]$. This is the first part of [[Poincaré's theorem|W0SW2ATN1Y]].
- A subgroup of index $2$ is [[normal|0V547YQRMV]].
- $[G : H] = 1$ if and only if $H = G$.

### History

Lagrange studied the values of a polynomial under the $n!$ permutations of its variables.
In modern terms, the number of these values is the index of the stabiliser of the polynomial in $S_n$.

### Common errors

- For an infinite group, $[G : H] = |G| / |H|$ has no meaning. The index of $2\mathbb{Z}$ in $\mathbb{Z}$ is $2$, but $|\mathbb{Z}| = |2\mathbb{Z}|$.
- A subgroup of finite index need not be finite, and a finite subgroup need not have finite index. The subgroup $2\mathbb{Z}$ is infinite with index $2$. The subgroup $\{e\}$ of $\mathbb{Z}$ is finite with infinite index.
- The index $[G : H]$ is not the number of elements outside $H$. In $S_3$ the subgroup $\{e, (1\,2)\}$ has index $3$, and $4$ elements lie outside it.

## Explanations

### L1 human

The index of a subgroup tells how many copies of the subgroup you need to cover the whole group.
The copies are the cosets, and they do not overlap.
For the even numbers inside the whole numbers, you need two copies: the even and the odd numbers.
So the index of the even numbers is $2$.
For the multiples of $5$, you need five copies, one for each remainder $0, 1, 2, 3, 4$.

### L2 human

We compute the index of $H = \langle (1\,2\,3\,4) \rangle$ in the [[symmetric group|0515A6D2Y1]] $S_4$.

1. The element $(1\,2\,3\,4)$ has order $4$, so $|H| = 4$.
2. The [[order of $S_4$|0PCKBBMEXC]] is $4! = 24$.
3. By the [[counting formula|04DC0SRN2K]], $[S_4 : H] = 24 / 4 = 6$.
4. Thus $S_4$ splits into $6$ left cosets of $H$, each with $4$ elements.

The typical use of the index is in the [[tower law|0ZQJ7KEFQ5]] and in arguments with group actions.
The group $G$ acts on the $[G : H]$ cosets of $H$, and this gives a homomorphism to the symmetric group $S_{[G : H]}$.

A trap is to compute the index of an infinite subgroup as a ratio of orders.
For $n\mathbb{Z}$ in $\mathbb{Z}$, both sets are countably infinite, and the index $n$ comes only from counting the cosets.

### L3 human

The index is the size of the homogeneous space $G/H$, and $[G : H]$ is finite exactly when $G/H$ is a finite $G$-set.
The subgroups of finite index define the profinite topology on $G$.
A group is residually finite when the intersection of all its subgroups of finite index is $\{e\}$.
A finitely generated group has only finitely many subgroups of index $n$.
The reason is that each one is the stabiliser of a point for an action on $n$ points, and the images of the generators in $S_n$ fix this action.
The counting of subgroups of index $n$ is the subject of subgroup growth.
In topology, a subgroup of index $n$ of the fundamental group gives a covering space of degree $n$.
In Galois theory, the degree $[E : F]$ of an intermediate field of a finite Galois extension $L/F$ is the index of the subgroup that fixes $E$.
