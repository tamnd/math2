---
tag: 4VW0VADHC0
kind: statement
role: theorem
name: Følner condition implies amenability
msc: ["43A07", "20F65"]
uses: [6WZR80CPBD, CEAT9BESKK, ZYNY2VFECQ, 1BXEJXQ2YT]
about: [6WZR80CPBD, CEAT9BESKK]
sources:
  - url: https://en.wikipedia.org/wiki/Amenable_group
---

## Statement

Let $G$ be a countable group that has a [[Følner sequence|6WZR80CPBD]] $(F_n)$.
Then $G$ is [[amenable|CEAT9BESKK]].
More precisely, every weak-$*$ cluster point of the averages $m_n(f) = \frac{1}{\abs{F_n}} \sum_{x \in F_n} f(x)$, $f \in \ell^\infty(G)$, is a left-[[invariant mean|ZYNY2VFECQ]] on $G$.

## Remarks

Each $m_n$ is positive and satisfies $m_n(\mathbf{1}) = 1$.
For $g \in G$ and $(g \cdot f)(x) = f(g^{-1} x)$, one has $m_n(g \cdot f) = \frac{1}{\abs{F_n}} \sum_{y \in g^{-1} F_n} f(y)$, so
$$\abs{m_n(g \cdot f) - m_n(f)} \le \norm{f}_\infty \frac{\abs{g^{-1} F_n \triangle F_n}}{\abs{F_n}} \to 0.$$
The means form a weak-$*$ compact set by the [[Banach–Alaoglu theorem|1BXEJXQ2YT]], so $(m_n)$ has a cluster point $m$, and the estimate shows that $m$ is invariant.

Example: the intervals $\set{0, \ldots, n-1}$ in $\Z$ give invariant means on $\Z$; restricted to functions supported on $\N$, they are Banach limits obtained from Cesàro averages.

The converse also holds: Følner's theorem says that every countable amenable group has a Følner sequence.
The same argument works for a locally compact group with a Følner sequence of compact sets, using normalized Haar measure on $F_n$.

## Explanations

### L1 human

If a group contains large finite sets that are almost unchanged by every shift, then averaging over these sets gives better and better shift-invariant averages.
Passing to a limit gives a perfectly shift-invariant average, which is what amenability asks for.

### L2 human

This is the easy half of Følner's characterization of amenability, and it is the usual way to prove that a given group is amenable.
For example, groups of polynomial growth, and in particular finitely generated nilpotent groups, have Følner sequences made of balls.
The limit step is not constructive: it uses compactness, and the resulting mean is not unique in general.
