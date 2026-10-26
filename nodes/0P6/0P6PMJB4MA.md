---
tag: 0P6PMJB4MA
kind: statement
role: proposition
name: Compactness via open covers
msc: [54D30]
uses: [00R0X1WGPX, 0NVPNC12JY, 0D5YHQGDJY]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_space
    locator: Compactness of subsets
---

## Statement

Let $X$ be a [[topological space|0CNQXVBHCX]] and let $K \subseteq X$.
Then $K$ is [[compact|00R0X1WGPX]] if and only if each family $(U_i)_{i \in I}$ of open subsets of $X$ with $K \subseteq \bigcup_{i \in I} U_i$ has a finite subfamily $U_{i_1}, \ldots, U_{i_n}$ with $K \subseteq U_{i_1} \cup \cdots \cup U_{i_n}$.

## Remarks

Proof: the open sets of the [[subspace topology|0D5YHQGDJY]] on $K$ are the sets $U \cap K$ with $U$ open in $X$. So covers of $K$ by open sets of $K$ and covers by open sets of $X$ match each other.
For $K = X$, the statement is the definition of a [[compact space|0QPHW703PV]].
Thus compactness of a subset does not depend on the space around it. If $K \subseteq Y \subseteq X$, then $K$ is compact in $Y$ if and only if it is compact in $X$.

## Explanations

### L1 human

To test if a subset is compact, you can use open sets of the big space.
Each time you cover the subset with open sets, finitely many of them must already be enough.
