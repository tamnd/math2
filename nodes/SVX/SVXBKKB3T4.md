---
tag: SVXBKKB3T4
kind: definition
name: Costate equation
msc: [49K15, 93C15]
defines: WS9MRAZMFW
uses: [RACVWG5QTK, ZPDTVZQN5K, ZT6F4C2YHK]
sources:
  - url: https://en.wikipedia.org/wiki/Costate_equation
---

## Definition

Let $U \subseteq \R^m$ be nonempty, $T > 0$, and let $f \colon [0, T] \times \R^n \times U \to \R^n$ and $L \colon [0, T] \times \R^n \times U \to \R$ be continuous with continuous partial derivatives in $x$.
Let $H(t, x, u, p, \lambda_0) = p \cdot f(t, x, u) - \lambda_0 L(t, x, u)$ be the [[Hamiltonian|RACVWG5QTK]], and fix $\lambda_0 \ge 0$.
Let $u \colon [0, T] \to U$ be a measurable bounded control with trajectory $x$ of the [[control system|ZPDTVZQN5K]] $x' = f(t, x, u)$.
The *costate equation* along $(x, u)$ is the linear differential equation
$$p'(t) = -\frac{\partial H}{\partial x}(t, x(t), u(t), p(t), \lambda_0) = -\Big(\frac{\partial f}{\partial x}(t, x(t), u(t))\Big)^{T} p(t) + \lambda_0 \nabla_x L(t, x(t), u(t))$$
for an [[absolutely continuous|ZT6F4C2YHK]] function $p \colon [0, T] \to \R^n$, required to hold for almost every $t \in [0, T]$.
A solution $p$ is a *costate* or *adjoint* vector along $(x, u)$.

## Remarks

Example: $x' = u$ in $\R$ with running cost $\int \frac12 (x^2 + u^2) \, dt$ and $\lambda_0 = 1$.
Then $H = p u - \frac12 (x^2 + u^2)$ and $\partial H / \partial x = -x$, so the costate equation is $p' = x$.
Non-example: $p' = +\partial H / \partial x$ is not the costate equation, because the sign is wrong.
With it, the quantity $p \cdot \delta x$ for a solution $\delta x$ of the linearized equation $\delta x' = (\partial f / \partial x) \delta x$ would not be constant when $\lambda_0 = 0$.
The costate equation is fixed by a boundary condition, the transversality condition.
For a free final state and an endpoint cost $\varphi(x(T))$ to be minimized, it is $p(T) = -\lambda_0 \nabla \varphi(x(T))$.
