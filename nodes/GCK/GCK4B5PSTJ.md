---
tag: GCK4B5PSTJ
kind: statement
role: fact
name: Third law of thermodynamics
msc: [80A05, 80A10]
uses: [SPY89W0RJ7, AJ8M9MGZGF, 5EKTEE00FZ, 9MVG566SX3, B06S5CKP74, SYYGZ18FF5]
about: [SPY89W0RJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Third_law_of_thermodynamics
same_as:
  wikidata: Q29166
  wikipedia: Third law of thermodynamics
---

## Statement

Let a system be in internal [[equilibrium|5EKTEE00FZ]].
As its [[thermodynamic temperature|AJ8M9MGZGF]] $T$ tends to $0^+$, its [[entropy|SPY89W0RJ7]] tends to a constant $S_0$.
This constant does not depend on the other state variables, such as pressure, volume or magnetic field.
In Planck's form, $S_0 = 0$ for a perfect crystal.

## Remarks

Two other common forms are the [[Nernst heat theorem|9MVG566SX3]] and the [[unattainability principle|B06S5CKP74]].
One consequence concerns [[heat capacities|SYYGZ18FF5]].
Along a path at fixed external parameters, $S(T) - S(T_1) = \int_{T_1}^{T} C(\tau) / \tau \, d\tau$, where $C$ is the heat capacity.
Since $S$ has a finite limit at $0$, the integral must converge at $0$, so $C$ cannot tend to a positive limit as $T \to 0^+$.
In practice $C(T) \to 0$ as $T \to 0^+$.
The law does not hold for glasses and other systems frozen out of equilibrium, which keep a nonzero residual entropy.

## Explanations

### L1 human

As a system gets colder and colder, its entropy settles down to a fixed lowest value.
For a perfect crystal this lowest value is zero: there is only one way to arrange it.

### L2 human

The third law fixes the additive constant in the entropy, which the second law leaves free.
So one can speak of absolute entropies and tabulate them.
It also forces heat capacities and thermal expansion coefficients to vanish at absolute zero.
