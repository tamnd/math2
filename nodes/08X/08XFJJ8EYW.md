---
tag: 08XFJJ8EYW
kind: definition
name: Comparison of topologies
msc: [54A10]
defines: 072J68M6HX
uses: [0CNQXVBHCX, 0FE8Q5S42Y]
sources:
  - url: https://en.wikipedia.org/wiki/Comparison_of_topologies
    locator: Definition
---

## Definition

Let $X$ be a set and let $\tau_1$ and $\tau_2$ be [[topologies|0CNQXVBHCX]] on $X$.
If $\tau_1 \subseteq \tau_2$, then $\tau_1$ is coarser (or weaker) than $\tau_2$, and $\tau_2$ is finer (or stronger) than $\tau_1$.
If also $\tau_1 \neq \tau_2$, then $\tau_1$ is strictly coarser and $\tau_2$ is strictly finer.

## Remarks

On each set $X$, the [[indiscrete topology|0XJ02JBD6S]] is the coarsest topology and the [[discrete topology|0S2TEHX4E1]] is the finest topology.
We have $\tau_1 \subseteq \tau_2$ if and only if the identity map $(X, \tau_2) \to (X, \tau_1)$ is [[continuous|0SY9ECQ19Q]].
Two topologies need not be comparable: on $\{a, b\}$, the topologies $\{\varnothing, \{a\}, X\}$ and $\{\varnothing, \{b\}, X\}$ are not comparable.

## Explanations

### L1 human

A finer topology has more open sets, so it can separate points in more ways.
A coarser topology has fewer open sets, so more sequences converge and more maps into it are continuous.
