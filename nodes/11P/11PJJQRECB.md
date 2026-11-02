---
tag: 11PJJQRECB
kind: definition
name: Relative CW complex
msc: [57Q05, 55U10]
defines: D0DAFG8QK6
uses: [0CNQXVBHCX, 05DSV40EB9, A486VR787Z, 0V8046R0P9, 5W95QFHXPR]
sources:
  - url: https://en.wikipedia.org/wiki/CW_complex
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]] and let $A \subseteq X$ be a subspace.
For $n \ge 0$ let $D^n$ be the closed unit [[ball|05DSV40EB9]] in $\R^n$ with boundary $S^{n-1}$, where $S^{-1} = \emptyset$.
A *relative CW structure* on $(X, A)$ is a sequence of subspaces $A = X^{-1} \subseteq X^0 \subseteq X^1 \subseteq \cdots$ of $X$ such that:

1. For each $n \ge 0$ there are a set $J_n$ and maps $\varphi_j \colon S^{n-1} \to X^{n-1}$, $j \in J_n$, with the following property.
   The space $X^n$ is the pushout of $X^{n-1} \leftarrow \bigsqcup_{j \in J_n} S^{n-1} \to \bigsqcup_{j \in J_n} D^n$, where the left map is given by the $\varphi_j$.
   That is, $X^n$ is the [[quotient|0V8046R0P9]] of the [[disjoint union|A486VR787Z]] $X^{n-1} \sqcup \bigsqcup_{j} D^n$ that identifies each $x \in S^{n-1}$ in the $j$-th disk with $\varphi_j(x)$.
2. $X = \bigcup_{n \ge -1} X^n$.
3. A subset $C \subseteq X$ is closed if and only if $C \cap X^n$ is closed in $X^n$ for every $n$.

A *relative CW complex* is a pair $(X, A)$ with a relative CW structure.
The images of the open disks $D^n \setminus S^{n-1}$ are the $n$-cells of $X$ relative to $A$.

## Remarks

When $A = \emptyset$, a relative CW complex is the same as a [[CW complex|5W95QFHXPR]].
If $A$ is a subcomplex of a CW complex $X$, then $(X, A)$ is a relative CW complex.

Example: let $A = S^1$ and $X = D^2$.
Take $X^0 = X^1 = S^1$ with $J_0 = J_1 = \emptyset$, and $X^2 = D^2$ with one $2$-cell attached by the identity $S^1 \to S^1$.
Clause 1 holds since $D^2$ is the pushout of $S^1 \leftarrow S^1 \to D^2$, and clauses 2 and 3 hold since the filtration stops at $X^2 = X$.

Non-example: let $A = \set{0}$ and $X = \set{0} \cup \set{1/m : m \ge 1} \subseteq \R$.
The only cells available are $0$-cells, so $X = X^0$.
Clause 1 then forces $X^0$ to be the disjoint union of $A$ and a discrete set, but in $X$ the points $1/m$ converge to $0$, so clause 1 fails.
