---
tag: 0WCP0PVET6
kind: concept
name: Proof by cases
aliases: [proof-by-exhaustion, case-analysis]
msc: [00A35]
uses: [0B94TKFQJX, 0H5GKDTB01, 0ZNX6DQ3EJ]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_by_exhaustion
    locator: lead section
same_as:
  wikidata: Q9299950
  wikipedia: Proof by exhaustion
---

## Summary

A proof by cases splits the situation into a finite number of cases that cover all possibilities.
Then it proves the statement in each case.
The basic form is this rule: from $p \lor q$, $p \to r$ and $q \to r$, conclude $r$.

## Remarks

Another name is proof by exhaustion, mainly when the cases are many.
Example: $n^2 + n$ is even for each integer $n$. If $n$ is even, $n^2$ and $n$ are even. If $n$ is odd, $n^2$ and $n$ are odd. In both cases, the sum is even.
A split into $p$ and $\neg p$ uses the [[law of excluded middle|0RYYK8PG4S]].

## Explanations

### L1 human

When one argument does not work for all cases, split the cases.
Integers are even or odd, so a proof for even integers and a proof for odd integers together cover all integers.
Make sure that no case is missing.
