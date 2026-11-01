---
tag: HQMNCB9FZ5
kind: definition
name: Fréchet–Urysohn space
msc: [54D55]
defines: R3B4V9WW2S
uses: [0CQHFPGJ45, 0QEAJB91GZ, 0W4CN9E2W5, 0CP5NDD21C, WMB2MAEDX4]
sources:
  - url: https://en.wikipedia.org/wiki/Fréchet–Urysohn_space
---

## Definition

A [[topological space|0CQHFPGJ45]] $X$ is a *Fréchet–Urysohn space* when the following holds.
For every $A \subseteq X$ and every point $x$ in the [[closure|0QEAJB91GZ]] $\overline{A}$, there is a sequence $(x_n)$ in $A$ that [[converges|0W4CN9E2W5]] to $x$.

## Remarks

A Fréchet–Urysohn space is [[sequential|WMB2MAEDX4]]: if $A$ is sequentially closed and $x \in \overline{A}$, a sequence in $A$ converges to $x$, so $x \in A$.
Every subspace of a Fréchet–Urysohn space is Fréchet–Urysohn.
A sequential space is Fréchet–Urysohn if and only if each of its subspaces is sequential.

Example: every [[first-countable space|0CP5NDD21C]] is Fréchet–Urysohn.
For $x \in \overline{A}$ and a decreasing neighbourhood base $U_1 \supseteq U_2 \supseteq \cdots$ at $x$, pick $x_n \in A \cap U_n$; then $x_n \to x$.

Non-example: let $X$ be an uncountable set whose closed sets are $X$ and the countable subsets, and let $A \subset X$ with $A$ and $X \setminus A$ uncountable.
Then $\overline{A} = X$, but the only convergent sequences are eventually constant.
So a point $x \notin A$ is in $\overline{A}$ but is not the limit of a sequence in $A$.

The name Fréchet space is also used, but it has other meanings.
