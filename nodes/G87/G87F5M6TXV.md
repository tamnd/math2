---
tag: G87F5M6TXV
kind: definition
name: Lifting property
msc: [18A32, 55U35]
defines: AZK4RD8XV0
uses: [A2DE66937D, WV898P4X16, G4QDM01P6J]
sources:
  - url: https://en.wikipedia.org/wiki/Lifting_property
---

## Definition

Let $i \colon A \to B$ and $p \colon X \to Y$ be morphisms in a [[category|A2DE66937D]] $\mathcal{C}$.
The morphism $i$ has the *left lifting property* with respect to $p$ if this holds.
For all morphisms $u \colon A \to X$ and $v \colon B \to Y$ with $p \circ u = v \circ i$, there is a morphism $d \colon B \to X$ with $d \circ i = u$ and $p \circ d = v$.
In that case $p$ is said to have the *right lifting property* with respect to $i$.
If the morphism $d$ is always unique, $i$ and $p$ are *orthogonal*.

## Remarks

The data $u, v$ form a [[commutative square|WV898P4X16]], and $d$ is a diagonal filler of the square.
A common notation is $i \pitchfork p$, or $i \perp p$ for orthogonality.
Fix a class $M$ of morphisms.
The morphisms with the left lifting property with respect to all members of $M$ contain all isomorphisms and are closed under composition.

Example: in the category of sets, let $i \colon \emptyset \to \set{*}$ and let $p \colon X \to Y$ be surjective.
A square is then just a point $y = v(*)$ of $Y$, and a filler is a point $x$ of $X$ with $p(x) = y$.
It exists since $p$ is surjective.

Non-example: with the same $i$, let $p \colon \emptyset \to \set{*}$.
Take $u$ the empty map and $v = \id$; a filler would be a map $\set{*} \to \emptyset$, which does not exist.

In topology, a Hurewicz fibration is a map with the right lifting property with respect to all inclusions $Z \times \set{0} \to Z \times [0, 1]$; this is the [[homotopy lifting property|G4QDM01P6J]].
