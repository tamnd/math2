---
tag: BS1RD4F5MD
kind: definition
name: Duality in order theory
msc: [06A06]
defines: MRYFDAG5G8
uses: [011C29Q1S1]
sources:
  - url: https://en.wikipedia.org/wiki/Duality_(order_theory)
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]].
The *dual* of $P$ is the poset $P^{\mathrm{op}} = (P, \ge)$ on the same set, where $x \ge y$ means $y \le x$.
The *dual* of a statement about partial orders is the statement obtained by replacing $\le$ with $\ge$ throughout.
Then each defined notion is replaced by its dual notion, such as [[upper bound|0H5J02P8S9]] by lower bound and [[greatest element|0Z7HDDXX3X]] by [[least element|0T2NTJCV83]].

## Remarks

The relation $\ge$ is again a partial order, since reflexivity, antisymmetry and transitivity are symmetric in the two sides.
For example, the dual of $(\N, \le)$ is $\N$ with the reverse order, in which $0$ is the greatest element and there is no least element.
The dual of the dual of $P$ is $P$ itself.
Duality principle: if a statement holds in every poset, then its dual statement holds in every poset.
The reason is that the dual statement for $P$ is the original statement for $P^{\mathrm{op}}$.
The dual of $P$ is also written $P^{\partial}$ or $P^{*}$.

## Explanations

### L1 human

The dual order reads the same order backwards.
A theorem about orders, read backwards, is again a theorem.
