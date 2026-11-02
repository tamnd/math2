---
tag: JKCFHKT13F
kind: definition
name: Fourier–Stieltjes transform
msc: ["42A38", "42B10", "43A25"]
defines: 5X8PK7H6W3
uses: [NY6TYHRGMS, 0WQXY32Q8D, DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_transform
---

## Definition

Let $n \ge 1$ and let $\mu$ be a finite [[complex measure|NY6TYHRGMS]] on the [[Borel sets|0WQXY32Q8D]] of $\R^n$.
The *Fourier–Stieltjes transform* of $\mu$ is the function $\hat\mu \colon \R^n \to \C$ given by
$$\hat\mu(\xi) = \int_{\R^n} e^{-2\pi i x \cdot \xi}\, d\mu(x), \qquad \xi \in \R^n.$$

## Remarks

The integral exists because the integrand has modulus $1$ and $\mu$ has finite total variation $\norm{\mu}$.
So $\abs{\hat\mu(\xi)} \le \norm{\mu}$, and $\hat\mu$ is uniformly continuous on $\R^n$.

Example: the Dirac measure $\delta_a$ at a point $a \in \R^n$ is a finite measure, and $\hat\delta_a(\xi) = e^{-2\pi i a \cdot \xi}$; in particular $\hat\delta_0 = 1$.

Example: if $d\mu = f\, dx$ with $f \in L^1(\R^n)$, then $\hat\mu$ is the usual [[Fourier transform|DPVM34ADZV]] $\hat f$.

Non-example: Lebesgue measure on $\R$ is not finite, and $\int_\R e^{-2\pi i x \xi}\, dx$ diverges for every $\xi$; its transform exists only as a tempered distribution.

Unlike the transform of an integrable function, $\hat\mu$ need not tend to $0$ at infinity, as the example $\delta_0$ shows.
The transform is injective: $\hat\mu = 0$ implies $\mu = 0$.
It turns convolution of measures into products, $\widehat{\mu * \nu} = \hat\mu\, \hat\nu$.
For a probability measure $\mu$ on $\R$, the characteristic function $\varphi(t) = \int e^{itx}\, d\mu(x)$ equals $\hat\mu(-t / (2\pi))$.
On $\R$, writing $\mu$ through a function $F$ of bounded variation, the transform is the Stieltjes integral $\int e^{-2\pi i x \xi}\, dF(x)$.
