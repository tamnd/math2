---
tag: 0HAZEFH137
kind: statement
role: proposition
name: Interior is the largest open subset
msc: [54A05]
uses: [0C38S0KMJK, 0PNWCM559P]
sources:
  - url: https://en.wikipedia.org/wiki/Interior_(topology)
    locator: Definitions
---

## Statement

Let $X$ be a [[topological space|0CNQXVBHCX]] and let $S \subseteq X$.
Then $\operatorname{int} S \subseteq S$, the set $\operatorname{int} S$ is open, and each open set $U$ of $X$ with $U \subseteq S$ satisfies $U \subseteq \operatorname{int} S$.

## Remarks

Here $\operatorname{int} S$ is the [[interior|0C38S0KMJK]] of $S$. The openness is the statement [[interior is open|0PNWCM559P]].
A consequence: $S$ is open if and only if $\operatorname{int} S = S$.
If $S \subseteq T$, then $\operatorname{int} S \subseteq \operatorname{int} T$.

## Explanations

### L1 human

Among all open sets inside $S$, the interior is the biggest one.
Each open set inside $S$ is already inside the interior.
