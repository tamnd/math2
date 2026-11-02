---
tag: 3DJMFT0SQM
kind: definition
name: Similarity solution
msc: [35C06, 35B06, 76M55]
defines: 579J5K9K5Z
uses: [GC5BDZ6QBC, VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Self-similar_solution
---

## Definition

Let $n \ge 1$ and consider a [[partial differential equation|GC5BDZ6QBC]] for a function $u \colon \R^n \times (0, \infty) \to \R$.
Let $\alpha, \beta \in \R$, and for $\lambda > 0$ put $u_\lambda(x, t) = \lambda^{\alpha} u(\lambda^{\beta} x, \lambda t)$.
Assume that the equation is invariant under these scalings: if $u$ is a solution, then so is $u_\lambda$ for every $\lambda > 0$.
A solution $u$ is a *similarity solution*, or *self-similar solution*, with exponents $(\alpha, \beta)$ if $u_\lambda = u$ for every $\lambda > 0$.

## Remarks

Taking $\lambda = 1/t$ shows that $u$ is self-similar exactly when
$$u(x, t) = t^{-\alpha}\, v\!\left( \frac{x}{t^{\beta}} \right)$$
for a function $v$ on $\R^n$, namely $v = u(\cdot, 1)$.
Substituting this form turns the equation into an equation for $v$ in the variable $\eta = x / t^\beta$.

Example: the [[heat equation|VP2HN86VAG]] $u_t = \Delta u$ is invariant for $\beta = 1/2$ and every $\alpha$.
The heat kernel $\Phi(x, t) = (4\pi t)^{-n/2} e^{-\abs{x}^2 / (4t)}$ is self-similar with $\alpha = n/2$, $\beta = 1/2$.
Check: $\lambda^{n/2} \Phi(\lambda^{1/2} x, \lambda t) = \lambda^{n/2} (4\pi\lambda t)^{-n/2} e^{-\lambda \abs{x}^2/(4\lambda t)} = \Phi(x, t)$.

Non-example: $u(x, t) = e^{-t} \sin x$ solves $u_t = u_{xx}$ for $n = 1$, but it is not self-similar.
A self-similar solution would have zero set $\sqrt{t}\, Z$ at time $t$, with $Z$ the zero set of $v$.
But the zero set of $u(\cdot, t)$ is $\pi \Z$ for every $t$.
At $t = 1$ this forces $Z = \pi \Z$, and then at $t = 4$ the zero set would be $2 \pi \Z \ne \pi \Z$.

For a scalar conservation law $u_t + F(u)_x = 0$, the scalings with $\alpha = 0$, $\beta = 1$ are symmetries.
The corresponding similarity solutions $u = v(x/t)$ include the [[rarefaction waves|MFN4Q5SH8H]] and the solutions of the [[Riemann problem|GJWKX22VVE]].

## Explanations

### L1 human

A similarity solution looks the same at every time after the right change of scale.
Its whole history is encoded in the profile $v$ at time $1$.
