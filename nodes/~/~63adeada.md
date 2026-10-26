---
tag: ~63adeada
kind: statement
role: corollary
name: A set is closed iff it equals its closure
msc: [54A05]
uses: [~23de8188]
sources:
  - url: https://en.wikipedia.org/wiki/Closure_(topology)
    locator: Properties
---

## Statement

Let $X$ be a [[topological space|~77bfcc55]] and let $S \subseteq X$.
Then $S$ is [[closed|~dfeacff3]] in $X$ if and only if $\overline{S} = S$.

## Remarks

Proof: if $S$ is closed, then $\overline{S} \subseteq S$ by [[closure is the smallest closed superset|~23de8188]], and $S \subseteq \overline{S}$ always holds. If $\overline{S} = S$, then $S$ is closed because the [[closure is closed|~56583d76]].
The dual statement is: $S$ is open if and only if $\operatorname{int} S = S$.

## Explanations

### L1 human

A closed set already contains all the points that you can approach from inside it.
So taking the closure adds nothing.
