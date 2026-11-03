---
tag: M3PMFEGSN2
kind: definition
name: Mackey–Glass equation
msc: [92C30, 34K60, 34K23]
defines: C5E5KKWXWS
uses: [39PCDRDB01]
sources:
  - url: https://en.wikipedia.org/wiki/Mackey%E2%80%93Glass_equations
---

## Definition

Let $\beta > 0$, $\gamma > 0$, $n > 0$ and $\tau \ge 0$ be constants.
The *Mackey–Glass equation* is the [[delay differential equation|39PCDRDB01]]
$$x'(t) = \beta \, \frac{x(t - \tau)}{1 + x(t - \tau)^n} - \gamma \, x(t).$$
The unknown is a function $x(t) \ge 0$.
It comes with an initial history $x(t) = \phi(t)$ for $t \in [-\tau, 0]$, where $\phi$ is continuous and nonnegative.

## Remarks

The first term is the production, which depends on the state at the earlier time $t - \tau$; the term $\gamma x(t)$ is the loss.
Example: the constant $x^* = (\beta/\gamma - 1)^{1/n}$ is a solution when $\beta > \gamma$, because then $\beta / (1 + (x^*)^n) = \gamma$, so the right side vanishes.
For $\beta \le \gamma$ the only constant solution with $x \ge 0$ is $x = 0$.
Non-example: the logistic equation $x' = x(1 - x)$ has no delay term, so it is not of Mackey–Glass form.
A choice of parameters often used to show chaotic behaviour is $\beta = 0.2$, $\gamma = 0.1$, $n = 10$ and $\tau = 17$.
