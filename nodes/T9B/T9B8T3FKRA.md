---
tag: T9B8T3FKRA
kind: problem
name: Maximum cut
msc: [90C27, 05C85, 68Q17]
uses: [FJPER80BJC, 00C0BR7D7H, JGZWHWA8P8, 4WEVBDQ8SR, 0ZVQKTRKVQ]
about: [FJPER80BJC, 00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_cut
same_as:
  wikidata: Q942557
  wikipedia: Maximum cut
history:
  posed_by: "Richard M. Karp"
  first_stated: "1972"
  notes: "Karp listed the weighted decision version among his 21 NP-complete problems in 1972, the earliest well-documented statement as an algorithmic problem. Erdős had earlier studied large bipartite subgraphs and the simple half-approximation."
---

## Problem

Let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]] with edge weights $w \colon E \to [0, \infty)$.
For $S \subseteq V$, the *cut* $\delta(S)$ is the set of edges with one end in $S$ and the other end in $V \setminus S$.
The *maximum cut problem* asks for a set $S \subseteq V$ that maximizes the total weight $\sum_{e \in \delta(S)} w(e)$.
In the unweighted version, all weights equal $1$, and the goal is a cut with the most edges.

## Remarks

The decision version is [[NP-complete|JGZWHWA8P8]], even without weights.
In contrast, a minimum cut separating two given vertices can be found in polynomial time by maximum flow methods.
In the unweighted version, every edge can be cut exactly when $G$ is [[bipartite|0ZVQKTRKVQ]], and one side of a bipartition is then an optimal $S$.
Putting each vertex into $S$ with probability $1/2$, independently, cuts each edge with probability $1/2$.
So some cut has at least half of the total weight, and this gives an [[approximation algorithm|4WEVBDQ8SR]] of ratio $1/2$.
The [[Goemans–Williamson algorithm|ATERHVE8T7]] improves the ratio to about $0.878$ by semidefinite programming.
Håstad showed that a ratio better than $16/17$ is NP-hard to reach.
Assuming the [[unique games conjecture|SWZ51W5WJ4]], the Goemans–Williamson ratio is best possible.
For planar graphs, the problem can be solved in polynomial time.

## Explanations

### L1 human

Split the vertices of a network into two teams so that as many links as possible join players of different teams.
For a triangle, the best split puts one vertex alone and cuts $2$ of the $3$ edges; no split cuts all three, since the triangle has an odd cycle.
A random split already cuts half of the edges on average.
Doing much better than that, for every graph, is hard, and the exact limit is tied to deep questions in complexity theory.
