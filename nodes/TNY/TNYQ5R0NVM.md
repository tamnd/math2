---
tag: TNYQ5R0NVM
kind: statement
role: theorem
name: Fundamental theorem of space curves
msc: [53A04]
uses: [7JQS6VKFEZ, S4BZ697DSH, 00R1JDDV5X, 0H3YY8CPKH, ZM6W89YNS7]
about: [7JQS6VKFEZ, S4BZ697DSH]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_curves
same_as:
  wikidata: Q57486
  wikipedia: Fundamental theorem of curves
---

## Statement

Let $I \subseteq \R$ be an open interval, and let $\kappa \colon I \to \R$ and $\tau \colon I \to \R$ be smooth functions with $\kappa(s) > 0$ for all $s \in I$.
Then there is a smooth curve $\gamma \colon I \to \R^3$ parametrised by [[arc length|00R1JDDV5X]] whose [[curvature|7JQS6VKFEZ]] is $\kappa$ and whose [[torsion|S4BZ697DSH]] is $\tau$.
If $\tilde\gamma \colon I \to \R^3$ is another such curve, then $\tilde\gamma = \rho \circ \gamma$ for a unique orientation-preserving rigid motion $\rho$ of $\R^3$.
Here a rigid motion is a map $x \mapsto Rx + b$ with $R$ a rotation matrix and $b \in \R^3$.

## Remarks

For existence, solve the [[Frenet–Serret formulas|ZM6W89YNS7]] as a linear system of ordinary differential equations for $(T, N, B)$, with an orthonormal positive initial frame at some $s_0 \in I$.
The solution stays orthonormal because the coefficient matrix is skew-symmetric; then set $\gamma(s) = \int_{s_0}^s T(u) \, du$.
For uniqueness, move $\tilde\gamma$ by a rigid motion so that both curves have the same point and frame at $s_0$.
Then the uniqueness of solutions of the linear system gives equal frames and equal curves.
Example: constant $\kappa = a/(a^2+b^2)$ and $\tau = b/(a^2+b^2)$ with $a > 0$ give exactly the helices $(a \cos t, a \sin t, bt)$, $t = s / \sqrt{a^2 + b^2}$, up to rigid motion.
The hypothesis $\kappa > 0$ matters: if $\kappa$ vanishes on an interval, the torsion is not defined there and the curve is not determined by $\kappa$ alone.
An orientation-reversing motion, such as a reflection, changes the sign of $\tau$, so it does not keep the torsion.

## Explanations

### L1 human

If you know at each moment how sharply a curve bends and how much it twists, you know the curve.
The only freedom left is where you place it in space and which way you point it.
This is like following driving instructions: "turn this much, climb this much" fixes the route once the start is given.

### L2 human

The theorem says that $(\kappa, \tau)$ is a complete system of invariants of unit-speed space curves with positive curvature.
The symmetry group here is the group of orientation-preserving rigid motions, a subgroup of the [[Euclidean group|0H3YY8CPKH]].
For plane curves the analogue is simpler: the signed curvature determines a unit-speed curve up to orientation-preserving rigid motion, through $\theta' = k$ and $\gamma' = (\cos \theta, \sin \theta)$.
The same idea, a frame solving a linear system, reappears in the theory of surfaces, where the Gauss–Codazzi equations are the integrability conditions.
