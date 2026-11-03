---
tag: XXVTZXXWWB
kind: definition
name: Tidal harmonic constituents
msc: [86A05, 42A16]
defines: Y07010W5HJ
uses: [2E2KCFNMHE, G12KXDHPPS]
sources:
  - url: https://en.wikipedia.org/wiki/Theory_of_tides
---

## Definition

Expand the [[tide-generating potential|2E2KCFNMHE]] of the Moon and the Sun at a fixed place as a sum of cosines in time.
Each term has an angular frequency $\sigma$ that is an integer combination of six astronomical rates:
$$\sigma = k_1 \omega_1 + k_2 \omega_2 + \cdots + k_6 \omega_6, \qquad k_1, \dots, k_6 \in \Z.$$
Here $\omega_1, \omega_2, \omega_3$ are the rates of the mean lunar time and of the mean longitudes of the Moon and the Sun.
The rates $\omega_4, \omega_5, \omega_6$ are those of the longitudes of the lunar perigee, the lunar node and the solar perigee.
The *harmonic model* of the tide at a place is
$$\zeta(t) = Z_0 + \sum_{j=1}^{J} H_j \cos(\sigma_j t + \chi_j - G_j).$$
Here $\sigma_j$ are such astronomical frequencies, and $\chi_j$ is the astronomical phase of the term at $t = 0$.
The amplitude $H_j \ge 0$ and the phase lag $G_j$ are local constants, and $Z_0$ is the mean level.
The term of index $j$ is the *tidal harmonic constituent* of frequency $\sigma_j$.

## Remarks

Example: the principal lunar semidiurnal constituent $M_2$ has period $12.4206$ h, and the principal solar $S_2$ has period $12$ h exactly.
The lunisolar diurnal $K_1$ has period $23.9345$ h, and the principal lunar diurnal $O_1$ has period $25.8193$ h.
Adding $M_2$ and $S_2$ of amplitudes $H_M > H_S$ gives a beat with range between $2(H_M - H_S)$ and $2(H_M + H_S)$, with period about $14.77$ days: the spring–neap cycle.
Non-example: a storm surge is not a constituent; it is not periodic with an astronomical frequency.
In practice slow modulations, mainly by the lunar node with period about $18.6$ years, are included as nodal factors multiplying $H_j$ and corrections to the phase.
Shallow-water constituents, such as $M_4$ with twice the frequency of $M_2$, arise from nonlinear effects and are added to the model in the same form.
The coefficients $(k_1, \dots, k_6)$ of a constituent are encoded by its [[Doodson number|YZ4RBHA6E7]].
