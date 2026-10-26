---
tag: 0XMF00T4XQ
kind: statement
role: theorem
name: Squeeze theorem
aliases: [sandwich-theorem]
msc: [40A05]
uses: [0XKWSSY8P2]
sources:
  - url: https://en.wikipedia.org/wiki/Squeeze_theorem
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Limit_of_a_sequence
    locator: Properties
same_as:
  wikidata: Q1065257
  wikipedia: Squeeze theorem
---

## Statement

Let $(a_n)$, $(b_n)$ and $(c_n)$ be real sequences and let $L$ be a real number.
Assume that there is a natural number $N$ such that $a_n \le c_n \le b_n$ for all $n \ge N$.
Assume that $a_n \to L$ and $b_n \to L$ as $n \to \infty$.
Then $c_n \to L$ as $n \to \infty$.

## Remarks

The theorem gives the existence of the limit of $(c_n)$. It does not assume it.
For example, $-1/n \le \sin(n)/n \le 1/n$, so $\sin(n)/n \to 0$.
The same statement holds for the [[limit of a function|0TXTSEMHR5]] at a point.
Other names are the sandwich theorem and, in some countries, the two policemen theorem.

## Explanations

### L1 human

If a sequence is trapped between two sequences that go to the same limit, it must go there too.
For large $n$, the upper and lower sequences are both close to $L$, and $c_n$ lies between them.
