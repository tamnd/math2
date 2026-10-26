---
tag: 01CJRJKDAA
kind: statement
role: theorem
name: The complex numbers cannot be ordered
msc: [12J15]
uses: [010JCV9J4E, 07KBQCG9KV]
sources:
  - url: https://en.wikipedia.org/wiki/Ordered_field
    locator: Orderability of fields
---

## Statement

There is no total order $\le$ on $\mathbb{C}$ that makes $\mathbb{C}$, with its usual addition and multiplication, an [[ordered field|010JCV9J4E]].

## Remarks

Proof: in an ordered field, each square is nonnegative, and $1 = 1^2 > 0$. Then $-1 < 0$. But $-1 = i^2$ is a square, by [[i squared is minus one|07KBQCG9KV]], a contradiction.
There are total orders on the set $\mathbb{C}$, for example the lexicographic order. They are not compatible with the field operations.
Thus inequalities such as $z < w$ make sense only for real numbers $z$ and $w$.

## Explanations

### L1 human

You cannot say which of $i$ and $0$ is larger in a way that keeps the usual rules of inequalities.
If $i > 0$, then $i \cdot i > 0$, so $-1 > 0$. If $i < 0$, then $-i > 0$ and $(-i)(-i) > 0$, so again $-1 > 0$.
Both cases are impossible.
