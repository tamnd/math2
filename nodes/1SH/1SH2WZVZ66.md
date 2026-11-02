---
tag: 1SH2WZVZ66
kind: statement
role: theorem
name: Huygens principle
msc: [35L05, 35L15]
uses: [5EHD2XBQDG]
about: [5EHD2XBQDG]
sources:
  - url: https://en.wikipedia.org/wiki/Huygens%E2%80%93Fresnel_principle
---

## Statement

Let $n \ge 3$ be odd and let $g \in C^{m+1}(\R^n)$, $h \in C^{m}(\R^n)$ with $m = \frac{n+1}{2}$.
Let $u \in C^2(\R^n \times [0, \infty))$ be the solution of the [[wave equation|5EHD2XBQDG]]
$$u_{tt} = \Delta u \ \text{ on } \R^n \times (0, \infty), \qquad u(\cdot, 0) = g, \quad u_t(\cdot, 0) = h.$$
Let $x \in \R^n$ and $t > 0$.
Then $u(x, t)$ depends only on the values of $g$, $h$ and their derivatives of order at most $m$ on the sphere $\set{y : \abs{y - x} = t}$.
In particular, if $g$ and $h$ vanish outside a ball $B(0, R)$, then $u(x, t) = 0$ whenever $t > \abs{x} + R$ or $t < \abs{x} - R$.

## Remarks

For $n = 3$, Kirchhoff's formula makes this explicit:
$$u(x, t) = \frac{1}{4\pi t^2}\int_{\abs{y - x} = t} \big( t\, h(y) + g(y) + \nabla g(y) \cdot (y - x) \big)\, dS(y).$$
The proof in general odd dimension uses spherical means, which reduce the equation to a one-dimensional wave equation solved by d'Alembert's formula.
The hypothesis that $n$ is odd and at least $3$ is necessary.
For $n = 2$, Poisson's formula gives $u(x, t)$ as an integral over the whole disc $\abs{y - x} \le t$, and a pulse leaves a tail: $u(x, t)$ need not vanish for $t > \abs{x} + R$.
For $n = 1$, the integral term of d'Alembert's formula also depends on $h$ in the whole interval $[x - t, x + t]$.
This sharp form is also called the strong Huygens principle.

## Explanations

### L1 human

In three-dimensional space a short sound reaches you as a short sound: you hear it when the wave front arrives, and then silence.
The Huygens principle says this precisely: the solution at a point depends only on the data on a sphere around it, not inside the sphere.
In a flat, two-dimensional world this fails, and a short clap would be heard with a lingering echo.
The principle holds in every odd dimension from $3$ on and in no even dimension.

### L2 human

The statement follows from the explicit solution formulas for the wave equation obtained by spherical means and the method of descent.
In odd dimensions the formula contains only surface integrals over the sphere of radius $t$, while in even dimensions it contains integrals over the whole ball.
The weaker statement that $u(x, t)$ depends only on data in the closed ball of radius $t$ holds in all dimensions; it is finite speed of propagation.
The name refers to the physical Huygens principle of wave optics, where each point of a wave front acts as a source of secondary waves.
