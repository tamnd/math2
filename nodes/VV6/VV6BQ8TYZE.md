---
tag: VV6BQ8TYZE
kind: definition
name: Sequence alignment
msc: [92D20, 68W32]
defines: G42Y4TPD4N
uses: [1P6EP01HZF, W6KG32T7AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Sequence_alignment
---

## Definition

Let $\Sigma$ be a finite alphabet and let $-$ be a gap symbol not in $\Sigma$.
A *(global) alignment* of [[strings|1P6EP01HZF]] $s_1, \dots, s_k$ over $\Sigma$ is a $k$-tuple of strings $s_1', \dots, s_k'$ over $\Sigma \cup \set{-}$ such that:

1. all $s_i'$ have the same length $L$;
2. deleting every $-$ from $s_i'$ gives $s_i$, for each $i$;
3. no column $j \le L$ has $s_i'[j] = -$ for all $i$.

Given a score $\sigma(x, y)$ for each pair $x, y \in \Sigma \cup \set{-}$, not both $-$, the score of a pairwise alignment ($k = 2$) is $\sum_{j=1}^{L} \sigma(s_1'[j], s_2'[j])$.
A *local alignment* of $s_1$ and $s_2$ is a global alignment of a substring of $s_1$ with a substring of $s_2$.

## Remarks

Example: $s_1' = ACGT$ and $s_2' = A{-}GT$ is an alignment of $ACGT$ and $AGT$: both rows have length $4$, deleting the gap from $s_2'$ gives $AGT$, and no column is all gaps.
With score $+1$ for a match, $-1$ for a mismatch and $-1$ for a gap, its score is $1 - 1 + 1 + 1 = 2$.
Non-example: $ACGT{-}$ over $A{-}GT{-}$ fails clause 3, since its last column consists of gaps only.
With score $0$ for a match and $-1$ for a mismatch or a gap, the best pairwise score is minus the unit-cost [[edit distance|W6KG32T7AJ]] of the two strings.
For $k \ge 3$ one speaks of a multiple sequence alignment.
