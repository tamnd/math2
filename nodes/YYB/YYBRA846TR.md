---
tag: YYBRA846TR
kind: statement
role: proposition
name: Bose–Einstein condensation
msc: [82B10, 82D50, 81V73]
uses: [R5HWSRAK4H, W733NG6P3M, FPYQWE8X12, 1XWBY4N0VT, 96CHDZKGQ0]
about: [W733NG6P3M, R5HWSRAK4H]
sources:
  - url: https://en.wikipedia.org/wiki/Bose%E2%80%93Einstein_condensate
  - url: https://en.wikipedia.org/wiki/Bose_gas
---

## Statement

Consider the ideal [[Bose gas|W733NG6P3M]] of spinless bosons of mass $m$ in a cube of volume $V$ in $\R^3$ with periodic boundary conditions.
Take the grand canonical ensemble at temperature $T > 0$.
Choose the chemical potential $\mu < 0$ so that the mean total number of particles is $N$.
Let $N_0$ be the mean number of particles in the lowest state, of energy $0$.
Let $\zeta$ be the [[Riemann zeta function|1XWBY4N0VT]], and define
$$T_c = \frac{2 \pi \hbar^2}{m k_B} \left( \frac{n}{\zeta(3/2)} \right)^{2/3}.$$
Then in the [[thermodynamic limit|FPYQWE8X12]] $N, V \to \infty$ with $n = N/V$ fixed,
$$\frac{N_0}{N} \to \begin{cases} 0 & \text{if } T \ge T_c, \\ 1 - (T / T_c)^{3/2} & \text{if } T < T_c. \end{cases}$$

## Remarks

The density of particles outside the lowest state is at most about $\zeta(3/2)/\lambda^3$, where $\lambda = h/\sqrt{2\pi m k_B T}$, and this bound is proportional to $T^{3/2}$.
Above $T_c$ the bound exceeds $n$, $\mu$ stays bounded away from $0$, and $N_0$ stays bounded, so $N_0/N \to 0$.
Below $T_c$ the excited states saturate, $\mu \to 0$, and the remaining fraction $1 - (T/T_c)^{3/2}$ must sit in the lowest state.
The dimension matters: in a two-dimensional box the excited-state density is $-\ln(1 - z)/\lambda^2$ with $z = e^{\mu / k_B T}$, which is unbounded as $z \to 1$, so the ideal gas does not condense at any $T > 0$.
A condensate was first produced in the laboratory in 1995, in a dilute ultracold gas of rubidium atoms.

## Explanations

### L1 human

Cool a gas of bosons enough and a macroscopic fraction of all the particles falls into the single state of lowest energy.
This happens at a definite temperature $T_c$, not gradually at absolute zero.
Below $T_c$ the condensed fraction grows from $0$ to $1$ as the temperature drops to $0$.
The condensate is a single quantum wave on a large scale, which is why it shows interference and superfluid flow.

### L2 human

The result is the simplest example of a phase transition caused only by quantum statistics, without any interaction.
It comes from the bound $g_{3/2}(z) \le \zeta(3/2)$ for the [[polylogarithm|96CHDZKGQ0]] in the formula for the density of the [[Bose gas|W733NG6P3M]].
The free energy is not analytic at $T_c$; the specific heat has a cusp there in three dimensions.
Interactions change the picture: weak repulsion is treated by Bogoliubov theory, and superfluid helium-4 is a strongly interacting relative.
