---
tag: MW198BJJNK
kind: definition
name: Singular control
msc: [49K15, 93C15]
defines: 91RFB97TNV
uses: [RACVWG5QTK, WS9MRAZMFW, 7RPV2T29CF, GK1Z3Q1WRZ, ZPDTVZQN5K]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_control
---

## Definition

Let $a < b$, $T > 0$, and let $f_0, f_1 \colon \R^n \to \R^n$ and $L_0, L_1 \colon \R^n \to \R$ be of class $C^1$.
Consider the [[control system|ZPDTVZQN5K]] $x' = f_0(x) + u f_1(x)$ with scalar control $u(t) \in [a, b]$ and running cost $\int_0^T (L_0(x) + u L_1(x)) \, dt$.
Let $(x, u, p, \lambda_0)$ be an extremal, that is, a quadruple that satisfies the conclusions of [[Pontryagin's maximum principle|7RPV2T29CF]].
The [[Hamiltonian|RACVWG5QTK]] along it is $H = H_0 + u \Phi$ with $H_0 = p \cdot f_0(x) - \lambda_0 L_0(x)$, where the *switching function* is
$$\Phi(t) = p(t) \cdot f_1(x(t)) - \lambda_0 L_1(x(t)).$$
The control $u$ is *singular* on an interval $J \subseteq [0, T]$ of positive length if $\Phi(t) = 0$ for all $t \in J$.
An extremal arc on such an interval $J$ is a *singular arc*.

## Remarks

Where $\Phi(t) > 0$ the maximum condition forces $u(t) = b$, and where $\Phi(t) < 0$ it forces $u(t) = a$.
Where $\Phi$ vanishes only at isolated times, the control is [[bang–bang|GK1Z3Q1WRZ]].
Example: minimize $\int_0^2 x^2 \, dt$ for $x' = u$, $x(0) = 1$, $u \in [-1, 1]$, with free final state.
The optimal control is $u = -1$ on $[0, 1]$ and $u = 0$ on $[1, 2]$, with $x(t) = 1 - t$ on $[0, 1]$ and $x = 0$ on $[1, 2]$.
Here $H = p u - x^2$, $\Phi = p$, and the [[costate equation|WS9MRAZMFW]] is $p' = 2x$ with $p(2) = 0$.
So $p = 0$ on $[1, 2]$, and the control is singular there, with the interior value $u = 0$.
Non-example: in the same problem, the control is not singular on $[0, 1)$, since $p(t) = -(1 - t)^2 < 0$ there.
To find a singular control, one differentiates $\Phi$ in time until $u$ appears and solves for $u$.
