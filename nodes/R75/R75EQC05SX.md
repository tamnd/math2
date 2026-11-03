---
tag: R75EQC05SX
kind: definition
name: String-searching algorithm
msc: [68W32, 68R15, 68W40]
defines: TQ3YZDGCHM
uses: [RABRP2KG81, 1P6EP01HZF, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/String-searching_algorithm
---

## Definition

Let $\Sigma$ be a finite [[alphabet|RABRP2KG81]].
Let $P = p_1 \cdots p_m$ and $T = t_1 \cdots t_n$ be [[strings|1P6EP01HZF]] over $\Sigma$ with $1 \le m \le n$; $P$ is the *pattern* and $T$ is the *text*.
The pattern *occurs at position* $i$ of $T$, where $1 \le i \le n - m + 1$, if $t_{i + j - 1} = p_j$ for all $j = 1, \dots, m$.
A *string-searching algorithm* is an [[algorithm|9DMSG5HAQX]] that, given $P$ and $T$, outputs the set of all positions at which $P$ occurs in $T$.

## Remarks

Example: the naive algorithm checks, for each $i = 1, \dots, n - m + 1$, the $m$ equalities $t_{i + j - 1} = p_j$ in turn.
It outputs exactly the positions of occurrence, so it is a string-searching algorithm, and it uses $O(nm)$ comparisons.
For $T = abracadabra$ and $P = abra$ it outputs $\set{1, 8}$.

Non-example: a procedure that stops and outputs the first position of an occurrence solves only the weaker problem of finding one occurrence, not all of them.

Many variants exist: searching for several patterns at once, as in the Aho–Corasick algorithm, or allowing a bounded number of mismatches.
