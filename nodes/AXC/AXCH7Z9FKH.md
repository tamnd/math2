---
tag: AXCH7Z9FKH
kind: conjecture
name: 1/3–2/3 conjecture
msc: [06A07]
uses: [0QV2JS9RJ3, 0FRXBVVR03, W8DZ5KGGHN]
about: [W8DZ5KGGHN]
sources:
  - url: https://en.wikipedia.org/wiki/1/3–2/3_conjecture
history:
  posed_by: "Sergey Kislitsyn"
  first_stated: "1968"
---

## Statement

Let $(P, \le)$ be a finite [[partially ordered set|0QV2JS9RJ3]] that is not a [[total order|0FRXBVVR03]].
For $x, y \in P$, let $p(x, y)$ be the fraction of the [[linear extensions|W8DZ5KGGHN]] of $P$ in which $x$ comes before $y$.
Then there are elements $x, y \in P$ with
$$\frac{1}{3} \le p(x, y) \le \frac{2}{3}.$$

## Remarks

The conjecture is open.
The bounds cannot be improved: for $P = \set{a, b, c}$ with $a < b$ as the only relation, the linear extensions are $cab$, $acb$ and $abc$, so $p(a, c) = 2/3$, $p(c, b) = 2/3$ and $p(a, b) = 1$.
Kahn and Saks proved that a pair with $3/11 \le p(x, y) \le 8/11$ always exists.
Brightwell, Felsner and Trotter improved the constant $3/11$ to $(5 - \sqrt{5})/10 \approx 0.276$.
Linial proved the conjecture for posets of width $2$.
The conjecture was later stated again, independently, by Michael Fredman and by Nathan Linial.

## Explanations

### L1 human

Suppose that some comparisons between items are already known, and the goal is to sort them completely.
The conjecture says that one can always find a comparison whose answer is not too predictable: each answer occurs in at least one third of the remaining possible orders.
Such a comparison cuts the number of possible orders by a fixed factor, which is why the question matters for sorting with partial information.
