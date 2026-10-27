---
tag: 0BB5TPGQ1N
kind: concept
name: Proof by contrapositive
aliases: [proof-by-contraposition]
msc: [00A35]
topics: [G9JFJGY4TQ]
specializes: [0B94TKFQJX]
uses: [04T1CT7212, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Contraposition
    locator: lead section
same_as:
  wikidata: Q1077442
  wikipedia: Contraposition
---

## Summary

A proof by contrapositive proves an [[implication|0ZNX6DQ3EJ]] $p \to q$ by a [[direct proof|0NTF6DMVAP]] of $\neg q \to \neg p$.
The method is correct because $p \to q$ is logically equivalent to its [[contrapositive|04T1CT7212]].

## Remarks

Example: for an integer $n$, if $n^2$ is even, then $n$ is even. The contrapositive is "if $n$ is odd, then $n^2$ is odd", which has a short direct proof.
A [[proof by contradiction|0J0XBKG64S]] is different: it assumes $p$ and $\neg q$ together, and it gets any contradiction.

## Explanations

### L1 human

Sometimes the negation of the conclusion gives you more to work with.
"If $n^2$ is even, then $n$ is even" is hard to start.
"If $n$ is odd, then $n^2$ is odd" is easy, and it says the same thing.
