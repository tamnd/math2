---
tag: P5A9ATRSV2
kind: definition
name: Fortuin–Kasteleyn random cluster model
msc: [82B20, 60K35, 82B43]
defines: VCTMYPDXPX
uses: [00C0BR7D7H, 0JG9W3KA6B, 059TJN0NZ1]
sources:
  - url: https://en.wikipedia.org/wiki/Random_cluster_model
---

## Definition

Let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]], let $p \in [0, 1]$ and let $q > 0$.
For a subset $\omega \subseteq E$, let $k(\omega)$ be the number of [[connected components|0JG9W3KA6B]] of the graph $(V, \omega)$, isolated vertices included.
The *random cluster measure* $\phi_{p, q}$ on $G$ is the [[probability measure|059TJN0NZ1]] on the subsets of $E$ given by
$$\phi_{p, q}(\omega) = \frac{1}{Z} \, p^{\abs{\omega}} (1 - p)^{\abs{E \setminus \omega}} q^{k(\omega)},$$
where $Z = \sum_{\omega \subseteq E} p^{\abs{\omega}} (1 - p)^{\abs{E \setminus \omega}} q^{k(\omega)}$.
The edges in $\omega$ are called open.

## Remarks

For $q = 1$ the factor $q^{k(\omega)}$ is $1$, and $\phi_{p, 1}$ is Bernoulli bond [[percolation|BH7YPXCYDK]]: each edge is open independently with probability $p$.
For integer $q \ge 2$ and $p = 1 - e^{-\beta}$, the Edwards–Sokal coupling relates $\phi_{p, q}$ to the $q$-state [[Potts model|5GY2J6ZGXJ]] with energy $-\sum_{\set{x, y} \in E} \delta_{\sigma_x, \sigma_y}$ at inverse temperature $\beta$.
Under this coupling, $\phi_{p, q}$ is the law of the open edges, and the Potts spins are obtained by giving each open cluster an independent uniform colour.
Two Potts spins at $x$ and $y$ are then correlated through the event that $x$ and $y$ lie in the same open cluster.
Non-example: the measure proportional to $p^{\abs{\omega}} (1 - p)^{\abs{E \setminus \omega}} q^{\abs{\omega}}$ is not of this form for $q \ne 1$, since its extra weight counts edges, not components; it is just Bernoulli percolation with another parameter.
The partition function $Z$ is, up to a change of variables, the Tutte polynomial of $G$.
