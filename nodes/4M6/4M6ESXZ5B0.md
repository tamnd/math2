---
tag: 4M6ESXZ5B0
kind: proof
name: Proof of the handshaking lemma by double counting
msc: [05C07]
proves: 0XAP8WHNES
uses: [0JD5C82QMB, 0WNGQBPPQX, 0T0F6CCS9W, 0F8YBHF2W3]
sources:
  - url: https://en.wikipedia.org/wiki/Handshaking_lemma
---

## Proof

We use [[double counting|0F8YBHF2W3]] of vertex–edge incidences.

1. The set $V$ is finite. The [[edge set|0WNGQBPPQX]] $E$ consists of $2$-element subsets of $V$, so $E$ is finite too.
2. Let $R = \set{(v, e) \in V \times E : v \in e}$, the set of incidences.
3. Fix $v \in V$. The number of $e \in E$ with $(v, e) \in R$ is the number of edges that contain $v$. By the definition of the [[degree|0T0F6CCS9W]], this is $\deg(v)$.
4. Fix $e \in E$. The number of $v \in V$ with $(v, e) \in R$ is $\abs{e} = 2$, since each edge of a [[graph|0JD5C82QMB]] is a $2$-element subset of $V$.
5. Counting $R$ by its first coordinate gives $\abs{R} = \sum_{v \in V} \deg(v)$, by step 3.
6. Counting $R$ by its second coordinate gives $\abs{R} = \sum_{e \in E} 2 = 2 \abs{E}$, by step 4.
7. Comparing steps 5 and 6 gives $\sum_{v \in V} \deg(v) = 2 \abs{E}$.

## Idea

Each edge has exactly two ends. Adding up the degrees counts every edge once at each end, so every edge is counted twice.
