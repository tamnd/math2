---
tag: 36WNFJTRRR
kind: statement
role: theorem
name: Sacks–Uhlenbeck bubbling
msc: ["58E20", 53C43]
uses: [KZJYG9DS3M, E6HDE1DFXD, 5K0N8QMV6Q, 7CBT4SM83Y, AP4A0GX0V2]
about: [KZJYG9DS3M]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_map
---

## Statement

Let $(M, g)$ be a closed [[Riemann surface|5K0N8QMV6Q]] with a conformal metric, and let $(N, h)$ be a compact [[Riemannian manifold|7CBT4SM83Y]].
Let $u_k \colon M \to N$ be a sequence of [[harmonic maps|KZJYG9DS3M]] whose [[energies|E6HDE1DFXD]] $E(u_k)$ are bounded by a constant $C$.
Then there are a subsequence, still written $u_k$, a finite set $S \subset M$ and a harmonic map $u_\infty \colon M \to N$ with these properties.

1. The maps $u_k$ converge to $u_\infty$ in $C^\infty$ on compact subsets of $M \setminus S$.
2. For each $p \in S$ there are points $x_k \to p$ and radii $r_k \to 0$ with the following property.
The rescaled maps $v_k(y) = u_k(\exp_{x_k}(r_k y))$, defined on growing discs in $\R^2$, converge in $C^\infty$ on compact subsets of $\R^2$.
Their limit is a nonconstant harmonic map $v \colon \R^2 \to N$.
3. Each such limit $v$ has finite energy and extends to a nonconstant harmonic map $S^2 \to N$.

## Remarks

The key input is an $\varepsilon$-regularity estimate.
There is $\varepsilon > 0$ such that a harmonic map with energy less than $\varepsilon$ on a disc has all its derivatives bounded on the half disc.
Since the total energy is at most $C$, energy at least $\varepsilon$ can concentrate at no more than $C / \varepsilon$ points, and these points form $S$.
Near a point of $S$ one rescales the maps so that the concentrating energy stays visible, and the limit is a harmonic map on the plane.
Its extension to $S^2$ uses the removable singularity theorem for harmonic maps of finite energy on a punctured disc.
The energy of a map from a surface does not change under conformal changes of the domain, and this scale invariance is why bubbles can form.

If $N$ carries no nonconstant harmonic map $S^2 \to N$, then $S$ is empty and the convergence is smooth on all of $M$.
This happens, for example, when $N$ has nonpositive sectional curvature, since then every harmonic map from $S^2$ to $N$ is constant.
Sacks and Uhlenbeck used this analysis, for a perturbed energy, to show that every homotopy class of maps $M \to N$ contains a harmonic map when $\pi_2(N) = 0$.

## Explanations

### L1 human

Harmonic maps from a surface are like rubber sheets in equilibrium inside a curved space.
If the sheets in a sequence have bounded total stretching, most of each sheet settles down to a limit.
At a few points, however, a tiny piece of a sheet can wrap around a whole sphere inside the target and pinch off.
These pinched-off spheres are the bubbles.
The theorem says that this is the only thing that can go wrong.

### L2 human

The theorem is the prototype of compactness up to bubbling.
The same pattern reappears for pseudoholomorphic curves, for Yang–Mills connections in dimension four and for many other conformally invariant problems.
It explains why the existence theory for harmonic maps of surfaces depends on the second homotopy group of the target.
Compare with the [[Eells–Sampson theorem|AP4A0GX0V2]], where nonpositive curvature of the target rules out bubbles and the heat flow converges.
