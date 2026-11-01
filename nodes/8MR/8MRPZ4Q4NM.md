---
tag: 8MRPZ4Q4NM
kind: definition
name: Word metric
msc: ["20F65"]
defines: VCHJVR9NGH
uses: [G5S1M9, 082DWWXMRJ, 0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Word_metric
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $S$ be a subset of $G$ that generates $G$.
The *word length* $\abs{g}_S$ of $g \in G$ is the least integer $n \ge 0$ such that $g = s_1^{\varepsilon_1} s_2^{\varepsilon_2} \cdots s_n^{\varepsilon_n}$ for some $s_1, \ldots, s_n \in S$ and $\varepsilon_1, \ldots, \varepsilon_n \in \set{1, -1}$.
The *word metric* on $G$ with respect to $S$ is the map $d_S \colon G \times G \to \Z_{\ge 0}$ given by
$$d_S(g, h) = \abs{g^{-1} h}_S.$$

## Remarks

$d_S$ is a [[metric|0VKD1TP7F3]].
It is symmetric because $\abs{g^{-1}}_S = \abs{g}_S$, and the triangle inequality holds because $\abs{gh}_S \le \abs{g}_S + \abs{h}_S$.
It is invariant under left multiplication: $d_S(kg, kh) = d_S(g, h)$ for all $k \in G$.
It equals the path distance between $g$ and $h$ in the [[Cayley graph|0GYQK9NDJF]] of $G$ with respect to $S$.
If $S$ and $T$ are finite generating sets, there is a constant $C \ge 1$ with $d_T \le C d_S$ and $d_S \le C d_T$.

Example: let $G = \Z$ and $S = \set{2, 3}$.
Then $\abs{1}_S = 2$: the number $1$ is not in $\set{\pm 2, \pm 3}$, so $\abs{1}_S \ge 2$, and $1 = 3 + (-2)$.
So $d_S(0, 1) = 2$, while $d_{\set{1}}(0, 1) = 1$.

Non-example: in $\Z$, the set $S = \set{2}$ does not generate $\Z$.
The number $1$ is not a sum of terms $\pm 2$, so $\abs{1}_S$ is not defined, and $d_S(0, 1)$ is not a real number.
