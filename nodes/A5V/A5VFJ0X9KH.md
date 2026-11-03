---
tag: A5VFJ0X9KH
kind: statement
role: fact
name: Henry's law
msc: [80A50, 80A10]
uses: [WVH4PVW64P, N7R0H2VNDJ, 5EKTEE00FZ, 57YCS65Z5T]
about: [WVH4PVW64P]
sources:
  - url: https://en.wikipedia.org/wiki/Henry%27s_law
same_as:
  wikidata: Q285804
  wikipedia: Henry's law
---

## Statement

Consider a volatile solute $B$ dissolved in a liquid solvent at temperature $T$.
Assume the solution is in [[thermodynamic equilibrium|5EKTEE00FZ]] with a gas phase in which $B$ has partial pressure $p_B$.
Let $x_B$ be the mole fraction of $B$ in the liquid.
Then, for dilute solutions,
$$p_B = K_H\, x_B \quad \text{in the limit } x_B \to 0.$$
That is, $p_B / x_B$ tends to a constant $K_H > 0$ as $x_B \to 0$.
The Henry constant $K_H$ depends on $T$ and on the pair of solute and solvent.

## Remarks

Assume the gas phase is an [[ideal gas|N7R0H2VNDJ]].
Then the law is equivalent to a form of the [[chemical potential|WVH4PVW64P]] of the solute: $\mu_B = \mu_B^{\infty}(T, p) + RT \ln x_B$, up to terms that vanish as $x_B \to 0$.
In general $K_H$ differs from the vapour pressure $p_B^*$ of pure $B$, so this is not [[Raoult's law|7MR97B1NER]] for the solute.
By the [[Gibbs–Duhem equation|57YCS65Z5T]], if the solute obeys Henry's law then the solvent obeys Raoult's law in the same dilute limit.
The amount of carbon dioxide dissolved in a sealed drink is set by the pressure of the gas above it.
When the bottle is opened the pressure drops and the gas comes out of solution.
Many conventions are in use: the law is also written with concentration or molality in place of mole fraction, and with the constant inverted.

## Explanations

### L1 human

Henry's law says that the amount of gas that dissolves in a liquid is proportional to the pressure of that gas above the liquid.
Double the pressure and twice as much gas dissolves.
This is why fizzy drinks are bottled under pressure, and why divers who rise too fast can get bubbles in their blood.

### L2 human

Henry's law and Raoult's law are the two limiting laws of dilute solutions: the solute follows Henry, the solvent follows Raoult.
Together they underlie the colligative properties, such as the lowering of the freezing point, at leading order in the solute fraction.
The temperature dependence of $K_H$ is described by a van 't Hoff type equation involving the enthalpy of solution.
