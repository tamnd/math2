---
tag: MXPYYSFZ6G
kind: definition
name: Recombination
msc: [85A40]
defines: EH021K5438
uses: [2JZQPRFZWS, J70F32P86W, 8K69WPX4GS]
sources:
  - url: https://en.wikipedia.org/wiki/Recombination_(cosmology)
---

## Definition

Consider an expanding universe with [[scale factor|J70F32P86W]] $a$ and [[redshift|8K69WPX4GS]] $z$.
Let $n_e$ be the number density of free electrons and $n_H$ the total number density of hydrogen nuclei.
The *ionisation fraction* is $x_e = n_e / n_H$.
*Recombination* is the epoch during which $x_e$ falls from close to $1$ to a small residual value, as electrons bind to protons into neutral hydrogen.
The *redshift of recombination* is often defined as the redshift at which $x_e = 1/2$.

## Remarks

Let $B = 13.6$ eV be the binding energy of hydrogen.
In thermal equilibrium, ignoring helium, the [[Saha equation|2JZQPRFZWS]] gives
$$\frac{x_e^2}{1 - x_e} = \frac{1}{n_H} \left( \frac{m_e k T}{2 \pi \hbar^2} \right)^{3/2} e^{-B / k T}.$$
Here $k$ is the Boltzmann constant, $m_e$ the electron mass and $\hbar$ the reduced Planck constant.
There are about a billion photons per baryon, so $n_H$ is tiny compared with the photon density.
Hence the right side stays large until $k T \approx 0.3$ eV, far below $B$.
This is a temperature of about $3000$ to $4000$ K.
A full treatment out of equilibrium gives a slower recombination.
It is largely complete by $z \approx 1100$, when the photons last scatter.

Example: the transition from $x_e \approx 1$ to $x_e \ll 1$ in hydrogen, between redshifts of roughly $1500$ and $1000$, is recombination.
Non-example: the earlier capture of electrons by helium nuclei, at higher redshifts, is called helium recombination; it does not satisfy the definition, which concerns hydrogen.
The later epoch when the gas became ionised again by the first stars and quasars is reionisation, not recombination.
