---
tag: ~9fdddcbe
kind: statement
role: axiom
name: Axiom of choice
aliases: [ac, axiom-of-choice]
msc: ["03E25"]
uses: [~385ddbcc, ~d103e2ff]
sources:
  - url: https://en.wikipedia.org/wiki/Axiom_of_choice
    locator: lead section
same_as:
  wikidata: Q179692
  wikipedia: Axiom of choice
---

## Statement

Let $X$ be a [[set|~bd92ceee]] of nonempty sets.
Then there is a [[choice function|~385ddbcc]] on $X$, that is, a function $c \colon X \to \bigcup X$ such that $c(S) \in S$ for each $S \in X$.

## Remarks

An equivalent form: for each [[family|~1788469e]] $(A_i)_{i \in I}$ of nonempty sets, the product $\prod_{i \in I} A_i$ is nonempty.
Over ZF, it is equivalent to [[Zorn's lemma|~6a9de93f]], to the [[well-ordering theorem|~c22307cc]] and to the [[comparability of cardinals|~be610989]].
It is independent of ZF, if ZF is consistent.
Kurt Gödel showed in 1938 that ZF does not refute it, and Paul Cohen showed in 1963 that ZF does not prove it.

## History

Ernst Zermelo formulated the axiom in 1904 for his proof of the [[well-ordering theorem|~c22307cc]].

## Explanations

### L1 human

For finitely many nonempty boxes, you can pick one object from each box, one box at a time.
For infinitely many boxes without a rule to pick, the axiom of choice says that a selection still exists.
From infinitely many pairs of shoes, you can take the left shoe of each pair.
From infinitely many pairs of identical socks, there is no such rule, and you need the axiom.
