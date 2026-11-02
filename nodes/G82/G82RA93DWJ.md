---
tag: G82RA93DWJ
kind: definition
name: Klein–Gordon equation
msc: [35Q40, 35L05, 35L71]
defines: AYCCDQWCJF
uses: [92C3S03AQZ, 5EHD2XBQDG, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Klein%E2%80%93Gordon_equation
---

## Definition

Let $n \ge 1$ and $m \ge 0$.
The *Klein–Gordon equation* with mass $m$ is the [[hyperbolic equation|92C3S03AQZ]] for $u \colon \R^n \times \R \to \C$:
$$\frac{\partial^2 u}{\partial t^2} - \Delta u + m^2 u = 0,$$
where $\Delta$ is the [[Laplacian|0E0B6RA8K0]] in $x$.
With the speed of light $c$ and the reduced Planck constant $\hbar$ restored, it reads $\frac{1}{c^2} u_{tt} - \Delta u + \frac{m^2 c^2}{\hbar^2} u = 0$.

## Remarks

Example: for $k \in \R^n$ and $\omega = \sqrt{\abs{k}^2 + m^2}$, the plane wave $u(x, t) = e^{i(k \cdot x - \omega t)}$ is a solution, since $u_{tt} = -\omega^2 u$ and $\Delta u = -\abs{k}^2 u$, so $u_{tt} - \Delta u + m^2 u = (-\omega^2 + \abs{k}^2 + m^2) u = 0$.
Non-example: the plane wave $e^{i(k \cdot x - \abs{k} t)}$ solves the [[wave equation|5EHD2XBQDG]] but not the Klein–Gordon equation with $m > 0$, since then the left side is $m^2 u \ne 0$.
For $m = 0$ the equation is the wave equation with speed $1$.
The conserved energy is $E(t) = \frac{1}{2}\int_{\R^n} \big(\abs{u_t}^2 + \abs{\nabla u}^2 + m^2 \abs{u}^2\big)\, dx$.
