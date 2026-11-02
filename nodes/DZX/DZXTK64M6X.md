---
tag: DZXTK64M6X
kind: statement
role: theorem
name: Fenichel's theorem
msc: ["34E15", 34C45, 34D15]
uses: [0NT64JV96A, 0BQAA2BK3Q, WWZTW11664, G6J21TGRMM]
about: [G6J21TGRMM]
sources:
  - url: https://en.wikipedia.org/wiki/Slow_manifold
---

## Statement

Let $r \ge 1$ be an integer, and let $f \colon \R^n \times \R^m \times \R \to \R^n$ and $g \colon \R^n \times \R^m \times \R \to \R^m$ be of class $C^{r+1}$.
Consider the [[singularly perturbed|G6J21TGRMM]] slow-fast system of [[ordinary differential equations|0NT64JV96A]]
$$\dot x = f(x, y, \varepsilon), \quad \varepsilon \dot y = g(x, y, \varepsilon).$$
Let $K \subseteq \R^n$ be a compact set that is the closure of an open set with smooth boundary.
Let $h_0 \colon K \to \R^m$ be of class $C^{r+1}$ with $g(x, h_0(x), 0) = 0$ for all $x \in K$.
So $M_0 = \set{(x, h_0(x)) : x \in K}$ is part of the *critical manifold* $\set{g = 0}$.
Assume that $M_0$ is *normally hyperbolic*: for each $x \in K$, no [[eigenvalue|0BQAA2BK3Q]] of $\partial_y g(x, h_0(x), 0)$ has real part $0$.
Then there is $\varepsilon_1 > 0$ such that for $0 < \varepsilon \le \varepsilon_1$ there is a $C^r$ function $h_\varepsilon \colon K \to \R^m$ with these properties.

1. The *slow manifold* $M_\varepsilon = \set{(x, h_\varepsilon(x)) : x \in K}$ is locally [[invariant|WWZTW11664]].
   A solution that starts on $M_\varepsilon$ stays on it as long as $x$ remains in the interior of $K$.
2. $h_\varepsilon$ depends in a $C^r$ way on $\varepsilon$, and $h_\varepsilon = h_0 + O(\varepsilon)$ uniformly on $K$.
3. Suppose that along $M_0$, the matrix $\partial_y g$ has $k$ eigenvalues with negative and $m - k$ with positive real part.
   Then $M_\varepsilon$ has local stable and unstable manifolds of dimensions $n + k$ and $n + m - k$.
   They are $O(\varepsilon)$-close to the stable and unstable manifolds of $M_0$ for the fast system at $\varepsilon = 0$.

## Remarks

At $\varepsilon = 0$, every point of $M_0$ is an equilibrium of the fast system $y' = g(x, y, 0)$, where the prime is the derivative in $\tau = t / \varepsilon$.
Normal hyperbolicity means that the contraction or expansion transverse to $M_0$ dominates the dynamics along $M_0$.
The proof applies the persistence theory of normally hyperbolic invariant manifolds, developed by Fenichel, to the system in the fast time with $\varepsilon$ added as a variable.

Example: for $\dot x = -x$, $\varepsilon \dot y = -y + x^2$, the critical manifold is $y = x^2$, normally attracting since $\partial_y g = -1$.
One checks that $y = h_\varepsilon(x) = x^2 / (1 - 2\varepsilon)$ is invariant for $\varepsilon < 1/2$: along it $\varepsilon \dot y = -2\varepsilon x^2 / (1 - 2\varepsilon) = -y + x^2$.
So $h_\varepsilon = x^2 + O(\varepsilon)$, as the theorem predicts.

Normal hyperbolicity is needed: at fold points, where an eigenvalue of $\partial_y g$ crosses $0$, the slow manifold can fail to continue, as in relaxation oscillations and canard phenomena.
The slow manifold is in general not unique, but any two choices are exponentially close in $1/\varepsilon$.

## Explanations

### L1 human

When a system has fast and slow parts, the fast part quickly settles near a surface of rest points.
Fenichel's theorem says that, for a small but positive speed ratio, there is a true surface nearby that the motion follows exactly.
On that surface, the system can be studied with fewer variables.

### L2 human

The theorem is the foundation of geometric singular perturbation theory.
It complements [[Tikhonov's theorem|8X8Y61MGHW]], which gives convergence on finite time intervals.
On the slow manifold, the flow is a regular perturbation of the reduced flow $\dot x = f(x, h_0(x), 0)$.
Combined with the stable and unstable fibrations, it is used to construct travelling waves and periodic orbits of relaxation type.
