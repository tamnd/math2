---
tag: 2SP692ZRAH
kind: example
name: Kelvin–Voigt material
msc: [74D05]
instance_of: [GCX1B3DAJN]
uses: [PQ8Z5HS2JR, JSSYGY0V87, YFTQJ7VY31, 0KPHENZ5S7]
sources:
  - url: https://en.wikipedia.org/wiki/Kelvin–Voigt_material
same_as:
  wikidata: Q3048149
  wikipedia: Kelvin–Voigt material
---

## Example

The *Kelvin–Voigt material* is the model of a linear spring of modulus $E > 0$ in parallel with a linear dashpot of viscosity $\eta > 0$.
In parallel the strain $\varepsilon$ is the same in both elements and the stresses add, so
$$\sigma = E \varepsilon + \eta \dot\varepsilon.$$
Let $\tau = \eta / E$ be the retardation time.
[[Creep|YFTQJ7VY31]]: a stress step $\sigma_0$ at time $0$ with $\varepsilon(0) = 0$ gives the linear equation $\tau \dot\varepsilon + \varepsilon = \sigma_0 / E$, whose solution is
$$\varepsilon(t) = \frac{\sigma_0}{E} \left(1 - e^{-t/\tau}\right),$$
so the creep compliance is $J(t) = (1 - e^{-t/\tau})/E$.
The strain approaches the elastic value $\sigma_0/E$ with a delay, which is the rate dependence of a [[viscoelastic|GCX1B3DAJN]] material.

## Remarks

Unlike the [[Maxwell material|PQ8Z5HS2JR]], the creep is bounded and fully recoverable after unloading.
A sudden strain step would need an infinite stress, since the dashpot cannot move instantly; in the sense of distributions the [[relaxation modulus|JSSYGY0V87]] is $E + \eta \delta(t)$, with $\delta$ the [[Dirac delta|0KPHENZ5S7]].
So the model describes creep and recovery well but stress relaxation poorly.

## Explanations

### L1 human

Put a spring and a piston in oil side by side, joined at both ends.
When you hang a weight on them, the oil slows the stretch, so the spring reaches its full extension only gradually.
Take the weight off and the spring slowly pulls everything back.
A rubber sole that sinks slowly when you step on it and slowly springs back behaves in this way.
