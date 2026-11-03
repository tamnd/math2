---
tag: QMSMPVY8ED
kind: statement
role: fact
name: Boltzmann's entropy formula
msc: [82B03, 82B30]
uses: [1SFZNN31JW, TDGEGWHXCT, S1NST0AG71]
about: [1SFZNN31JW, TDGEGWHXCT]
sources:
  - url: https://en.wikipedia.org/wiki/Boltzmann%27s_entropy_formula
same_as:
  wikidata: Q375553
  wikipedia: Boltzmann's entropy formula
---

## Statement

Let a macrostate of a system consist of $W \ge 1$ [[microstates|S1NST0AG71]], and let the system be described by the [[microcanonical ensemble|TDGEGWHXCT]] on them.
Each of these microstates then has probability $1/W$.
The [[Gibbs entropy|1SFZNN31JW]] of this ensemble is
$$S = k_B \ln W,$$
where $k_B$ is the Boltzmann constant.

## Remarks

The proof is one line: $S = -k_B \sum_{i=1}^{W} \frac{1}{W} \ln \frac{1}{W} = k_B \ln W$.
Boltzmann used $S = k_B \ln W$ as the definition of the entropy of a macrostate, and the formula is engraved on his tombstone in Vienna.
Example: $N$ independent spins with exactly $K$ pointing up give $W = \binom{N}{K}$.
By Stirling's formula, $S \approx -N k_B (x \ln x + (1 - x) \ln (1 - x))$ for large $N$, where $x = K/N$.
The formula needs the microstates to be equally likely; for a non-uniform distribution the Gibbs entropy is strictly smaller than $k_B \ln W$.

## Explanations

### L1 human

The entropy of a state of a large system is the logarithm of the number of ways to realize it, times a constant.
A macrostate that can be realized in many ways has high entropy, and an isolated system drifts towards such states simply because there are more of them.
The logarithm makes entropy add up when two independent systems are put together, since the numbers of ways multiply.

### L2 human

The formula links mechanics to thermodynamics: from the count $W(E, V, N)$ one gets $S$, and then temperature by $1/T = \partial S / \partial E$ and pressure by $p/T = \partial S / \partial V$.
It is the special case of the Gibbs entropy for the uniform distribution, and the uniform distribution maximizes the Gibbs entropy on $W$ states.
For continuous systems, $W$ is a phase-space volume divided by $N! \, h^{3N}$; this choice gives the [[Sackur–Tetrode equation|H2HGR6T5V0]] for the ideal gas.
