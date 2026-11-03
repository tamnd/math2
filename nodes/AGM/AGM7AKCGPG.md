---
tag: AGM7AKCGPG
kind: statement
role: fact
name: Byerlee's law
msc: [86A60, 74A55]
uses: [4XE2B2PBGC, KG2XWEMJ30, Q5CF1Z6179]
about: [4XE2B2PBGC]
sources:
  - url: https://en.wikipedia.org/wiki/Byerlee%27s_law
same_as:
  wikidata: Q3955356
  wikipedia: Byerlee's law
---

## Statement

Let a pre-existing fault surface in rock carry an effective normal stress $\sigma_n$ (normal stress minus pore-fluid pressure) and a shear stress $\tau$.
For most rock types, the shear stress needed to make the two sides slide is, to good approximation,
$$\tau = 0.85 \, \sigma_n \quad \text{for } \sigma_n < 200 \text{ MPa},$$
$$\tau = 50 \text{ MPa} + 0.6 \, \sigma_n \quad \text{for } 200 \text{ MPa} \leq \sigma_n \leq 1700 \text{ MPa}.$$

## Remarks

This is an empirical law, found by Byerlee in 1978 from a compilation of laboratory [[friction|4XE2B2PBGC]] experiments on many rock types.
It has the form of a Coulomb friction law, with friction coefficients $0.85$ and $0.6$; see [[Mohr–Coulomb theory|Q5CF1Z6179]].
Its most striking feature is that it hardly depends on the rock type.
Some minerals, notably several clays, are weaker and do not follow it.
Example: at $\sigma_n = 100$ MPa, sliding needs $\tau = 85$ MPa; at $\sigma_n = 500$ MPa it needs $\tau = 350$ MPa.
The stresses are components of the [[Cauchy stress tensor|KG2XWEMJ30]] on the fault plane, with compression taken positive.

## Explanations

### L1 human

How hard must you push to make one block of rock slide over another?
Byerlee found that the answer is roughly the same for granite, sandstone and most other rocks: about 0.6 to 0.85 times the force that presses the blocks together.
This makes it possible to estimate the strength of faults deep in the crust without knowing exactly what rock they cut.

### L2 human

Since the normal stress grows with depth through the weight of the rock, the law gives a frictional strength of the brittle crust that increases linearly with depth.
Combined with a creep law for deeper, hotter rock, this gives the strength envelope of the lithosphere.
Used in [[Anderson's theory of faulting|HMXJS7QFQN]] with the friction angle $\phi = \arctan 0.6 \approx 31^\circ$, it gives normal faults dipping near $60^\circ$ and thrust faults dipping near $30^\circ$.
Pore-fluid pressure lowers the effective normal stress and so weakens faults.
