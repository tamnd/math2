---
tag: CC27DAMRWK
kind: statement
role: fact
name: Saint-Venant's principle
msc: [74G50, 74B05]
uses: [6W00ZECYT0, KG2XWEMJ30, QJW6NMNXJM]
about: [6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Saint-Venant%27s_principle
same_as:
  wikidata: Q632673
  wikipedia: Saint-Venant's principle
---

## Statement

Let an elastic body in [[linear elasticity|6W00ZECYT0]] carry loads on a part of its boundary that lies in a ball of small diameter $d$.
Suppose the loads are self-equilibrated, that is, their resultant force and their resultant moment are both zero.
Then the [[stresses|KG2XWEMJ30]] they produce are negligible at points whose distance from the loaded region is large compared with $d$.
Equivalently, two load systems on the same small region with the same resultant force and moment produce nearly the same stresses far from that region.

## Remarks

As stated, this is a heuristic principle used by engineers, not a theorem: the words "small", "large" and "negligible" are not made precise.
Mathematical versions exist for particular geometries.
Toupin proved such a version for a prismatic cylinder loaded on one end by self-equilibrated tractions.
The strain energy stored in the part of the cylinder beyond distance $s$ from the loaded end decays exponentially in $s$.
The rate depends on the cross-section and the elastic constants.
The principle justifies replacing complicated end loads on a beam by their resultant force and moment, as in beam theory and in the Saint-Venant torsion and bending solutions.
The self-equilibrium hypothesis is necessary: a single point force on a half-space produces stresses that decay only like the inverse square of the distance, as the [[Boussinesq problem|QJW6NMNXJM]] shows.

## Explanations

### L1 human

Grip the end of a long rubber bar in any way you like, as long as the total pull is the same.
Near your hand the stresses depend a lot on how you grip.
A few bar widths away, the bar cannot tell the difference: it only feels the total pull and the total twist.
This is Saint-Venant's principle, and it is why engineers can ignore the details of how loads are applied.

### L2 human

In practice the principle lets one solve a simple problem, with idealised end loads, and trust the solution away from the ends.
The region where the details matter has a size comparable to the loaded region, for example one or two depths of a beam.
Its rigorous forms are decay estimates for solutions of the elasticity equations with zero resultant data, close in spirit to Phragmén–Lindelöf type estimates for elliptic equations.
