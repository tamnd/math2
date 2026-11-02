---
tag: SP56AYYR3T
kind: definition
name: Delay differential equation
msc: [34K06, 34K05]
defines: 39PCDRDB01
uses: [0NT64JV96A, ZMCFEEPEKT]
sources:
  - url: https://en.wikipedia.org/wiki/Delay_differential_equation
---

## Definition

Let $n, k \ge 1$, let $0 < \tau_1 < \cdots < \tau_k$ be constants, and let $f \colon \R \times (\R^n)^{k+1} \to \R^n$ be a function.
A *delay differential equation* with constant delays $\tau_1, \ldots, \tau_k$ is an equation
$$x'(t) = f\bigl(t, x(t), x(t - \tau_1), \ldots, x(t - \tau_k)\bigr)$$
for an unknown function $x$ with values in $\R^n$.
Let $t_0 \in \R$ and let $\phi \colon [-\tau_k, 0] \to \R^n$ be continuous, the *history*.
A *solution* of the initial value problem is a continuous $x \colon [t_0 - \tau_k, t_0 + T) \to \R^n$, for some $T > 0$, with these properties.
It equals the history: $x(t_0 + \theta) = \phi(\theta)$ for $\theta \in [-\tau_k, 0]$.
It is differentiable on $(t_0, t_0 + T)$, and the equation holds there.

## Remarks

Example: $x'(t) = -x(t - 1)$, with $n = k = 1$, $\tau_1 = 1$ and $f(t, u, v) = -v$.
Its characteristic equation, from $x = e^{\lambda t}$, is $\lambda = -e^{-\lambda}$, which has infinitely many complex roots.

Non-example: $x'(t) = x(t + 1)$ is not a delay equation, since the rate at time $t$ depends on a later time; such equations are called advanced.
An [[ordinary differential equation|0NT64JV96A]] $x' = f(t, x)$ is the degenerate case in which $f$ does not depend on the delayed arguments.

Delay equations are a special case of [[functional differential equations|ZMCFEEPEKT]] of retarded type, with $F(t, x_t) = f(t, x_t(0), x_t(-\tau_1), \ldots, x_t(-\tau_k))$.
Delays may also vary with time or with the state, as in $x'(t) = f(t, x(t), x(t - \tau(t)))$.

## Explanations

### L1 human

The derivative now depends on where the solution was some time ago.
So the start of the problem is a whole piece of past, not one point.
