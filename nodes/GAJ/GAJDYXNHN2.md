---
tag: GAJDYXNHN2
kind: definition
name: Fisher's equation
msc: [35K57, 35K58, 35Q92]
defines: AXV2PH7FEZ
uses: [TAAHWE917M, 09EGC6F8PT, M37M411KP7]
sources:
  - url: https://en.wikipedia.org/wiki/KPP%E2%80%93Fisher_equation
---

## Definition

Let $D > 0$ and $r > 0$ be constants.
*Fisher's equation* is the [[reaction–diffusion equation|TAAHWE917M]] for a function $u(x, t)$ of $x \in \R$ and $t > 0$:
$$u_t = D\, u_{xx} + r\, u (1 - u).$$
Here $u_t$ and $u_{xx}$ are [[partial derivatives|09EGC6F8PT]].
The same name is used for $u_t = D \Delta u + r u(1 - u)$ with $x \in \R^n$.

## Remarks

The constants $u \equiv 0$ and $u \equiv 1$ are solutions: both sides vanish.
The state $0$ is unstable and the state $1$ is stable for the reaction $u' = r u(1 - u)$.
A [[travelling wave|M37M411KP7]] is a solution $u(x, t) = U(x - ct)$ with $U(-\infty) = 1$ and $U(+\infty) = 0$.
Such a wave with $0 \le U \le 1$ exists if and only if $c \ge 2\sqrt{rD}$.
A non-example is the heat equation $u_t = D u_{xx}$: it has no reaction term, so it is not Fisher's equation for any $r > 0$.
The rescaling $x \mapsto x\sqrt{r/D}$, $t \mapsto r t$ reduces the equation to $u_t = u_{xx} + u(1 - u)$.
