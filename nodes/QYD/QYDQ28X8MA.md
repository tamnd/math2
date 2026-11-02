---
tag: QYDQ28X8MA
kind: counterexample
name: Wild knot
msc: [57M30, 57K10]
uses: [QYEAZTYGPT, 00ZG9Y9TR4, 0QT00PB5G2]
sources:
  - url: https://en.wikipedia.org/wiki/Wild_knot
same_as:
  wikidata: Q2489408
  wikipedia: Wild knot
---

## Counterexample

A [[knot|QYEAZTYGPT]] is a [[topological embedding|00ZG9Y9TR4]] $K \colon S^1 \to \R^3$.
It is *tame* if there is a [[homeomorphism|0QT00PB5G2]] $h \colon \R^3 \to \R^3$ such that $h(K(S^1))$ is a closed polygon with finitely many sides; otherwise it is *wild*.

Let $p$ be a point of $\R^3$.
Take a sequence of small trefoil knots, of sizes tending to $0$, placed one after the other along an arc that ends at $p$.
Tie them all into one closed curve that passes through $p$, so that every neighbourhood of $p$ contains infinitely many of the small trefoils.
The result is a knot, and it is wild.
Every point of a polygonal knot has a small ball around it that meets the knot in one unknotted arc.
A homeomorphism of $\R^3$ carries this local picture along.
At $p$ the knot has no such ball, because every small ball around $p$ contains whole knotted trefoils of the sequence.
One shows that this local knotting cannot be undone.

## Remarks

So not every topological knot is tame, and knot theory usually restricts to tame knots, for example to smooth or polygonal ones.
The local flatness property at every point, which fails at $p$, characterizes tame knots among topological ones.
Wild knots and other wild embeddings, such as the Alexander horned sphere, are studied in the theory of wild embeddings.

## Explanations

### L1 human

Ordinary knots are tied in a rope with a finite number of crossings.
A wild knot is a closed curve with infinitely many knots tied in it, getting smaller and smaller and piling up at one point.
Near that point the curve is knotted at every scale, so it cannot be straightened into a nice polygon.
