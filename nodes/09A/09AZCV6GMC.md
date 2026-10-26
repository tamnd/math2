---
tag: 09AZCV6GMC
kind: definition
name: Sequence tending to infinity
msc: [40A05]
defines: 0VQA7F720Z
uses: [0CTV783HYT]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_of_a_sequence
    locator: Infinite limits
---

## Definition

Let $(a_n)$ be a [[real sequence|0CTV783HYT]].
The sequence tends to $+\infty$ if, for each real number $M$, there is a natural number $N$ such that $a_n > M$ for all $n \ge N$.
Then we write $a_n \to +\infty$ as $n \to \infty$, or $\lim_{n \to \infty} a_n = +\infty$.
The sequence tends to $-\infty$ if $-a_n \to +\infty$.

## Remarks

The sequences $n$, $n^2$ and $2^n$ tend to $+\infty$.
A sequence that tends to $+\infty$ is not bounded above, so it is a [[divergent sequence|01HR2AH0BX]].
The converse fails. The sequence $0, 1, 0, 2, 0, 3, \dots$ is not bounded above, but it does not tend to $+\infty$.

## Explanations

### L1 human

A sequence tends to infinity when its terms become larger than any number you name, and stay larger.
It is not enough that the terms are sometimes large.
