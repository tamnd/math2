---
tag: 8J8AW0TG9M
kind: statement
role: theorem
name: Besicovitch–Federer projection theorem
msc: [28A75, 28A78]
uses: [7N0GFMW05R, Q1TGZK8RN6]
about: [7N0GFMW05R]
sources:
  - book: isbn:9780521655958
---

## Statement

Let $1 \le m < n$ be integers, and let $\mathcal{H}^m$ be the $m$-dimensional [[Hausdorff measure|Q1TGZK8RN6]] on $\R^n$.
Let $G(n, m)$ be the Grassmannian of $m$-dimensional linear subspaces of $\R^n$, with its unique probability measure $\gamma_{n,m}$ that is invariant under the orthogonal group.
For $V \in G(n, m)$, let $P_V \colon \R^n \to V$ be the orthogonal projection onto $V$.
Let $E \subseteq \R^n$ be $\mathcal{H}^m$-measurable with $\mathcal{H}^m(E) < \infty$.

1. $E$ is purely $m$-unrectifiable if and only if $\mathcal{H}^m(P_V(E)) = 0$ for $\gamma_{n,m}$-almost every $V \in G(n, m)$.
2. If $E$ is [[$m$-rectifiable|7N0GFMW05R]] and $\mathcal{H}^m(E) > 0$, then $\mathcal{H}^m(P_V(E)) > 0$ for $\gamma_{n,m}$-almost every $V \in G(n, m)$.

## Remarks

Part 2 is the easier half.
A rectifiable set of positive measure has an approximate tangent plane $W$ at almost every point, and for almost every $V$ the projection $P_V$ is injective on $W$.
Then $P_V$ is bi-Lipschitz on a piece of $E$ of positive measure, so the projection has positive measure.
Part 1 is the deep half; Besicovitch proved it for $m = 1$ and $n = 2$, and Federer proved the general case.
Example: the four-corner Cantor set in $\R^2$ has positive and finite $\mathcal{H}^1$ measure and is purely $1$-unrectifiable, so almost all of its projections onto lines have length zero.

## Explanations

### L1 human

Shine light on a set and look at its shadows on lines or planes in all directions.
If the set is made of curve-like or surface-like pieces, almost every shadow has positive size.
If the set is a fractal dust with no such pieces, almost every shadow has size zero, even though the set itself has positive size.
So the shadows tell whether a set is rectifiable.

### L2 human

A set $E$ of finite measure splits as $E = R \cup P$ with $R$ rectifiable and $P$ purely unrectifiable.
The theorem says that almost every projection of $E$ sees only $R$.
It is the model for many later results that characterise rectifiability by densities, tangent measures or singular integrals.
It is used in the study of removable sets for bounded analytic functions, through the [[analytic capacity|QGQPHRANWZ]] of planar sets.
