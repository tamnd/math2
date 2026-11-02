---
tag: 6QS7X5GVMY
kind: problem
name: Variational inequality
msc: [47J20, 49J40]
uses: [HM2HHE3J51, 02AS45T3H9, Y1M03JQKKR, 86KRHS6X22]
about: [02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Variational_inequality
same_as:
  wikidata: Q4556320
  wikipedia: Variational inequality
history:
  posed_by: "Antonio Signorini"
---

## Problem

Let $H$ be a real [[Hilbert space|HM2HHE3J51]] with inner product $\ip{\cdot}{\cdot}$.
Let $K \subseteq H$ be a nonempty closed [[convex set|02AS45T3H9]], and let $F \colon K \to H$ be a map.
Find $u \in K$ such that
$$\ip{F(u)}{v - u} \ge 0 \quad \text{for all } v \in K.$$

## Remarks

If $K = H$, then taking $v = u \pm w$ shows that the inequality holds exactly when $F(u) = 0$, so the problem contains the equation $F(u) = 0$.
If $F = \nabla f$ for a convex differentiable function $f$, then $u$ solves the problem exactly when $u$ minimizes $f$ on $K$.
Stampacchia's theorem treats the linear case.
Let $a$ be a bounded [[coercive bilinear form|86KRHS6X22]] on $H$ and let $\ell$ be a continuous linear functional on $H$.
Then there is exactly one $u \in K$ with $a(u, v - u) \ge \ell(v - u)$ for all $v \in K$.
When $a$ is symmetric, this $u$ minimizes $\tfrac12 a(v, v) - \ell(v)$ over $K$.
For $H = \R^n$, $K$ compact and $F$ continuous, a solution always exists, by the Hartman–Stampacchia theorem, whose proof uses the Brouwer fixed point theorem.
For a continuous [[monotone|Y1M03JQKKR]] $F$ the solution set is closed and convex, and a strictly monotone $F$ has at most one solution.

## Explanations

### L1 human

A variational inequality describes an equilibrium under a constraint.
Think of a ball resting on a curved surface inside a box.
If the lowest point lies inside the box, the force there vanishes; if it lies on a wall, the force need not vanish but must push into the wall.
The inequality $\ip{F(u)}{v - u} \ge 0$ says exactly this: from $u$, no allowed direction $v - u$ goes "downhill".
Obstacle problems in elasticity, contact problems and many equilibrium models in economics take this form.
