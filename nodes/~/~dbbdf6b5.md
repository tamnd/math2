---
tag: ~dbbdf6b5
kind: statement
role: theorem
name: Heine–Borel theorem in finite-dimensional normed spaces
msc: [46B20]
uses: [~207cb5fd, ~7c2c8f85, ~090c4967, ~ebd1051c]
sources:
  - url: https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem
    locator: In the theory of topological vector spaces
  - url: https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem
    locator: In the theory of metric spaces
---

## Statement

Let $V$ be a finite-dimensional vector space over $\mathbb{R}$ or $\mathbb{C}$, with a norm $\|\cdot\|$ and the metric $d(x, y) = \|x - y\|$.
Then a subset $K \subseteq V$ is [[compact|~56dabfb9]] if and only if $K$ is [[closed|~dfeacff3]] and [[bounded|~f6a5aaba]].

## Remarks

Proof: choose a basis. By [[equivalence of norms in finite dimension|~7c2c8f85]], the norm is equivalent to the Euclidean norm of the coordinates. Equivalent norms have the same closed sets, bounded sets and compact sets. Then use the [[Heine–Borel theorem|~207cb5fd]] in $\mathbb{R}^n$ or $\mathbb{C}^n = \mathbb{R}^{2n}$.
In other words, each finite-dimensional normed space is a [[proper metric space|~090c4967]].
The converse also holds: if the closed unit ball is compact, the space is [[finite-dimensional|~54220a46]].

## Explanations

### L1 human

In each finite-dimensional normed space, the compact sets are the closed bounded sets, just as in $\mathbb{R}^n$.
