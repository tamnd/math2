---
tag: FBGXAXAEJ1
kind: definition
name: Complete category
msc: [18A35]
defines: FWGPKXCPB7
uses: [A2DE66937D, HJK75HDWFE, CHS5AFJGWE]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_category
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
$\mathcal{C}$ is *complete* if every [[diagram|HJK75HDWFE]] $F \colon J \to \mathcal{C}$ with $J$ a small category has a [[limit|CHS5AFJGWE]] in $\mathcal{C}$.
Here a category $J$ is small when its objects and its morphisms form sets.

## Remarks

Dually, $\mathcal{C}$ is *cocomplete* if every small diagram has a colimit.
A category is complete if and only if it has all small products and all equalizers.

Example: the category of sets is complete.
The limit of $F \colon J \to \mathbf{Set}$ is the set of families $(x_j)_{j \in J}$ with $x_j \in F(j)$ and $F(u)(x_j) = x_k$ for every morphism $u \colon j \to k$ of $J$.

Non-example: the category of finite sets is not complete.
Suppose $P$ were a product of countably many copies of $\set{0, 1}$ there.
Maps from a one-point set to $P$ would match the elements of $P$ with all sequences in $\set{0, 1}$, which form an uncountable set.

A small category that is complete is a preorder, by a theorem of Freyd.
So completeness is a property of large categories.
