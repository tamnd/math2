---
tag: ZZFFBXDTWN
kind: definition
name: Orderable group
msc: ["20F60", "06F15"]
defines: 9BM25E20JQ
uses: [G5S1M9, 0316AYH1SC, 1P8087YGYQ, VQ4SSKS53D, 071DDFVG4J, 020Z5SEN27]
sources:
  - url: https://en.wikipedia.org/wiki/Partially_ordered_group
---

## Definition

Let $G$ be a [[group|G5S1M9]].
The group $G$ is *orderable*, or *bi-orderable*, if there is a [[total order|0316AYH1SC]] $\le$ on $G$ such that for all $a, b, c \in G$,
$$a \le b \implies ca \le cb \text{ and } ac \le bc.$$
That is, $(G, \le)$ is a [[linearly ordered group|1P8087YGYQ]] for some order $\le$.

## Remarks

Example: $\Z^2$ under addition is orderable, since the lexicographic order is total and translation invariant.
Non-example: the cyclic group $\Z/2\Z$ is not orderable.
If $g$ is its nonzero element and $0 < g$, then adding $g$ gives $g < g + g = 0$, a contradiction; the case $g < 0$ is the same.
More generally, an orderable group is a [[torsion-free group|VQ4SSKS53D]].
Every torsion-free [[abelian group|071DDFVG4J]] is orderable.
Every [[free group|020Z5SEN27]] is orderable.
A group is orderable if and only if it has a subset $P$ with $PP \subseteq P$, $gPg^{-1} = P$ for each $g \in G$, and $G = P \sqcup \set{e} \sqcup P^{-1}$.
