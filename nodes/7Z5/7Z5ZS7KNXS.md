---
tag: 7Z5ZS7KNXS
kind: object
name: Out(F_n)
msc: [20F28, "20E05", 20F65]
instance_of: [0Q8Y862DTZ]
uses: [0KTW26C80J, 0Q8Y862DTZ, 0K1SCPBNKJ, 0FCHE902D7]
sources:
  - url: https://en.wikipedia.org/wiki/Out(Fn)
same_as:
  wikidata: Q7111377
  wikipedia: Out(Fn)
---

## Description

Let $n \ge 1$ and let $F_n$ be the [[free group|0KTW26C80J]] of rank $n$.
The group $\mathrm{Out}(F_n) = \Aut(F_n) / \mathrm{Inn}(F_n)$ is the [[outer automorphism group|0Q8Y862DTZ]] of $F_n$.
It is the quotient of the [[automorphism group|0K1SCPBNKJ]] of $F_n$ by its normal subgroup of inner automorphisms $x \mapsto g x g^{-1}$.

## Remarks

For $n = 1$, $F_1 = \Z$ has the two automorphisms $x \mapsto \pm x$ and no nontrivial inner automorphisms, so $\mathrm{Out}(F_1) \cong \Z/2\Z$.
Every automorphism of $F_n$ induces an automorphism of the abelianisation $\Z^n$, and inner automorphisms induce the identity.
This gives a homomorphism $\mathrm{Out}(F_n) \to \mathrm{GL}_n(\Z)$, into the [[general linear group|0FCHE902D7]] over $\Z$, which is surjective, because elementary matrices and sign changes lift to automorphisms of $F_n$.
For $n = 2$ this map is an isomorphism, so $\mathrm{Out}(F_2) \cong \mathrm{GL}_2(\Z)$.
For $n \ge 3$ its kernel is infinite.

$\mathrm{Out}(F_n)$ is finitely presented.
Culler and Vogtmann built a contractible space, Outer space, on which $\mathrm{Out}(F_n)$ acts properly; it plays the role that Teichmüller space plays for the [[mapping class group|JV5NYG913V]] of a surface.
$\mathrm{Out}(F_n)$ satisfies the [[Tits alternative|QYXGVES1XM]].

## Explanations

### L1 human

The free group on $n$ letters has many symmetries: for example, one may swap two letters, invert a letter, or replace $a$ by $ab$.
Some symmetries are boring, namely conjugation by a fixed element; dividing them out gives $\mathrm{Out}(F_n)$.
It is the free-group analogue of the group $\mathrm{GL}_n(\Z)$ of integer matrices with integer inverses, and for $n = 2$ the two groups coincide.
It is a central object of [[geometric group theory|2T3218RXTD]].
