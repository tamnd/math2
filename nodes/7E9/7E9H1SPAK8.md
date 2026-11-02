---
tag: 7E9H1SPAK8
kind: definition
name: Neutral differential equation
msc: [34K40, 34K05]
defines: 5C0N2ENRF2
uses: [39PCDRDB01]
sources:
  - url: https://en.wikipedia.org/wiki/Delay_differential_equation
---

## Definition

Let $\tau > 0$ and $n \ge 1$, and let $f \colon \R \times \R^n \times \R^n \times \R^n \to \R^n$ be a function.
A *neutral differential equation* with delay $\tau$ has the form
$$x'(t) = f\bigl(t, x(t), x(t - \tau), x'(t - \tau)\bigr).$$
Here $x$ is an unknown function with values in $\R^n$, and $f$ depends on its last argument.
An initial value problem prescribes a history $\phi$ on $[-\tau, 0]$ that is continuously differentiable.

## Remarks

Example: $x'(t) = \frac{1}{2} x'(t - 1) - x(t)$, with $f(t, u, v, w) = \frac{1}{2} w - u$, which depends on $w$.

Non-example: $x'(t) = -x(t - 1)$ is a [[delay differential equation|39PCDRDB01]] of retarded type, not a neutral one, since $f(t, u, v, w) = -v$ does not depend on $w$.

A more general form, due to Hale, is $\frac{d}{dt} D(t, x_t) = F(t, x_t)$, where $x_t$ is the segment of $x$ on $[t - \tau, t]$ and $D(t, \psi) = \psi(0) - g(t, \psi)$ for a suitable function $g$ of the past.
The linear case $\frac{d}{dt}\bigl(x(t) - c\, x(t - \tau)\bigr) = a\, x(t) + b\, x(t - \tau)$ is the standard test example.

## Explanations

### L1 human

A neutral equation lets past derivatives, not only past values, drive the present derivative.
This feature makes its solutions keep the roughness of their initial data.
