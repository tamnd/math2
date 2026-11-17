---
tag: 564VVAQTNR
kind: concept
name: Coset
aliases: [co-set, coset-in-a-group, coset-representative, cosets]
msc: ["20A05"]
topics: [1VHQWXC64D]
audience: ug1
uses: [G5S1M9, 0X1JXT47GA, 0G8VEZ3WTK, 0W95W33CMP]
sources:
  - wikipedia: en:98759@r1351557349
    locator: Coset
    note: adopted
    mention: wikipedia://en/98759
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Coset
    locator: History
  - book: isbn:9780471433347
    locator: Section 3.2
  - book: isbn:9781305657960
    locator: Chapter 7
same_as:
  wikidata: Q751969
  wikipedia: Coset
inventory: [S8KHNG9EDR]
---

## Summary

Let $G$ be a [[group|G5S1M9]] and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
For $g \in G$, the [[left coset|03DEH43F4H]] of $H$ that contains $g$ is the set $gH = \{gh : h \in H\}$.
The [[right coset|0NE1DK7H4T]] of $H$ that contains $g$ is the set $Hg = \{hg : h \in H\}$.
A coset of $H$ is a left coset or a right coset of $H$.
The left cosets are the [[equivalence classes|0W95W33CMP]] of the [[equivalence relation|0G8VEZ3WTK]] $a \sim b$ if and only if $a^{-1}b \in H$.
Cosets cut a group into pieces of equal size, and this fact is the base of [[Lagrange's theorem|3C53TD]] and of [[quotient groups|0KYX2N69J0]].

## Motivation

In the integers, the remainder after division by $3$ sorts each integer into one of three classes.
The class of $0$ is the subgroup $3\mathbb{Z}$ of the multiples of $3$.
The other two classes are $1 + 3\mathbb{Z}$ and $2 + 3\mathbb{Z}$.
Each class is a shifted copy of $3\mathbb{Z}$.
Cosets make this sorting work for each subgroup of each group.
The question "do $a$ and $b$ have the same remainder?" becomes the question "is $a^{-1}b$ in $H$?".

In the plane $\mathbb{R}^2$, a line $L$ through the origin is a subgroup under vector addition.
The cosets of $L$ are the lines parallel to $L$.
Thus a coset is a translate of the subgroup, and the cosets fill the plane without overlap.

## Notation

In this site a coset without an adjective is a left coset, as in most English textbooks.
Some older books, for example the books of Marshall Hall and of Derek Robinson, use right cosets as the standard.
The set of left cosets of $H$ in $G$ is written $G/H$.
The set of right cosets is written $H \backslash G$.
When the operation of $G$ is addition, the left coset of $g$ is written $g + H$.
An element $g$ of a coset $C$ is a representative of $C$, because $C = gH$ for each $g \in C$.

## Remarks

### Examples

- In $(\mathbb{Z}, +)$, the cosets of $3\mathbb{Z}$ are $3\mathbb{Z}$, $1 + 3\mathbb{Z}$ and $2 + 3\mathbb{Z}$, as [[this example|BM4VXG92DT]] shows. The remainder of $n$ after division by $3$ tells which coset contains $n$.
- In $(\mathbb{R}^2, +)$, the cosets of a line through the origin are the lines parallel to it, as [[this example|~8fba9792]] shows.
- In the [[symmetric group|0515A6D2Y1]] $S_3$, the subgroup $H = \{e, (1\,2)\}$ has the three left cosets $H$, $\{(1\,3), (1\,2\,3)\}$ and $\{(2\,3), (1\,3\,2)\}$, as [[this example|6VFF2TTXYZ]] shows.
- In each group $G$, the subgroup $\{e\}$ has the cosets $\{g\}$, one for each $g \in G$. The subgroup $G$ has the single coset $G$.
- In the [[circle group|04EAFVFTF7]] $\{z \in \mathbb{C} : |z| = 1\}$, the subgroup $\{1, -1\}$ has the cosets $\{z, -z\}$. Each coset is a pair of opposite points of the circle.

### Non-examples

- In $\mathbb{Z}/4\mathbb{Z}$, the set $\{1, 2\}$ is a translate of the subset $S = \{0, 1\}$, but it is not a coset of any subgroup. The only subgroup of order $2$ is $\{0, 2\}$, and its cosets are $\{0, 2\}$ and $\{1, 3\}$. [[This example|~0ae0cc90]] shows that the translates of $S$ overlap.
- In $\mathbb{Z}$, the set $3\mathbb{Z} \cup (1 + 3\mathbb{Z})$ is not a coset of any subgroup. A coset that contains $0$ is a subgroup $m\mathbb{Z}$. This set also contains $1$, so $m = 1$ and the coset is $\mathbb{Z}$. But $2$ is not in the set.
- In $S_3$, the set $\{e, (1\,2\,3)\}$ is not a coset of any subgroup. A coset $gK$ that contains $e$ is equal to $eK = K$, so the set would be a subgroup. But $(1\,2\,3)^2 = (1\,3\,2)$ is not in the set.

### Basic properties

- Each $g \in G$ is in its own left coset $gH$, because $g = ge$ and $e \in H$.
- Two left cosets $aH$ and $bH$ are equal if and only if $a^{-1}b \in H$. Otherwise they are disjoint. Thus the left cosets form a [[partition|08QMKTWF9T]] of $G$.
- [[Each coset has the same cardinality as $H$|0DKMBWTD7P]], because $h \mapsto gh$ is a bijection from $H$ to $gH$.
- The number of left cosets equals the number of right cosets. This common number is the [[index|0DTXBQPA2S]] $[G : H]$.
- The coset $eH = H$ is the only left coset that is a subgroup, because each other left coset does not contain $e$.
- In an [[abelian group|082GHNPJ53]], $gH = Hg$ for each $g$. In general $gH = Hg$ for each $g$ exactly when $H$ is a [[normal subgroup|0CB0DX5BVV]], by [[this result|01E7SWYJX3]].

### History

The idea of a coset is present in the work of Évariste Galois around 1830, but he gave it no name.
The English word "co-set" first appears in a paper of George Abram Miller from 1910.
Heinrich Weber used the German word "Nebengruppe".

### Common errors

- A coset $gH$ with $g \notin H$ is not a subgroup, because it does not contain the identity.
- The union $H \cup gH$ of two cosets is in general not a subgroup and not a coset. The set $3\mathbb{Z} \cup (1 + 3\mathbb{Z})$ is an example.
- The equality $gH = Hg$ does not mean $gh = hg$ for each $h \in H$. It means only that each $gh$ is equal to some $h'g$ with $h' \in H$.

## Explanations

### L1 human

Take the whole numbers and sort them by their remainder after division by $3$.
You get three groups of numbers: remainder $0$, remainder $1$ and remainder $2$.
The numbers with remainder $0$ are the multiples of $3$, and they form a subgroup.
The other two classes are the same subgroup moved by $1$ and moved by $2$.
These three classes are the cosets of the multiples of $3$.
Each number is in exactly one class, and each class looks the same as the others.

### L2 human

We find the left cosets of $H = \{0, 4, 8\}$ in $G = \mathbb{Z}/12\mathbb{Z}$, with addition modulo $12$.

1. The set $H$ is a subgroup, because $4 + 4 = 8$, $4 + 8 = 0$, $8 + 8 = 4$, and $-4 = 8$.
2. The coset of $0$ is $0 + H = \{0, 4, 8\}$.
3. The coset of $1$ is $1 + H = \{1, 5, 9\}$.
4. The coset of $2$ is $2 + H = \{2, 6, 10\}$.
5. The coset of $3$ is $3 + H = \{3, 7, 11\}$.
6. The coset of $4$ is $4 + H = \{4, 8, 0\} = H$, because $4 \in H$.
7. The four cosets in steps 2 to 5 are disjoint, and their union is $G$.

The typical use of cosets is to count.
Here $12 = 4 \cdot 3$: four cosets, each with three elements.
This is [[Lagrange's theorem|3C53TD]] in a small case.

A trap is to forget the order of the factors in a group that is not abelian.
In $S_3$ with $H = \{e, (1\,2)\}$, the left coset $(1\,3)H$ is $\{(1\,3), (1\,2\,3)\}$.
The right coset $H(1\,3)$ is $\{(1\,3), (1\,3\,2)\}$, which is a different set.
Thus "the coset of $(1\,3)$" has no meaning until the side is fixed.

### L3 human

The left cosets of $H$ are the orbits of the action of $H$ on $G$ by right multiplication, $g \mapsto gh$.
The set $G/H$ carries the [[action of $G$ by left multiplication|0AZG100DKH]], and this action is transitive with stabiliser $H$ at the point $H$.
Each transitive action of $G$ on a set is isomorphic to an action of this form, so cosets describe all transitive $G$-sets.
In geometry, $G/H$ is a homogeneous space, for example the sphere $SO(3)/SO(2)$.

When $H$ is a [[normal subgroup|0CB0DX5BVV]], the product $(aH)(bH) = abH$ is well defined, and $G/H$ is the [[quotient group|0KYX2N69J0]].
The same construction gives the residue classes of a ring modulo an ideal and the quotient of a vector space by a subspace.
Two-sided versions of cosets, the [[double cosets|~d8f44326]] $HgK$, are the orbits of $H \times K$ on $G$.
