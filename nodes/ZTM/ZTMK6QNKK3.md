---
tag: ZTMK6QNKK3
kind: definition
name: Input-to-state stability
msc: [93D25, 93D09, 34D20]
defines: GRDCEGQJYQ
uses: [0NT64JV96A, 0AW1E6YTJY, 0F2SYCKDT2]
sources:
  - url: https://en.wikipedia.org/wiki/Input-to-state_stability
---

## Definition

Let $f \colon \R^n \times \R^m \to \R^n$ be locally [[Lipschitz|0AW1E6YTJY]] with $f(0, 0) = 0$.
Consider the control system $\dot x(t) = f(x(t), u(t))$, where the inputs $u \colon [0, \infty) \to \R^m$ are measurable and essentially bounded, with norm $\norm{u}_\infty = \operatorname{ess\,sup}_{t \ge 0} \abs{u(t)}$.
A function $\gamma \colon [0, \infty) \to [0, \infty)$ is of *class $\mathcal{K}$* if it is continuous, strictly increasing and $\gamma(0) = 0$.
A function $\beta \colon [0, \infty) \times [0, \infty) \to [0, \infty)$ is of *class $\mathcal{KL}$* if two conditions hold.
For each $t$, $\beta(\cdot, t)$ is of class $\mathcal{K}$; for each $r$, $\beta(r, \cdot)$ is nonincreasing with limit $0$ at infinity.
The system is *input-to-state stable* (ISS) if there are $\beta$ of class $\mathcal{KL}$ and $\gamma$ of class $\mathcal{K}$ with this property.
For every $x_0 \in \R^n$ and every input $u$, the solution with $x(0) = x_0$ exists for all $t \ge 0$ and satisfies
$$\abs{x(t)} \le \beta(\abs{x_0}, t) + \gamma(\norm{u}_\infty) \quad \text{for all } t \ge 0.$$

## Remarks

Example: $\dot x = -x + u$ on $\R$.
By variation of constants, $x(t) = e^{-t} x_0 + \int_0^t e^{-(t - s)} u(s) \, ds$.
Hence $\abs{x(t)} \le e^{-t} \abs{x_0} + \norm{u}_\infty$, so the system is ISS with $\beta(r, t) = r e^{-t}$ and $\gamma(r) = r$.

Non-example: $\dot x = -x + x u$ on $\R$.
For $u = 0$ the origin is globally asymptotically stable.
But for the constant input $u = 2$ the equation is $\dot x = x$, so $x(t) = e^t x_0$ is unbounded, and no estimate of the ISS form can hold.

Taking $u = 0$ shows that an ISS system has a globally asymptotically stable equilibrium at $0$.
An equivalent characterisation uses an ISS Lyapunov function $V$: a smooth, positive definite, proper function with $\nabla V(x) \cdot f(x, u) \le -\alpha(\abs{x}) + \sigma(\abs{u})$ for some class $\mathcal{K}$ functions $\alpha$ (unbounded) and $\sigma$.

## Explanations

### L1 human

A system is ISS when bounded inputs give bounded states, and when the effect of the initial state fades away with time.
The function $\beta$ measures how fast the start is forgotten, and $\gamma$ measures how strongly the input pushes the state.
