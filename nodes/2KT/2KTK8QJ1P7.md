---
tag: 2KTK8QJ1P7
kind: definition
name: Merge sort
msc: [68P10, 68W40]
defines: GNGVP9EE8Y
uses: [MGKDQAM7K3, G9NFJ55KCX]
sources:
  - url: https://en.wikipedia.org/wiki/Merge_sort
---

## Definition

Let $(X, \le)$ be a totally ordered set.
The *merge* of two sorted sequences $u = (u_1, \dots, u_p)$ and $v = (v_1, \dots, v_q)$ over $X$ is defined recursively:

1. if $u$ is empty, the merge is $v$, and if $v$ is empty, the merge is $u$;
2. if $u_1 \le v_1$, the merge is $u_1$ followed by the merge of $(u_2, \dots, u_p)$ and $v$;
3. otherwise, it is $v_1$ followed by the merge of $u$ and $(v_2, \dots, v_q)$.

*Merge sort* is the [[sorting algorithm|MGKDQAM7K3]] that, on input $a = (a_1, \dots, a_n)$, returns $a$ if $n \le 1$.
Otherwise, with $m = \floor{n/2}$, it sorts $(a_1, \dots, a_m)$ and $(a_{m+1}, \dots, a_n)$ by merge sort and returns the merge of the results.

## Remarks

The merge of sequences of lengths $p$ and $q$ uses at most $p + q - 1$ comparisons.
So the worst-case number of comparisons $C(n)$ satisfies $C(n) \le C(\floor{n/2}) + C(\ceil{n/2}) + n - 1$, which gives $C(n) \le n \ceil{\log_2 n}$.
Clause 2 takes from $u$ on ties, so merge sort is stable.

Example: merge sort of $(3, 1, 2)$ splits it into $(3)$ and $(1, 2)$.
The second part is split into $(1)$ and $(2)$ and merged back into $(1, 2)$.
Merging $(3)$ with $(1, 2)$ takes $1$, then $2$, then appends $(3)$, giving $(1, 2, 3)$.

Non-example: concatenating the two sorted halves instead of merging them does not sort: for $(3, 1)$ the halves $(3)$ and $(1)$ give $(3, 1)$.
