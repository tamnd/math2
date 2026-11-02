---
tag: 4J4EW7FXWW
kind: statement
role: theorem
name: Mazur–Ulam theorem
msc: [46B04]
uses: [03J5RAKB30, 02HPP5VCZH, 0JF0TVYGWT]
about: [02HPP5VCZH, 0JF0TVYGWT]
sources:
  - url: https://en.wikipedia.org/wiki/Mazur%E2%80%93Ulam_theorem
same_as:
  wikidata: Q1660147
  wikipedia: Mazur–Ulam theorem
---

## Statement

Let $X$ and $Y$ be [[normed vector spaces|03J5RAKB30]] over $\R$.
Let $f \colon X \to Y$ be a surjective [[isometry|02HPP5VCZH]], that is, $f$ is onto and $\norm{f(x) - f(y)} = \norm{x - y}$ for all $x, y \in X$.
Then $f$ is [[affine|0JF0TVYGWT]]: the map $x \mapsto f(x) - f(0)$ is linear.

## Remarks

The heart of the proof is that $f$ preserves [[midpoints|0S706JBZBG]]: $f\left(\frac{x + y}{2}\right) = \frac{f(x) + f(y)}{2}$.
One proof describes the midpoint by distances only: it is fixed by every surjective isometry of $X$ that fixes $x$ and $y$.
The argument uses the point reflection $z \mapsto x + y - z$, which swaps $x$ and $y$.
Midpoint preservation and continuity then give real linearity of $f - f(0)$.

Surjectivity is needed.
The map $f \colon \R \to \R^2$, $f(t) = (t, \sin t)$, with the norm $\norm{(a, b)} = \max(\abs{a}, \abs{b})$ on $\R^2$, is an isometry because $\abs{\sin t - \sin s} \le \abs{t - s}$, but it is not affine.
The theorem is about real structure only: complex conjugation on $\C$ is a surjective isometry that is real-linear but not complex-linear.

## Explanations

### L1 human

If a map between normed spaces keeps all distances and covers the whole target, then it does not bend anything.
It is a linear map followed by a shift.
So the metric of a normed space already knows its linear structure.

### L2 human

The theorem shows that two real normed spaces are isometric as metric spaces exactly when they are isometrically isomorphic as normed spaces.
So isometric classification of Banach spaces can ignore nonlinear isometries.
For a Euclidean space it recovers the fact that every distance-preserving map of $\R^n$ onto itself is an orthogonal map followed by a translation.
