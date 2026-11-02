---
tag: 8F1HPGFW4F
kind: definition
name: Bessel potential space
msc: ["46E35", 42B35]
defines: DVJM7NBSF2
uses: [AES2T5JPFP, DPVM34ADZV, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_potential
---

## Definition

Let $n \ge 1$, let $s \in \R$ and let $1 < p < \infty$.
Let $\mathcal{F}$ denote the [[Fourier transform|DPVM34ADZV]] on the space $\mathcal{S}'(\R^n)$ of [[tempered distributions|AES2T5JPFP]].
The *Bessel potential space* $H^{s,p}(\R^n)$ is the set of all $f \in \mathcal{S}'(\R^n)$ such that
$$J^s f = \mathcal{F}^{-1}\big[ (1 + \abs{\xi}^2)^{s/2} \, \mathcal{F} f \big]$$
is a function in the [[Lebesgue space|SASP14MA1Z]] $L^p(\R^n)$.
Its norm is $\norm{f}_{H^{s,p}} = \norm{J^s f}_{L^p}$.

## Remarks

The operator $J^{-s} = (I - \Delta)^{-s/2}$ is the *Bessel potential* of order $s$.
For $s > 0$ it is convolution with an integrable kernel $G_s$ whose Fourier transform is $(1 + \abs{\xi}^2)^{-s/2}$.
So for $s > 0$, $H^{s,p}(\R^n)$ is the set of functions $G_s * g$ with $g \in L^p(\R^n)$, and $\norm{G_s * g}_{H^{s,p}} = \norm{g}_{L^p}$.

Example: for $s = 0$ the multiplier is $1$, so $J^0 f = f$ and $H^{0,p}(\R^n) = L^p(\R^n)$ with the same norm.

Non-example: the constant function $f = 1$ is a tempered distribution, but it is not in any $H^{s,p}(\R^n)$.
Its Fourier transform is a multiple of the Dirac mass at $0$, and the multiplier equals $1$ at $\xi = 0$.
So $J^s 1 = 1$, which is not in $L^p(\R^n)$ for $p < \infty$.

For an integer $k \ge 0$ and $1 < p < \infty$, $H^{k,p}(\R^n)$ equals the [[Sobolev space|M4CEZ5K9HP]] $W^{k,p}(\R^n)$ with an equivalent norm.
The proof of this uses the boundedness of the Riesz transforms on $L^p$.
For $p = 2$, Plancherel's theorem gives $H^{s,2}(\R^n) = H^s(\R^n)$, the [[fractional Sobolev space|N6NX1VT837]].
Other notations are $L^p_s$, $H^s_p$ and $W^{s,p}$.
