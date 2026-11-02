---
tag: NEC48RHNN0
kind: statement
role: theorem
name: Śleszyński–Pringsheim theorem
msc: [40A15, 30B70]
uses: [0BK6JBK58W, 0SRWNR42BQ, 6WYYMPH21Q]
about: [04P2RJ4WPS]
sources:
  - url: https://en.wikipedia.org/wiki/Śleszyński–Pringsheim_theorem
same_as:
  wikidata: Q8081891
  wikipedia: Śleszyński–Pringsheim theorem
---

## Statement

Let $a_1, a_2, \dots$ and $b_1, b_2, \dots$ be complex numbers such that $\abs{b_n} \ge \abs{a_n} + 1$ for every $n \ge 1$.
Then the [[continued fraction|0BK6JBK58W]]
$$f = \cfrac{a_1}{b_1 + \cfrac{a_2}{b_2 + \cfrac{a_3}{b_3 + \cdots}}}$$
converges, and its value satisfies $\abs{f} \le 1$.

## Remarks

Proof idea: with the [[fundamental recurrence formulas|6WYYMPH21Q]] ($b_0 = 0$), the denominators satisfy $\abs{B_n} \ge (\abs{a_n} + 1)\abs{B_{n-1}} - \abs{a_n}\abs{B_{n-2}}$.
By induction $\abs{B_n} - \abs{B_{n-1}} \ge \abs{a_1 \cdots a_n}$, so $1 = \abs{B_0} \le \abs{B_1} \le \cdots$ and no $B_n$ vanishes.
Then $\abs{f_n - f_{n-1}} = \frac{\abs{a_1 \cdots a_n}}{\abs{B_n}\abs{B_{n-1}}} \le \frac{1}{\abs{B_{n-1}}} - \frac{1}{\abs{B_n}}$, and this telescopes: the series $\sum (f_n - f_{n-1})$ converges absolutely with total at most $1$, where $f_0 = 0$.
Example: $a_n = 1$ and $b_n = 2$ satisfy the condition, and the value is $\sqrt{2} - 1$.
The condition cannot simply be dropped: for $a_n = -1$ and $b_n = 1$ one has $\abs{b_n} < \abs{a_n} + 1$, and the convergents repeat the cycle $-1, \infty, 0$, so the continued fraction diverges.

## Explanations

### L1 human

A continued fraction converges when each partial denominator is larger than the partial numerator by at least one in absolute value.
The value then lies in the closed unit disc.

### L2 human

This is a basic sufficient condition for convergence, in the same spirit as the comparison test for series.
Each map $w \mapsto \frac{a_n}{b_n + w}$ sends the closed unit disc into itself under the hypothesis, which explains the bound $\abs{f} \le 1$.
The [[Van Vleck theorem|KCCFZTP3MM]] is another classical criterion, for partial denominators in a sector.
