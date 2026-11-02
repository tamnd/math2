---
tag: NSXT1MYFY8
kind: definition
name: Littlewood–Paley decomposition
msc: [42B25]
defines: D1PAT0K446
uses: [DPVM34ADZV, SASP14MA1Z, AES2T5JPFP]
sources:
  - url: https://en.wikipedia.org/wiki/Littlewood%E2%80%93Paley_theory
---

## Definition

Let $n \ge 1$, and let $\hat f(\xi) = \int_{\R^n} f(x) e^{-2\pi i x \cdot \xi} \, dx$ be the [[Fourier transform|DPVM34ADZV]], extended to [[tempered distributions|AES2T5JPFP]].
Fix a smooth function $\chi \colon \R^n \to [0, 1]$ with $\chi(\xi) = 1$ for $\abs{\xi} \le 1$ and $\chi(\xi) = 0$ for $\abs{\xi} \ge 2$.
Let $\psi(\xi) = \chi(\xi) - \chi(2\xi)$.
For $j \in \Z$ and $f$ a tempered distribution, the *Littlewood–Paley piece* $\Delta_j f$ is defined by
$$\widehat{\Delta_j f}(\xi) = \psi(2^{-j}\xi) \, \hat f(\xi).$$
The *Littlewood–Paley decomposition* of $f$ is the series $\sum_{j \in \Z} \Delta_j f$.

## Remarks

The function $\psi$ vanishes for $\abs{\xi} \le 1/2$ and for $\abs{\xi} \ge 2$, so $\widehat{\Delta_j f}$ is supported in $\set{2^{j-1} \le \abs{\xi} \le 2^{j+1}}$.
For $\xi \ne 0$ the sum telescopes: $\sum_{j = -N}^{M} \psi(2^{-j}\xi) = \chi(2^{-M}\xi) - \chi(2^{N+1}\xi)$, which tends to $1$ as $M, N \to \infty$.
Hence $f = \sum_{j \in \Z} \Delta_j f$ with convergence in $L^2(\R^n)$ for $f \in L^2(\R^n)$, and in the [[Lp space|SASP14MA1Z]] $L^p(\R^n)$ for $1 < p < \infty$.
Each $\Delta_j f = f * \check\psi_j$ is a convolution with the Schwartz function $\check\psi_j(x) = 2^{jn} \check\psi(2^j x)$, where $\check\psi$ is the inverse Fourier transform of $\psi$.
An inhomogeneous version keeps $\Delta_j$ for $j \ge 1$ and replaces all $j \le 0$ by the single low-frequency piece with multiplier $\chi$.

Example: if $\hat f$ vanishes outside $\set{2^{k-1} \le \abs{\xi} \le 2^{k+1}}$ for some $k \in \Z$, then $\Delta_j f = 0$ unless $j \in \set{k - 1, k, k + 1}$.
Indeed $\psi(2^{-j}\xi) \ne 0$ needs $2^{j-1} < \abs{\xi} < 2^{j+1}$, and this meets the support of $\hat f$ only when $k - 2 < j < k + 2$.

Non-example: the cut-offs $\mathbf{1}_{\set{2^j \le \abs{\xi} < 2^{j+1}}}$ also sum to $1$ on $\xi \ne 0$, but they are not smooth, so they do not fit this definition.
For $n \ge 2$ such sharp cut-offs are badly behaved on $L^p(\R^n)$ for $p \ne 2$, as Fefferman's ball multiplier theorem shows for the indicator of a ball.
