---
tag: DVA7AZ0HDJ
kind: definition
name: Optimal control of partial differential equations
msc: [49J20, 49K20, 93C20]
defines: S2BBZPAFDR
uses: [T3V6ZNAMDN, GC5BDZ6QBC, 06GZ956657, 02AS45T3H9, M4CEZ5K9HP]
sources:
  - url: https://en.wikipedia.org/wiki/PDE-constrained_optimization
---

## Definition

Let $Y$, $Z$ and $V$ be real [[Banach spaces|06GZ956657]], called the state space, the target space of the equation, and the control space.
Let $e \colon Y \times V \to Z$ be a map that encodes a [[partial differential equation|GC5BDZ6QBC]] with its boundary conditions.
Thus $e(y, u) = 0$ means that $y$ solves the equation with control $u$.
Let $V_{\mathrm{ad}} \subseteq V$ be a nonempty set of admissible controls, and let $J \colon Y \times V \to \R$ be a cost functional.
An *optimal control problem for a partial differential equation* is the problem
$$\text{minimize } J(y, u) \quad \text{subject to } e(y, u) = 0, \; u \in V_{\mathrm{ad}}.$$
A pair $(y^*, u^*)$ with $e(y^*, u^*) = 0$ and $u^* \in V_{\mathrm{ad}}$ is *optimal* if $J(y^*, u^*) \le J(y, u)$ for all such pairs $(y, u)$.

## Remarks

Example: let $\Omega \subseteq \R^d$ be a bounded open set, let $y_d \in L^2(\Omega)$, $\alpha > 0$ and $a < b$.
Minimize $\frac12 \norm{y - y_d}_{L^2(\Omega)}^2 + \frac{\alpha}{2} \norm{u}_{L^2(\Omega)}^2$ over $u \in L^2(\Omega)$ with $a \le u \le b$ almost everywhere, where $y \in H^1_0(\Omega)$ is the weak solution of $-\Delta y = u$ in $\Omega$, $y = 0$ on $\partial \Omega$.
This fits the definition with $Y = H^1_0(\Omega)$, $V = L^2(\Omega)$, $Z = H^{-1}(\Omega)$ and $e(y, u) = -\Delta y - u$.
Here the problem has a unique solution, because the control-to-state map is linear and bounded.
So the reduced cost is strictly [[convex|02AS45T3H9]], continuous and coercive on the closed convex set $V_{\mathrm{ad}}$.
Non-example: if the state equation is an ordinary differential equation in $\R^n$, the problem is an ordinary [[optimal control|T3V6ZNAMDN]] problem, not one for a partial differential equation.
When $e(y, u) = 0$ has a unique solution $y = S(u)$ for each $u$, the problem reduces to minimizing $f(u) = J(S(u), u)$ over $V_{\mathrm{ad}}$.
