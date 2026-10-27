---
tag: 0F8YBHF2W3
kind: concept
name: Double counting
aliases: [counting-in-two-ways]
msc: [05A19]
topics: [G9JFJGY4TQ]
sources:
  - url: https://en.wikipedia.org/wiki/Double_counting_(proof_technique)
    locator: lead section
same_as:
  wikidata: Q1191750
  wikipedia: Double counting (proof technique)
---

## Summary

Double counting is a proof technique in combinatorics.
To prove that two expressions are equal, one shows that both count the elements of the same finite set.
Each expression comes from a different way to count that set.

A common form uses a relation $R \subseteq A \times B$ between finite sets $A$ and $B$.
For $a \in A$, let $d(a)$ be the number of $b \in B$ with $(a, b) \in R$.
For $b \in B$, let $e(b)$ be the number of $a \in A$ with $(a, b) \in R$.
Then both sums count the pairs in $R$, so
$$\sum_{a \in A} d(a) = |R| = \sum_{b \in B} e(b).$$

## Remarks

The [[handshaking lemma|0XAP8WHNES]] is double counting applied to the pairs of a vertex and an edge that contains it.
The [[symmetry of binomial coefficients|0R7JS3DP3W]] has a short proof by this technique.

## Explanations

### L1 human

Count the same thing in two ways, and the two answers must be equal.
For example, in a class each pair of friends shakes hands once. If you add the number of handshakes of each person, you count each handshake twice, so the sum is even.
