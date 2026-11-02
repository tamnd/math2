---
tag: C0GMFP0RF9
kind: definition
name: Zero object
msc: [18A30, 18A20]
defines: AQET9YHH6F
uses: [A2DE66937D, 859F0TFVA3, EK85VSSRMR, 0BNPC9850Y]
sources:
  - url: https://en.wikipedia.org/wiki/Zero_object_(algebra)
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
An object $0$ of $\mathcal{C}$ is a *zero object* if it is both an [[initial object and a terminal object|EK85VSSRMR]].
So for every object $X$ there is exactly one [[morphism|859F0TFVA3]] $0 \to X$ and exactly one morphism $X \to 0$.

## Remarks

A zero object is unique up to unique isomorphism, because an initial object is.
A category with a zero object is called pointed.

Example: in the category of groups, the [[trivial group|0BNPC9850Y]] $\{e\}$ is a zero object.
The only homomorphism $\{e\} \to G$ sends $e$ to the identity of $G$, and the only map $G \to \{e\}$ is the constant map, which is a homomorphism.
The same check shows that the zero module is a zero object in the category of modules over a ring.
It also shows that a one-point set is a zero object in the category of pointed sets.

Non-example: in the category of sets, a one-point set $\{*\}$ is terminal but not initial, since there are two functions $\{*\} \to \{0, 1\}$.
The empty set is initial but not terminal, since there is no function from a non-empty set to it.
So the category of sets has no zero object.
