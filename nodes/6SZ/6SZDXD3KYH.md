---
tag: 6SZDXD3KYH
kind: statement
role: theorem
name: Triangulability of analytic sets
msc: [32B25, 32B20, 57Q15]
uses: [K1HTQF26MA, V8GZ0W1ZZ5, 0QT00PB5G2, YH170WBQ6M, E1V22QQHYJ, GB7M582M5Y]
about: [K1HTQF26MA, YH170WBQ6M]
sources:
  - url: https://en.wikipedia.org/wiki/Subanalytic_set
---

## Statement

Let $X \subseteq \R^n$ be a closed [[subanalytic set|K1HTQF26MA]] and let $A_1, \dots, A_k$ be subanalytic subsets of $X$.
Then there are a locally finite [[simplicial complex|V8GZ0W1ZZ5]] $K$ and a [[homeomorphism|0QT00PB5G2]] $h \colon \abs{K} \to X$ from the polyhedron of $K$ onto $X$ with the following property.
Each $A_j$ is a union of sets $h(\sigma^\circ)$, where $\sigma^\circ$ is the interior of a simplex $\sigma$ of $K$.

## Remarks

Łojasiewicz proved the statement for [[semianalytic sets|E1V22QQHYJ]], and Hironaka extended it to subanalytic sets.
The proof first decomposes $X$ into finitely many pieces on which suitable coordinate projections are finite and well behaved, and then triangulates by induction on $n$.
Every closed real analytic subset of $\R^n$ is semianalytic, and every [[complex analytic set|GB7M582M5Y]] in $\C^n = \R^{2n}$ is a closed real analytic subset.
So both kinds of analytic sets are [[triangulable|YH170WBQ6M]], and a triangulation can be chosen compatible with the singular locus.
For instance, the cone $\set{x^2 + y^2 = z^2}$ in $\R^3$ can be triangulated with the vertex at the origin as a vertex of $K$.

## Explanations

### L1 human

An analytic set can have singular points, such as the tip of a cone or a crossing of two curves.
The theorem says that, however complicated it is, the set can be cut into pieces that are curved copies of points, segments, triangles and their higher analogues, glued along faces.
This makes analytic sets accessible to combinatorial topology.

### L2 human

Triangulability implies that a compact analytic set has finitely generated homology and a well defined Euler characteristic.
It also implies local conic structure: a small neighbourhood of a point of an analytic set is homeomorphic to the cone over its link.
The choice of a triangulation compatible with the subsets $A_j$ lets one treat a set together with a stratification of it.
