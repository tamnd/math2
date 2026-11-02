---
tag: S70JBRSQZX
kind: example
name: Arithmetic progression
msc: [11B25, 40A05]
instance_of: [0G9EKM0E15]
uses: [01QZNHQWYD]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetic_progression
same_as:
  wikidata: Q170008
  wikipedia: Arithmetic progression
---

## Example

Let $a$ and $d$ be real numbers.
The sequence $(a_n)_{n \ge 0}$ with $a_n = a + n d$ is the *arithmetic progression* with first term $a$ and common difference $d$.
It is a [[sequence|0G9EKM0E15]] in which each term minus the previous one is the same number: $a_{n+1} - a_n = d$ for every $n \ge 0$.
For example, $a = 3$ and $d = 4$ give $3, 7, 11, 15, \ldots$.

The sum of the first $n$ terms is
$$a_0 + a_1 + \cdots + a_{n-1} = n a + \frac{n(n-1)}{2} d = \frac{n (a_0 + a_{n-1})}{2}.$$
Check: $\sum_{k=0}^{n-1} (a + kd) = na + d \sum_{k=0}^{n-1} k$, and $\sum_{k=0}^{n-1} k = n(n-1)/2$ by the [[sum of the first natural numbers|01QZNHQWYD]].
For $3 + 7 + 11 + 15$ this gives $4 \cdot (3 + 15) / 2 = 36$.

## Remarks

The progression converges if and only if $d = 0$, since otherwise $\abs{a_n} \ge n \abs{d} - \abs{a}$ tends to $\infty$.
So the series $\sum_n a_n$ of an arithmetic progression diverges unless $a = d = 0$.
Each term is the average of its two neighbours: $a_n = (a_{n-1} + a_{n+1})/2$ for $n \ge 1$.

## Explanations

### L1 human

An arithmetic progression goes up or down in equal steps, like $2, 5, 8, 11$.
To add its terms, pair the first with the last, the second with the second to last, and so on.
Every pair has the same sum, so the total is the number of terms times the average of the first and the last term.
