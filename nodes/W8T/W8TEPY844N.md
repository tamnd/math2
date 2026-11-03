---
tag: W8TEPY844N
kind: example
name: Lattice gas
msc: [82B20, 82B26]
instance_of: [PAEME5EQRM]
uses: [R0KGM32QN6, 1C5S72A9JX]
sources:
  - url: https://en.wikipedia.org/wiki/Ising_model
---

## Example

Let $\Lambda$ be a finite box of $\Z^d$ with periodic boundary conditions, so that each site has $q = 2d$ nearest neighbours.
Let $\epsilon \in \R$ be the attraction between neighbouring particles, $\mu \in \R$ the chemical potential and $\beta \ge 0$ the inverse temperature.
A configuration is $n \colon \Lambda \to \set{0, 1}$, where $n_x = 1$ means that the site $x$ holds a particle.
Its energy is
$$H(n) = -\epsilon \sum_{\set{x, y}} n_x n_y - \mu \sum_{x \in \Lambda} n_x,$$
where the first sum runs over nearest-neighbour pairs.
The *lattice gas* is the probability measure on $\set{0, 1}^\Lambda$ proportional to $e^{-\beta H(n)}$.
It is a [[grand canonical ensemble|1C5S72A9JX]] of particles that sit on sites, at most one per site.

## Remarks

The substitution $n_x = (1 + \sigma_x)/2$ with $\sigma_x \in \set{-1, +1}$ turns it into the [[Ising model|R0KGM32QN6]].
Indeed $n_x n_y = (1 + \sigma_x + \sigma_y + \sigma_x \sigma_y)/4$, and each site lies in $q$ nearest-neighbour pairs.
So $H = -J \sum \sigma_x \sigma_y - h \sum_x \sigma_x + \text{const}$ with $J = \epsilon/4$ and $h = \mu/2 + q\epsilon/4$.
Thus the liquid-gas transition of the lattice gas corresponds to the magnetization transition of the Ising model, and the particle density corresponds to $(1 + m)/2$, where $m$ is the magnetization.

## Explanations

### L1 human

Chop space into cells, and let each cell be empty or hold one particle.
Neighbouring particles attract each other, and the chemical potential sets how much particles are wanted overall.
Calling a full cell "spin up" and an empty cell "spin down" turns this gas into the Ising magnet.
So a gas condensing into a liquid is the same mathematics as a magnet ordering.
