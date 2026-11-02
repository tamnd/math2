---
tag: 2XYQRM1NFH
kind: statement
role: theorem
name: Benamou–Brenier formula
msc: [49Q22, 35Q49, 28A33]
uses: [VEY29CS26X, 059TJN0NZ1]
about: [VEY29CS26X]
sources:
  - url: https://en.wikipedia.org/wiki/Wasserstein_metric
---

## Statement

Let $\mathcal{P}_2(\R^n)$ be the set of Borel [[probability measures|059TJN0NZ1]] on $\R^n$ with finite second moment.
Let $W_2$ be the [[Wasserstein distance|VEY29CS26X]] of order $2$ on it.
Let $\mu_0, \mu_1 \in \mathcal{P}_2(\R^n)$.
Consider pairs $(\mu_t, v_t)_{t \in [0, 1]}$ such that:

1. $t \mapsto \mu_t$ is a weakly continuous curve in $\mathcal{P}_2(\R^n)$ from $\mu_0$ to $\mu_1$;
2. $(t, x) \mapsto v_t(x) \in \R^n$ is a Borel vector field with $\int_0^1 \int \abs{v_t}^2 \, d\mu_t \, dt < \infty$;
3. the continuity equation $\partial_t \mu_t + \operatorname{div}(v_t \mu_t) = 0$ holds in the sense of distributions on $(0, 1) \times \R^n$.

Then
$$W_2(\mu_0, \mu_1)^2 = \inf \int_0^1 \int_{\R^n} \abs{v_t(x)}^2 \, d\mu_t(x) \, dt,$$
where the infimum runs over all such pairs, and it is attained.

## Remarks

Jean-David Benamou and Yann Brenier introduced the formula in 2000, as a basis for numerical computation of optimal transport.
To see that the infimum is at most $W_2(\mu_0, \mu_1)^2$, take an optimal coupling $\pi$ and move mass along straight lines.
So $\mu_t$ is the image of $\pi$ under $(x, y) \mapsto (1 - t) x + t y$, and the velocity of each particle is $y - x$.
The energy is then $\int \abs{x - y}^2 \, d\pi = W_2(\mu_0, \mu_1)^2$.
For the other inequality, note that a curve with velocity field $v$ is the image of the flow of $v$.
Jensen's inequality then bounds the cost of the induced coupling by the kinetic energy.
Example: for $\mu_0 = \delta_a$ and $\mu_1 = \delta_b$, the curve $\mu_t = \delta_{(1 - t)a + tb}$ with constant velocity $b - a$ has energy $\abs{b - a}^2 = W_2(\delta_a, \delta_b)^2$.
In the substitution $m_t = v_t \mu_t$ the problem becomes convex in $(\mu, m)$, which is what makes it useful for computation.

## Explanations

### L1 human

The Wasserstein distance measures the cost of moving one distribution of mass onto another.
The Benamou–Brenier formula says that this cost is the least kinetic energy of a flow of mass that carries the first distribution to the second in unit time.
So the static problem of matching points becomes a dynamic problem of moving a fluid.

### L2 human

The formula shows that $(\mathcal{P}_2(\R^n), W_2)$ behaves like a Riemannian manifold, in Otto's formal calculus: tangent vectors are velocity fields, and the squared length of a tangent vector is $\int \abs{v}^2 \, d\mu$.
Optimal curves are the displacement interpolations, along which displacement convexity is measured.
The same structure underlies the interpretation of the heat and Fokker–Planck equations as gradient flows, as in the Jordan–Kinderlehrer–Otto scheme.
