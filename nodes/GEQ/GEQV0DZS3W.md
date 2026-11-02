---
tag: GEQV0DZS3W
kind: definition
name: Nielsen fixed-point theory
msc: [55M20, 54H25]
defines: GHXMVWN3W5
uses: [0VGFHTM75Y, CCNKA8C711, F2F143KQ2M, ZSYCA4EGEZ]
sources:
  - url: https://en.wikipedia.org/wiki/Fixed-point_theorem
---

## Definition

Let $X$ be a compact connected polyhedron, that is, a space homeomorphic to a finite simplicial complex.
Let $f \colon X \to X$ be a [[continuous map|0VGFHTM75Y]] with fixed point set $\mathrm{Fix}(f) = \set{x \in X : f(x) = x}$.

1. Two fixed points $x, y$ are *Nielsen equivalent* if there is a path $c$ from $x$ to $y$ such that $f \circ c$ is [[path homotopic|CCNKA8C711]] to $c$.
2. The equivalence classes are the *fixed point classes* of $f$; there are finitely many, and each is open and closed in $\mathrm{Fix}(f)$.
3. Each fixed point class $F$ has a *fixed-point index* $i(f, F) \in \Z$.
   For a single fixed point $x$ in an open set of $\R^n$, it is the local degree of $u \mapsto u - f(u)$ at $x$.
4. A class $F$ is *essential* if $i(f, F) \neq 0$.

The *Nielsen number* $N(f)$ is the number of essential fixed point classes of $f$.

## Remarks

The sum of the indices of all fixed point classes is the [[Lefschetz number|ZSYCA4EGEZ]] $L(f)$.
The number $N(f)$ depends only on the homotopy class of $f$, and every map [[homotopic|F2F143KQ2M]] to $f$ has at least $N(f)$ fixed points.

Example: on the circle, let $f(z) = z^k$ with $k \neq 1$.
The fixed points are the $\abs{k - 1}$ roots of $z^{k-1} = 1$; they lie in distinct classes, each of index $\pm 1$, so $N(f) = \abs{1 - k} = \abs{L(f)}$.

Non-example of essentiality: for the identity of $S^1$, the single fixed point class is all of $S^1$.
Its index is $L(\id) = \chi(S^1) = 0$, so it is not essential.
Indeed a small rotation has no fixed point, and $N(\id) = 0$.

For compact manifolds of dimension at least $3$, Wecken's theorem says that some map homotopic to $f$ has exactly $N(f)$ fixed points.
