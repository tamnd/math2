---
tag: YG3QV4FZQF
kind: statement
role: fact
name: Arrhenius equation
msc: [80A30, "92E20"]
uses: [TTH05RV6SW, 0J0FCWV32D]
about: [TTH05RV6SW]
sources:
  - url: https://en.wikipedia.org/wiki/Arrhenius_equation
same_as:
  wikidata: Q507505
  wikipedia: Arrhenius equation
---

## Statement

Let $k(T)$ be the rate constant of the [[rate equation|TTH05RV6SW]] of a reaction at absolute temperature $T > 0$.
Over a range of temperatures, there are constants $A > 0$ and $E_a > 0$ such that
$$k(T) = A \exp\left(-\frac{E_a}{RT}\right).$$
Here $R$ is the molar gas constant and $\exp$ is the [[exponential function|0J0FCWV32D]].
The constant $A$ is the *pre-exponential factor* and $E_a$ is the *activation energy* of the reaction.

## Remarks

The equation is an empirical law; it holds well for many reactions over moderate temperature ranges, with $A$ and $E_a$ treated as constant.
A heuristic reason is that only collisions with energy at least $E_a$ per mole lead to reaction, and by the Boltzmann distribution the fraction of such collisions is about $e^{-E_a/(RT)}$.
Taking logarithms gives $\ln k = \ln A - (E_a/R)(1/T)$, so the plot of $\ln k$ against $1/T$ is a line of slope $-E_a/R$; this is how $E_a$ is measured.
Example: with $E_a = 50\ \mathrm{kJ/mol}$, going from $298\ \mathrm{K}$ to $308\ \mathrm{K}$ multiplies $k$ by $\exp\big((E_a/R)(1/298 - 1/308)\big) \approx e^{0.655} \approx 1.9$.
This is the origin of the rule of thumb that a reaction rate roughly doubles for a rise of $10$ degrees near room temperature.
Transition state theory gives a refined form in which the pre-exponential factor itself depends on $T$.

## Explanations

### L1 human

Reactions go faster when it is hotter, and the Arrhenius equation says how much faster.
Molecules must hit each other hard enough to climb an energy barrier, the activation energy.
Heating makes hard hits much more common, and the share of such hits grows like $e^{-E_a/(RT)}$.
So a small rise in temperature can cause a large rise in speed.

### L2 human

In kinetics, the Arrhenius law gives the temperature dependence of the rate constants that enter rate equations and mass-action systems.
The Arrhenius plot of $\ln k$ against $1/T$ is the standard way to extract an activation energy from measured rates.
A curved Arrhenius plot is a sign that the mechanism changes with temperature or that the pre-exponential factor depends on $T$.
