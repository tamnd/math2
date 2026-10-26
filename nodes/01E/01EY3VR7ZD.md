---
tag: 01EY3VR7ZD
kind: statement
role: lemma
name: Urysohn's lemma
aliases: [urysohn-lemma]
msc: [54D15]
uses: [0AJ646N339, 0SY9ECQ19Q, 0G5AV9Q4RR]
sources:
  - url: https://en.wikipedia.org/wiki/Urysohn%27s_lemma
    locator: Formal statement
same_as:
  wikidata: Q1816967
  wikipedia: Urysohn's lemma
---

## Statement

Let $X$ be a [[normal space|0AJ646N339]] and let $A, B \subseteq X$ be disjoint [[closed sets|0G5AV9Q4RR]].
Then there is a [[continuous map|0SY9ECQ19Q]] $f \colon X \to [0, 1]$ with $f(a) = 0$ for all $a \in A$ and $f(b) = 1$ for all $b \in B$.

## Remarks

The converse also holds: if such a function exists for all disjoint closed $A$ and $B$, then $X$ is normal. Take $U = f^{-1}([0, 1/2))$ and $V = f^{-1}((1/2, 1])$.
The proof builds open sets $U_r$ for the dyadic rationals $r \in [0, 1]$, nested by the order of $r$. Then $f(x)$ is the infimum of the $r$ with $x \in U_r$.
In a metric space, the function $f(x) = d(x, A) / (d(x, A) + d(x, B))$ works.
The [[Tietze extension theorem|0X52TNMTCJ]] extends this result to all continuous functions on closed sets.

## Explanations

### L1 human

In a normal space, a continuous function can separate two disjoint closed sets: it is $0$ on one set and $1$ on the other.
So normal spaces have many continuous real functions.
