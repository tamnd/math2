---
tag: HT40Z8QRYG
kind: definition
name: Fourier–Stieltjes transform of a measure
msc: [43A25, 43A10]
defines: FZQ7MVMPTN
uses: [ZR09S9R3AW, FMW57WNPDB, 8E2CDA2WSV, HZNEQQBCW4, NY6TYHRGMS, VHN5VW5Q92, 5X8PK7H6W3]
sources:
  - url: https://en.wikipedia.org/wiki/Pontryagin_duality
---

## Definition

Let $G$ be a [[locally compact abelian group|ZR09S9R3AW]] with [[Pontryagin dual|FMW57WNPDB]] $\widehat{G}$.
Let $M(G)$ be the [[measure algebra|8E2CDA2WSV]] of $G$, the space of finite [[complex|NY6TYHRGMS]] [[Radon measures|HZNEQQBCW4]] on $G$.
The *Fourier–Stieltjes transform* of $\mu \in M(G)$ is the function $\widehat{\mu} \colon \widehat{G} \to \C$ given by
$$\widehat{\mu}(\chi) = \int_G \overline{\chi(x)} \, d\mu(x), \qquad \chi \in \widehat{G}.$$

## Remarks

The integral exists because $\abs{\chi(x)} = 1$ and $\mu$ has finite total variation $\norm{\mu}$, so $\abs{\widehat{\mu}(\chi)} \le \norm{\mu}$.
The function $\widehat{\mu}$ is bounded and uniformly continuous on $\widehat{G}$, and $\widehat{\mu * \nu} = \widehat{\mu}\,\widehat{\nu}$ for the convolution of measures.

Example: the Dirac measure $\delta_a$ at $a \in G$ is in $M(G)$, and $\widehat{\delta_a}(\chi) = \overline{\chi(a)}$.
In particular $\widehat{\delta_0} = 1$, which does not vanish at infinity when $\widehat{G}$ is not compact.

Example: if $d\mu = f \, dx$ with $f \in L^1(G)$ and $dx$ a Haar measure, then $\widehat{\mu}$ is the [[Fourier transform|VHN5VW5Q92]] $\widehat{f}$.

Non-example: Lebesgue measure on $\R$ is a Radon measure, but it is not finite, so it is not in $M(\R)$, and $\int_\R e^{-2\pi i \xi x}\, dx$ diverges.

For $G = \R^n$ and $\chi_\xi(x) = e^{2\pi i x \cdot \xi}$, this is the classical [[Fourier–Stieltjes transform|5X8PK7H6W3]].
Some authors use $\chi(x)$ in place of $\overline{\chi(x)}$, which replaces $\widehat{\mu}(\chi)$ by $\widehat{\mu}(\overline{\chi})$.
