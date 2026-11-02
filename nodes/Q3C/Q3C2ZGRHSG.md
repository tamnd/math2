---
tag: Q3C2ZGRHSG
kind: definition
name: Integro-partial differential equation
msc: [45K05, 35R09]
defines: TH4NGC4016
uses: [YRKW2KX2CW, GC5BDZ6QBC]
sources:
  - url: https://en.wikipedia.org/wiki/Integro-differential_equation
---

## Definition

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be open.
An *integro-partial differential equation* on $\Omega$ is an equation for an unknown function $u \colon \Omega \to \R$ (or $\C$, or $\R^m$) such that:

1. at least one partial derivative of $u$ appears in it, and
2. at least one integral of $u$, or of a derivative of $u$, with respect to one or more of the variables appears in it.

A typical linear form is
$$\sum_{\abs{\alpha} \le k} a_\alpha(x) \, \partial^\alpha u(x) + \int_{\Omega} K(x, y) \, u(y) \, dy = f(x), \quad x \in \Omega,$$
with given coefficients $a_\alpha$, kernel $K$ and right side $f$.

## Remarks

Example: let $J \colon \R \to [0, \infty)$ be even and integrable, and consider $\partial_t u(x, t) = \int_{\R} J(x - y) \big(u(y, t) - u(x, t)\big) \, dy$ on $\R \times (0, \infty)$.
Write $\hat J(\omega) = \int_{\R} J(z) \cos(\omega z) \, dz$.
Then $u(x, t) = e^{(\hat J(\omega) - \hat J(0)) t} \cos(\omega x)$ is a solution, because $\int_{\R} J(x - y) \cos(\omega y) \, dy = \hat J(\omega) \cos(\omega x)$ for even $J$.

Non-example: the heat equation $\partial_t u = \partial_x^2 u$ contains no integral of $u$, so it fails clause 2 and is a [[partial differential equation|GC5BDZ6QBC]].
The equation $x'(t) = \int_0^t x(s) \, ds$ has an unknown of one variable only, so it is an [[integro-differential equation|YRKW2KX2CW]] but not a partial one.
