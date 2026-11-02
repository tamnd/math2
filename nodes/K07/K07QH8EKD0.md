---
tag: K07QH8EKD0
kind: statement
role: theorem
name: Hammersley–Clifford theorem
msc: [62H22, 60G60]
uses: [6W69H3A3G5, 0BYX1D7C2E, 00C0BR7D7H, 0THJ7416DX]
about: [6W69H3A3G5]
sources:
  - url: https://en.wikipedia.org/wiki/Hammersley%E2%80%93Clifford_theorem
same_as:
  wikidata: Q5645731
  wikipedia: Hammersley–Clifford theorem
---

## Statement

Let $G = (V, E)$ be a finite undirected [[graph|00C0BR7D7H]], and let $\mathcal{C}$ be the set of its [[cliques|0BYX1D7C2E]].
For each $v \in V$ let $S_v$ be a finite set, and let $X = (X_v)_{v \in V}$ be a random vector with values in $\prod_{v \in V} S_v$.
Assume that its probability mass function $p$ is strictly positive: $p(x) > 0$ for every $x$.
For $C \subseteq V$ write $x_C = (x_v)_{v \in C}$.
Then the following are equivalent.

1. $X$ is a [[Markov random field|6W69H3A3G5]] with respect to $G$.
2. There are functions $\psi_C > 0$, one for each $C \in \mathcal{C}$, such that for all $x$,
$$p(x) = \prod_{C \in \mathcal{C}} \psi_C(x_C).$$

## Remarks

That 2 implies 1 is direct.
Let $S$ separate $A$ from $B$, and enlarge $A$ and $B$ so that $A \cup B \cup S = V$ while $S$ still separates them.
No clique meets both $A$ and $B$, so each clique lies in $A \cup S$ or in $B \cup S$.
So $p$ is a function of $(x_A, x_S)$ times a function of $(x_B, x_S)$, which gives $X_A \perp X_B \mid X_S$.
For 1 implies 2, one writes $\log p$ as a sum of terms indexed by the subsets of $V$, by Möbius inversion.
The pairwise Markov property then shows that the terms of the non-cliques vanish.
This second step needs positivity, since it takes logarithms and divides by $p$.
The direction 2 implies 1 holds without positivity, but the direction 1 implies 2 can fail.
There are Markov random fields with zero probabilities on a cycle of four vertices that do not factorise over the cliques.

Example: for the Ising model on $G$, $p(x) \propto \exp\bigl(\beta \sum_{\set{u, v} \in E} x_u x_v + h \sum_v x_v\bigr)$ with $x_v \in \set{-1, 1}$.
This is a product of positive factors on edges and vertices, which are cliques, so the Ising model is a Markov random field.

## Explanations

### L1 human

The theorem says two descriptions of a random field agree.
One description lists independence facts: each variable cares only about its neighbours.
The other gives a formula: the probability is a product of terms, each involving only a group of mutually adjacent variables.
This holds as long as no configuration has probability zero.

### L2 human

The theorem is why Markov random fields are written as Gibbs distributions $p(x) \propto \exp(-\sum_C V_C(x_C))$ with clique potentials $V_C$.
Conversely, any such energy defines a Markov random field, and in Gibbs sampling the update of $x_v$ then depends only on the neighbours of $v$.
The same statement holds for positive densities with respect to a product measure, for example for Gaussian graphical models.
There the missing edges of the graph are the zero entries of the inverse covariance matrix.
For directed graphs, the analogous factorisation is the definition of a [[Bayesian network|21JT983G60]].
