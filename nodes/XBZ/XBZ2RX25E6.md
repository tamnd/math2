---
tag: XBZ2RX25E6
kind: definition
name: Harmonic space
msc: [31D05, 31C05]
defines: DWN0XEQHHK
uses: [0FE2SB8WVJ, TB6TM6R4MD, 0X3WGX95FE, 0DEB0JMN0W, P15K8RKHDV, VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Potential_theory
---

## Definition

Let $X$ be a [[locally compact|0FE2SB8WVJ]] Hausdorff space with a countable base.
To each open set $U \subseteq X$, let a linear subspace $\mathcal{H}(U)$ of the real [[continuous functions|0X3WGX95FE]] on $U$ be given.
Its elements are called *harmonic* on $U$.
An open set $V$ with compact closure $\overline{V} \subseteq X$ is *regular* if the following holds for every continuous $f \colon \partial V \to \R$.
There is a unique continuous $h \colon \overline{V} \to \R$ with $h|_V \in \mathcal{H}(V)$ and $h = f$ on $\partial V$, and $h \ge 0$ whenever $f \ge 0$.
The pair $(X, \mathcal{H})$ is a *harmonic space* if:

1. $\mathcal{H}$ is a [[sheaf|TB6TM6R4MD]]. Restrictions of harmonic functions to smaller open sets are harmonic. A continuous function on $U = \bigcup_i U_i$ that is harmonic on each $U_i$ is harmonic on $U$.
2. The regular sets form a base of the topology of $X$.
3. For every open $U$ and every increasing sequence $(h_n)$ in $\mathcal{H}(U)$ whose limit $h$ is locally bounded on $U$, the function $h$ lies in $\mathcal{H}(U)$.

## Remarks

These are the axioms in the form given by Bauer; several authors add a positivity or separation axiom, and some impose a stronger convergence axiom.
Example: $X = \R^n$ with $\mathcal{H}(U)$ the classical [[harmonic functions|0DEB0JMN0W]] on $U$.
Clause 1 is clear, since harmonicity is a local condition.
Every ball is regular, by the Poisson integral and the maximum principle, so clause 2 holds.
Clause 3 follows from [[Harnack's principle|P15K8RKHDV]].
A second example is $X = \R^n \times \R$ with $\mathcal{H}(U)$ the solutions of the [[heat equation|VP2HN86VAG]] $\partial_t u = \Delta u$ on $U$.
Non-example: on $X = \R^n$, let $\mathcal{H}(U)$ be all continuous functions on $U$.
No open set $V$ with nonempty boundary is regular, since a continuous extension of boundary values is never unique, so clause 2 fails.
