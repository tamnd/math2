---
tag: WT65A6ARGN
kind: definition
name: Inverse scattering transform
msc: [37K15, 35Q53, 35Q51]
defines: 6GY3X4Y8X5
uses: [G3A4S7CSB3, KTT75QC72Z, 89AA6XJY5K]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_scattering_transform
---

## Definition

Consider the [[Korteweg–De Vries equation|KTT75QC72Z]] $u_t - 6 u u_x + u_{xxx} = 0$ for $u(x, t)$ real, smooth and decaying fast as $\abs{x} \to \infty$.
For each $t$, let $L_t = -\partial_x^2 + u(\cdot, t)$ be the one-dimensional [[Schrödinger operator|89AA6XJY5K]] with potential $u(\cdot, t)$.
Its *scattering data* $S(t)$ consist of:

1. the finitely many eigenvalues $-\kappa_1^2, \dots, -\kappa_N^2$ of $L_t$, with $\kappa_n > 0$;
2. the norming constants $c_n(t) > 0$, where the normalised eigenfunction $\psi_n$ satisfies $\psi_n(x) \sim c_n e^{-\kappa_n x}$ as $x \to +\infty$;
3. the reflection coefficient $b(k, t)$ for $k \in \R$, where a solution of $L_t \psi = k^2 \psi$ satisfies $\psi(x) \sim e^{-ikx} + b(k, t) e^{ikx}$ as $x \to +\infty$ and $\psi(x) \sim a(k, t) e^{-ikx}$ as $x \to -\infty$.

The *inverse scattering transform* solves the initial value problem with data $u(x, 0)$ in three steps.

1. Direct scattering: compute $S(0)$ from $u(\cdot, 0)$.
2. Time evolution: $\kappa_n$ stays constant, $c_n(t) = c_n(0) e^{4 \kappa_n^3 t}$ and $b(k, t) = b(k, 0) e^{8 i k^3 t}$.
3. Inverse scattering: set $F(x) = \sum_{n} c_n(t)^2 e^{-\kappa_n x} + \frac{1}{2\pi} \int_{\R} b(k, t) e^{ikx} \, dk$, solve the Gelfand–Levitan–Marchenko equation
$$K(x, y) + F(x + y) + \int_x^\infty K(x, z) F(z + y) \, dz = 0 \quad (y > x)$$
for $K$, and put $u(x, t) = -2 \frac{d}{dx} K(x, x)$.

## Remarks

The time evolution in step 2 comes from the [[Lax pair|G3A4S7CSB3]] of the equation: $L_t$ evolves by conjugation, so its eigenvalues do not move.

Example: take $N = 1$ and $b = 0$, so that $F(x) = c^2 e^{-\kappa x}$ with $c = c_1(t)$.
The kernel $K(x, y) = -\dfrac{c^2 e^{-\kappa (x + y)}}{1 + (c^2/2\kappa) e^{-2\kappa x}}$ solves the equation.
With $w = (c^2/2\kappa) e^{-2\kappa x}$ this gives $u = -8\kappa^2 w/(1 + w)^2 = -2\kappa^2 \operatorname{sech}^2(\kappa(x - x_0))$, where $w = e^{-2\kappa(x - x_0)}$.
Since $c^2$ grows like $e^{8\kappa^3 t}$, the centre is $x_0 = 4\kappa^2 t + \text{const}$: this is the one-[[soliton|63D4AXYCT4]] solution moving with speed $4\kappa^2$.

Non-example: the method needs a Lax pair, and most nonlinear evolution equations have none.
For instance, the generalised KdV equation $u_t + u^p u_x + u_{xxx} = 0$ with an integer $p \ge 3$ is not integrable, and the steps above do not apply to it.

Other equations with a Lax pair, such as the [[nonlinear Schrödinger equation|GEJHRXC176]] and the [[sine-Gordon equation|802QSF9NM3]], have inverse scattering transforms built on other spectral problems.

## Explanations

### L1 human

The inverse scattering transform turns a hard nonlinear evolution into three linear steps.
Map the initial wave to spectral data, move the data forward by explicit exponentials, and map back by solving a linear integral equation.
