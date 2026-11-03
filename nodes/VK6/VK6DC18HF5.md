---
tag: VK6DC18HF5
kind: definition
name: Debye length
msc: [82D10, 82D15]
defines: ZSNW9FC08R
uses: [FC64B1A65B, GYNMZ9201M]
sources:
  - url: https://en.wikipedia.org/wiki/Debye_length
---

## Definition

Consider a medium of permittivity $\varepsilon$ at absolute temperature $T$ that contains mobile charge carriers of species $i = 1, \dots, s$.
Species $i$ has charge $q_i$ and mean number density $n_i \ge 0$, not all $n_i q_i^2$ zero, and the medium is neutral: $\sum_i n_i q_i = 0$.
Let $k_B$ be Boltzmann's constant.
The *Debye length* is
$$\lambda_D = \sqrt{\frac{\varepsilon k_B T}{\sum_i n_i q_i^2}}.$$

## Remarks

It is the length for which the linearized equation $\nabla^2 \varphi = \varphi / \lambda_D^2$ holds, obtained from [[Poisson's equation|FC64B1A65B]] when the carriers follow the [[Boltzmann distribution|GYNMZ9201M]] and the potential is weak.
Example: a $1{:}1$ salt such as NaCl at concentration $c$ has two species with $q = \pm e$ and $n = c N_A$, where $N_A$ is Avogadro's number, so $\lambda_D = \sqrt{\varepsilon k_B T / (2 c N_A e^2)}$.
In water at $25$ degrees Celsius this is about $0.304 / \sqrt{c}$ nanometres with $c$ in mol per litre, so about $0.96$ nm at $c = 0.1$.
Non-example: a gas of neutral molecules has no free charges, so the sum in the denominator is $0$ and there is no screening length.
For an electron plasma with immobile ions, the usual form is $\lambda_D = \sqrt{\varepsilon_0 k_B T_e / (n_e e^2)}$, where $T_e$ and $n_e$ are the electron temperature and density.

## Explanations

### L1 human

The formula balances thermal energy, which spreads the charges out, against electric attraction, which pulls them in.
A larger temperature or permittivity gives a longer length, and more or stronger charges give a shorter one.
