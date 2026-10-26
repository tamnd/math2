---
tag: 0PHT6NBYPB
kind: statement
role: theorem
name: Heine–Borel theorem in finite-dimensional normed spaces
msc: [46B20]
uses: [07PFYV65MB, 03MC70ZRNR, 0Z4V98VN5E, 0KNJWEVSMG]
sources:
  - url: https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem
    locator: In the theory of topological vector spaces
  - url: https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem
    locator: In the theory of metric spaces
---

## Statement

Let $V$ be a finite-dimensional vector space over $\mathbb{R}$ or $\mathbb{C}$, with a norm $\|\cdot\|$ and the metric $d(x, y) = \|x - y\|$.
Then a subset $K \subseteq V$ is [[compact|00R0X1WGPX]] if and only if $K$ is [[closed|0G5AV9Q4RR]] and [[bounded|0P953MG05E]].

## Remarks

Proof: choose a basis. By [[equivalence of norms in finite dimension|03MC70ZRNR]], the norm is equivalent to the Euclidean norm of the coordinates. Equivalent norms have the same closed sets, bounded sets and compact sets. Then use the [[Heine–Borel theorem|07PFYV65MB]] in $\mathbb{R}^n$ or $\mathbb{C}^n = \mathbb{R}^{2n}$.
In other words, each finite-dimensional normed space is a [[proper metric space|0Z4V98VN5E]].
The converse also holds: if the closed unit ball is compact, the space is [[finite-dimensional|0VZVV8VME5]].

## Explanations

### L1 human

In each finite-dimensional normed space, the compact sets are the closed bounded sets, just as in $\mathbb{R}^n$.
