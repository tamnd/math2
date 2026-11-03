---
tag: PQ8Z5HS2JR
kind: example
name: Maxwell material
msc: [74D05]
instance_of: [GCX1B3DAJN]
uses: [JSSYGY0V87, YFTQJ7VY31]
sources:
  - url: https://en.wikipedia.org/wiki/Maxwell_model
same_as:
  wikidata: Q3046593
  wikipedia: Maxwell model
---

## Example

The *Maxwell material* is the model of a linear spring of modulus $E > 0$ in series with a linear dashpot of viscosity $\eta > 0$.
In series the stress $\sigma$ is the same in both elements and the strains add, so with $\sigma = E \varepsilon_1$ and $\sigma = \eta \dot\varepsilon_2$ one gets
$$\dot\varepsilon = \frac{\dot\sigma}{E} + \frac{\sigma}{\eta}.$$
Let $\tau = \eta / E$ be the relaxation time.
Relaxation: a strain step $\varepsilon_0$ at time $0$ gives $\sigma(0^+) = E \varepsilon_0$, and then $\dot\varepsilon = 0$ gives $\dot\sigma = -\sigma / \tau$, so the [[relaxation modulus|JSSYGY0V87]] is $G(t) = E e^{-t/\tau}$.
[[Creep|YFTQJ7VY31]]: a stress step $\sigma_0$ gives $\varepsilon(t) = \sigma_0 / E + \sigma_0 t / \eta$, so the creep compliance is $J(t) = 1/E + t/\eta$.
The stress depends on the past strain rates and fades with time, so the Maxwell material is [[viscoelastic|GCX1B3DAJN]].

## Remarks

The creep strain grows without bound under constant stress and the stress relaxes fully to $0$.
So the Maxwell material behaves like a fluid on long time scales and like a solid on short ones.
It does not describe the bounded creep of most polymers, which the Kelvin–Voigt material and the standard linear solid capture better.

## Explanations

### L1 human

Imagine a spring tied to a piston in a cylinder of oil.
Pull quickly and the spring stretches at once while the piston hardly moves.
Hold the pull and the piston slowly slides, so the spring relaxes and the force fades away.
Silly Putty behaves like this: it bounces when thrown, but flows into a puddle if left alone.
