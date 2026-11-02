---
tag: V313FN8HRW
kind: statement
role: theorem
name: Homotopy invariance of homology
msc: [55N10, 55P10]
uses: [M0Q5CFJ7ZH, F2F143KQ2M, XZG6MTSWCN, R5WP8Z69Q8]
about: [M0Q5CFJ7ZH, XZG6MTSWCN]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_homology
---

## Statement

Let $X$ and $Y$ be topological spaces and let $f, g \colon X \to Y$ be continuous maps that are [[homotopic|F2F143KQ2M]].
Then the induced maps on [[singular homology|M0Q5CFJ7ZH]] are equal: $f_* = g_* \colon H_n(X) \to H_n(Y)$ for every $n \ge 0$.
In particular, a [[homotopy equivalence|XZG6MTSWCN]] $f \colon X \to Y$ induces isomorphisms $f_* \colon H_n(X) \to H_n(Y)$ for every $n$.

## Remarks

The proof cuts the prism $\Delta^n \times [0, 1]$ into $(n+1)$-simplices.
A homotopy $H \colon X \times [0,1] \to Y$ from $f$ to $g$ then gives a prism operator $P \colon C_n(X) \to C_{n+1}(Y)$ with $\partial P + P \partial = g_\# - f_\#$.
So $f_\#$ and $g_\#$ are chain homotopic, and chain homotopic maps induce the same map on homology.
The second claim follows by applying the first to $g \circ f \simeq \id_X$ and $f \circ g \simeq \id_Y$.

Example: a [[contractible space|R5WP8Z69Q8]] $X$, such as $\R^n$ or a convex set, is homotopy equivalent to a point.
Hence $H_0(X) \cong \Z$ and $H_n(X) = 0$ for $n \ge 1$.
The same holds with any coefficients and for relative homology of pairs, with homotopies of pairs.

## Explanations

### L1 human

Homology does not change when a space or a map is deformed continuously.
Two spaces that can be squeezed into each other without tearing, such as a thick annulus and a circle, have the same homology.
This is what makes homology a tool for shapes up to deformation rather than for exact geometry.

### L2 human

This is the homotopy axiom of the Eilenberg–Steenrod axioms for singular homology.
It lets one replace a space by a simpler homotopy equivalent one, for example a deformation retract, before computing.
It also shows that singular homology factors through the homotopy category of spaces.
Together with excision, the long exact sequence of a pair and the homology of a point, it is enough to compute the homology of spheres and of CW complexes.
