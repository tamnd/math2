---
tag: F18MBATVVP
kind: concept
name: Nonlinear Volterra equation
msc: [45D05, 45G10]
specializes: [BSCYBP6AS6]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_integral_equation
---

## Summary

A nonlinear Volterra equation is an integral equation $\varphi(t) = f(t) + \int_a^t K(t, s, \varphi(s))\, ds$.
The upper limit of integration is the variable itself, and the unknown may enter the integrand nonlinearly.
It extends the linear [[Volterra integral equation|DND8CBEVXT]] and contains every initial value problem $y' = F(t, y)$, $y(a) = y_0$, in integral form.
When $K$ is [[Lipschitz|0AW1E6YTJY]] in its last variable, successive approximations give a unique solution on the whole interval.
When the Lipschitz bound holds only on bounded sets, a solution may exist only on a short interval.

## Explanations

### L1 human

The value of the unknown at time $t$ depends on its whole past, through a rule that may be nonlinear.
Because only the past matters, the solution can be built forward step by step.
For example, $\varphi(t) = 1 + \int_0^t \varphi(s)^2\, ds$ is solved by $\varphi(t) = 1/(1 - t)$, which blows up at $t = 1$.
So, unlike the linear case, a solution need not last for all time.
