---
tag: 8X8Y61MGHW
kind: statement
role: theorem
name: Tikhonov's theorem on slow-fast systems
msc: ["34E15", 34D15]
uses: [0NT64JV96A, 0FXDW992DS, 0N8NGKDZDZ, 0NB689782W, G6J21TGRMM, YCFPD0GE5G]
about: [G6J21TGRMM]
sources:
  - url: https://en.wikipedia.org/wiki/Tikhonov%27s_theorem_(dynamical_systems)
same_as:
  wikidata: Q7801912
  wikipedia: Tikhonov's theorem (dynamical systems)
---

## Statement

Let $f \colon \R^n \times \R^m \to \R^n$ and $g \colon \R^n \times \R^m \to \R^m$ be continuously differentiable.
For $\varepsilon > 0$ consider the [[singularly perturbed|G6J21TGRMM]] [[initial value problem|0FXDW992DS]] for a system of [[ordinary differential equations|0NT64JV96A]]
$$\dot x = f(x, y), \quad \varepsilon \dot y = g(x, y), \quad x(0) = x^0, \quad y(0) = y^0.$$
Let $T > 0$, and assume the following.

1. There are an open set $U \subseteq \R^n$ and a continuously differentiable $\varphi \colon U \to \R^m$ with $g(x, \varphi(x)) = 0$ for all $x \in U$.
2. For each $x \in U$, all eigenvalues of the matrix $\partial_y g(x, \varphi(x))$ have negative real part.
3. The *reduced problem* $\dot{\bar x} = f(\bar x, \varphi(\bar x))$, $\bar x(0) = x^0$, has a solution $\bar x$ on $[0, T]$ with values in $U$.
4. The solution of the *boundary layer problem* $\frac{d\hat y}{d\tau} = g(x^0, \hat y)$, $\hat y(0) = y^0$, exists for all $\tau \ge 0$ and tends to $\varphi(x^0)$ as $\tau \to \infty$.

Then there is $\varepsilon_1 > 0$ such that for $0 < \varepsilon < \varepsilon_1$ the solution $(x_\varepsilon, y_\varepsilon)$ exists on $[0, T]$.
Moreover, as $\varepsilon \to 0$, $x_\varepsilon \to \bar x$ uniformly on $[0, T]$, and $y_\varepsilon \to \varphi(\bar x)$ uniformly on $[t_0, T]$ for every $t_0 \in (0, T]$.

## Remarks

In the fast time $\tau = t / \varepsilon$, the variable $x$ hardly moves, and $y$ follows the boundary layer equation, in which $\varphi(x)$ is an [[asymptotically stable|0NB689782W]] [[equilibrium point|0N8NGKDZDZ]] by hypothesis 2.
So $y$ first jumps quickly to near the slow manifold $y = \varphi(x)$, and then the system moves slowly along it according to the reduced problem.
The proof turns this into estimates with a Lyapunov function for the fast subsystem, uniform in $x$ on a compact neighbourhood of the reduced trajectory.

Example: $\dot x = -x + y$, $\varepsilon \dot y = x - 2y$, with $x(0) = 1$, $y(0) = 5$.
Here $\varphi(x) = x / 2$ and $\partial_y g = -2 < 0$, and the reduced problem $\dot{\bar x} = -\bar x / 2$ gives $\bar x(t) = e^{-t/2}$.
The theorem gives $x_\varepsilon(t) \to e^{-t/2}$ and $y_\varepsilon(t) \to e^{-t/2} / 2$ for $t > 0$, while $y_\varepsilon(0) = 5$, so $y$ has a [[boundary layer|YCFPD0GE5G]] at $t = 0$.

Stability of the slow manifold is needed.
For $\dot x = 0$, $\varepsilon \dot y = y$ with $y(0) = y^0 \neq 0$, the root is $\varphi = 0$ but $\partial_y g = 1 > 0$, and $y_\varepsilon(t) = y^0 e^{t/\varepsilon}$ does not converge.

## Explanations

### L1 human

Some systems have a fast part and a slow part.
If the fast part always settles quickly to a rest state, one can replace it by that rest state and only study the slow part.
The theorem says this replacement gives the right answer as the speed gap becomes infinite, except for a short initial jump.

### L2 human

Tikhonov's theorem justifies the quasi-steady-state approximation of chemical kinetics, such as the Michaelis–Menten law in enzyme kinetics.
It is a result on finite time intervals; Fenichel's theorem, the basis of geometric singular perturbation theory, gives the invariant slow manifold for $\varepsilon > 0$.
The approximation can be refined to all orders by the method of matched asymptotic expansions, under extra smoothness.
