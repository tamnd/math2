---
tag: YFHBKVA8K1
kind: definition
name: Unit hydrograph
msc: [86A05]
defines: 2BXWR9MDJ5
uses: [2Z29JN3VES]
sources:
  - url: https://en.wikipedia.org/wiki/Hydrograph
---

## Definition

Let a drainage basin have area $A$, and let $D > 0$ be a time interval.
Excess rainfall is the part of the rainfall that becomes direct runoff, and direct runoff is the discharge at the outlet minus the base flow.
Suppose that a unit depth of excess rainfall falls at a uniform rate over the whole basin during the interval $[0, D]$.
The *$D$-hour unit hydrograph* of the basin is the function $U_D(t)$, $t \ge 0$, that gives the resulting direct runoff discharge at the outlet.
The model assumes that the basin is linear and time invariant.
Then, if excess rainfall depths $P_1, \dots, P_M$ (in units) fall during the successive intervals $[(m-1)D, mD]$, the direct runoff is
$$Q(t) = \sum_{m=1}^{M} P_m \, U_D\big(t - (m-1)D\big),$$
where $U_D(s) = 0$ for $s < 0$.

## Remarks

The total volume under a unit hydrograph equals the volume of one unit of excess rainfall over the basin: $\int_0^\infty U_D(t)\,dt = A \cdot (\text{unit depth})$.
For example, take $D = 1$ hour and sampled values $U_D = 0, 2, 5, 3, 1, 0$ at hours $0, \dots, 5$.
For depths $P_1 = 2$ and $P_2 = 1$, the runoff at hour $2$ is $2 \cdot 5 + 1 \cdot 2 = 12$, a discrete [[convolution|2Z29JN3VES]].
A non-example is the hydrograph of a storm of duration $D$ with two units of excess rainfall.
It is not a unit hydrograph, since the rainfall depth is not one unit; under linearity it equals $2 U_D$.
The limit $D \to 0$ gives the instantaneous unit hydrograph $u(t)$, the impulse response of the basin, and then $Q(t) = \int_0^t i(\tau)\, u(t - \tau)\, d\tau$ for an excess rainfall intensity $i$.
