---
tag: TE7MC2EXEC
kind: definition
name: Geomagnetic secular variation
msc: [86A25]
defines: JXVMPHF681
uses: [NDPHH8SR3E, PGPW2Y7GPD]
sources:
  - url: https://en.wikipedia.org/wiki/Geomagnetic_secular_variation
---

## Definition

Let $B_{\mathrm{int}}(x, t)$ be the internal part of [[Earth's magnetic field|NDPHH8SR3E]], averaged over times of about a year to remove external variations.
The *geomagnetic secular variation* is its rate of change $\partial_t B_{\mathrm{int}}(x, t)$, on time scales from about a year to several centuries.
Let $g_n^m(t)$ and $h_n^m(t)$ be the internal Gauss coefficients of [[Gauss's spherical harmonic analysis|PGPW2Y7GPD]].
The *secular variation coefficients* are $\dot g_n^m = \frac{d g_n^m}{dt}$ and $\dot h_n^m = \frac{d h_n^m}{dt}$, and
$$\partial_t B_{\mathrm{int}} = -\nabla \Bigl( a \sum_{n \ge 1} \sum_{m=0}^{n} \Bigl(\frac{a}{r}\Bigr)^{n+1} \bigl(\dot g_n^m \cos m\phi + \dot h_n^m \sin m\phi\bigr) P_n^m(\cos\theta) \Bigr).$$

## Remarks

Example: in the axial dipole part, $B_r$ at the north geographic pole equals $2 g_1^0$.
So a coefficient $\dot g_1^0 = 10$ nT per year changes it by $20$ nT per year.
Since $g_1^0 < 0$ at present, a positive $\dot g_1^0$ means a weakening dipole.
Non-example: the daily variation and magnetic storms are changes of the external field with periods of hours to days, so they are not secular variation.
Reversals and excursions are changes over thousands of years and more, and are usually treated separately, although secular variation is part of the same core process.
Abrupt changes in the second time derivative of the field, called geomagnetic jerks, interrupt otherwise smooth secular variation every few years to decades.

## Explanations

### L1 human

Secular variation is how fast the core field changes from year to year.
Field models list it as a yearly rate of change for each Gauss coefficient.
