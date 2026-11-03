---
tag: CP2ZE0SHFH
kind: definition
name: Evolutionary graph theory
msc: [92D15, 91A22]
defines: 23VJ5SVAGB
uses: [A9M7VKRRV9, 0R5HTV7REV, 5APPKBE8Q4]
sources:
  - url: https://en.wikipedia.org/wiki/Evolutionary_graph_theory
---

## Definition

Let $W = (w_{ij})$ be an $N \times N$ matrix with $w_{ij} \ge 0$ and $\sum_j w_{ij} = 1$ for each $i$; it defines a weighted [[directed graph|0R5HTV7REV]] on the vertices $1, \dots, N$.
Each vertex holds one individual, either a resident of fitness $1$ or a mutant of fitness $r > 0$.
The *Moran process on the graph* $W$ is the Markov chain on the sets of mutant vertices in which each step is:

1. choose a vertex $i$ for reproduction with probability proportional to the fitness of its individual;
2. choose a vertex $j$ with probability $w_{ij}$;
3. replace the individual at $j$ by a copy of the individual at $i$.

Evolutionary graph theory studies such processes.
A main quantity is the [[fixation probability|5APPKBE8Q4]] $\rho_W$: the probability that a single mutant at a uniformly random vertex takes over all vertices.

## Remarks

Example: the complete graph with $w_{ij} = 1/(N - 1)$ for $i \ne j$ gives the well-mixed [[Moran process|A9M7VKRRV9]], where a single mutant fixes with probability $(1 - 1/r)/(1 - 1/r^N)$ for $r \ne 1$.
If $W$ is also doubly stochastic, so that every vertex receives total weight $1$, the fixation probability equals this Moran value; this is the isothermal theorem.
Non-example: a matrix with a row of sum $0$ fails the condition on $W$, because the individual at that vertex could never place offspring and clause 2 would be undefined.
Graphs whose fixation probability exceeds the Moran value for all $r > 1$ are called amplifiers of selection; for large $N$ the star is one, with fixation probability close to $(1 - 1/r^2)/(1 - 1/r^{2N})$.
