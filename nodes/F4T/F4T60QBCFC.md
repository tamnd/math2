---
tag: F4T60QBCFC
kind: proof
name: Proof that the interior is the largest open subset
msc: [54A05]
proves: 0HAZEFH137
uses: [0CNQXVBHCX, 0C38S0KMJK, 01ZQQDCERP, 05GK32H72H, 0PNWCM559P]
sources:
  - url: https://en.wikipedia.org/wiki/Interior_(topology)
---

## Proof

1. Let $X$ be a [[topological space|0CNQXVBHCX]] and let $S \subseteq X$.
2. Let $\mathcal{U}$ be the family of all [[open sets|01ZQQDCERP]] $U$ of $X$ with $U \subseteq S$. By the definition of the [[interior|0C38S0KMJK]], $\operatorname{int} S$ is the [[union|05GK32H72H]] of the members of $\mathcal{U}$.
3. Let $x \in \operatorname{int} S$. Then $x \in U$ for some $U \in \mathcal{U}$. Since $U \subseteq S$, we get $x \in S$. So $\operatorname{int} S \subseteq S$.
4. By [[interior is open|0PNWCM559P]], the set $\operatorname{int} S$ is open.
5. Let $U$ be an open set of $X$ with $U \subseteq S$. Then $U \in \mathcal{U}$.
6. Each member of a family is contained in the union of the family. So $U \subseteq \operatorname{int} S$.

## Idea

The interior is the union of all open sets that fit inside $S$. Each of them lies in the union, and the union still fits inside $S$. So the interior is the biggest open set that fits.
