---
tag: ZZCNP3N36B
kind: statement
role: proposition
name: Chapman–Jouguet condition
msc: [76L05, 80A25, 76V05]
uses: [FBR0PYYJJ7, FRVV0NHBXT, SN4J6KP03C, S4XMYJ3V42]
about: [FBR0PYYJJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Chapman%E2%80%93Jouguet_condition
same_as:
  wikidata: Q2992261
  wikipedia: Chapman–Jouguet condition
---

## Statement

Consider a steady planar [[detonation|FBR0PYYJJ7]] modelled as a discontinuity in a gas with a smooth equation of state.
The unburnt gas has pressure $p_1$ and specific volume $v_1 = 1/\rho_1$, and the reaction releases a heat $q > 0$ per unit mass.
For a wave speed $D > 0$, let the mass flux be $m = \rho_1 D$.
The burnt states $(v, p)$ compatible with the conservation of mass and momentum lie on the Rayleigh line $p - p_1 = -m^2 (v - v_1)$.
The burnt states compatible with the conservation of energy lie on the reactive Hugoniot curve $e(p, v) - e(p_1, v_1) + \tfrac12 (p + p_1)(v - v_1) = q$.
Here $e$ is the specific internal energy without chemical energy.
Assume that the burnt gas has convex isentropes in the $(v, p)$ plane and that the detonation branch of the reactive Hugoniot curve is convex.
Then:

1. There is a smallest speed $D_{CJ}$ for which the Rayleigh line meets the detonation branch. For $D = D_{CJ}$ the line is tangent to the branch at a single point, the Chapman–Jouguet point.
2. For $D > D_{CJ}$ the Rayleigh line meets the detonation branch in two points, the strong and the weak detonation. For $D < D_{CJ}$ it does not meet it.
3. At the Chapman–Jouguet point the burnt gas moves away from the front at exactly its own [[speed of sound|SN4J6KP03C]]. That is, $m^2 v^2 = c^2$ for the burnt state.

## Remarks

Clauses 1 and 2 follow from the convexity of the detonation branch: the slope $-m^2$ of the Rayleigh line through the fixed point $(v_1, p_1)$ decreases as $D$ grows.
For clause 3, along the Hugoniot curve one has $T\, ds = \tfrac12 (v_1 - v)\, dp + \tfrac12 (p - p_1)\, dv$ by the first law of thermodynamics, which vanishes where the Rayleigh line is tangent to the Hugoniot curve.
So at the tangent point the Hugoniot curve is tangent to the isentrope, and $m^2 = -(\partial p/\partial v)_s = c^2/v^2$, which says that the burnt gas speed $mv$ relative to the front equals $c$.
The Chapman–Jouguet hypothesis, which goes beyond the statement, says that an unsupported detonation travels at the speed $D_{CJ}$.
Measured detonation speeds in many gaseous mixtures are close to $D_{CJ}$.

## Explanations

### L1 human

A detonation could, in principle, run at many speeds, as far as the conservation laws are concerned.
There is a slowest possible one, and at that speed the burnt gas leaves the front at exactly the speed of sound.
Chapman and Jouguet proposed that a freely running detonation picks this speed, and experiments agree well.

### L2 human

The condition closes the jump relations, which otherwise leave the speed as a free parameter.
At the Chapman–Jouguet point the burnt gas leaves at the speed of sound, so rarefaction waves behind the front cannot overtake it.
Behind a strong detonation the flow is subsonic, so rarefactions overtake and weaken it unless a piston supports it.
Weak detonations are usually excluded by the structure of the reaction zone.
The [[ZND model|8KJJKCR26M]] resolves the reaction zone and recovers the Chapman–Jouguet speed as the speed of the self-sustained steady wave.
