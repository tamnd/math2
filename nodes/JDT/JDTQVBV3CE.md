---
tag: JDTQVBV3CE
kind: proof
name: Proof that the interior is open
msc: [54A05]
proves: 0PNWCM559P
uses: [0CNQXVBHCX, 0C38S0KMJK, 01ZQQDCERP, 05GK32H72H]
sources:
  - url: https://en.wikipedia.org/wiki/Interior_(topology)
---

## Proof

1. Let $(X, \tau)$ be a [[topological space|0CNQXVBHCX]] and let $S \subseteq X$.
2. Let $\mathcal{U}$ be the family of all [[open sets|01ZQQDCERP]] $U$ of $X$ with $U \subseteq S$. Each member of $\mathcal{U}$ is in $\tau$.
3. By the definition of the [[interior|0C38S0KMJK]], $\operatorname{int} S$ is the [[union|05GK32H72H]] of the members of $\mathcal{U}$.
4. By the second axiom of a topology, the union of each family of members of $\tau$ is in $\tau$.
5. So $\operatorname{int} S \in \tau$, that is, $\operatorname{int} S$ is open in $X$.

## Idea

The interior is built as a union of open sets. The axioms of a topology say that every such union is open. So no work is needed beyond the definition.
