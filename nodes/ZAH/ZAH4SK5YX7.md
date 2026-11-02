---
tag: ZAH4SK5YX7
kind: statement
role: theorem
name: Boutet de Monvel's embedding theorem
msc: [32V30, 32V20, 32W10]
uses: [ZC78JKZX9S, 80MTNXWW80, JFKYYK2CEB]
about: [ZC78JKZX9S]
sources:
  - url: https://en.wikipedia.org/wiki/CR_manifold
---

## Statement

Let $M$ be a compact smooth [[CR manifold|ZC78JKZX9S]] of hypersurface type, of real dimension $2n + 1$ with $n \ge 2$.
Assume that $M$ is strongly pseudoconvex, that is, its [[Levi form|80MTNXWW80]] is definite at every point.
Then there is a smooth CR embedding of $M$ into $\C^N$ for some $N$.

## Remarks

The theorem is due to L. Boutet de Monvel.
The proof uses Kohn's analysis of the tangential Cauchy–Riemann operator $\bar\partial_b$ and of the [[Kohn Laplacian|ZBQ6TVNZZ8]].
On a compact strongly pseudoconvex manifold of real dimension at least $5$, this analysis gives good solvability of $\bar\partial_b$.
This produces many global [[CR functions|JFKYYK2CEB]], and finitely many of them give an embedding.
The boundary of a bounded strongly pseudoconvex domain in $\C^{n+1}$ with smooth boundary is an example where the embedding is given from the start.
The bound on the dimension is necessary: in real dimension $3$ there are compact strongly pseudoconvex CR manifolds with no CR embedding into any $\C^N$, such as [[Rossi's example|1TJXANASFE]].

## Explanations

### L1 human

A CR manifold carries part of the structure of a hypersurface in complex space, but it is defined abstractly, without a surrounding space.
Assume the manifold is compact, curves in the strongly convex way, and has dimension at least five.
Then the theorem says that it really sits inside some complex space.
So in these dimensions the abstract notion gives nothing new.

### L2 human

The result is a global embedding theorem, in contrast with local realisation questions, where Kuranishi and others worked on embedding small pieces.
Combined with results on filling, it shows that such $M$ bound complex spaces with isolated singularities.
The three-dimensional case behaves very differently and is an active subject: there embeddability is a delicate property that is not preserved under small deformations.
