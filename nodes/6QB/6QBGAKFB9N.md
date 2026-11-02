---
tag: 6QBGAKFB9N
kind: statement
role: corollary
name: Finite Desarguesian planes are Pappian
msc: ["51A30", "51E15", "12E15"]
uses: [0RRNVX1VKA, HPX85PA8NX, B6C3J2GJWP, 5Z19Y02MME, 0EA5BTA0CX, 0ZXZ82FTX2, DANFNN8C4Y, MAM2MDG0XG]
about: [HPX85PA8NX, B6C3J2GJWP]
sources:
  - url: https://en.wikipedia.org/wiki/Wedderburn%27s_little_theorem
---

## Statement

Let $\Pi$ be a finite [[projective plane|DANFNN8C4Y]] in which [[Desargues's theorem|5Z19Y02MME]] holds.
Then [[Pappus's hexagon theorem|B6C3J2GJWP]] holds in $\Pi$.
Moreover $\Pi$ is isomorphic to $PG(2, q)$, the projective plane over the [[finite field|0ZXZ82FTX2]] with $q$ elements, for a prime power $q$.

## Remarks

A [[Desarguesian plane|HPX85PA8NX]] is coordinatized by a [[division ring|0EA5BTA0CX]] $D$, in the sense that $\Pi \cong PG(2, D)$; see the [[coordinatization of projective planes|MAM2MDG0XG]].
If $\Pi$ is finite, $D$ is finite, so $D$ is a field by [[Wedderburn's little theorem|0RRNVX1VKA]].
A finite field has prime power order $q$, and in a plane over a field Pappus's theorem holds.

Finiteness is necessary.
The projective plane over the quaternions is Desarguesian, but Pappus's theorem fails in it, because the quaternions are not commutative.

In the other direction, Hessenberg's theorem says that Pappus's theorem implies Desargues's theorem in every projective plane.
So for finite planes the two configuration theorems are equivalent.

## Explanations

### L1 human

Desargues's theorem and Pappus's theorem are two classical facts about points and lines that may or may not hold in an abstract projective plane.
In general Pappus is stronger.
For finite planes they turn out to be the same, because of an algebraic fact: a finite skew field is commutative.

### L2 human

Desargues's theorem lets one build coordinates from a division ring, and Pappus's theorem holds exactly when that division ring is commutative.
Wedderburn's little theorem is therefore the algebraic input that makes every finite Desarguesian plane classical.
It also shows that the order of a finite Desarguesian plane is a prime power.
A finite plane that is not of the form $PG(2, q)$, such as the Hall plane of order $9$, must therefore fail Desargues's theorem.
