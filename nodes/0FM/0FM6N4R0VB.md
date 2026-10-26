---
tag: 0FM6N4R0VB
kind: statement
role: theorem
name: Monotone convergence theorem for sequences
msc: [40A05]
uses: [0KN22AAW5R, 05FQ3VGAR9, 0XKWSSY8P2]
sources:
  - url: https://en.wikipedia.org/wiki/Monotone_convergence_theorem
    locator: Convergence of a monotone sequence of real numbers
same_as:
  wikidata: Q1153584
  wikipedia: Monotone convergence theorem
---

## Statement

Let $(a_n)$ be an increasing real sequence, in the sense of a [[monotone sequence|0KN22AAW5R]].
Assume that $(a_n)$ is bounded above.
Then $(a_n)$ converges, and its limit is the supremum $\sup \{a_n : n \in \mathbb{N}\}$.

## Remarks

The supremum $s$ exists by the completeness of $\mathbb{R}$. For $\varepsilon > 0$ there is $N$ with $a_N > s - \varepsilon$, and then $s - \varepsilon < a_n \le s$ for all $n \ge N$.
The statement fails in $\mathbb{Q}$. The decimal approximations $1, 1.4, 1.41, 1.414, \dots$ of $\sqrt{2}$ increase and are bounded, but they have no limit in $\mathbb{Q}$.
The node [[decreasing sequence bounded below converges|02V2GYAC8P]] gives the dual statement.
An increasing sequence that is not bounded above [[tends to infinity|09AZCV6GMC]].

## Explanations

### L1 human

An increasing sequence that cannot pass a ceiling must pile up somewhere.
It piles up at the lowest ceiling, which is the supremum of its terms.
