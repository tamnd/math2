---
tag: D99FZQ2SQT
kind: statement
role: theorem
name: Gauss–Legendre Runge–Kutta methods
msc: [65L06, 65L04, 65P10]
uses: [7DBPJKYC6C, RH8BD7PW5F, 9V3QA0KTW8, Y7KSGE97GK, 1F16G4V64X, B4C25SXFRE]
about: [7DBPJKYC6C]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_method
same_as:
  wikidata: Q5527853
  wikipedia: Gauss–Legendre method
---

## Statement

Let $s \ge 1$ and let $c_1 < \cdots < c_s$ be the zeros in $(0, 1)$ of the [[shifted Legendre polynomial|9V3QA0KTW8]] of degree $s$.
Let $\ell_1, \ldots, \ell_s$ be the [[Lagrange basis polynomials|Y7KSGE97GK]] of these nodes.
The *$s$-stage Gauss–Legendre method* is the implicit [[Runge–Kutta method|7DBPJKYC6C]] with
$$a_{ij} = \int_0^{c_i} \ell_j(\theta) \, d\theta, \qquad b_j = \int_0^1 \ell_j(\theta) \, d\theta, \qquad i, j = 1, \ldots, s.$$
Then:

1. It has order $2s$, and no Runge–Kutta method with $s$ stages has order greater than $2s$.
2. Its stability function $R(z)$, defined by $y_{n+1} = R(h\lambda) y_n$ for $y' = \lambda y$, is the $(s, s)$ [[Padé approximant|1F16G4V64X]] of $e^z$.
   Moreover $\abs{R(z)} \le 1$ whenever $\operatorname{Re} z \le 0$, so the method is A-stable.
3. Its coefficients satisfy $b_i a_{ij} + b_j a_{ji} = b_i b_j$ for all $i, j$, so the method is a [[symplectic integrator|B4C25SXFRE]] and preserves every quadratic first integral of the equation.

## Remarks

The method is the collocation method at the nodes $c_i$: it finds the polynomial $u$ of degree $s$ with $u(t_n) = y_n$ and $u'(t_n + c_i h) = f(t_n + c_i h, u(t_n + c_i h))$ for each $i$, and sets $y_{n+1} = u(t_n + h)$.
The weights $b_j$ and nodes $c_j$ form the Gauss–Legendre quadrature rule on $[0, 1]$, which is exact up to degree $2s - 1$; collocation theory turns this into order $2s$.
Example: $s = 1$ gives $c_1 = \frac12$, $a_{11} = \frac12$, $b_1 = 1$, the implicit midpoint method $y_{n+1} = y_n + h f\big(t_n + \frac h2, \frac{y_n + y_{n+1}}{2}\big)$, with $R(z) = \frac{1 + z/2}{1 - z/2}$; clause 3 reads $\frac12 + \frac12 = 1$.
Example: $s = 2$ gives $c = \frac12 \mp \frac{\sqrt3}{6}$, $b = (\frac12, \frac12)$, $a_{11} = a_{22} = \frac14$, $a_{12} = \frac14 - \frac{\sqrt3}{6}$, $a_{21} = \frac14 + \frac{\sqrt3}{6}$, a method of order $4$.
The price of these properties is that each step needs the solution of a nonlinear system of dimension $sd$ for a system of dimension $d$.

## Explanations

### L1 human

Gauss–Legendre methods are the most accurate Runge–Kutta methods for a given number of stages: with $s$ stages they reach order $2s$.
They place their internal evaluation points at the same special positions as Gaussian quadrature.
They are implicit, so each step requires solving equations, but they stay stable for every step size on decaying problems and they conserve energy-like quantities very well over long times.

### L2 human

The family links three topics: Gaussian quadrature, which fixes the nodes; collocation, which gives the order; and geometric integration, through the symplecticity condition.
For Hamiltonian systems they are standard high-order symplectic methods, used for long-time simulations in celestial mechanics and molecular dynamics.
Their stability function satisfies $\abs{R(iy)} = 1$ on the imaginary axis and $\abs{R(z)} \to 1$ as $z \to -\infty$, so unlike [[backward Euler|M7XKVNATFA]] they do not damp very stiff components.
