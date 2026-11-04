---
tag: YBNEDEAREF
kind: proof
name: Proof that a set is closed if and only if it equals its closure
msc: [54A05]
proves: 0D2W7FS52T
uses: [0CNQXVBHCX, 0G5AV9Q4RR, 0DRKT1QJR7, 0SHC6Z304Z]
sources:
  - url: https://en.wikipedia.org/wiki/Closure_(topology)
---

## Proof

1. Let $X$ be a [[topological space|0CNQXVBHCX]], let $S \subseteq X$, and let $\overline{S}$ be the [[closure|0DRKT1QJR7]] of $S$.
2. By [[closure is the smallest closed superset|0SHC6Z304Z]], we have $S \subseteq \overline{S}$, and $\overline{S}$ is [[closed|0G5AV9Q4RR]].
3. Suppose that $S$ is closed. Then $S$ is a closed set with $S \subseteq S$.
4. By the same result, $\overline{S} \subseteq S$. With step 2, $\overline{S} = S$.
5. Conversely, suppose that $\overline{S} = S$. By step 2, $\overline{S}$ is closed, so $S$ is closed.

## Idea

The closure always contains $S$ and is always closed. If $S$ is already closed, it is one of the closed sets the closure must fit inside. So the two sets agree.
