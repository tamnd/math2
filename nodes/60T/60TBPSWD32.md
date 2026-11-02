---
tag: 60TBPSWD32
kind: example
name: Symm's integral equation
msc: [31A10, 45A05, 65R20]
instance_of: [ZDS77Q0F06]
sources:
  - url: https://en.wikipedia.org/wiki/Newtonian_potential
---

## Example

Let $\Gamma \subset \R^2$ be a closed $C^2$ curve, and let $f$ be a continuous function on $\Gamma$.
Symm's integral equation asks for a density $\psi$ on $\Gamma$ with
$$-\frac{1}{2\pi} \int_\Gamma \ln \abs{x - y} \, \psi(y) \, ds(y) = f(x), \quad x \in \Gamma.$$
The left side is the [[single layer potential|9T6ZEV4125]] of $\psi$ in the plane, a [[logarithmic potential|46NHWJHW44]], restricted to $\Gamma$.
The unknown appears only under the integral, so it is an [[integral equation of the first kind|ZDS77Q0F06]], with the [[weakly singular kernel|94TNBAAJYX]] $-\frac{1}{2\pi}\ln\abs{x - y}$.
Solving it gives a single layer potential that solves the interior Dirichlet problem for the Laplace equation with boundary values $f$.

Check on the circle $\Gamma = \set{x : \abs{x} = a}$, with $y = a e^{i\theta}$ and $x = a e^{i\phi}$:
by the mean value property, $\frac{1}{2\pi} \int_0^{2\pi} \ln \abs{x - a e^{i\theta}} \, d\theta = \ln a$ for $\abs{x} = a$, and $\ln \abs{e^{i\phi} - e^{i\theta}} = -\sum_{n \ge 1} \frac{\cos n(\phi - \theta)}{n}$.
Hence the operator maps $\psi = 1$ to the constant $-a \ln a$, and $\psi(\theta) = e^{in\theta}$ with $n \ne 0$ to $\frac{a}{2\abs{n}} e^{in\phi}$.
So on a circle of radius $a \ne 1$ the equation is uniquely solvable for every trigonometric polynomial $f$.
For $a = 1$ the constant density $\psi = 1$ solves the homogeneous equation.

## Remarks

The circle example shows the general picture: the homogeneous equation has only the zero solution unless $\Gamma$ has logarithmic capacity $1$, and this exceptional case can be avoided by rescaling.
The eigenvalues $\frac{a}{2\abs{n}}$ tend to $0$, so the solution depends unstably on $f$ in the supremum norm, as for every first-kind equation with a compact operator.
Because of its simple structure, the equation is a standard test case for boundary element and collocation methods.

## Explanations

### L1 human

Put an unknown charge density on a closed curve in the plane, and ask that its potential takes prescribed values on the curve.
That is Symm's equation.
On a circle everything can be computed with Fourier series: each wave pattern of the charge is just multiplied by a number.
