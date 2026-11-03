---
tag: PPHFS2P4G4
kind: statement
role: theorem
name: Friedmann equations
msc: ["83F05", "83C05"]
uses: [Q8MSCRDFAT, ECJMS4VDTF, J70F32P86W, 3MCZ97SW6V, H4FNPG6ZY1, WVKKDY9V61]
about: [J70F32P86W, ECJMS4VDTF]
sources:
  - url: https://en.wikipedia.org/wiki/Friedmann_equations
same_as:
  wikidata: Q467736
  wikipedia: Friedmann equations
---

## Statement

Use units with $c = 1$, and let $G$ be Newton's constant and $\Lambda \in \R$ a [[cosmological constant|WVKKDY9V61]].
Let $g = -dt^2 + a(t)^2 \gamma_k$ be a [[Friedmann–Lemaître–Robertson–Walker metric|ECJMS4VDTF]] on $I \times \Sigma$, where $\gamma_k$ has constant sectional curvature $k$ and $a$ is the [[scale factor|J70F32P86W]].
Let the matter be a [[perfect fluid|H4FNPG6ZY1]] at rest in the comoving frame, with energy density $\rho(t)$ and pressure $p(t)$, so $T = (\rho + p)\, dt \otimes dt + p\, g$.
Then $g$ satisfies the [[Einstein field equations|3MCZ97SW6V]] $G_{ab} + \Lambda g_{ab} = 8\pi G\, T_{ab}$ if and only if, on $I$,

1. the expansion equation $$\left( \frac{\dot a}{a} \right)^2 = \frac{8\pi G}{3}\rho - \frac{k}{a^2} + \frac{\Lambda}{3},$$
2. the acceleration equation $$\frac{\ddot a}{a} = -\frac{4\pi G}{3}(\rho + 3p) + \frac{\Lambda}{3}.$$

As a consequence, the continuity equation $\dot\rho + 3 \frac{\dot a}{a} (\rho + p) = 0$ holds on $I$.

## Remarks

The proof is a computation of the Einstein tensor of $g$.
In the comoving frame its only nonzero components are $G^t{}_t = -3(\dot a^2 + k)/a^2$ and $G^i{}_j = -\left( 2\ddot a/a + (\dot a^2 + k)/a^2 \right) \delta^i{}_j$.
The time-time component gives the expansion equation.
The space-space components, combined with the expansion equation, give the acceleration equation.
The continuity equation is the conservation law $\nabla_a T^{ab} = 0$, which follows from the contracted Bianchi identity $\nabla_a G^{ab} = 0$.
Where $\dot a \neq 0$ it can also be obtained by differentiating the expansion equation in $t$ and using the acceleration equation.
Example: with $k = 0$, $\Lambda = 0$ and dust ($p = 0$), the continuity equation gives $\rho a^3 = \text{const}$, and the expansion equation then gives $a \propto t^{2/3}$.
In terms of $H = \dot a / a$, the expansion equation reads $\Omega - 1 = k/(a^2 H^2)$ with $\Omega = 8\pi G \rho/(3H^2) + \Lambda/(3H^2)$, so the sign of $k$ is fixed by whether $\Omega$ exceeds $1$.
The equations are named after Alexander Friedmann, who derived them in 1922 for $k > 0$ and in 1924 for $k < 0$.

## Explanations

### L1 human

The Friedmann equations tell how fast a uniform universe expands, given what it is filled with.
The first one is like an energy balance: the expansion rate squared is fed by the matter density, and reduced or raised by the curvature of space.
The second one says that ordinary matter and pressure slow the expansion down, while a positive cosmological constant speeds it up.

### L2 human

Under the [[cosmological principle|Q8MSCRDFAT]], the ten Einstein equations reduce to these two ordinary differential equations for $a(t)$.
Together with an equation of state $p = p(\rho)$ they form a closed system.
All the standard models, such as the Einstein–de Sitter, de Sitter, Milne and Lambda-CDM models, are solutions of them.
The acceleration equation shows that if $\rho + 3p > 0$ and $\Lambda \le 0$, then $\ddot a < 0$, which forces a Big Bang in the finite past of an expanding model.
