---
tag: ZF18TYQMSZ
kind: proof
name: Proof that the closure is the set of limits of sequences
msc: ["54E35"]
proves: 003QP7A8HG
uses: [063W5JMY85, 0DRKT1QJR7, 06JYPJ4WHH, 068P0P32DW, 0A3GWZ86AY, 0SHC6Z304Z, 09GQ3ZTQJ9]
sources:
  - url: https://en.wikipedia.org/wiki/Closure_(topology)
---

## Proof

We prove each direction separately.

1. Let $(X, d)$ be a [[metric space|063W5JMY85]], let $S \subseteq X$, let $x \in X$, and let $\overline{S}$ be the [[closure|0DRKT1QJR7]] of $S$.
2. First let $x \in \overline{S}$. By the [[description of the closure in a metric space|068P0P32DW]], each $n \ge 1$ gives a point $s_n \in S$ with $d(x, s_n) < 1/n$.
3. We show that $s_n \to x$, in the sense of [[convergence|06JYPJ4WHH]]. Let $\varepsilon > 0$.
4. The [[reals are Archimedean|0A3GWZ86AY]], so there is a natural number $N$ with $N \varepsilon > 1$. Then $N \ge 1$, and $1/N < \varepsilon$.
5. For $n \ge N$, symmetry of $d$ gives $d(s_n, x) = d(x, s_n) < 1/n \le 1/N < \varepsilon$. So $s_n \to x$.
6. Conversely, let $(s_n)$ be a sequence of points of $S$ with $s_n \to x$.
7. By [[closure is the smallest closed superset|0SHC6Z304Z]], $S \subseteq \overline{S}$ and $\overline{S}$ is closed. So $(s_n)$ is a sequence of points of the closed set $\overline{S}$.
8. Since [[closed sets contain their limits|09GQ3ZTQJ9]], we get $x \in \overline{S}$.

## Idea

A point of the closure has points of $S$ at distance less than $1/n$ for every $n$, and these form a sequence that tends to it. Conversely, the closure is a closed set that contains $S$. So it keeps every limit of points of $S$.
