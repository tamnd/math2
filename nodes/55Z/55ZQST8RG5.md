---
tag: 55ZQST8RG5
kind: example
name: de Sitter universe
msc: ["83F05", "83C15"]
instance_of: [H7PS83YCER]
uses: [ECJMS4VDTF, PPHFS2P4G4, WVKKDY9V61, 6XMAXW649B]
sources:
  - url: https://en.wikipedia.org/wiki/De_Sitter_universe
same_as:
  wikidata: Q3036474
  wikipedia: De Sitter universe
---

## Example

Let $\Lambda > 0$ be a [[cosmological constant|WVKKDY9V61]] and $H = \sqrt{\Lambda/3}$, in units with $c = 1$.
The *de Sitter universe* is the spatially flat [[Friedmann–Lemaître–Robertson–Walker metric|ECJMS4VDTF]] with no matter and scale factor $a(t) = e^{Ht}$:
$$ds^2 = -dt^2 + e^{2Ht} \left( dx^2 + dy^2 + dz^2 \right), \qquad t \in \R.$$

Check: here $k = 0$, $\rho = p = 0$ and $\dot a / a = H$ is constant.
The first [[Friedmann equation|PPHFS2P4G4]] reads $H^2 = \Lambda/3$, which holds by the choice of $H$.
The second reads $\ddot a / a = H^2 = \Lambda/3$, which also holds.
So the metric solves the vacuum Einstein equations with cosmological constant $\Lambda$.

## Remarks

The Hubble parameter is constant and the deceleration parameter is $q = -1$, so the expansion accelerates forever.
There is a cosmological event horizon at proper distance $1/H$ from every comoving observer, and no particle horizon.
These coordinates cover only half of the maximally symmetric [[de Sitter space|6XMAXW649B]]; slicings with $k = +1$, $a(t) = H^{-1}\cosh(Ht)$, and with $k = -1$, $a(t) = H^{-1}\sinh(Ht)$, describe the same spacetime or parts of it.
The model is the late-time limit of the Lambda-CDM model and the approximate geometry of the inflationary epoch.

## Explanations

### L1 human

The de Sitter universe is empty space with a positive cosmological constant.
Its size grows exponentially: in each fixed interval of time, all distances are multiplied by the same factor.
Distant galaxies would eventually recede faster than light can catch up with them, so each observer is surrounded by a horizon.
It is the simplest model of an accelerating universe.
