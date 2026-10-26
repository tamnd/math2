---
tag: 05DEJR6TGF
kind: statement
role: theorem
name: Zeckendorf's theorem
msc: [11B39]
uses: [0GA9K57A39]
sources:
  - url: https://en.wikipedia.org/wiki/Zeckendorf's_theorem
    locator: lead section
same_as:
  wikidata: Q1188392
  wikipedia: Zeckendorf's theorem
---

## Statement

Let $F_k$ be the [[Fibonacci numbers|0GA9K57A39]], and let $N$ be a positive integer.
Then there is a unique finite set $\{c_1, \dots, c_r\}$ of integers, with $r \ge 1$, such that
$$N = F_{c_1} + F_{c_2} + \dots + F_{c_r},$$
each $c_i \ge 2$, and $c_{i+1} \ge c_i + 2$ for $1 \le i < r$.

## Remarks

The condition says that the sum uses distinct Fibonacci numbers and no two consecutive ones. The bound $c_i \ge 2$ excludes $F_0 = 0$ and the repeated value $F_1 = F_2 = 1$.
Example: $100 = 89 + 8 + 3 = F_{11} + F_6 + F_4$.
The greedy method finds the representation: subtract the largest Fibonacci number that is at most $N$, and repeat.

## Explanations

### L1 human

Each positive integer is a sum of different Fibonacci numbers, no two of them neighbours in the sequence, in exactly one way.
For example, $20 = 13 + 5 + 2$.
