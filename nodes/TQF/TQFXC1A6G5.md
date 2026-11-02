---
tag: TQFXC1A6G5
kind: statement
role: theorem
name: Simplicial approximation theorem
msc: [55U10, 57Q05]
uses: [V8GZ0W1ZZ5, J5DZEYCEX2, F2F143KQ2M]
about: [V8GZ0W1ZZ5]
sources:
  - url: https://en.wikipedia.org/wiki/Simplicial_approximation_theorem
same_as:
  wikidata: Q3983972
  wikipedia: Simplicial approximation theorem
---

## Statement

Let $K$ and $L$ be [[simplicial complexes|V8GZ0W1ZZ5]] with $K$ finite, and let $\abs{K}$ and $\abs{L}$ be their geometric realizations.
For a point $y \in \abs{L}$, let $\operatorname{supp}(y)$ be the smallest closed simplex of $\abs{L}$ that contains $y$.
A simplicial map $g \colon K \to L$ is a *simplicial approximation* of a continuous map $f \colon \abs{K} \to \abs{L}$ if $\abs{g}(x) \in \operatorname{supp}(f(x))$ for every $x \in \abs{K}$.
Let $f \colon \abs{K} \to \abs{L}$ be continuous.
Let $\operatorname{sd}^m K$ be the $m$-fold [[barycentric subdivision|J5DZEYCEX2]] of $K$, so that $\abs{\operatorname{sd}^m K} = \abs{K}$.
Then there are an integer $m \ge 0$ and a simplicial map $g \colon \operatorname{sd}^m K \to L$ that is a simplicial approximation of $f$.

## Remarks

A vertex map $g$ is a simplicial approximation of $f$ as soon as $f(\operatorname{st} v) \subseteq \operatorname{st} g(v)$ for every vertex $v$, where $\operatorname{st}$ denotes the open star.
The open stars of the vertices of $L$ form an open cover of $\abs{L}$, so their preimages under $f$ form an open cover of the compact metric space $\abs{K}$.
Repeated barycentric subdivision makes the simplices smaller than a Lebesgue number of this cover.
Then each open star of $\operatorname{sd}^m K$ maps into some open star of $L$, and choosing such a vertex for each $v$ gives $g$.

A simplicial approximation $g$ of $f$ is [[homotopic|F2F143KQ2M]] to $f$ by the straight-line homotopy, which stays in $\operatorname{supp}(f(x))$.

Subdivision is necessary.
Let $K = L$ be the boundary of a triangle, so $\abs{K}$ is a circle, and let $f$ wrap this circle twice around itself.
A simplicial map $K \to L$ is either a bijection on vertices, of degree $\pm 1$, or misses a vertex, of degree $0$.
Since a simplicial approximation is homotopic to $f$, which has degree $2$, no simplicial map $K \to L$ approximates $f$.

## Explanations

### L1 human

A continuous map between triangulated spaces can be very irregular.
The theorem says that after cutting the source into small enough triangles, the map can be replaced by one that sends triangles linearly onto triangles.
The new map is close to the old one and homotopic to it.

### L2 human

Simplicial approximation shows that the set of homotopy classes of maps $\abs{K} \to \abs{L}$ is countable when $K$ and $L$ are finite.
It is used to prove that simplicial homology is a homotopy invariant and agrees with singular homology, and to compute $\pi_k(S^n) = 0$ for $k < n$.
The analogue for CW complexes is the cellular approximation theorem.
