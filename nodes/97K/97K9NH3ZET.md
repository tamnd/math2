---
tag: 97K9NH3ZET
kind: definition
name: Maxwell–Boltzmann statistics
msc: [82B05, 82D05]
defines: B60C1S87XB
uses: [GYNMZ9201M, 1C5S72A9JX]
sources:
  - url: https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_statistics
---

## Definition

Consider a system of non-interacting particles in thermal equilibrium at temperature $T > 0$.
Let the single-particle energy levels be $\varepsilon_1, \varepsilon_2, \ldots$, where level $i$ has degeneracy $g_i \ge 1$.
Let $k_B$ be the Boltzmann constant, $\beta = 1/(k_B T)$, and $\mu$ the chemical potential.
The particles obey *Maxwell–Boltzmann statistics* if the mean number of particles in level $i$ is
$$\bar n_i = g_i \, e^{-\beta (\varepsilon_i - \mu)}.$$
For a fixed total number $N$ of particles this reads
$$\frac{\bar n_i}{N} = \frac{g_i e^{-\beta \varepsilon_i}}{Z}, \qquad Z = \sum_j g_j e^{-\beta \varepsilon_j},$$
where $Z$ is the single-particle partition function, assumed finite.

## Remarks

Example: take two levels, $\varepsilon_1 = 0$ and $\varepsilon_2 = \varepsilon > 0$, each with $g_i = 1$.
Then $Z = 1 + e^{-\beta \varepsilon}$, and the fractions are $1/(1 + e^{-\beta\varepsilon})$ and $e^{-\beta\varepsilon}/(1 + e^{-\beta\varepsilon})$.
They are positive and sum to $1$, and the upper level is less populated, as it should be.

Non-example: for fermions the mean occupation of one state is $1/(e^{\beta(\varepsilon - \mu)} + 1)$, which is never of the form $e^{-\beta(\varepsilon - \mu)}$.
The two agree only approximately, when $e^{\beta(\varepsilon - \mu)} \gg 1$, that is when every state is rarely occupied.
The same holds for [[Bose–Einstein statistics|R5HWSRAK4H]], with $-1$ in place of $+1$.

The fractions $\bar n_i / N$ form the [[Boltzmann distribution|GYNMZ9201M]] over single-particle levels.
For a classical ideal gas, the continuum version over momenta gives the [[Maxwell–Boltzmann distribution|3QSVWQJX11]].
