---
tag: HC7T9KAAY9
kind: definition
name: Petri net
msc: [68Q85, 68Q10]
defines: 6S22209QQS
uses: [0ZVQKTRKVQ]
sources:
  - url: https://en.wikipedia.org/wiki/Petri_net
---

## Definition

A *Petri net* is a triple $N = (P, T, W)$ where:

1. $P$ and $T$ are finite disjoint sets, the *places* and the *transitions*;
2. $W \colon (P \times T) \cup (T \times P) \to \N$ is the *weight function*, with $\N = \set{0, 1, 2, \dots}$.

A *marking* is a map $M \colon P \to \N$.
A transition $t$ is *enabled* at $M$ if $M(p) \ge W(p, t)$ for every $p \in P$.
An enabled transition $t$ can *fire*, and this gives the marking $M'$ with
$$M'(p) = M(p) - W(p, t) + W(t, p) \quad \text{for all } p \in P.$$
A marking is *reachable* from an initial marking $M_0$ if it arises from $M_0$ by a finite sequence of firings.

## Remarks

The arcs are the pairs with $W(x, y) > 0$; they form a [[bipartite graph|0ZVQKTRKVQ]] between $P$ and $T$.

Example: let $P = \set{p, q}$, $T = \set{t}$, $W(p, t) = 1$, $W(t, q) = 2$ and the other weights $0$.
From $M_0 = (1, 0)$, the transition $t$ is enabled because $M_0(p) = 1 \ge 1$, and firing gives $(0, 2)$.

Non-example of enabling: at $(0, 2)$, the transition $t$ is not enabled, because $0 < W(p, t) = 1$.
So $(0, 2)$ is a dead marking of this net.

The reachability problem for Petri nets, whether a given marking is reachable from $M_0$, is decidable.
