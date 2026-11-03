---
tag: 8JH9AJ4P2A
kind: statement
role: theorem
name: Dobrushin uniqueness criterion
msc: [82B05, 82B20, 60K35]
uses: [DG9F3W6MZM, 3SZESKX3N5, 059TJN0NZ1]
about: [DG9F3W6MZM]
sources:
  - url: https://en.wikipedia.org/wiki/Gibbs_measure
---

## Statement

Let $S$ be a finite set and $\Omega = S^{\Z^d}$.
Let $\Phi = (\Phi_A)$ be an interaction with $\sup_{x} \sum_{A \ni x} \norm{\Phi_A}_\infty < \infty$, let $\beta > 0$, and let $\mathcal{G}$ be the set of [[Gibbs measures|DG9F3W6MZM]] for $\beta \Phi$.
For a site $i$ and $\omega \in \Omega$, let $\gamma_i(\cdot \mid \omega)$ be the single-site Gibbs kernel: the [[probability measure|059TJN0NZ1]] on $S$ proportional to $s \mapsto e^{-\beta H_{\set{i}}^\omega(s)}$.
For sites $i \ne j$, define the Dobrushin coefficient
$$C_{ij} = \sup \set{ \norm{\gamma_i(\cdot \mid \omega) - \gamma_i(\cdot \mid \omega')}_{TV} : \omega_k = \omega'_k \text{ for all } k \ne j },$$
and $C_{ii} = 0$.
Here $\norm{\cdot}_{TV}$ is the [[total variation distance|3SZESKX3N5]], $\norm{p - q}_{TV} = \max_{B \subseteq S} \abs{p(B) - q(B)}$.
If $\sup_{i} \sum_{j} C_{ij} < 1$, then $\mathcal{G}$ has exactly one element.

## Remarks

Existence holds for any such interaction, so the content is uniqueness.
Proof idea: for two Gibbs measures, bound the total variation distance of their marginal at site $i$ by $\sum_j C_{ij}$ times the distances at the sites $j$.
Iterating this contraction drives the distances to $0$.
A simple sufficient condition is $4 \beta \sup_i \sum_{A \ni i} (\abs{A} - 1) \norm{\Phi_A}_\infty < 1$, so the criterion applies at high temperature, that is, for small $\beta$.
Example: take the nearest-neighbour Ising model on $\Z^d$ with coupling $J > 0$ and no field.
Then $C_{ij} = \frac{1}{2} \tanh(2 \beta J)$ for neighbours $i, j$ and $0$ otherwise, so uniqueness holds when $d \tanh(2 \beta J) < 1$.
The criterion is not necessary: in dimension one the Ising model has a unique Gibbs measure at every $\beta$.

## Explanations

### L1 human

A Gibbs measure is fixed by local rules, and the question is whether the rules pin down one global state.
Dobrushin's criterion says yes when each spin depends only weakly on the others: changing all neighbours together moves its distribution by less than a total of one.
Then influences die out with distance and the boundary is forgotten.

### L2 human

The criterion is a contraction argument, in the spirit of the Banach fixed-point theorem, on the space of measures.
Besides uniqueness, it gives decay of correlations for the unique Gibbs measure.
It is a high-temperature result; at low temperature, uniqueness can fail, as for the Ising model in dimension $d \ge 2$.
It also gives fast mixing of the Glauber dynamics, and it has a close analogue, the path coupling method, in the analysis of Markov chains.
