---
tag: PADZ7D9KBT
kind: statement
role: lemma
name: Tucker's lemma
msc: ["05E45", 55M25]
uses: [V8GZ0W1ZZ5, 0Q0H13G8ZB]
about: [V8GZ0W1ZZ5]
sources:
  - url: https://en.wikipedia.org/wiki/Tucker's_lemma
same_as:
  wikidata: Q7851042
  wikipedia: Tucker's lemma
---

## Statement

Let $n \ge 1$ and let $T$ be a triangulation of the [[closed ball|0Q0H13G8ZB]] $B^n \subset \R^n$ by a finite [[simplicial complex|V8GZ0W1ZZ5]].
Assume that $T$ is antipodally symmetric on the boundary.
This means that $-\sigma$ is a simplex of $T$ for every simplex $\sigma$ of $T$ contained in the boundary sphere.
Let $\lambda$ be a labelling of the vertices of $T$ by elements of $\set{\pm 1, \pm 2, \ldots, \pm n}$ such that $\lambda(-v) = -\lambda(v)$ for every vertex $v$ on the boundary.
Then $T$ has a *complementary edge*: an edge $\set{u, w}$ of $T$ with $\lambda(u) = -\lambda(w)$.

## Remarks

Tucker's lemma is a combinatorial form of the [[Borsuk–Ulam theorem|QHJ0GBQE2E]].
To derive the lemma from Borsuk–Ulam, send a vertex with label $\pm i$ to $\pm e_i$ and extend linearly on simplices to a map $f \colon B^n \to \R^n$.
With no complementary edge, the image of $f$ avoids $0$.
Then $f / \norm{f}$ restricts to an odd map from the boundary sphere $S^{n-1}$ to $S^{n-1}$ that extends over the ball, which is impossible.
Conversely, applying the lemma to finer and finer triangulations proves the Borsuk–Ulam theorem.
There are also constructive path-following proofs, which give algorithms to find a complementary edge.

Example: for $n = 1$, subdivide $[-1, 1]$ into intervals and label the vertices by $\pm 1$ with $\lambda(-1) = -\lambda(1)$.
Moving from $-1$ to $1$ the label changes sign, so some interval of the subdivision has endpoints labelled $1$ and $-1$.

The antipodal condition on the boundary is needed: if every vertex gets the label $1$, no edge is complementary.

## Explanations

### L1 human

Cut a disc into small triangles and write one of the labels $\pm 1, \pm 2$ at each corner, so that opposite points on the rim get opposite labels.
Then somewhere two neighbouring corners carry opposite labels, such as $2$ and $-2$.

### L2 human

Tucker's lemma is to the Borsuk–Ulam theorem what [[Sperner's lemma|HQG3V5Z6MR]] is to the Brouwer fixed-point theorem.
Because it is finite and combinatorial, it is the usual route to applications of Borsuk–Ulam in combinatorics, such as necklace splitting and Kneser's conjecture, and to algorithms for them.
