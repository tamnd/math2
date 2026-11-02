---
tag: FAMZ5Z5JK4
kind: definition
name: Besov space
msc: ["46E35", 42B35]
defines: 95QBBPRJ9E
uses: [AES2T5JPFP, CG9JEATW3Q, DPVM34ADZV, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Besov_space
---

## Definition

Let $n \ge 1$.
Let $\psi_0$ be a function in the [[Schwartz space|CG9JEATW3Q]] $\mathcal{S}(\R^n)$ with $\psi_0(\xi) = 1$ for $\abs{\xi} \le 1$ and $\psi_0(\xi) = 0$ for $\abs{\xi} \ge 2$.
For $j \ge 1$ let $\psi_j(\xi) = \psi_0(2^{-j} \xi) - \psi_0(2^{-j+1} \xi)$, so that $\sum_{j \ge 0} \psi_j = 1$ and $\psi_j$ is supported in $2^{j-1} \le \abs{\xi} \le 2^{j+1}$.
For a [[tempered distribution|AES2T5JPFP]] $f$, let $\Delta_j f = \mathcal{F}^{-1}(\psi_j \, \mathcal{F} f)$, where $\mathcal{F}$ is the [[Fourier transform|DPVM34ADZV]]; each $\Delta_j f$ is a smooth function.
Let $s \in \R$ and $0 < p, q \le \infty$.
The *Besov space* $B^s_{p,q}(\R^n)$ is the set of tempered distributions $f$ with
$$\norm{f}_{B^s_{p,q}} = \Big( \sum_{j=0}^{\infty} 2^{jsq} \norm{\Delta_j f}_{L^p(\R^n)}^q \Big)^{1/q} < \infty,$$
with the usual change to $\sup_{j \ge 0} 2^{js} \norm{\Delta_j f}_{L^p}$ when $q = \infty$.

## Remarks

A different choice of $\psi_0$ gives the same space with an equivalent quasi-norm.
For $p, q \ge 1$ the space is a Banach space; otherwise it is a complete quasi-normed space.
Here $L^p(\R^n)$ is the [[Lp space|SASP14MA1Z]], with the same formula when $0 < p < 1$.

Example: $B^s_{2,2}(\R^n)$ is the space $H^s(\R^n)$ of tempered distributions with $(1 + \abs{\xi}^2)^{s/2} \hat f \in L^2$.
Indeed, by Plancherel, $\norm{\Delta_j f}_{L^2}^2 = \int \psi_j^2 \abs{\hat f}^2 \, d\xi$ up to a constant factor, and $2^{2js}$ is comparable with $(1 + \abs{\xi}^2)^s$ on the support of $\psi_j$.

Non-example: the Dirac delta $\delta$ on $\R^n$ is not in $B^0_{1,q}(\R^n)$ for $q < \infty$.
Here $\Delta_j \delta = \mathcal{F}^{-1} \psi_j$, and for $j \ge 1$ this function is $x \mapsto 2^{(j-1)n} (\mathcal{F}^{-1} \psi_1)(2^{j-1} x)$.
So $\norm{\Delta_j \delta}_{L^1}$ is the same nonzero number for all $j \ge 1$, and the sum defining the norm diverges.
The same computation shows that $\delta \in B^0_{1,\infty}(\R^n)$.

For $s > 0$ not an integer, $B^s_{\infty,\infty}(\R^n)$ is the Hölder space $C^{k,\alpha}(\R^n)$ with $k = \floor{s}$ and $\alpha = s - k$.
