---
tag: KA95J9V6AS
kind: concept
name: Stochastic Volterra equation
msc: [60H20, 45R05, 45D05]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_differential_equation
---

## Summary

A stochastic Volterra equation is a [[Volterra integral equation|DND8CBEVXT]] driven by noise.
It has the form $X(t) = X_0(t) + \int_0^t a(t, s, X(s)) \, ds + \int_0^t b(t, s, X(s)) \, dW(s)$, where the last integral is an Itô integral against a [[Wiener process|22735FGJV6]].
When the coefficients $a$ and $b$ do not depend on $t$ and $X_0$ is constant, it reduces to a [[stochastic differential equation|B219G9SHJA]].
The dependence on $t$ lets the noise and the drift have memory.
Such memory is used in models of rough volatility in finance and of viscoelastic materials under random forcing.

## Explanations

### L1 human

A stochastic differential equation moves a quantity by small random kicks whose effect lasts forever and unchanged.
In a stochastic Volterra equation the effect of a kick received at time $s$ may change with the elapsed time.
For example, it may fade away.
So the system remembers its past noise in a weighted way.
The process $\int_0^t (t - s)^{H - 1/2} \, dW(s)$ with $H > 0$ is a simple example: recent kicks are weighted differently from old ones.
