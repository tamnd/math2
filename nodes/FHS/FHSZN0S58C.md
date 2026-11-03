---
tag: FHSZN0S58C
kind: statement
role: fact
name: Chilton–Colburn J-factor analogy
msc: [80A19, 76R05, 76R50]
uses: [6T2FKXGS25, C4KSBMR413, RJ2CK83N11]
about: [QFBG7W198Q]
sources:
  - url: https://en.wikipedia.org/wiki/Chilton_and_Colburn_J-factor_analogy
same_as:
  wikidata: Q3879391
  wikipedia: Chilton and Colburn J-factor analogy
---

## Statement

Consider forced flow with free-stream or mean speed $U$ along a surface, with no form drag, so that the drag is skin friction only.
Let $C_f$ be the skin friction coefficient, $\mathrm{St}$ the [[Stanton number|6T2FKXGS25]] and $\Pr$ the [[Prandtl number|C4KSBMR413]].
Let $\mathrm{St}_m = h_m / U$ be the mass transfer Stanton number, with mass transfer coefficient $h_m$.
Let $\mathrm{Sc} = \nu / D$ be the Schmidt number, with kinematic viscosity $\nu$ and diffusivity $D$.
The Colburn factors are $j_H = \mathrm{St} \, \Pr^{2/3}$ and $j_D = \mathrm{St}_m \, \mathrm{Sc}^{2/3}$.
For $0.6 < \Pr < 60$ and $0.6 < \mathrm{Sc} < 3000$, the following hold approximately:
$$j_H = \frac{C_f}{2}, \qquad j_D = \frac{C_f}{2}.$$

## Remarks

This is an empirical correlation, not a theorem.
For the laminar flat plate it agrees with the Blasius and Pohlhausen results, which give $\mathrm{St}_x \Pr^{2/3} = 0.332 \, \mathrm{Re}_x^{-1/2} = C_{f,x}/2$.
For $\Pr = 1$ it reduces to the [[Reynolds analogy|RJ2CK83N11]] $\mathrm{St} = C_f / 2$.
For turbulent flow in smooth pipes it holds roughly, which makes friction data a cheap source of heat and mass transfer estimates.
On bluff bodies the measured drag includes pressure drag, and the analogy with the total drag coefficient fails.

## Explanations

### L1 human

Friction, heat transfer and mass transfer at a wall are all carried by the same thin layer of fluid.
The Chilton–Colburn analogy says that, after a correction by a power of the Prandtl or Schmidt number, the three effects have the same size.
So an engineer who knows the friction can estimate how fast heat or a dissolved substance moves to the wall.

### L2 human

The exponent $2/3$ comes from the laminar flat-plate result $\mathrm{Nu}_x \propto \Pr^{1/3}$, since $\mathrm{St} = \mathrm{Nu} / (\mathrm{Re} \Pr)$.
The analogy extends the Reynolds analogy from $\Pr = 1$ to common liquids and gases.
Replacing $\Pr$ by $\mathrm{Sc}$ turns every heat transfer correlation of this form into a mass transfer correlation.
