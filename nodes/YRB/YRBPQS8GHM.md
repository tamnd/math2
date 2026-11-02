---
tag: YRBPQS8GHM
kind: definition
name: Functional differential equation
msc: [34K05]
defines: ZMCFEEPEKT
uses: [0NT64JV96A, 0FXDW992DS]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_differential_equation
---

## Definition

Let $r \ge 0$ and $n \ge 1$, and let $C = C([-r, 0], \R^n)$ be the space of continuous functions with the supremum norm.
For a continuous function $x$ defined on an interval containing $[t - r, t]$, let $x_t \in C$ be the segment $x_t(\theta) = x(t + \theta)$ for $\theta \in [-r, 0]$.
Let $\Omega \subseteq \R \times C$ be open and let $F \colon \Omega \to \R^n$.
A *(retarded) functional differential equation* is the equation
$$x'(t) = F(t, x_t).$$
A *solution* through $(\sigma, \phi) \in \Omega$ is a continuous $x \colon [\sigma - r, \sigma + T) \to \R^n$, for some $T > 0$, such that $x_\sigma = \phi$, $(t, x_t) \in \Omega$ and $x'(t) = F(t, x_t)$ for $t \in (\sigma, \sigma + T)$.

## Remarks

Example: $x'(t) = -\int_{-1}^{0} x(t + \theta) \, d\theta$ is of this form with $r = 1$ and $F(t, \psi) = -\int_{-1}^{0} \psi(\theta) \, d\theta$.

Non-example: $x'(t) = x(t + 1)$ is not of this form, since $x'(t)$ depends on the value at the later time $t + 1$, which is not part of $x_t$.

For $r = 0$, $C$ is $\R^n$ and the equation is an [[ordinary differential equation|0NT64JV96A]].
If $F$ is continuous and locally Lipschitz in its second argument, the [[initial value problem|0FXDW992DS]] has a unique local solution through each $(\sigma, \phi) \in \Omega$.
Equations whose derivative term also involves the past, such as $\frac{d}{dt}\bigl(x(t) - c\, x(t - r)\bigr) = F(t, x_t)$, are called neutral.

## Explanations

### L1 human

The derivative at time $t$ is any rule that reads the solution on the window $[t - r, t]$.
The window slides forward in time and plays the role of the state.
