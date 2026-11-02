---
tag: PDP7CHN4B4
kind: definition
name: Displacement convexity
msc: [49Q22, 52A41, 35K55]
defines: N05WC9ZCWA
uses: [CVQVBMHH4X, 3N66TM3TSQ, P0P21KDV6E, 07Q7CNM5WF]
sources:
  - url: https://en.wikipedia.org/wiki/Wasserstein_metric
---

## Definition

Let $\mathcal{P}_2^{\mathrm{ac}}(\R^n)$ be the set of Borel probability measures on $\R^n$ with finite second moment that are [[absolutely continuous|P0P21KDV6E]] with respect to Lebesgue measure.
For $\mu_0, \mu_1 \in \mathcal{P}_2^{\mathrm{ac}}(\R^n)$, let $\nabla \varphi$ be the optimal map from $\mu_0$ to $\mu_1$ given by [[Brenier's theorem|CVQVBMHH4X]].
The *displacement interpolation* between them is the curve
$$\mu_t = \left( (1 - t) \id + t \nabla \varphi \right)_\# \mu_0, \qquad t \in [0, 1],$$
where $_\#$ denotes the [[pushforward|3N66TM3TSQ]].
A functional $F \colon \mathcal{P}_2^{\mathrm{ac}}(\R^n) \to (-\infty, +\infty]$ is *displacement convex* if, for all $\mu_0, \mu_1 \in \mathcal{P}_2^{\mathrm{ac}}(\R^n)$, the function $t \mapsto F(\mu_t)$ is convex on $[0, 1]$.

## Remarks

Example: let $V \colon \R^n \to \R$ be [[convex|07Q7CNM5WF]] and $F(\mu) = \int V \, d\mu$.
Then $F(\mu_t) = \int V\big((1 - t) x + t \nabla \varphi(x)\big) \, d\mu_0(x)$, and the integrand is convex in $t$ for each $x$, so $F$ is displacement convex.

Non-example: on $\R$, let $V(x) = -x^2$, let $\mu_0$ be uniform on $[0, 1]$ and $\mu_1$ uniform on $[2, 3]$.
The optimal map is $x \mapsto x + 2$, so $\mu_t$ is uniform on $[2t, 2t + 1]$ and $F(\mu_t) = -\int_0^1 (x + 2t)^2 \, dx = -\left(\tfrac13 + 2t + 4t^2\right)$, which is strictly concave in $t$.

The interpolation $\mu_t$ is a constant-speed geodesic for the Wasserstein distance $W_2$, so displacement convexity is convexity along $W_2$-geodesics.
The functional $F$ is *$\lambda$-displacement convex*, for a real $\lambda$, if $t \mapsto F(\mu_t) - \frac{\lambda}{2} t^2 W_2(\mu_0, \mu_1)^2$ is convex.
McCann showed that the entropy $\int \rho \log \rho \, dx$ of a density $\rho$ is displacement convex on $\R^n$.
The interaction energy $\iint W(x - y) \, d\mu(x) \, d\mu(y)$ with $W$ convex is also displacement convex.
It need not be convex in the usual sense: for $W(z) = \abs{z}^2$ it equals twice the variance of $\mu$, which is concave under mixtures $(1 - t)\mu_0 + t\mu_1$.
