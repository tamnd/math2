---
tag: WF22KK7C3R
kind: statement
role: theorem
name: Stable manifold theorem
msc: [34C45, 37D10]
uses: [07BNRFQ0PJ, 02903SSA48, 01TPMXM6NM, 047NDTEPCV, WWZTW11664]
about: [01TPMXM6NM, WWZTW11664]
sources:
  - url: https://en.wikipedia.org/wiki/Stable_manifold_theorem
same_as:
  wikidata: Q7595768
  wikipedia: Stable manifold theorem
---

## Statement

Let $U$ be an open subset of $\R^n$, let $k \ge 1$, and let $f \colon U \to \R^n$ be of class $C^k$.
Let $x_0 \in U$ be a [[hyperbolic equilibrium point|01TPMXM6NM]] of the [[autonomous system|07BNRFQ0PJ]] $x' = f(x)$, with [[flow|02903SSA48]] $\varphi$.
Let $A = Df(x_0)$ be the [[Jacobian matrix|047NDTEPCV]].
Let $E^s$ be the sum of the generalised eigenspaces of $A$ for eigenvalues with negative real part.
Let $E^u$ be the sum of those for eigenvalues with positive real part.
Then there is an open neighbourhood $V$ of $x_0$ in $U$ such that:

1. The local stable manifold $W^s_{\mathrm{loc}} = \set{x \in V : \varphi_t(x) \in V \text{ for all } t \ge 0}$ is an embedded $C^k$ submanifold of $\R^n$ of dimension $\dim E^s$ whose tangent space at $x_0$ is $E^s$.
2. For each $x \in W^s_{\mathrm{loc}}$, $\varphi_t(x) \to x_0$ as $t \to +\infty$.
3. The local unstable manifold $W^u_{\mathrm{loc}} = \set{x \in V : \varphi_t(x) \in V \text{ for all } t \le 0}$ is an embedded $C^k$ submanifold of dimension $\dim E^u$ with tangent space $E^u$ at $x_0$.
4. For each $x \in W^u_{\mathrm{loc}}$, $\varphi_t(x) \to x_0$ as $t \to -\infty$.

## Remarks

One proof writes the solutions that stay near $x_0$ as fixed points of an integral equation built from the variation of constants formula.
Then it applies the contraction mapping principle; another proof uses the graph transform.
The global stable manifold $W^s(x_0) = \set{x \in U : \varphi_t(x) \to x_0 \text{ as } t \to \infty}$ is the union of the sets $\varphi_{-t}(W^s_{\mathrm{loc}})$ for $t \ge 0$, and it is an [[invariant set|WWZTW11664]].
Example: for $x' = -x$, $y' = y + x^2$, the origin is hyperbolic with $E^s$ the $x$-axis and $E^u$ the $y$-axis.
On the curve $y = -x^2/3$ one has $y' = (-2x/3)(-x) = 2x^2/3 = y + x^2$, so the curve is invariant; it is the stable manifold, tangent to $E^s$, while the unstable manifold is the $y$-axis.
Hyperbolicity is needed: for $x' = x^2$, $y' = -y$, the set of points that tend to the origin is the closed half-plane $x \le 0$, which is not a curve.

## Explanations

### L1 human

Near a saddle point, the points that flow into the saddle form a smooth surface, and the points that come out of it form another.
These surfaces are curved copies of the flat stable and unstable directions of the linearised system.

### L2 human

The theorem is the nonlinear version of the splitting of $\R^n$ into $E^s \oplus E^u$ for a linear system.
Together with the [[Hartman–Grobman theorem|0S8WX8A4V9]], it gives the local picture near a hyperbolic equilibrium.
Stable and unstable manifolds organise the global phase portrait: their intersections give homoclinic and heteroclinic orbits.
The same result holds for hyperbolic fixed points of diffeomorphisms and for hyperbolic periodic orbits.
