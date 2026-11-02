---
tag: VBS4A8G5XA
kind: definition
name: Universal property
msc: [18A05, 18A40]
defines: EN4DD2FAJH
uses: [A2DE66937D, 28NQ0KRHD3, EK85VSSRMR, 0KTW26C80J, 0JYTG5K9Y4]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_property
---

## Definition

Let $F \colon \mathcal{C} \to \mathcal{D}$ be a [[functor|28NQ0KRHD3]] between [[categories|A2DE66937D]] and let $X$ be an object of $\mathcal{D}$.
A *universal morphism from $X$ to $F$* is a pair $(A, u)$, with $A$ in $\mathcal{C}$ and $u \colon X \to F(A)$ in $\mathcal{D}$, with this property.
For every object $A'$ of $\mathcal{C}$ and every morphism $f \colon X \to F(A')$, there is exactly one $g \colon A \to A'$ with $F(g) \circ u = f$.
Dually, a *universal morphism from $F$ to $X$* is a pair $(A, v)$ with $v \colon F(A) \to X$, with the following property.
For every $A'$ and every $f \colon F(A') \to X$, there is exactly one $g \colon A' \to A$ with $v \circ F(g) = f$.
An object or morphism is said to have a *universal property* when it is part of such a pair.

## Remarks

Equivalently, $(A, u)$ is an initial object of the comma category $(X \downarrow F)$, whose objects are pairs $(A', f \colon X \to F(A'))$; in the dual case it is a terminal object of $(F \downarrow X)$.
Since [[initial objects|EK85VSSRMR]] are unique up to unique isomorphism, so are universal morphisms.

Example: let $U \colon \mathbf{Grp} \to \mathbf{Set}$ send a group to its underlying set, and let $S$ be a set.
The [[free group|0KTW26C80J]] $F(S)$ with the inclusion $u \colon S \to U(F(S))$ of generators is a universal morphism from $S$ to $U$.
Indeed, every function $f \colon S \to U(H)$ to a group $H$ extends to exactly one [[group homomorphism|0JYTG5K9Y4]] $g \colon F(S) \to H$ with $g \circ u = f$.

Non-example: take $S = \{s\}$ and the pair $(\Z \times \Z, \ s \mapsto (1, 0))$.
The function $s \mapsto 1 \in \Z$ extends to the homomorphisms $(m, n) \mapsto m$ and $(m, n) \mapsto m + n$, so uniqueness fails and this pair is not universal.
