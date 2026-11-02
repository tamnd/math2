---
tag: 2GSRBDT96M
kind: statement
role: theorem
name: Whitney embedding theorem
msc: [57R40, 58A05]
uses: [F45VQ47GPV, 6RW68JGBHC, VKFW27WXEZ, 0XPR1E85W0]
about: [F45VQ47GPV]
sources:
  - url: https://en.wikipedia.org/wiki/Whitney_embedding_theorem
same_as:
  wikidata: Q1306095
  wikipedia: Whitney embedding theorem
---

## Statement

Let $n \ge 1$ and let $M$ be a [[smooth manifold|F45VQ47GPV]] of dimension $n$, Hausdorff and second countable.
A *smooth embedding* is an [[immersion|6RW68JGBHC]] that is a homeomorphism onto its image.
Then there is a smooth embedding of $M$ into the [[Euclidean space|0XPR1E85W0]] $\R^{2n}$.
In particular $M$ is diffeomorphic to an [[embedded submanifold|VKFW27WXEZ]] of $\R^{2n}$.

## Remarks

There is also a weak version: every such $M$ embeds in $\R^{2n+1}$, and any smooth map $M \to \R^{2n+1}$ can be approximated by embeddings.
Its proof starts from an embedding into some large $\R^N$, built from charts and bump functions.
Then $N$ is lowered by generic linear projections.
Sard's theorem shows that almost every projection stays an injective immersion while $N > 2n + 1$.
To reach $2n$, one first takes an immersion into $\R^{2n}$ with only transverse double points.
Then one removes the double points in pairs; for $n \ge 3$ this step uses the Whitney trick, and $n = 1, 2$ are treated directly.
The bound $2n$ is sharp in general: for $n$ a power of $2$, the real projective space $\R P^n$ does not embed in $\R^{2n - 1}$.
Example: the circle ($n = 1$) embeds in $\R^2$, and the Klein bottle ($n = 2$) embeds in $\R^4$ but not in $\R^3$.

## Explanations

### L1 human

Every smooth manifold, however it was defined, can be realised as a smooth shape inside an ordinary Euclidean space.
Twice its dimension is always enough room.
So abstract manifolds are no more general than the curved surfaces and solids that sit inside some $\R^N$.

### L2 human

The theorem reconciles the intrinsic definition of a manifold by charts with the older picture of a manifold as a subset of $\R^N$.
It allows one to borrow structures from $\R^N$, such as a Riemannian metric induced from the dot product or a normal bundle and a tubular neighbourhood.
The weak version is a typical general position argument, a precursor of transversality theory.
The strong version introduced the Whitney trick, which later became the key step in the h-cobordism theorem.
