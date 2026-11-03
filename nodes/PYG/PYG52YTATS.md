---
tag: PYG52YTATS
kind: definition
name: Intermittency in turbulence
msc: [76F05, 76F02]
defines: Y38WBWP6K8
uses: [VY307F8Z0S, 0FGAJSPX8E, 0ZY9DX8FBF, A3HKV3BHDR, NYRS1BJKRQ]
sources:
  - url: https://en.wikipedia.org/wiki/Intermittency
---

## Definition

Let $\mathbf{u}(x, t)$ be a statistically homogeneous and isotropic turbulent velocity field in $\R^3$, and let $\mathbf{e}$ be a unit vector.
For $r > 0$, the longitudinal velocity increment is $\delta u(r) = (\mathbf{u}(x + r\mathbf{e}, t) - \mathbf{u}(x, t)) \cdot \mathbf{e}$.
Its structure function of order $p$ is $S_p(r) = \langle \delta u(r)^p \rangle$, where $\langle \cdot \rangle$ is the ensemble average.
Its flatness is $F(r) = S_4(r) / S_2(r)^2$, the [[kurtosis|0FGAJSPX8E]] of $\delta u(r)$.
The flow is *intermittent* at small scales if the law of the normalised increment $\delta u(r) / S_2(r)^{1/2}$ changes with $r$ in the inertial range.
Its [[probability density function|0ZY9DX8FBF]] then has a flatness $F(r)$ that grows as $r$ decreases.
When $S_p(r)$ behaves like $r^{\zeta_p}$ in the inertial range, this means that $p \mapsto \zeta_p$ is not a linear function.

## Remarks

The [[Kolmogorov 1941 theory|A3HKV3BHDR]] predicts $\zeta_p = p/3$, which is linear, so it describes a flow without intermittency.
A Gaussian random field with a power-law spectrum is a non-example: its normalised increments are standard normal for every $r$, so $F(r) = 3$ for all $r$.
In experiments $F(r)$ rises well above $3$ as $r$ approaches the [[Kolmogorov microscale|NYRS1BJKRQ]], and the measured $\zeta_p$ fall below $p/3$ for large $p$.
For the moments $\langle \abs{\delta u(r)}^p \rangle$, Hölder's inequality forces the scaling exponents to be concave in $p$.
Multifractal models explain the nonlinear exponents by a whole range of local scaling exponents of the velocity.
