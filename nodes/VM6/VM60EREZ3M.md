---
tag: VM60EREZ3M
kind: definition
name: Greedy algorithm
msc: [68W40, 90C27]
defines: PSM6NKYJB8
uses: [9DMSG5HAQX, PX31ZNYS3Z]
sources:
  - url: https://en.wikipedia.org/wiki/Greedy_algorithm
---

## Definition

Let $E$ be a finite set, and let $w \colon E \to \R$ be a weight function.
Let $\mathcal{I}$ be a nonempty family of subsets of $E$, the *feasible* sets, closed under taking subsets.
The *greedy algorithm* for maximizing $w(A) = \sum_{e \in A} w(e)$ over $A \in \mathcal{I}$ is the [[algorithm|9DMSG5HAQX]] that:

1. orders $E$ as $e_1, \dots, e_m$ with $w(e_1) \ge w(e_2) \ge \cdots \ge w(e_m)$;
2. starts with $A = \emptyset$;
3. for $i = 1, \dots, m$, replaces $A$ by $A \cup \set{e_i}$ if $w(e_i) > 0$ and $A \cup \set{e_i} \in \mathcal{I}$;
4. returns $A$.

More generally, a *greedy algorithm* is any algorithm that builds a solution by a sequence of irrevocable choices, each of which optimizes a local criterion.

## Remarks

The Rado–Edmonds theorem: the greedy algorithm returns a maximum-weight feasible set for every $w$ if and only if $(E, \mathcal{I})$ is a [[matroid|PX31ZNYS3Z]].

Example: let $E$ be the edges of a connected graph and $\mathcal{I}$ the edge sets without cycles, the independent sets of the graphic matroid.
With weights $-\mathrm{length}$ shifted to be positive, the greedy algorithm is [[Kruskal's algorithm|5FPWTYFJRA]], and it returns a minimum spanning tree.

Non-example: let $E = \set{a, b, c}$ with $w(a) = 3$, $w(b) = w(c) = 2$, and $\mathcal{I} = \set{\emptyset, \set{a}, \set{b}, \set{c}, \set{b, c}}$.
Greedy picks $a$ and then can add nothing, so it returns weight $3$, while $\set{b, c}$ has weight $4$.
This family is not a matroid: $\set{a}$ and $\set{b, c}$ are independent, but neither $b$ nor $c$ can be added to $\set{a}$.
