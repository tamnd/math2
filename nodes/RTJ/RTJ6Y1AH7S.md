---
tag: RTJ6Y1AH7S
kind: definition
name: Coupled map lattice
msc: [37L60, 37N20]
defines: 77JZ2QRZ4M
uses: [BBZP1R872N, AYVTR2ES5B]
sources:
  - url: https://en.wikipedia.org/wiki/Coupled_map_lattice
---

## Definition

Let $N \ge 3$, let $f \colon \R \to \R$ be a map, and let $\varepsilon \in [0, 1]$ be a coupling strength.
Index the sites by $i \in \Z / N\Z$.
The *diffusively coupled map lattice* with local map $f$ is the discrete-time [[dynamical system|BBZP1R872N]] on $\R^{N}$ given by $x_{n+1} = F(x_n)$, where
$$F(x)_i = (1 - \varepsilon) f(x_i) + \frac{\varepsilon}{2} \big( f(x_{i-1}) + f(x_{i+1}) \big), \qquad i \in \Z / N\Z.$$

## Remarks

The sites form a ring, which is the usual periodic boundary condition; the same rule makes sense on $\Z$ or on higher-dimensional lattices, with the average over all nearest neighbours.
More general coupled map lattices allow other local maps and other coupling rules.

Example: if $\varepsilon = 0$, then $F(x)_i = f(x_i)$, so each site evolves by [[iterating|AYVTR2ES5B]] $f$ on its own.
If all sites start equal, $x_i = s$ for all $i$, then $F(x)_i = (1 - \varepsilon) f(s) + \varepsilon f(s) = f(s)$ for all $i$.
So the spatially uniform states form an invariant set on which the lattice reduces to the single map $f$.

Non-example: a cellular automaton has the same discrete space and time.
But its states take values in a finite set, not in $\R$, so it is not a coupled map lattice.

A common choice is the [[logistic map|QN9X9BNKTX]] $f(x) = r x (1 - x)$ or the quadratic map $f(x) = 1 - a x^2$, with $\varepsilon$ and the parameter of $f$ as the two control parameters.
