---
tag: EJ0N7F9TYQ
kind: definition
name: Morrey quasiconvexity
msc: [49J45, 26B25]
defines: DVJ17KVWXP
uses: [M4CEZ5K9HP, 07GR3TNW4H, GK4P8G0PB2]
sources:
  - url: https://en.wikipedia.org/wiki/Quasiconvexity_(calculus_of_variations)
---

## Definition

Let $m, n \ge 1$ and let $f \colon \R^{m \times n} \to \R$ be continuous.
The function $f$ is *quasiconvex* (in the sense of Morrey) if
$$f(\xi) \le \frac{1}{\abs{D}} \int_D f\big(\xi + \nabla \varphi(x)\big) \, dx$$
for every bounded open set $D \subseteq \R^n$, every $\xi \in \R^{m \times n}$ and every $\varphi \in W^{1,\infty}_0(D; \R^m)$.
Here $W^{1,\infty}_0(D; \R^m)$ is the [[Sobolev space|M4CEZ5K9HP]] of Lipschitz maps that vanish on $\partial D$.
The number $\abs{D}$ is the Lebesgue measure of $D$.

## Remarks

If the inequality holds for one bounded open set $D$ with $\abs{\partial D} = 0$, it holds for all of them; often $D$ is the unit cube.

Example: every [[convex|07GR3TNW4H]] $f$ is quasiconvex.
Since $\varphi = 0$ on $\partial D$, the average of $\nabla \varphi$ over $D$ is $0$, and Jensen's inequality gives the inequality.

Non-example: $f(\xi) = -\abs{\xi}^2$ is not quasiconvex.
For $\varphi \ne 0$, the cross term $2 \int_D \xi : \nabla \varphi \, dx$ vanishes, so the average of $f(\xi + \nabla \varphi)$ is $-\abs{\xi}^2 - \frac{1}{\abs{D}} \int_D \abs{\nabla \varphi}^2 \, dx < f(\xi)$.

Every quasiconvex function is [[rank-one convex|GK4P8G0PB2]].
For $m = 1$ or $n = 1$, quasiconvexity is ordinary convexity.
For $m \ge 3$ and $n \ge 2$, Šverák gave a rank-one convex function that is not quasiconvex; the case $m = 2$ is open.
