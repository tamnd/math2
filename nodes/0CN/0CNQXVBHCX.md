---
tag: 0CNQXVBHCX
kind: definition
name: Topological space
msc: [54A05]
defines: 0CQHFPGJ45
uses: [0FE8Q5S42Y, 05GK32H72H, 0HBRW4E6G1, 0ECVK59Y03]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_space
    locator: Definition via open sets
---

## Definition

Let $X$ be a set.
A topology on $X$ is a set $\tau$ of [[subsets|0FE8Q5S42Y]] of $X$ with these three properties:

1. The [[empty set|0ECVK59Y03]] $\varnothing$ and the set $X$ are in $\tau$.
2. For each family $(U_i)_{i \in I}$ of members of $\tau$, the [[union|05GK32H72H]] $\bigcup_{i \in I} U_i$ is in $\tau$.
3. For all $U, V \in \tau$, the [[intersection|0HBRW4E6G1]] $U \cap V$ is in $\tau$.

A topological space is a pair $(X, \tau)$ where $X$ is a set and $\tau$ is a topology on $X$.

## Remarks

The members of $\tau$ are the [[open sets|01ZQQDCERP]] of the space. Their complements are the [[closed sets|0G5AV9Q4RR]].
By induction, property 3 gives that each finite intersection of open sets is open. Infinite intersections need not be open.
Each metric gives a topology, the [[metric topology|0A6YRNZB2R]]. Other basic examples are the [[discrete topology|0S2TEHX4E1]] and the [[indiscrete topology|0XJ02JBD6S]].
One can also define a topology by its closed sets, or by the [[neighbourhoods of its points|09CJ00H3NW]].

## Explanations

### L1 human

A topology tells you which subsets of $X$ count as open, without any distances.
The rules copy the properties of open sets in metric spaces. Any union of open sets is open, and a finite intersection of open sets is open.
