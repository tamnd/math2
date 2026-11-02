---
tag: 2CM2MC5HQ6
kind: definition
name: Cellular automaton
msc: [37B15, 68Q80]
defines: 5QXNC6NTVN
uses: [A1XE59ZHNM]
sources:
  - url: https://en.wikipedia.org/wiki/Cellular_automaton
---

## Definition

Let $A$ be a finite set of states and let $d \ge 1$.
A configuration is an element $x = (x_u)_{u \in \Z^d}$ of $A^{\Z^d}$.
Let $N \subseteq \Z^d$ be a finite set, called the neighbourhood, and let $f \colon A^N \to A$ be a map, called the local rule.
The *cellular automaton* with neighbourhood $N$ and local rule $f$ is the map $F \colon A^{\Z^d} \to A^{\Z^d}$ given by
$$F(x)_u = f\big((x_{u + n})_{n \in N}\big) \quad \text{for all } u \in \Z^d.$$

## Remarks

Example: rule 90 has $d = 1$, $A = \set{0, 1}$, $N = \set{-1, 1}$ and $f(a, b) = a + b \bmod 2$.
So $F(x)_i = x_{i-1} + x_{i+1} \bmod 2$, and the value at $i$ depends only on the sites $i \pm 1$, as required.
Non-example: the map $F(x)_i = x_{2i}$ on $\set{0,1}^{\Z}$ is not a cellular automaton.
The value at $i$ reads the site $2i$, so no fixed finite set $N$ of offsets works for all $i$.
Equivalently, it does not commute with the shift, which the [[Curtis–Hedlund–Lyndon theorem|N35QM9G83G]] requires.
The dynamics is the iteration of $F$, with $F^t(x)$ the configuration at time $t$.
In one dimension with $A = \set{0,1}$ and $N = \set{-1, 0, 1}$, the $2^8 = 256$ local rules are the elementary cellular automata, numbered by Wolfram's convention.
