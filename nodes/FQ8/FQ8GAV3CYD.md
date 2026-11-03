---
tag: FQ8GAV3CYD
kind: definition
name: Rosseland approximation
msc: [80A21, 85A25]
defines: KR1VNY8XAT
uses: [FYYQNDT6X2, A2RMYX8A65, XBQBT9E7JT, 9YJZ1PP2Y8, 6JQVMS9Y7R, J027RJ924H]
sources:
  - url: https://en.wikipedia.org/wiki/Opacity
---

## Definition

Consider a [[participating medium|FYYQNDT6X2]] with refractive index $n$, spectral extinction coefficient $\beta_\lambda > 0$, and temperature field $T(x)$, in [[local thermodynamic equilibrium|J027RJ924H]].
Let $E_{b\lambda}(T)$ be the [[black-body|A2RMYX8A65]] spectral emissive power in the medium and $\sigma$ the [[Stefan–Boltzmann|6JQVMS9Y7R]] constant.
The *Rosseland mean extinction coefficient* $\beta_R$ is defined by
$$\frac{1}{\beta_R} = \frac{\int_0^\infty \beta_\lambda^{-1} \, \partial_T E_{b\lambda}(T) \, d\lambda}{\int_0^\infty \partial_T E_{b\lambda}(T) \, d\lambda}.$$
The *Rosseland approximation* replaces the radiative transfer equation by the radiative heat flux
$$q_r = -\frac{16 n^2 \sigma T^3}{3 \beta_R} \nabla T.$$
It is meant for optically thick media, in which the mean free path $1/\beta_\lambda$ is much smaller than the length over which $T$ changes.

## Remarks

The flux has the form of [[Fourier's law|9YJZ1PP2Y8]] with the radiative [[thermal conductivity|XBQBT9E7JT]] $k_R = 16 n^2 \sigma T^3 / (3 \beta_R)$.
The denominator in the definition of $\beta_R$ equals $4 n^2 \sigma T^3$.

Example: a grey medium, with $\beta_\lambda = \beta$ for all $\lambda$.
Then the two integrals differ by the factor $1/\beta$, so $\beta_R = \beta$ and $k_R = 16 n^2 \sigma T^3 / (3\beta)$.

Non-example: a thin gas layer between two walls, with optical thickness much less than $1$.
Radiation crosses it mostly without interaction, the optically thick condition fails, and the approximation gives wrong fluxes; it also fails within a few mean free paths of a wall.

In astrophysics the same weighted harmonic mean, per unit mass, is the Rosseland mean opacity.
