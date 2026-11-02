---
tag: JBWB5H8JZG
kind: statement
role: theorem
name: Riesz's subsequence theorem
msc: [28A20]
uses: [G5WT6QN8WR, BP8S3Z5TW9, RARTMA0ZEC, 0F1PR74BRX]
about: [G5WT6QN8WR]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_in_measure
---

## Statement

Let $(X, \Sigma, \mu)$ be a measure space, and let $f_1, f_2, \ldots$ and $f$ be measurable functions from $X$ to $\R$.
If $f_n \to f$ [[in measure|G5WT6QN8WR]], then there is a [[subsequence|0F1PR74BRX]] $(f_{n_k})$ such that $f_{n_k}(x) \to f(x)$ for [[almost every|RARTMA0ZEC]] $x \in X$.

## Remarks

Choose $n_1 < n_2 < \cdots$ with $\mu(E_k) < 2^{-k}$, where $E_k = \set{x : \abs{f_{n_k}(x) - f(x)} \ge 2^{-k}}$.
Let $E = \bigcap_{j} \bigcup_{k \ge j} E_k$; then $\mu(E) \le \sum_{k \ge j} 2^{-k} = 2^{1-j}$ for every $j$, so $\mu(E) = 0$.
For $x \notin E$, one has $\abs{f_{n_k}(x) - f(x)} < 2^{-k}$ for all large $k$, so $f_{n_k}(x) \to f(x)$.
Example: the sliding indicator functions $f_{2^k + j} = \mathbf{1}_{[j 2^{-k}, (j+1) 2^{-k}]}$ on $[0, 1]$ converge to $0$ in measure but at no point; the subsequence $f_{2^k}$, the indicators of $[0, 2^{-k}]$, converges to $0$ at every $x \ne 0$.
The passage to a subsequence is necessary, as this example shows.

## Explanations

### L1 human

Convergence in measure is weak: it allows the sequence to fail to converge at every point.
This theorem says that one can always pick out a subsequence that does converge, except on a set of measure zero.

### L2 human

The result is a standard tool to pass from integral estimates to pointwise statements.
For example, if $f_n \to f$ in $L^p$, then $f_n \to f$ in measure, so a subsequence converges to $f$ almost everywhere; this is a step in the proof that $L^p$ is complete.
On a space of finite measure, it gives a characterisation of convergence in measure.
There, $f_n \to f$ in measure if and only if every subsequence has a further subsequence converging to $f$ almost everywhere.
