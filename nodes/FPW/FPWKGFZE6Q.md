---
tag: FPWKGFZE6Q
kind: statement
role: lemma
name: Hopf lemma
msc: [35B50, 35J15]
uses: [D2JF19HF91, XY8GEQSWPR]
about: [XY8GEQSWPR]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_lemma
same_as:
  wikidata: Q17027555
  wikipedia: Hopf lemma
---

## Statement

Let $U \subseteq \R^n$ be open, and let
$$L u = \sum_{i,j=1}^{n} a_{ij}(x) \, \partial_i \partial_j u + \sum_{i=1}^{n} b_i(x) \, \partial_i u$$
have bounded coefficients on $U$, with $a_{ij} = a_{ji}$ and $\sum_{i,j} a_{ij}(x) \xi_i \xi_j \ge \theta \abs{\xi}^2$ for some $\theta > 0$ and all $x \in U$, $\xi \in \R^n$.
Let $x_0 \in \partial U$, and assume the interior ball condition at $x_0$: there is an open ball $B \subseteq U$ with $x_0 \in \partial B$.
Let $\nu$ be the outer unit normal of $B$ at $x_0$.
Let $u$ be twice continuously differentiable on $U$ and continuous at $x_0$ on $U \cup \set{x_0}$, with $L u \ge 0$ in $U$ and $u(x) < u(x_0)$ for all $x \in U$.
If the one-sided derivative $\frac{\partial u}{\partial \nu}(x_0) = \lim_{t \to 0^+} \frac{u(x_0) - u(x_0 - t \nu)}{t}$ exists, then
$$\frac{\partial u}{\partial \nu}(x_0) > 0.$$

## Remarks

Proof idea: let $B$ have centre $y$ and radius $R$, and set $v(x) = e^{-\lambda \abs{x - y}^2} - e^{-\lambda R^2}$.
For $\lambda$ large, $L v > 0$ on the annulus $A = \set{R/2 < \abs{x - y} < R}$, and $v = 0$ on the outer sphere.
For small $\varepsilon > 0$, the function $u - u(x_0) + \varepsilon v$ satisfies $L(\cdot) \ge 0$ in $A$ and is at most $0$ on $\partial A$, so it is at most $0$ in $A$ by the weak [[maximum principle|D2JF19HF91]].
At $x_0$ this gives $\frac{\partial u}{\partial \nu}(x_0) \ge -\varepsilon \frac{\partial v}{\partial \nu}(x_0) = 2 \varepsilon \lambda R e^{-\lambda R^2} > 0$.

The interior ball condition is needed.
Let $U$ be the part of the unit disc in the first quadrant, $x_0 = 0$ and $u(x, y) = -xy$.
Then $\Delta u = 0$ and $u < 0 = u(x_0)$ in $U$, but $\nabla u(0) = 0$, so every directional derivative at $0$ vanishes.
At the corner $0$ there is no ball inside $U$ touching $0$.

## Explanations

### L1 human

At a boundary point where a solution of an elliptic equation reaches a strict maximum, the solution cannot approach that value flatly.
It must rise towards the boundary with a strictly positive slope in the normal direction.
For a temperature in equilibrium, the hottest boundary point actually sends heat into the region.

### L2 human

The Hopf lemma is the step that turns the weak maximum principle into the strong one.
If an interior maximum occurred, one would find a small ball touching the set where the maximum is attained.
The lemma would then give a nonzero gradient at a maximum point, which is impossible.
It also gives uniqueness up to constants for the Neumann problem, and it is a basic tool in the moving plane method for proving symmetry of solutions.
The smoothness of the boundary in the form of the interior ball condition holds, for example, for every bounded open set with $C^2$ boundary.
