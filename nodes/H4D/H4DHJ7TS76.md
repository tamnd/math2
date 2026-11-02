---
tag: H4DHJ7TS76
kind: definition
name: Continuous wavelet transform
msc: [42C40, 42A38, 94A12]
defines: 57FR21NDGV
uses: [2BBB8NY5ZA, SASP14MA1Z, DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_wavelet_transform
---

## Definition

Let $\psi \in L^2(\R)$ be a nonzero function that satisfies the [[admissibility condition|2BBB8NY5ZA]]
$$C_\psi = \int_\R \frac{\abs{\hat\psi(\xi)}^2}{\abs{\xi}} \, d\xi < \infty,$$
where $\hat\psi(\xi) = \int_\R \psi(t) e^{-2\pi i t \xi} \, dt$ is the [[Fourier transform|DPVM34ADZV]].
Let $f \in L^2(\R)$ (see [[Lp space|SASP14MA1Z]]).
Let $a \ne 0$ (the scale) and $b$ (the position) be real numbers.
The *continuous wavelet transform* of $f$ with respect to $\psi$ is
$$W_\psi f(a, b) = \frac{1}{\sqrt{\abs{a}}} \int_\R f(t) \, \overline{\psi\!\left(\frac{t - b}{a}\right)} \, dt.$$

## Remarks

The integral converges by the Cauchy–Schwarz inequality, and $\abs{W_\psi f(a, b)} \le \norm{f}_2 \norm{\psi}_2$.
Taking the Fourier transform in $b$ and using the Plancherel theorem gives Calderón's identity
$$\int_{\R \setminus \set{0}} \int_\R \abs{W_\psi f(a, b)}^2 \, db \, \frac{da}{a^2} = C_\psi \norm{f}_2^2.$$
So $f$ can be recovered from $W_\psi f$, in a weak sense, by $f = C_\psi^{-1} \int \int W_\psi f(a, b) \, \abs{a}^{-1/2} \psi((\cdot - b)/a) \, db \, da / a^2$.
Many authors take only $a > 0$; then the constant changes and, for real $\psi$, one obtains $\tfrac12 C_\psi$.

Example: the Mexican hat $\psi(t) = (1 - t^2) e^{-t^2/2}$ has $\hat\psi(\xi)$ equal to a constant times $\xi^2 e^{-2\pi^2 \xi^2}$, so $C_\psi < \infty$ and $W_\psi$ is defined.

Non-example: for the Gaussian $\psi(t) = e^{-\pi t^2}$, $\hat\psi(0) = 1$, and $C_\psi$ diverges near $\xi = 0$.
The formula for $W_\psi f$ still makes sense, but Calderón's identity fails, and this choice is excluded by the definition.
