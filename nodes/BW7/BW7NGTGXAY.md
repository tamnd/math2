---
tag: BW7NGTGXAY
kind: definition
name: Melnikov method
msc: [34C37, 34C28]
defines: A755BDRP1A
uses: [0EDKGA2FAK, 0C5PREPZWG, 6DBSQKZK4W, 0ATF6Q0633]
sources:
  - url: https://en.wikipedia.org/wiki/Melnikov_distance
---

## Definition

Let $H \colon \R^2 \to \R$ be smooth and let $f = (\partial H / \partial y, -\partial H / \partial x)$, so that $u' = f(u)$ is a planar [[Hamiltonian system|0EDKGA2FAK]].
Let $p$ be a [[hyperbolic|0C5PREPZWG]] saddle of this system, and let $q_0(t)$ be a solution whose orbit is a [[homoclinic orbit|6DBSQKZK4W]] of $p$.
Let $g \colon \R^2 \times \R \to \R^2$ be smooth and [[periodic|0ATF6Q0633]] of period $T > 0$ in its last variable.
Consider the perturbed system
$$u' = f(u) + \varepsilon\, g(u, t), \qquad \varepsilon \text{ small}.$$
For $a, b \in \R^2$ put $a \wedge b = a_1 b_2 - a_2 b_1$.
The *Melnikov function* of the perturbation along $q_0$ is
$$M(t_0) = \int_{-\infty}^{\infty} f(q_0(t)) \wedge g\big(q_0(t), t + t_0\big)\, dt, \qquad t_0 \in \R.$$
The *Melnikov method* is the study of the perturbed system through the zeros of $M$.

## Remarks

The integral converges because $f(q_0(t)) \to f(p) = 0$ exponentially fast as $t \to \pm\infty$.
The function $M$ is $T$-periodic in $t_0$.
For small $\varepsilon$, the perturbed system has a hyperbolic periodic orbit near $p$.
The distance between its stable and unstable manifolds, measured along the normal to the unperturbed loop at $q_0(0)$, is $\varepsilon M(t_0) / \norm{f(q_0(0))} + O(\varepsilon^2)$, with a suitable sign convention.
The basic theorem says: if $M$ has a simple zero, then for small $\varepsilon \ne 0$ these manifolds intersect transversally; if $M$ has no zero, they do not intersect.

Example: for $H = \frac{1}{2} y^2 - \frac{1}{2} x^2 + \frac{1}{4} x^4$ and $g = (0, -\delta y + \gamma \cos(\omega t))$, the system is the damped, forced Duffing equation.
Here $q_0(t) = (\sqrt{2} \operatorname{sech} t, -\sqrt{2} \operatorname{sech} t \tanh t)$, and a direct computation gives $M(t_0) = -\frac{4}{3} \delta + c\, \gamma \sin(\omega t_0)$ with a constant $c$ that depends only on $\omega$.

Non-example: if $g(u, t) = (0, t)$, then $g$ is not periodic in $t$.
The perturbed system is then not periodic in time, there is no Poincaré map of period $T$, and the theorem above does not apply.
