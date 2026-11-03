---
tag: ENTVWXCEBD
kind: concept
name: Kemeny–Young method
msc: [91B12, 91B14]
specializes: [WZYEADV8E1]
sources:
  - url: https://en.wikipedia.org/wiki/Kemeny_method
same_as:
  wikidata: Q6386915
  wikipedia: Kemeny method
---

## Summary

The Kemeny–Young method is a voting rule that outputs a full ranking of the candidates.
It chooses the ranking that agrees with the voters' rankings on the largest total number of pairs of candidates.
Equivalently it minimizes the total number of pairwise disagreements with the ballots, measured by the Kendall tau distance.
It is a [[Condorcet method|WZYEADV8E1]], and computing it is NP-hard.

## Explanations

### L1 human

Every ballot is a ranking, and each ranking takes a side on every pair of candidates.
For each possible final ranking, count how many of these pairwise sides it agrees with, summed over all ballots.
The Kemeny–Young ranking is the one with the highest count.
For instance, if three voters say $a \succ b \succ c$ and two say $b \succ c \succ a$, the ranking $a \succ b \succ c$ agrees on $11$ pairwise votes, more than any other ranking.
