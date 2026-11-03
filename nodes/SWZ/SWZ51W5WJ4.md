---
tag: SWZ51W5WJ4
kind: conjecture
name: Unique games conjecture
msc: [68Q17, 68Q25]
uses: [MHA48AWBXN, 00C0BR7D7H]
about: [X97H4RM1XR]
sources:
  - url: https://en.wikipedia.org/wiki/Unique_games_conjecture
history:
  posed_by: Subhash Khot
  first_stated: "2002"
---

## Statement

A *unique game* with alphabet size $k$ is given by a finite [[graph|00C0BR7D7H]] $G = (V, E)$ and, for each edge $e = \set{u, v}$, a permutation $\pi_e$ of $\set{1, \ldots, k}$.
A labeling $\ell \colon V \to \set{1, \ldots, k}$ satisfies the edge $e$ if $\pi_e(\ell(u)) = \ell(v)$, with the edge read in a fixed direction.
The *value* of the game is the largest fraction of edges satisfied by a labeling.

**Conjecture.**
For every $\varepsilon > 0$ and $\delta > 0$ there is an integer $k$ with the following property.
Consider unique games with alphabet size $k$.
It is [[NP-hard|MHA48AWBXN]] to distinguish those of value at least $1 - \varepsilon$ from those of value at most $\delta$.

## Remarks

The conjecture is open.
Deciding whether the value is exactly $1$ is easy: fixing the label of one vertex in each connected component forces all other labels.
So the conjecture concerns only nearly satisfiable games.

If the conjecture holds, several known approximation algorithms are optimal.
Khot, Kindler, Mossel and O'Donnell showed that the Goemans–Williamson ratio for MAX-CUT, about $0.878$, cannot then be beaten in polynomial time unless $\mathrm{P} = \mathrm{NP}$.
Khot and Regev showed that vertex cover would then be NP-hard to approximate within $2 - \varepsilon$ for every $\varepsilon > 0$.

In 2018 Khot, Minzer and Safra, building on joint work with Dinur and Kindler, proved the 2-to-2 games conjecture.
A consequence is the weaker form of the conjecture with completeness $1/2$ in place of $1 - \varepsilon$.

## Explanations

### L1 human

Imagine coloring the points of a network with $k$ colors, where each link says: "if this end has color $i$, the other end must have color $\pi(i)$".
If all links can be satisfied, a simple propagation finds the coloring.
Now suppose only almost all links can be satisfied.
The conjecture says that then even satisfying a small fraction of them is as hard as any problem in NP.
Many sharp limits on approximation algorithms follow from this one guess.
