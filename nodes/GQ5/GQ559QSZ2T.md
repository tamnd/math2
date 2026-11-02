---
tag: GQ559QSZ2T
kind: definition
name: Fourier transform of tempered distributions
msc: [46F12, 42B10]
defines: 5PVSQXCTCT
uses: [0KPHENZ5S7]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_transform
---

## Definition

Let $n \ge 1$, let $\mathcal{S}(\R^n)$ be the [[Schwartz space|CG9JEATW3Q]], and let $\mathcal{S}'(\R^n)$ be the space of [[tempered distributions|AES2T5JPFP]].
For $\varphi \in \mathcal{S}(\R^n)$, let
$$\mathcal{F}\varphi(\xi) = \int_{\R^n} \varphi(x)\, e^{-2\pi i x \cdot \xi}\, dx$$
be its [[Fourier transform|DPVM34ADZV]].
For $T \in \mathcal{S}'(\R^n)$, the *Fourier transform* $\mathcal{F}T$ is the tempered distribution given by
$$\langle \mathcal{F}T, \varphi \rangle = \langle T, \mathcal{F}\varphi \rangle \quad \text{for all } \varphi \in \mathcal{S}(\R^n).$$

## Remarks

The definition makes sense because $\mathcal{F}$ is a continuous linear bijection of $\mathcal{S}(\R^n)$ onto itself.
For an integrable function $f$, viewed as a tempered distribution, $\mathcal{F}f$ is the usual Fourier transform; this follows from Fubini's theorem, $\int (\mathcal{F}f)\varphi = \int f (\mathcal{F}\varphi)$.
On $\mathcal{S}'(\R^n)$, $\mathcal{F}$ is a linear bijection, and $\mathcal{F}(\partial_j T) = 2\pi i \xi_j\, \mathcal{F}T$.

Example: for the [[Dirac delta|0KPHENZ5S7]] $\delta$ at $0$, $\langle \mathcal{F}\delta, \varphi \rangle = \mathcal{F}\varphi(0) = \int \varphi(x)\, dx$.
So $\mathcal{F}\delta$ is the constant function $1$.
By the Fourier inversion formula, $\mathcal{F}1 = \delta$ in the same way.

Non-example: on $\R$, the function $e^{\abs{x}}$ is locally integrable but does not define a tempered distribution.
For the Schwartz function $\varphi(x) = 1/\cosh(x/2)$, the integral $\int e^{\abs{x}} \varphi(x)\, dx$ diverges.
So the formula above does not define a Fourier transform of $e^{\abs{x}}$ as a tempered distribution.
