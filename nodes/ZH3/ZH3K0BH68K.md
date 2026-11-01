---
tag: ZH3K0BH68K
kind: conjecture
name: Graceful tree conjecture
msc: [05C78, 05C05]
uses: [00C0BR7D7H, 062D9KXJB1]
about: [062D9KXJB1]
sources:
  - url: https://en.wikipedia.org/wiki/Graceful_labeling
history:
  posed_by: "Gerhard Ringel and Anton Kotzig"
  first_stated: "1964"
---

## Statement

Let $G$ be a finite simple [[graph|00C0BR7D7H]] with $m$ edges.
Let $V$ be the vertex set of $G$.
A *graceful labeling* of $G$ is an injective map $f \colon V \to \set{0, 1, \ldots, m}$ with the following property.
The edge labels $\abs{f(u) - f(v)}$, for the edges $uv$ of $G$, are pairwise distinct.
Then the edge labels are exactly $1, 2, \ldots, m$.
The conjecture: every finite [[tree|062D9KXJB1]] has a graceful labeling.

## Remarks

The conjecture is open.
It is also called the Ringel–Kotzig conjecture.
It is known for many families of trees, for example paths, stars and caterpillars, and computer searches have checked it for all trees with few vertices.
A path $v_0 v_1 \cdots v_m$ has the graceful labeling $0, m, 1, m - 1, 2, \ldots$, with edge labels $m, m - 1, \ldots, 1$.
Rosa showed that a graceful labeling of a tree $T$ with $m$ edges gives a decomposition of the complete graph $K_{2m+1}$ into $2m + 1$ copies of $T$.
So the conjecture would imply Ringel's conjecture on such decompositions.
Ringel's conjecture was proved for all large $m$ by Montgomery, Pokrovskiy and Sudakov, by other methods.
Not every graph is graceful: for example the cycle $C_n$ has a graceful labeling only when $n \equiv 0$ or $3 \pmod 4$.

## Explanations

### L1 human

Write distinct numbers from $0$ to $m$ on the vertices of a tree with $m$ edges.
Label each edge by the difference of the numbers at its ends.
The labeling is graceful when the edges get the labels $1, 2, \ldots, m$, each exactly once.
The conjecture says that every tree can be labeled in this way.
It is easy to check for small trees, but no general proof is known.
