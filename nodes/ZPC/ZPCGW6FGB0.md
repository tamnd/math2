---
tag: ZPCGW6FGB0
kind: statement
role: fact
name: Landauer's principle
msc: [82B30, 94A17, 80A05]
uses: [T11MGWEKJ3, SPY89W0RJ7, CY4GJQGF06, KK46Q2YV1D]
about: [SPY89W0RJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Landauer%27s_principle
same_as:
  wikidata: Q657486
  wikipedia: Landauer's principle
---

## Statement

Let a physical memory store one bit: its states form two disjoint classes, the logical states $0$ and $1$.
Let the memory be in contact with a heat bath at absolute [[temperature|KK46Q2YV1D]] $T$, and let it hold $0$ or $1$ with probability $1/2$ each.
Let a physical process reset the memory to the logical state $0$, whatever the initial state was.
Then the mean [[heat|CY4GJQGF06]] $Q$ released into the bath satisfies
$$Q \ge k_B T \ln 2,$$
where $k_B$ is the Boltzmann constant.

## Remarks

The idea is that the reset lowers the [[entropy|SPY89W0RJ7]] of the memory by $k_B \ln 2$, since two equally likely logical states become one.
The [[second law|T11MGWEKJ3]] for memory and bath together then forces the bath entropy to grow by at least $k_B \ln 2$, that is, heat at least $k_B T \ln 2$ must flow into the bath.
At room temperature, $T = 300$ K, the bound is about $2.9 \times 10^{-21}$ J per bit.
Logically reversible operations, which are injective on logical states, are not subject to this bound.
The bound was stated by Rolf Landauer in 1961, and it was observed in experiments with a colloidal particle in a double-well potential in 2012.

## Explanations

### L1 human

Forgetting costs energy.
Wiping one bit of memory must give off at least a tiny amount of heat, $k_B T \ln 2$.
The reason is that wiping makes the memory more ordered, and the second law says that the disorder must go somewhere, into the surroundings as heat.

### L2 human

Landauer's principle links information theory and thermodynamics: one bit of Shannon information corresponds to $k_B \ln 2$ of thermodynamic entropy.
It sets a lower bound on the energy use of irreversible computation, far below what present computers use.
It is the key to the standard resolution of the paradox of Maxwell's demon, in the analysis of Charles Bennett.
