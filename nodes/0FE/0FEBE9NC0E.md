---
tag: 0FEBE9NC0E
kind: statement
role: theorem
name: A subgroup whose index is the smallest prime divisor of the order is normal
msc: [20D60]
uses: [0W77CVBCHQ, 04QEBF8S49]
sources:
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: Properties
---

## Statement

Let $G$ be a finite [[group|G5S1M9]] and let $p$ be the smallest prime number that divides $|G|$. Let $H$ be a [[subgroup|0X1JXT47GA]] of $G$ of [[index|0DTXBQPA2S]] $p$.
Then $H$ is [[normal|0CB0DX5BVV]] in $G$.

## Remarks

For $p = 2$ this is the fact that [[subgroups of index two are normal|0V547YQRMV]].
The proof lets $G$ act on the $p$ left cosets of $H$. The kernel $K$ of this action lies in $H$, and $[G : K]$ divides both $|G|$ and $p!$.
Since $p$ is the smallest prime divisor of $|G|$, this forces $[G : K] = p$, so $H = K$ is normal.

## Explanations

### L1 human

Index $2$ is not the only small index that forces normality.
If the index is the smallest prime that divides the order of the group, the subgroup is also normal.
For example, a subgroup of index $3$ in a group of order $75 = 3 \cdot 5^2$ is normal.
