---
tag: 5T6HCEK1M8
kind: definition
name: Final functor
msc: [18A30]
defines: M5910N7YF0
uses: [28NQ0KRHD3, PC6HG1JEGM, BJS1CGTKQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Final_functor
---

## Definition

Let $F \colon \mathcal{C} \to \mathcal{D}$ be a [[functor|28NQ0KRHD3]].
For an object $d$ of $\mathcal{D}$, let $d \downarrow F$ be the [[comma category|PC6HG1JEGM]] whose objects are pairs $(c, f)$ with $c$ an object of $\mathcal{C}$ and $f \colon d \to F c$.
A morphism $(c, f) \to (c', f')$ in it is a morphism $h \colon c \to c'$ with $F(h) \circ f = f'$.
$F$ is *final* if for every object $d$ of $\mathcal{D}$ the category $d \downarrow F$ is nonempty and connected.

## Remarks

Here a category is connected when any two objects are joined by a finite zigzag of morphisms.
If $F$ is final, then for every functor $G \colon \mathcal{D} \to \mathcal{E}$ the [[colimit|BJS1CGTKQ5]] of $G \circ F$ exists if and only if the colimit of $G$ exists.
The canonical morphism $\operatorname{colim} (G \circ F) \to \operatorname{colim} G$ is then an isomorphism.
For small $\mathcal{C}$ and $\mathcal{D}$ this property for all $G$ is equivalent to finality.

Example: let $\mathcal{D}$ have a terminal object $t$, and let $F$ be the functor from the one-object category picking out $t$.
For each $d$ the category $d \downarrow F$ has one object, the unique arrow $d \to t$, and only its identity, so it is nonempty and connected.
Hence $\operatorname{colim} G = G(t)$ for every $G$.

Non-example: let $\mathcal{D}$ be the poset $\set{0 < 1}$ and let $F$ pick out $0$.
There is no arrow $1 \to 0$, so $1 \downarrow F$ is empty and $F$ is not final.

The inclusion of a cofinal subset of a directed set is a final functor.
