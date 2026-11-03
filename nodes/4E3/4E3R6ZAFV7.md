---
tag: 4E3R6ZAFV7
kind: definition
name: Edit distance
msc: [68W32, 68R15, 68P30]
defines: W6KG32T7AJ
uses: [RABRP2KG81, 1P6EP01HZF, 063W5JMY85, EP5HNGSXFA]
sources:
  - url: https://en.wikipedia.org/wiki/Edit_distance
  - url: https://en.wikipedia.org/wiki/Levenshtein_distance
---

## Definition

Let $\Sigma$ be a finite [[alphabet|RABRP2KG81]] and let $\Sigma^*$ be the set of finite [[strings|1P6EP01HZF]] over $\Sigma$.
An *edit operation* changes a string $x \in \Sigma^*$ in one of these ways:

1. insertion of one symbol of $\Sigma$ at some place in $x$;
2. deletion of one symbol of $x$;
3. substitution of one symbol of $x$ by a different symbol of $\Sigma$.

The *edit distance*, or *Levenshtein distance*, $d(x, y)$ of $x, y \in \Sigma^*$ is the least number of edit operations that turn $x$ into $y$.

## Remarks

Example: $d(abc, acd) = 2$.
Deleting $b$ and then inserting $d$ at the end turns $abc$ into $acd$, so $d \le 2$.
A single operation either changes the length or changes exactly one position, while $abc$ and $acd$ have equal length and differ in two positions, so $d \ge 2$.

Non-example: if only substitutions are allowed, the strings $ab$ and $b$ are at no finite distance, since substitution never changes the length.
That restricted distance is the [[Hamming distance|EP5HNGSXFA]], defined only for strings of equal length.

Since each operation can be undone by one operation, $d$ is symmetric, and $d$ is a [[metric|063W5JMY85]] on $\Sigma^*$.
For $x = x_1 \cdots x_m$ and $y = y_1 \cdots y_n$, let $D(i, j)$ be the edit distance of the prefixes $x_1 \cdots x_i$ and $y_1 \cdots y_j$.
Then $D(i, 0) = i$, $D(0, j) = j$, and
$$D(i, j) = \min\bigl(D(i - 1, j) + 1,\ D(i, j - 1) + 1,\ D(i - 1, j - 1) + [x_i \ne y_j]\bigr),$$
where $[x_i \ne y_j]$ is $1$ if $x_i \ne y_j$ and $0$ otherwise.
This gives $d(x, y) = D(m, n)$ in time $O(mn)$.
Other edit distances use other sets of operations, for example adding the transposition of two adjacent symbols.
