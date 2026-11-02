---
tag: P6KHVSTPZV
kind: concept
name: Weak topology
msc: [46A20]
sources:
  - url: https://en.wikipedia.org/wiki/Weak_topology
same_as:
  wikidata: Q505760
  wikipedia: Weak topology
---

## Summary

Let $(X, Y)$ be a [[dual pair|R68HNB5SVR]].
The weak topology $\sigma(X, Y)$ is the coarsest topology on $X$ making every map $x \mapsto \langle x, y \rangle$ continuous.
For a topological vector space $E$, the weak topology is $\sigma(E, E')$, defined by its [[continuous linear forms|4A82S5FVRT]], and the weak-* topology on $E'$ is $\sigma(E', E)$.
Weak topologies have fewer open sets than norm topologies, so more sets are compact; this is the content of the [[Banach–Alaoglu theorem|1BXEJXQ2YT]].

## Explanations

### L1 human

In the weak topology, a sequence converges when every continuous linear measurement of it converges.
This is much easier to satisfy than convergence in norm.
In $\ell^2$, the unit vectors $e_1, e_2, e_3, \ldots$ converge weakly to $0$: for each fixed $y \in \ell^2$, the numbers $\langle e_n, y \rangle = y_n$ tend to $0$.
Yet $\norm{e_n} = 1$ for all $n$, so they do not converge to $0$ in norm.
