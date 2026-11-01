---
tag: DT5PH9QVQ7
kind: statement
role: theorem
name: Compactness via ultrafilters
msc: [54D30, 54A20]
uses: [0CQHFPGJ45, 15PF73BKY6, J64Y3JC0RE, 70M1VAPFN0, 0TVJZYB6SH, 0ZCY0Z80B6]
about: [0TVJZYB6SH, J64Y3JC0RE]
sources:
  - url: https://en.wikipedia.org/wiki/Ultrafilter
---

## Statement

Let $X$ be a [[topological space|0CQHFPGJ45]].
A [[filter|15PF73BKY6]] $\mathcal F$ on $X$ [[converges|70M1VAPFN0]] to $x \in X$ when every [[neighbourhood|0ZCY0Z80B6]] of $x$ belongs to $\mathcal F$.
Then $X$ is [[compact|0TVJZYB6SH]] if and only if every [[ultrafilter|J64Y3JC0RE]] on $X$ converges to at least one point of $X$.

## Remarks

Suppose $X$ is compact and an ultrafilter $\mathcal U$ converges to no point.
Then each $x$ has an open neighbourhood $V_x \notin \mathcal U$, so $X \setminus V_x \in \mathcal U$.
Finitely many $V_x$ cover $X$, and the intersection of their complements is empty but lies in $\mathcal U$, a contradiction.
Conversely, if an open cover has no finite subcover, the complements of its members generate a proper filter; an ultrafilter that contains it cannot converge to any point.
This direction uses the ultrafilter lemma, a weak form of the axiom of choice.

The theorem gives a short proof of [[Tychonoff's theorem|0JTRSJKCFB]]: an ultrafilter on a product converges as soon as all its images under the projections converge.
If $X$ is also [[Hausdorff|0S1FJ8VEX9]], each ultrafilter has exactly one limit.
For example, on $X = [0, 1]$, the ultrafilter of all sets that contain a fixed point $p$ converges to $p$.

## Explanations

### L1 human

An ultrafilter on a space is a way of choosing, for every subset, whether it is large or small, in a consistent way.
The theorem says that a space is compact exactly when every such choice points to some place in the space.
It is the filter version of the fact that, in a compact metric space, every sequence has a convergent subsequence.

### L2 human

For general spaces, sequences are not enough to describe compactness, but ultrafilters are.
The criterion turns proofs about open covers into proofs about limits.
Its best-known use is the proof of Tychonoff's theorem, where convergence in a product is checked coordinate by coordinate.
It also leads to the Stone–Čech compactification of a discrete space as the space of ultrafilters on it.
