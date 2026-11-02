---
tag: DWMQ3V205V
kind: definition
name: Universal covering group
msc: ["22E15", 57M10]
defines: SWW2993CVJ
uses: [7JBRGCVJRB, 3XZRRE165N, Y1YPE6PM52, S1XK3HXHFX, 0V032VWTHD]
sources:
  - url: https://en.wikipedia.org/wiki/Covering_group
---

## Definition

Let $G$ be a [[connected|0V032VWTHD]] [[Lie group|7JBRGCVJRB]].
A *universal covering group* of $G$ is a Lie group $\tilde G$ together with a map $p \colon \tilde G \to G$ such that:

1. $\tilde G$ is connected and simply connected, that is, its [[fundamental group|S1XK3HXHFX]] is trivial;
2. $p$ is a homomorphism of Lie groups;
3. $p$ is a [[covering map|3XZRRE165N]].

## Remarks

Existence: let $p \colon \tilde G \to G$ be the [[universal cover|Y1YPE6PM52]] of the manifold $G$, and choose $\tilde e$ over the identity $e$.
There is a unique Lie group structure on $\tilde G$ with identity $\tilde e$ for which $p$ is a homomorphism.
The universal covering group is unique up to isomorphism over $G$.
The kernel of $p$ is a discrete central subgroup of $\tilde G$, isomorphic to $\pi_1(G)$.

Example: $p \colon \R \to S^1$, $p(t) = e^{2\pi i t}$, is a homomorphism from $(\R, +)$, a covering map, and $\R$ is simply connected; the kernel is $\Z = \pi_1(S^1)$.

Example: identify $SU(2)$ with the unit quaternions and $\R^3$ with the purely imaginary quaternions.
The map sending $q$ to the rotation $v \mapsto q v q^{-1}$ is a universal covering group $SU(2) \to SO(3)$ with kernel $\set{\pm 1}$.

Non-example: the identity map $SO(3) \to SO(3)$ is a homomorphism and a covering map, but $SO(3)$ is not simply connected, since $\pi_1(SO(3)) \cong \Z/2$.
