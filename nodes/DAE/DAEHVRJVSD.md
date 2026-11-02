---
tag: DAEHVRJVSD
kind: statement
role: theorem
name: Transversality conditions for variable endpoints
msc: [49K05]
uses: [JRQZ803Q5Y, PS0VV149ET, 5B8NFYB2XQ, QTRPNFDFJ8, 09EGC6F8PT]
about: [PS0VV149ET, QTRPNFDFJ8]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_variations
---

## Statement

Let $L \colon \R \times \R \times \R \to \R$, written $L(x, z, p)$, be of class $C^2$, with [[partial derivative|09EGC6F8PT]] $L_p$ in $p$.
Let $\psi \colon \R \to \R$ be of class $C^1$, and fix $a, A \in \R$.
Consider pairs $(y, b)$ with $b > a$, $y \in C^2([a, b])$, $y(a) = A$ and $y(b) = \psi(b)$, and set $J(y, b) = \int_a^b L(x, y, y') \, dx$.
Suppose that $(y_0, b_0)$ minimises $J$ among all such pairs.
Then:

1. $y_0$ solves the [[Euler–Lagrange equation|PS0VV149ET]] $\frac{d}{dx} L_p(x, y_0, y_0') = L_z(x, y_0, y_0')$ on $[a, b_0]$;
2. at the free end, the *transversality condition*
$$\Big[ L(x, y_0, y_0') + \big(\psi'(x) - y_0'(x)\big) L_p(x, y_0, y_0') \Big]_{x = b_0} = 0$$
holds.

## Remarks

The proof computes the [[first variation|5B8NFYB2XQ]] of $J$ along a family $(y_t, b_t)$ of competitors with $y_t(b_t) = \psi(b_t)$.
Variations that fix both ends give the Euler–Lagrange equation.
Moving the end along the curve $y = \psi(x)$ gives a boundary term, $L \, \delta b + L_p (\delta y - y' \delta b)$ at $b_0$, with $\delta y = \psi' \delta b$; it must vanish, which is the transversality condition.

Special cases.
If instead $b$ is fixed and $y(b)$ is free, the end moves on the vertical line $x = b$, and the same computation gives the [[natural boundary condition|QTRPNFDFJ8]] $L_p = 0$ at $b$.
If $L(x, z, p) = f(x, z) \sqrt{1 + p^2}$ with $f(b_0, y_0(b_0)) \ne 0$, the condition simplifies to $\psi'(b_0) \, y_0'(b_0) = -1$: the extremal meets the curve $y = \psi(x)$ at a right angle.

Example: for $f = 1$, $J$ is arc length, and the condition says that the shortest segment from the point $(a, A)$ to a curve meets the curve orthogonally.

## Explanations

### L1 human

When the end of a curve may slide along a given line or curve, the best curve must meet that curve in a special way.
For the shortest path from a point to a curve, the special way is a right angle.
For other functionals, the angle is fixed by a formula involving the integrand.

### L2 human

The transversality condition replaces the missing boundary value.
The Euler–Lagrange equation has order two and one end is fixed, so one more condition fixes the extremal; then $y(b_0) = \psi(b_0)$ fixes the unknown $b_0$.
In optimal control, the [[Pontryagin maximum principle|7RPV2T29CF]] has transversality conditions of the same kind on the costate at a free final state or final time.
