---
tag: ZMW8Q5SAW2
kind: problem
name: Multi-commodity flow problem
msc: [90C35, 90B10, 05C21]
uses: [ZSNXTW5E2K, 0KFYGSHHF5]
about: [ZSNXTW5E2K]
sources:
  - url: https://en.wikipedia.org/wiki/Multi-commodity_flow_problem
same_as:
  wikidata: Q6934437
  wikipedia: Multi-commodity flow problem
history:
  posed_by: "unknown"
  first_stated: "unknown"
---

## Problem

Let $(V, E)$ be a finite [[directed graph|0KFYGSHHF5]] with a capacity $c_e \ge 0$ on each edge $e$.
Let $K_1, \dots, K_k$ be commodities, where $K_i = (s_i, t_i, d_i)$ has a source $s_i$, a sink $t_i \ne s_i$ and a demand $d_i \ge 0$.
A *multi-commodity flow* is a family of functions $f_1, \dots, f_k \colon E \to [0, \infty)$ such that:

1. For each $i$ and each vertex $v \notin \set{s_i, t_i}$, the flow $f_i$ entering $v$ equals the flow $f_i$ leaving $v$.
2. For each $i$, the net flow $f_i$ leaving $s_i$ equals $d_i$.
3. For each edge $e$, $\sum_{i=1}^k f_i(e) \le c_e$.

Decide whether a multi-commodity flow exists, and find one if it does.

## Remarks

The commodities share the capacities but cannot be exchanged: flow of commodity $i$ must go from $s_i$ to $t_i$.
With real-valued flows the problem is a linear program, so it can be solved in polynomial time.
If the flows must be integers, the problem is NP-complete, even for two commodities and unit capacities, by a result of Even, Itai and Shamir (1976).
For one commodity, integrality is free by the integral flow theorem, so this is a real difference.
Optimization versions ask for a minimum-cost multi-commodity flow, or for the largest $\lambda$ such that the demands $\lambda d_i$ can be routed together.

Example: in the graph with edges $a \to b$ and $b \to c$ of capacity $1$, take $K_1 = (a, b, 1)$ and $K_2 = (b, c, 1)$.
The flows $f_1 = 1$ on $a \to b$ and $f_2 = 1$ on $b \to c$ satisfy all three clauses.
If $K_2$ were $(a, c, 1)$ instead, both commodities would need the edge $a \to b$, and clause 3 would fail.

## Explanations

### L1 human

Several kinds of goods share one network of roads or cables.
Each kind must travel from its own origin to its own destination, and the roads have a common capacity.
The question is whether all demands can be met at once.
Unlike the one-commodity case, rounding a fractional answer to whole units can be impossible, and the whole-unit version is hard.
