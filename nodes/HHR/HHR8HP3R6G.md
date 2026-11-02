---
tag: HHR8HP3R6G
kind: statement
role: theorem
name: Variational principle for topological entropy
msc: [37B40, 37A35]
uses: [0TVJZYB6SH, 0VKD1TP7F3, 0VGFHTM75Y, 059TJN0NZ1, B232EZ1FMB, BDZYBXBFDE, X1D1C7VH6P, 1DHZ81S0YE]
about: [BDZYBXBFDE, X1D1C7VH6P]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_entropy
---

## Statement

Let $X$ be a [[compact|0TVJZYB6SH]] [[metric space|0VKD1TP7F3]] and let $f \colon X \to X$ be a [[continuous map|0VGFHTM75Y]].
Let $\mathcal{M}(f)$ be the set of $f$-[[invariant|B232EZ1FMB]] Borel [[probability measures|059TJN0NZ1]] on $X$.
For $\mu \in \mathcal{M}(f)$, let $h_\mu(f)$ be the [[Kolmogorov–Sinai entropy|X1D1C7VH6P]] of $f$ with respect to $\mu$.
Then the [[topological entropy|BDZYBXBFDE]] satisfies
$$h_{\mathrm{top}}(f) = \sup_{\mu \in \mathcal{M}(f)} h_\mu(f).$$
The supremum may be taken over the ergodic measures in $\mathcal{M}(f)$ only.

## Remarks

The set $\mathcal{M}(f)$ is nonempty by the [[Krylov–Bogolyubov theorem|1DHZ81S0YE]].
The inequality $h_\mu(f) \le h_{\mathrm{top}}(f)$ follows by comparing a finite measurable partition with an open cover, and Misiurewicz gave a short proof of the reverse inequality.
For the reverse inequality one builds, from large $(n, \varepsilon)$-separated sets, averaged measures whose weak-$\ast$ limit is invariant and has entropy close to $h_{\mathrm{top}}(f)$.
The restriction to ergodic measures follows from the ergodic decomposition, since $h_\mu$ is the average of the entropies of the ergodic components.
Example: for the full shift on $k$ symbols, $h_{\mathrm{top}} = \log k$, and the Bernoulli measure giving each symbol mass $1/k$ has entropy $\log k$, so the supremum is attained.
The supremum is not always attained; a measure that attains it is called a measure of maximal entropy.

## Explanations

### L1 human

There are two ways to measure how chaotic a system is.
Topological entropy counts distinguishable orbits, while measure-theoretic entropy measures the unpredictability of typical orbits for a given statistics.
The variational principle says that the first is the best possible value of the second.

### L2 human

The theorem lets one compute topological entropy from a well-chosen invariant measure, and conversely bounds all measure-theoretic entropies by a topological quantity.
It is the starting point of the thermodynamic formalism, where entropy is replaced by pressure and the maximizing measures become equilibrium states.
Measures of maximal entropy exist when $\mu \mapsto h_\mu(f)$ is upper semicontinuous, for example for expansive homeomorphisms.
