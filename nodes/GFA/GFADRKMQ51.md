---
tag: GFADRKMQ51
kind: definition
name: Sequential space
msc: [54D55]
defines: WMB2MAEDX4
uses: [0CQHFPGJ45, 0W4CN9E2W5, 0ZCK8DQYN1, 02BH3MCBQB, 0CP5NDD21C]
sources:
  - url: https://en.wikipedia.org/wiki/Sequential_space
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
A set $A \subseteq X$ is sequentially closed when the following holds.
If a sequence $(x_n)$ in $A$ [[converges|0W4CN9E2W5]] in $X$ to a point $x$, then $x \in A$.
$X$ is a *sequential space* when every sequentially closed subset of $X$ is [[closed|0ZCK8DQYN1]].

## Remarks

Every closed set is sequentially closed, so in a sequential space the two notions agree.
Equivalently, a set $U$ is [[open|02BH3MCBQB]] if and only if every sequence that converges to a point of $U$ is eventually in $U$.
In a sequential space, a map to any topological space is continuous if and only if it preserves limits of convergent sequences.
Quotients of sequential spaces are sequential, and the sequential spaces are exactly the quotients of first-countable spaces.

Example: every [[first-countable space|0CP5NDD21C]] is sequential.
If $x \in \overline{A}$ and $U_1 \supseteq U_2 \supseteq \cdots$ is a neighbourhood base at $x$, choose $x_n \in A \cap U_n$; then $x_n \to x$, so a sequentially closed $A$ contains $x$.

Non-example: let $X$ be an uncountable set whose closed sets are $X$ and the countable subsets.
A convergent sequence in $X$ is eventually constant, so every subset of $X$ is sequentially closed.
But an uncountable proper subset is not closed, so $X$ is not sequential.
