---
tag: MRBGM52H94
kind: definition
name: Wiener–Hopf method
msc: ["45E10", 47A68, "30E25"]
defines: H4NXEY6QTZ
uses: [QYY4NMDY5H, DPVM34ADZV, 0NAHXR1FRH, 0EHKVRF4J6, BYKP1V2AQN]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener%E2%80%93Hopf_method
---

## Definition

Consider the [[Wiener–Hopf equation|QYY4NMDY5H]] $\varphi(x) - \int_0^\infty k(x - t)\, \varphi(t)\, dt = f(x)$ for $x \ge 0$, with $k \in L^1(\R)$.
Write $\hat g(\xi) = \int_{\R} g(x)\, e^{i \xi x}\, dx$ for the [[Fourier transform|DPVM34ADZV]].
For this convention, the transform of a function supported in $[0, \infty)$ is [[holomorphic|0NAHXR1FRH]] in the upper half-plane $\operatorname{Im} \xi > 0$.
The transform of a function supported in $(-\infty, 0]$ is holomorphic in the lower half-plane.
The *Wiener–Hopf method* is the following procedure.

1. Extend $\varphi$ and $f$ by $0$ to $x < 0$, and let $\psi(x) = \int_0^\infty k(x - t) \varphi(t)\, dt$ for $x < 0$ and $\psi(x) = 0$ for $x \ge 0$. Then $\varphi - k * \varphi = f - \psi$ on all of $\R$.
2. Take Fourier transforms: $\bigl(1 - \hat k(\xi)\bigr)\, \hat\varphi(\xi) = \hat f(\xi) - \hat\psi(\xi)$, where $\hat\varphi$ and $\hat f$ are upper functions and $\hat\psi$ is a lower function.
3. Factor the symbol as $1 - \hat k = a_- \, a_+$. Here $a_+$ and $1/a_+$ are holomorphic and bounded in the upper half-plane. Also $a_-$ and $1/a_-$ are holomorphic and bounded in the lower half-plane.
4. Split $\hat f / a_- = g_+ + g_-$ into an upper and a lower part, for example with Cauchy integrals.
5. The equation becomes $a_+ \hat\varphi - g_+ = g_- - \hat\psi / a_-$. The left side extends to the upper half-plane and the right side to the lower half-plane, so together they define an entire function. Growth bounds and [[Liouville's theorem|0EHKVRF4J6]] show that it is a polynomial, often $0$.
6. Then $\hat\varphi = (g_+ + P)/a_+$ for that polynomial $P$, and $\varphi$ is recovered by the inverse Fourier transform.

## Remarks

The factorization in step 3 exists when $1 - \hat k$ has no zeros on $\R$ and its winding number about $0$ is zero.
Otherwise rational factors such as $\bigl((\xi - i)/(\xi + i)\bigr)^\nu$ appear, see [[Wiener–Hopf factorization|BYKP1V2AQN]].
The same steps apply to boundary value problems for partial differential equations, where step 1 comes from a transform in one variable along a half-line boundary.

Example: for $k(x) = \frac{1}{2} e^{-\abs{x}}$ one has $\hat k(\xi) = \frac{1}{1 + \xi^2}$, so $1 - \hat k(\xi) = \frac{\xi^2}{\xi^2 + 1} = \frac{\xi}{\xi - i} \cdot \frac{\xi}{\xi + i}$.
The factor $\xi/(\xi + i)$ is holomorphic in the upper half-plane and $\xi/(\xi - i)$ in the lower half-plane.
Both vanish at the real point $0$.
This zero of the symbol on $\R$ allows the solution $1 + x$ of the homogeneous equation, which grows linearly.

Non-example: a direct Fourier transform of the equation, without step 1, does not work, because the integral covers only $t \ge 0$ and the equation holds only for $x \ge 0$.
