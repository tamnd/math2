---
tag: QXPJTWGE4D
kind: definition
name: Polynomial-time reduction
msc: [68Q17, 68Q15]
defines: V0K79AD81V
uses: [5MFZ4VNY6D, 758EYCN27B, T00W8RQT8E, JTAH37JTHD, GVT2NKN37K]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial-time_reduction
---

## Definition

Let $\Sigma$ be a finite alphabet, and let $A, B \subseteq \Sigma^*$ be [[languages|5MFZ4VNY6D]].
A *polynomial-time reduction* from $A$ to $B$ is a function $f \colon \Sigma^* \to \Sigma^*$ with two properties.

1. Some deterministic [[Turing machine|758EYCN27B]] computes $f$ and halts within $p(\abs{x})$ steps on every input $x$, for some polynomial $p$.
2. For every $x \in \Sigma^*$, $x \in A$ holds exactly when $f(x) \in B$.

The language $A$ is *polynomial-time reducible* to $B$, written $A \le_p B$, if such an $f$ exists.

## Remarks

Example: let $A$ be the set of encodings of pairs $(G, k)$ where the graph $G$ has an independent set of size $k$.
Let $B$ be the set of pairs $(G, k)$ where $G$ has a clique of size $k$.
The map $(G, k) \mapsto (\overline{G}, k)$, with $\overline{G}$ the complement graph, is computable in polynomial time.
A set of vertices is independent in $G$ exactly when it is a clique in $\overline{G}$, so clause 2 holds and $A \le_p B$.

Non-example: the map that sends $(G, k)$ to a fixed yes-instance of $B$ when $A$ holds, and to a fixed no-instance otherwise, satisfies clause 2.
No polynomial-time algorithm is known to compute it, so it is not known to satisfy clause 1.

Such reductions are also called Karp reductions or polynomial-time [[many-one reductions|JTAH37JTHD]].
The relation $\le_p$ is reflexive and transitive.
If $A \le_p B$ and $B \in$ [[P|GVT2NKN37K]], then $A \in \mathrm{P}$.
A Cook reduction is the weaker notion where $A$ is decided in polynomial time by a machine that may ask many questions about $B$.
