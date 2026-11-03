---
tag: H2XT5TQJ7K
kind: example
name: Generalized Maxwell model
msc: [74D05]
instance_of: [GCX1B3DAJN]
uses: [PQ8Z5HS2JR, EEJR84RYFR, TXTNM6KXHE, JSSYGY0V87]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_Maxwell_model
same_as:
  wikidata: Q5532446
  wikipedia: Generalized Maxwell model
---

## Example

The *generalized Maxwell model*, also called the Maxwell–Wiechert model, is a spring of modulus $E_\infty \ge 0$ in parallel with $n$ [[Maxwell material|PQ8Z5HS2JR]] arms.
Arm $i$ has a spring of modulus $E_i > 0$ and a dashpot of viscosity $\eta_i > 0$, and relaxation time $\tau_i = \eta_i / E_i$.
In parallel the strain is common and the stresses add.
Under a strain step $\varepsilon_0$, arm $i$ carries the stress $E_i \varepsilon_0 e^{-t/\tau_i}$ and the lone spring carries $E_\infty \varepsilon_0$.
So the [[relaxation modulus|JSSYGY0V87]] is
$$G(t) = E_\infty + \sum_{i=1}^n E_i e^{-t/\tau_i},$$
which is a [[Prony series|TXTNM6KXHE]] when the $\tau_i$ are distinct.

## Remarks

For $n = 1$ it is the [[standard linear solid|EEJR84RYFR]], and for $n = 1$ and $E_\infty = 0$ it is the Maxwell material.
Conversely every Prony series with positive coefficients is the relaxation modulus of such a model, which is why measured relaxation data are fitted by it.

## Explanations

### L1 human

One Maxwell arm relaxes with a single time constant, but real polymers relax over many time scales at once.
Putting many Maxwell arms side by side, each with its own speed, gives a material that relaxes partly in seconds, partly in hours, and partly in years.
An extra spring alone keeps a lasting stiffness, so the material can behave as a solid in the long run.
