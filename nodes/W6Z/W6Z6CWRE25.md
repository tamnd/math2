---
tag: W6Z6CWRE25
kind: example
name: Airfoil equation
msc: ["45E05", 76B10, 76G25]
instance_of: [E30EA6ETZ4]
uses: [5JYBXH9BP6, 0SYR10HD4R, E30EA6ETZ4]
sources:
  - url: https://en.wikipedia.org/wiki/Airfoil
    locator: Thin airfoil theory
---

## Example

The *airfoil equation* asks for a function $\varphi$ on $(-1, 1)$ with
$$\frac{1}{\pi}\, \mathrm{PV}\!\int_{-1}^{1} \frac{\varphi(t)}{t - x}\, dt = f(x), \quad -1 < x < 1,$$
for a given function $f$, where $\mathrm{PV}$ is the [[Cauchy principal value|0SYR10HD4R]].
So it inverts the [[finite Hilbert transform|5JYBXH9BP6]], and it is a [[singular integral equation|E30EA6ETZ4]] of the first kind.
In thin airfoil theory the chord of the wing is scaled to $[-1, 1]$, and $\varphi$ is the density of vorticity along the chord.
The right side $f$ is fixed by the free stream speed, the angle of attack and the slope of the camber line.

For $f$ smooth enough, the solutions are
$$\varphi(x) = -\frac{1}{\pi \sqrt{1 - x^2}}\, \mathrm{PV}\!\int_{-1}^{1} \frac{\sqrt{1 - t^2}\, f(t)}{t - x}\, dt + \frac{C}{\sqrt{1 - x^2}},$$
with an arbitrary constant $C$.

Check on Chebyshev polynomials.
Let $T_n$ and $U_{n-1}$ be the Chebyshev polynomials of the first and second kind, $n \ge 1$.
For $-1 < x < 1$ one has
$$\frac{1}{\pi}\, \mathrm{PV}\!\int_{-1}^{1} \frac{T_n(t)}{\sqrt{1 - t^2}\,(t - x)}\, dt = U_{n-1}(x), \qquad \frac{1}{\pi}\, \mathrm{PV}\!\int_{-1}^{1} \frac{\sqrt{1 - t^2}\, U_{n-1}(t)}{t - x}\, dt = -T_n(x).$$
For $f = U_{n-1}$ the second identity turns the formula into $\varphi = T_n / \sqrt{1 - x^2}$ plus the free term, and the first identity confirms that this solves the equation.
The free term solves the homogeneous equation, since $\frac{1}{\pi}\, \mathrm{PV}\!\int_{-1}^{1} \frac{dt}{\sqrt{1 - t^2}\,(t - x)} = 0$ for $-1 < x < 1$.

## Remarks

The constant $C$ is not fixed by the equation.
In aerodynamics it is fixed by the Kutta condition, which asks that $\varphi$ stay bounded at the trailing edge $x = 1$.
The lift of the airfoil is proportional to $\int_{-1}^{1} \varphi(t)\, dt$.

## Explanations

### L1 human

A thin wing in a steady flow is replaced by a line of small vortices along its chord.
The flow must slide along the wing, and this condition gives one equation for the strength of the vortices.
That equation is the airfoil equation, and it has an explicit solution.
The solution is unique only after one adds a physical condition at the rear edge of the wing.
