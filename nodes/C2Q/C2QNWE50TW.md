---
tag: C2QNWE50TW
kind: statement
role: fact
name: Principle of minimum energy
msc: [80A05, 80A10]
uses: [GYNNJBMTCP, 5EKTEE00FZ, SPY89W0RJ7, F6JVQ12X43, TY49WH2PPB]
about: [F6JVQ12X43, 5EKTEE00FZ]
sources:
  - url: https://en.wikipedia.org/wiki/Principle_of_minimum_energy
same_as:
  wikidata: Q3743693
  wikipedia: Principle of minimum energy
---

## Statement

Let a composite [[thermodynamic system|GYNNJBMTCP]] have fixed total [[entropy|SPY89W0RJ7]] $S$, total volume $V$ and total amounts of substance $N$.
Let $x$ denote the internal variables left free after some internal constraints are removed.
Then in [[equilibrium|5EKTEE00FZ]] the values of $x$ minimise the total [[internal energy|F6JVQ12X43]] $U(S, V, N; x)$.
The minimum is over all values of $x$ compatible with the fixed totals.

## Remarks

The principle is equivalent to the [[principle of maximum entropy|TY49WH2PPB]], given that temperature is positive, that is, $S$ increases with $U$.
Suppose the energy were not minimal at an equilibrium state.
Then one could withdraw some energy as work at constant entropy, and give it back as heat.
The energy would return to its old value while the entropy would increase, so the entropy was not maximal, a contradiction.
Example: for two subsystems exchanging volume at fixed entropies, minimising $U_1(S_1, V_1) + U_2(S_2, V - V_1)$ gives $p_1 = p_2$, where $p_i = -\partial U_i / \partial V_i$ is the pressure.

## Explanations

### L1 human

A ball rolls to the bottom of a bowl: mechanical systems settle at minimum energy.
Thermodynamic systems do the same, provided their entropy is held fixed.

### L2 human

The minimum energy principle is the version of the maximum entropy principle in the energy representation.
Its Legendre transforms give the minimum principles for the other potentials.
For example, at fixed temperature and volume the Helmholtz free energy is minimal in equilibrium, and at fixed temperature and pressure the Gibbs free energy is.
