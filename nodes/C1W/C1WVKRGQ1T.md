---
tag: C1WVKRGQ1T
kind: statement
role: theorem
name: Helgason support theorem
msc: [44A12, 53C65]
uses: [VJNZJ352PC]
about: [VJNZJ352PC]
sources:
  - url: https://en.wikipedia.org/wiki/Radon_transform
---

## Statement

Let $n \ge 2$ and let $f \colon \R^n \to \C$ be continuous and rapidly decreasing, that is, $\abs{x}^k f(x)$ is bounded on $\R^n$ for every integer $k \ge 0$.
Let $K \subseteq \R^n$ be a compact convex set.
Assume that the [[Radon transform|VJNZJ352PC]] of $f$ vanishes on every hyperplane that does not meet $K$.
That is, $R f(\theta, s) = 0$ whenever the hyperplane $x \cdot \theta = s$ is disjoint from $K$.
Then $f(x) = 0$ for every $x \notin K$.

## Remarks

The decay hypothesis cannot be dropped.
In $\R^2 = \C$, let $k \ge 2$ be an integer and let $f$ be continuous with $f(z) = z^{-k}$ for $\abs{z} \ge 1$.
Take a line $z = z_0 + t w$, $t \in \R$, that misses the closed unit disk.
The function $t \mapsto (z_0 + tw)^{-k}$ has its only pole off the real axis, and it decays like $\abs{t}^{-k}$.
Closing the contour in the half-plane without the pole gives integral $0$.
So $R f$ vanishes on all lines missing the unit disk, while $f \ne 0$ outside it; here $\abs{x}^k f(x)$ is bounded but $\abs{x}^{k+1} f(x)$ is not.

The convexity of $K$ is also needed.
The hyperplanes that miss a compact set are those that miss its convex hull, so the data can only locate the support up to the convex hull.

## Explanations

### L1 human

Suppose every X-ray that misses a certain convex region sees nothing.
The theorem says that, under a mild decay condition, there is indeed nothing outside that region.
It is not obvious: a ray that misses the region could in principle pass through material whose contributions cancel.

### L2 human

The theorem gives the exterior problem of tomography its uniqueness: a body is determined outside a convex obstacle by the lines that avoid the obstacle.
It is a sharper form of injectivity of the [[Radon transform|VJNZJ352PC]], local in the set of hyperplanes.
The example with $z^{-k}$ shows that rapid decrease is the right hypothesis.
The theorem is due to Helgason and has analogues for Radon transforms on symmetric spaces.
