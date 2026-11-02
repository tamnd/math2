---
tag: QTTW954WCK
kind: definition
name: Lattice of equational theories
msc: [08B15, 08B05, 03C05]
defines: 2R8QQTP1CE
uses: [F1M51B4MDG, PKD440G2XW, D7A0ZGZT5S, QKGW3Z9BHW, 3YYKGWJJND]
sources:
  - url: https://en.wikipedia.org/wiki/Equational_logic
---

## Definition

Let $\sigma$ be a signature and let $X$ be a countably infinite set of variables.
An [[equational theory|F1M51B4MDG]] of signature $\sigma$ is a set $T$ of [[identities|PKD440G2XW]] over $X$ that contains every identity true in all models of $T$.
The *lattice of equational theories* of $\sigma$ is the set of all equational theories of signature $\sigma$, ordered by inclusion.
For an equational theory $T_0$, the lattice of equational theories *extending* $T_0$ is its subset of theories that contain $T_0$.

## Remarks

The meet of a family of theories is their intersection.
The join is the smallest theory containing their union, that is, the set of consequences of the union.
So the lattice is a [[complete lattice|D7A0ZGZT5S]], whose top is the theory containing every identity, including $x \approx y$.
Identify a theory $T$ with the set of pairs $(s, t)$ such that $s \approx t \in T$.
This makes $T$ a [[fully invariant congruence|QKGW3Z9BHW]] of the [[term algebra|3YYKGWJJND]] over $X$, and every fully invariant congruence arises this way.
Example: the identities true in all groups form a theory, and so do those true in all abelian groups; the first is contained in the second.
Non-example: the set $\set{xy \approx yx}$ alone is not a theory, because it does not contain its consequences $zw \approx wz$ and $x \approx x$.
The map $T \mapsto \operatorname{Mod}(T)$ is a dual isomorphism onto the lattice of varieties of signature $\sigma$.
