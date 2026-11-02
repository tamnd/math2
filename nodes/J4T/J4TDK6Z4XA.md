---
tag: J4TDK6Z4XA
kind: statement
role: theorem
name: Dispersive estimate for the Schrödinger equation
msc: [35Q41, 35B45, 42B37]
uses: [EPZR6H2WJN, AYMJ2NFR4W, DPVM34ADZV, SASP14MA1Z]
about: [EPZR6H2WJN]
sources:
  - url: https://en.wikipedia.org/wiki/Strichartz_estimate
---

## Statement

Let $n \ge 1$.
For $f \in L^2(\R^n)$ and $t \in \R$, let $e^{it\Delta} f$ be the solution at time $t$ of the free [[Schrödinger equation|EPZR6H2WJN]] $i \partial_t u + \Delta u = 0$ with $u(0) = f$.
It is defined by the [[Fourier transform|DPVM34ADZV]] $\hat f(\xi) = \int_{\R^n} f(x) e^{-i x \cdot \xi} \, dx$ as $\widehat{e^{it\Delta} f}(\xi) = e^{-it\abs{\xi}^2} \hat f(\xi)$.
Then for all $f \in L^1(\R^n) \cap L^2(\R^n)$ and all $t \ne 0$,
$$\norm{e^{it\Delta} f}_{L^\infty(\R^n)} \le (4\pi \abs{t})^{-n/2} \norm{f}_{L^1(\R^n)}.$$

## Remarks

For $t \ne 0$ the solution operator has an explicit kernel:
$$e^{it\Delta} f(x) = (4\pi i t)^{-n/2} \int_{\R^n} e^{i \abs{x - y}^2 / (4t)} f(y) \, dy,$$
with the principal branch of the square root.
The kernel has modulus $(4\pi\abs{t})^{-n/2}$ at every point, and the estimate follows at once.
The formula for the kernel comes from the Fourier transform of the complex Gaussian $e^{-it\abs{\xi}^2}$, or from the heat kernel by replacing $t$ by $it$.

The solution also conserves the $L^2$ norm: $\norm{e^{it\Delta} f}_{L^2} = \norm{f}_{L^2}$, by Plancherel's theorem.
Interpolation between this and the dispersive estimate with the Riesz–Thorin theorem gives, for $2 \le r \le \infty$ and $1/r + 1/r' = 1$,
$$\norm{e^{it\Delta} f}_{L^r} \le (4\pi\abs{t})^{-n(1/2 - 1/r)} \norm{f}_{L^{r'}}.$$

The decay rate $\abs{t}^{-n/2}$ cannot be improved.
For the Gaussian $f(x) = e^{-\abs{x}^2}$ one computes $\abs{e^{it\Delta} f(0)} = (1 + 16 t^2)^{-n/4}$, which is of exact order $\abs{t}^{-n/2}$ for large $\abs{t}$.
The $L^1$ norm on the right cannot be replaced by the $L^2$ norm.
For fixed $t$, the operator $e^{it\Delta}$ maps $L^2(\R^n)$ onto $L^2(\R^n)$, which contains unbounded functions, so no bound of $\norm{e^{it\Delta} f}_{L^\infty}$ by a multiple of $\norm{f}_{L^2}$ holds.

## Explanations

### L1 human

A free quantum particle described by the Schrödinger equation spreads out over time.
Waves of different frequencies travel at different speeds, so an initially concentrated wave packet disperses.
The estimate says how fast: in $n$ dimensions, the peak height of the wave decays like $\abs{t}^{-n/2}$, as long as the initial wave has finite total mass in $L^1$.

### L2 human

The dispersive estimate is the pointwise decay input for the [[Strichartz estimates|4PDKJ8N1S9]].
Combined with the $TT^*$ argument and the Hardy–Littlewood–Sobolev inequality, it gives space-time integrability of $e^{it\Delta} f$ for $L^2$ data.
These bounds are the basic tool of the local and global well-posedness theory of nonlinear Schrödinger equations.
The same pattern applies to other [[dispersive equations|AYMJ2NFR4W]] such as the wave and Airy equations, with different decay rates.
One proves a pointwise decay bound from an oscillatory kernel and interpolates it with energy conservation.
