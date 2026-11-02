---
tag: CVQVBMHH4X
kind: statement
role: theorem
name: Brenier's theorem
msc: [49Q22, 35J96, 60A10]
uses: [K8EBASR5VG, HTR7J0W66V, 3N66TM3TSQ, 07Q7CNM5WF, P0P21KDV6E, 0ABK9V9Y64]
about: [K8EBASR5VG]
sources:
  - url: https://en.wikipedia.org/wiki/Transportation_theory_(mathematics)
---

## Statement

Let $\mu$ and $\nu$ be Borel probability measures on $\R^n$ with finite second moments, $\int \abs{x}^2 \, d\mu < \infty$ and $\int \abs{y}^2 \, d\nu < \infty$.
Suppose that $\mu$ is [[absolutely continuous|P0P21KDV6E]] with respect to Lebesgue measure.
Then:

1. There is a [[convex function|07Q7CNM5WF]] $\varphi \colon \R^n \to \R \cup \set{+\infty}$, differentiable at $\mu$-almost every point, such that the [[pushforward|3N66TM3TSQ]] of $\mu$ by its [[gradient|0ABK9V9Y64]] is $\nu$: $(\nabla \varphi)_\# \mu = \nu$.
2. The [[coupling|HTR7J0W66V]] $\pi = (\id, \nabla \varphi)_\# \mu$ is the unique coupling of $\mu$ and $\nu$ that minimizes $\int \abs{x - y}^2 \, d\pi(x, y)$.
3. The map $\nabla \varphi$ is unique: if $\psi$ is another convex function with $(\nabla \psi)_\# \mu = \nu$, then $\nabla \psi = \nabla \varphi$ $\mu$-almost everywhere.

## Remarks

Yann Brenier proved the theorem in work on the polar factorization of vector fields, published in 1987 and 1991.
The proof uses Kantorovich duality: since $\abs{x - y}^2 = \abs{x}^2 + \abs{y}^2 - 2 \ip{x}{y}$, an optimal plan maximizes $\int \ip{x}{y} \, d\pi$, and its support lies in the subdifferential of a convex function $\varphi$.
A convex function is differentiable outside a Lebesgue null set.
So absolute continuity of $\mu$ makes the subdifferential single-valued $\mu$-almost everywhere, and the plan is carried by the graph of $\nabla \varphi$.
Example: if $\nu$ is the image of $\mu$ under $x \mapsto A x + b$ with $A$ symmetric positive definite, then $\varphi(x) = \frac12 \ip{Ax}{x} + \ip{b}{x}$ works, and the affine map is optimal.
Absolute continuity cannot be dropped: if $\mu = \delta_0$ and $\nu$ is not a Dirac mass, no map pushes $\mu$ to $\nu$.
When $\mu$ and $\nu$ have densities $f$ and $g$, the potential $\varphi$ solves the [[Monge–Ampère equation|14AKAC0S0T]] $g(\nabla \varphi) \det D^2 \varphi = f$ in a weak sense.

## Explanations

### L1 human

To move one distribution of mass in space onto another at the least total squared distance, there is a best plan, and it moves each point to a single destination.
Brenier's theorem says that this best map is the gradient of a convex function, the higher-dimensional version of an increasing function.
In one dimension it is the map that sends the left part of one distribution to the left part of the other, in order.

### L2 human

The theorem solves the [[Monge problem|K8EBASR5VG]] for the quadratic cost.
It gives the polar factorization: a nondegenerate map $u$ pushing $\mu$ to $\nu$ factors as $u = \nabla \varphi \circ s$, where $\varphi$ is convex and $s$ preserves $\mu$.
It is the basis of the Wasserstein geometry of probability measures, of displacement convexity, and of regularity theory for the Monge–Ampère equation through Caffarelli's work.
