---
tag: 7T740SFHHV
kind: definition
name: Bisimulation
msc: [68Q85, 68Q55, 03B45]
defines: X27BR4YP2Y
uses: [05AVARPXA2]
sources:
  - url: https://en.wikipedia.org/wiki/Bisimulation
---

## Definition

A *labelled transition system* is a triple $(S, A, \to)$ of a set $S$ of states, a set $A$ of actions and a relation $\to \subseteq S \times A \times S$.
One writes $p \xrightarrow{a} p'$ when $(p, a, p') \in {\to}$.
A [[binary relation|05AVARPXA2]] $R \subseteq S \times S$ is a *bisimulation* if, for every pair $(p, q) \in R$ and every action $a \in A$:

1. if $p \xrightarrow{a} p'$, then there is $q'$ with $q \xrightarrow{a} q'$ and $(p', q') \in R$;
2. if $q \xrightarrow{a} q'$, then there is $p'$ with $p \xrightarrow{a} p'$ and $(p', q') \in R$.

Two states $p$ and $q$ are *bisimilar*, written $p \sim q$, if $(p, q) \in R$ for some bisimulation $R$.

## Remarks

The union of all bisimulations is a bisimulation, so $\sim$ is the largest bisimulation.
It is an equivalence relation on $S$.
It is the greatest fixed point of a monotone map on the [[complete lattice|D7A0ZGZT5S]] of relations on $S$.

Example: let $p$ have the single transition $p \xrightarrow{a} p$, and let $q_0 \xrightarrow{a} q_1$ and $q_1 \xrightarrow{a} q_0$.
The relation $R = \set{(p, q_0), (p, q_1)}$ is a bisimulation.
Each move of $p$ lands in $p$, and each $q_i$ can answer with a move to $q_{1-i}$, which is again related to $p$.
The converse direction holds in the same way.

Non-example: let $p \xrightarrow{a} p_1$, $p_1 \xrightarrow{b} p_2$, $p_1 \xrightarrow{c} p_3$, and let $q \xrightarrow{a} q_1$, $q \xrightarrow{a} q_2$, $q_1 \xrightarrow{b} q_3$, $q_2 \xrightarrow{c} q_4$.
Both $p$ and $q$ have the traces $a$, $ab$ and $ac$.
They are not bisimilar.
The move $q \xrightarrow{a} q_1$ must be matched by $p \xrightarrow{a} p_1$, and then $p_1 \xrightarrow{c} p_3$ cannot be matched from $q_1$, so clause 2 fails for $(p_1, q_1)$.
