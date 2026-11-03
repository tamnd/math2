---
tag: C1XJ28NXZ7
kind: definition
name: Piezoelectricity
msc: [74F15, "74E10"]
defines: XYSSPAC1XG
uses: [KG2XWEMJ30, 8QS6QMJF5Z, V56XAESDNE, SX32X1D537]
sources:
  - url: https://en.wikipedia.org/wiki/Piezoelectricity
---

## Definition

Consider a linear dielectric elastic material with [[stress|KG2XWEMJ30]] $T_{kl}$ and [[infinitesimal strain|8QS6QMJF5Z]] $S_{ij}$.
Let $E_k$ be the electric field and $D_i$ the electric displacement, with indices from $1$ to $3$ and summation over repeated indices.
Its linear constitutive law in strain–charge form is the following.
$$S_{ij} = s^E_{ijkl} T_{kl} + d_{kij} E_k, \qquad D_i = d_{ikl} T_{kl} + \epsilon^T_{ik} E_k$$
Here $s^E$ is the elastic compliance at constant field, $\epsilon^T$ is the permittivity at constant stress, and $d_{ikl} = d_{ilk}$ is the tensor of piezoelectric coefficients.
The material is *piezoelectric* if $d \neq 0$.
The term $d_{ikl} T_{kl}$ is the direct piezoelectric effect and the term $d_{kij} E_k$ is the converse effect.

## Remarks

Example: $\alpha$-quartz has nonzero coefficients, among them $d_{111}$ (often written $d_{11}$ in Voigt notation), so a normal stress $T_{11}$ produces an electric displacement $D_1 = d_{111} T_{11}$ at zero field.
Non-example: a crystal with a centre of symmetry, such as rock salt, is not piezoelectric.
The inversion $x \mapsto -x$ leaves $S$, $T$ unchanged and reverses $E$, $D$, so it maps $d$ to $-d$.
Invariance under this symmetry forces $d = 0$.
With $E = 0$ the first equation is [[Hooke's law|V56XAESDNE]] in compliance form, the inverse of the [[elasticity tensor|SX32X1D537]] relation.
Of the $32$ crystal classes, $21$ lack a centre of symmetry, and all of these except the cubic class $432$ allow piezoelectricity.
