---
tag: Z72JWTXM3W
kind: definition
name: Triebel–Lizorkin space
msc: ["46E35", 42B35]
defines: TBNP6KYW4Z
uses: [AES2T5JPFP, CG9JEATW3Q, DPVM34ADZV, SASP14MA1Z, 95QBBPRJ9E]
sources:
  - url: https://en.wikipedia.org/wiki/Triebel%E2%80%93Lizorkin_space
---

## Definition

Let $n \ge 1$.
Let $\psi_0 \in \mathcal{S}(\R^n)$, the [[Schwartz space|CG9JEATW3Q]], satisfy $\psi_0(\xi) = 1$ for $\abs{\xi} \le 1$ and $\psi_0(\xi) = 0$ for $\abs{\xi} \ge 2$, and for $j \ge 1$ let $\psi_j(\xi) = \psi_0(2^{-j} \xi) - \psi_0(2^{-j+1} \xi)$.
For a [[tempered distribution|AES2T5JPFP]] $f$, let $\Delta_j f = \mathcal{F}^{-1}(\psi_j \, \mathcal{F} f)$, where $\mathcal{F}$ is the [[Fourier transform|DPVM34ADZV]].
Let $s \in \R$, $0 < p < \infty$ and $0 < q \le \infty$.
The *Triebel–Lizorkin space* $F^s_{p,q}(\R^n)$ is the set of tempered distributions $f$ with
$$\norm{f}_{F^s_{p,q}} = \Big\| \Big( \sum_{j=0}^{\infty} 2^{jsq} \abs{\Delta_j f}^q \Big)^{1/q} \Big\|_{L^p(\R^n)} < \infty,$$
with the inner sum replaced by $\sup_{j \ge 0} 2^{js} \abs{\Delta_j f}$ when $q = \infty$.

## Remarks

A different choice of $\psi_0$ gives the same space with an equivalent quasi-norm, and for $p, q \ge 1$ it is a Banach space.
Compare the [[Besov space|95QBBPRJ9E]] $B^s_{p,q}$, where the $L^p$ norm is taken before the sum over $j$.
For $p = q$ the two definitions coincide, so $F^s_{p,p} = B^s_{p,p}$.

Example: for $1 < p < \infty$, $F^0_{p,2}(\R^n) = L^p(\R^n)$ with equivalent norms, where $L^p$ is the [[Lp space|SASP14MA1Z]].
This is the Littlewood–Paley theorem: $\norm{f}_{L^p}$ is comparable with $\norm{(\sum_j \abs{\Delta_j f}^2)^{1/2}}_{L^p}$.
More generally, $F^k_{p,2}(\R^n)$ is the Sobolev space $W^{k,p}(\R^n)$ for integers $k \ge 0$ and $1 < p < \infty$.

Non-example: a nonzero constant function $c$ is not in any $F^s_{p,q}(\R^n)$ with $p < \infty$.
Here $\Delta_0 c = c$, because $\mathcal{F} c$ is a multiple of the Dirac delta and $\psi_0(0) = 1$, and the constant $\abs{c}$ is not in $L^p(\R^n)$.
