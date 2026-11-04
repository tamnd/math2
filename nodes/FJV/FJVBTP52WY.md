---
tag: FJVBTP52WY
kind: proof
name: Proof that the closure is the smallest closed superset
msc: [54A05]
proves: 0SHC6Z304Z
uses: [0CNQXVBHCX, 0DRKT1QJR7, 0G5AV9Q4RR, 0839XNQXDK, 02TZDKG50Q]
sources:
  - url: https://en.wikipedia.org/wiki/Closure_(topology)
---

## Proof

1. Let $X$ be a [[topological space|0CNQXVBHCX]] and let $S \subseteq X$.
2. Let $\mathcal{F}$ be the family of all [[closed sets|0G5AV9Q4RR]] $F$ of $X$ with $S \subseteq F$. By the definition of the [[closure|0DRKT1QJR7]], $\overline{S}$ is the [[intersection|0839XNQXDK]] of the members of $\mathcal{F}$.
3. Let $s \in S$. Each $F \in \mathcal{F}$ contains $S$, so $s \in F$ for each $F \in \mathcal{F}$. Thus $s \in \overline{S}$, and $S \subseteq \overline{S}$.
4. By [[closure is closed|02TZDKG50Q]], the set $\overline{S}$ is closed.
5. Let $F$ be a closed set of $X$ with $S \subseteq F$. Then $F \in \mathcal{F}$.
6. The intersection of a family is contained in each member of the family. So $\overline{S} \subseteq F$.

## Idea

The closure is the intersection of all closed sets that contain $S$. Every one of them contains $S$, so the intersection does too. And the intersection sits inside each of them, so it is the smallest.
