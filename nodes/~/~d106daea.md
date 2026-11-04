---
kind: statement
msc:
- 39A06
name: A solution of (A-r)f=0 is a geometric sequence fixed by its value at 0
role: lemma
sources:
- locator: source/s_recurrence_rigorous.ptx:62
  url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_recurrence_rigorous.ptx#L62
tag: ~d106daea
uses:
- MBK6AE6734
---

## Statement

Let $A$ be the [[shift operator|MBK6AE6734]] on functions $f:\mathbb{Z}\to\mathbb{C}$, so that $(Af)(n)=f(n+1)$.
Let $r$ be a nonzero number, and let $f$ satisfy the operator equation $(A-r)f=0$, that is, $f(n+1)=r\,f(n)$ for all integers $n$.
Put $c=f(0)$.
Then $f(n)=c\,r^n$ for every integer $n$.

## Remarks

The values of $f$ at nonnegative $n$ follow from the rule $f(n+1)=rf(n)$ by induction upward from $0$.
The values at negative $n$ follow by induction downward from $0$, using $f(n)=r^{-1}f(n+1)$. This step is where $r\neq 0$ is needed.
If $r=0$, the claim can fail: a function with $f(0)=c$ and $f(n)=0$ for $n\ge 1$ is a solution, but its values at negative $n$ are not fixed by $c$.
