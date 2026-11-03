---
tag: VXFPHHXKXV
kind: definition
name: Initial mass function
msc: [85A35, 85A15]
defines: V46YZHA7P3
uses: [0ZY9DX8FBF]
sources:
  - url: https://en.wikipedia.org/wiki/Initial_mass_function
---

## Definition

Consider a population of stars that form together.
Let $m$ denote the mass of a star at birth, ranging over an interval $(m_{\min}, m_{\max})$ with $0 < m_{\min} < m_{\max}$.
The *initial mass function* of the population is a function $\xi \colon (m_{\min}, m_{\max}) \to [0, \infty)$ such that $\xi(m) \, dm$ is the number of stars born with mass in $[m, m + dm]$.
Equivalently, after normalising to total number $1$, it is the [[probability density function|0ZY9DX8FBF]] of the birth mass of a star drawn from the population.

## Remarks

Example: the Salpeter initial mass function, proposed in 1955, is $\xi(m) = A \, m^{-2.35}$ with a constant $A > 0$.
For it, equal small mass intervals at $m = 1$ and at $m = 10$ solar masses contain numbers of stars in the ratio $10^{2.35} \approx 224$.
Non-example: the present-day mass function of the stars in the solar neighbourhood is not an initial mass function, because massive stars have already died and are missing from the count.
Many authors use instead the density per logarithmic mass interval, $m \, \xi(m)$, which changes the power law exponent by $1$.
Observed initial mass functions flatten below about half a solar mass, so a single power law overestimates the number of very low-mass stars.
