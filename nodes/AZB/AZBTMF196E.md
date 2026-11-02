---
tag: AZBTMF196E
kind: example
name: Lens space
msc: [57K30, 57M10]
instance_of: [R20TB2KEQQ]
sources:
  - url: https://en.wikipedia.org/wiki/Lens_space
same_as:
  wikidata: Q2470499
  wikipedia: Lens space
---

## Example

Let $p \ge 2$ and $q$ be coprime integers, and let $\zeta = e^{2\pi i/p}$.
View the $3$-sphere as $S^3 = \set{(z_1, z_2) \in \C^2 : \abs{z_1}^2 + \abs{z_2}^2 = 1}$.
The map $g(z_1, z_2) = (\zeta z_1, \zeta^q z_2)$ generates an action of the cyclic group $\Z/p$ on $S^3$.
The lens space $L(p, q)$ is the quotient $S^3 / (\Z/p)$.

The action is free.
Indeed, suppose $g^k$ fixes $(z_1, z_2)$ with $0 < k < p$.
Then $\zeta^k \ne 1$ forces $z_1 = 0$, and $\zeta^{kq} \ne 1$ (because $q$ is prime to $p$) forces $z_2 = 0$, which is impossible on $S^3$.
So the quotient map is a [[covering map|3XZRRE165N]] and $L(p, q)$ is a closed orientable [[3-manifold|R20TB2KEQQ]].
Its [[fundamental group|S1XK3HXHFX]] is $\Z/p$, since $S^3$ is simply connected.

## Remarks

The integral homology of $L(p, q)$ is $H_0 = \Z$, $H_1 = \Z/p$, $H_2 = 0$ and $H_3 = \Z$.
For $p = 2$ one gets $L(2, 1)$, the [[real projective space|1DDYB6VVSR]] $\mathbb{RP}^3$.
A lens space is also the union of two solid tori glued along their boundary tori, so it has a [[Heegaard splitting|EDE9919B5R]] of genus $1$.
The spaces $L(p, q)$ and $L(p, q')$ are homeomorphic if and only if $q' \equiv \pm q^{\pm 1} \pmod p$.
They are homotopy equivalent if and only if $q q' \equiv \pm n^2 \pmod p$ for some integer $n$.
So $L(7, 1)$ and $L(7, 2)$ are homotopy equivalent, because $2 \equiv 3^2 \pmod 7$, but they are not homeomorphic, because $2 \not\equiv \pm 1 \pmod 7$.

## Explanations

### L1 human

A lens space is what one gets by folding the $3$-sphere onto itself by a rotation of order $p$ that moves every point.
Two lens spaces can have the same fundamental group and the same homology, and even be homotopy equivalent, while still being different manifolds.
This makes them the first test case for any new invariant of $3$-manifolds.
