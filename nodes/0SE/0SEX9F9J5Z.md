---
tag: 0SEX9F9J5Z
kind: definition
name: Order of a group
msc: [20A05]
topics: [BAZT8JJ70S]
audience: ug1
defines: 0B85S2V2DR
uses: [G5S1M9, 0G0ASKNA6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Order_(group_theory)
    locator: lead section
  - book: isbn:9781305657960
    locator: Chapter 3
---

## Definition

Let $G$ be a [[group|G5S1M9]].
The order of $G$, written $|G|$, is the [[cardinality|0G0ASKNA6Z]] of the set of elements of $G$.
The group $G$ is a finite group when this set is [[finite|070R982G4B]], and then $|G|$ is the number of elements of $G$.
The group $G$ is an infinite group, or a group of infinite order, when this set is infinite.

## Notation

Some books write $\#G$, $o(G)$ or $\operatorname{card}(G)$ for $|G|$.
The same word "order" is also used for the [[order of an element|0WE2NHZJ7B]] $g$, written $\ord(g)$.
The order of $g$ equals the order of the subgroup $\langle g \rangle$ that $g$ generates.

## Remarks

The [[trivial group|0BNPC9850Y]] has order $1$, and the [[group of $n$th roots of unity|0WX11EA3F3]] has order $n$.
The group $(\mathbb{Z}, +)$ of [[integers|0C4JS9RF5M]] has infinite order.
The order depends only on the set, not on the operation, but the definition applies only when the operation makes the set a group.
[[Lagrange's theorem|3C53TD]] says that the order of a subgroup of a finite group divides the order of the group.
The concept page [[order of a group|0B85S2V2DR]] gives the examples, the non-examples and the first properties.

## Explanations

### L1 human

The order of a group tells how big the group is.
For a finite group, it is the number of elements.
For example, the rotations of a square that map the square onto itself form a group of order $4$.
The word "order" has a second meaning in group theory: the order of a single element.

### L2 human

To find the order of a finite group, we list its elements without repeats and count them.
For example, take the group $\{1, -1, i, -i\}$ of complex numbers under multiplication.

1. The four numbers $1$, $-1$, $i$ and $-i$ are different.
2. Each product of two of them is again one of them, for example $i \cdot (-i) = -i^2 = 1$.
3. Thus the group has exactly $4$ elements, and its order is $4$.

A trap is to count one element two times under two names.
In $\mathbb{Z}/5\mathbb{Z}$, the classes of $2$ and $7$ are the same element, so the group still has order $5$.
