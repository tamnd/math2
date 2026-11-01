---
tag: X4DHMZD5JA
kind: concept
name: Quadratic variation
msc: [60G44, 60H05]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_variation
same_as:
  wikidata: Q7268374
  wikipedia: Quadratic variation
---

## Summary

The quadratic variation of a process is the limit of the sums of squared increments over finer and finer partitions of a time interval.
For smooth paths it is zero, but for Brownian motion it equals the elapsed time.
It is the correction term in [[Itô's lemma|2J1RVQB0CM]] and a basic tool for [[semimartingales|4EJB6E2AZK]].

## Explanations

### L1 human

Cut the time interval $[0, t]$ into many small pieces, square the change of the path on each piece, and add.
For a smooth curve each change is about the length of the piece, so the squares are tiny and the sum goes to zero.
A Brownian path is so rough that its change over a piece of length $h$ is about $\sqrt{h}$.
Then each square is about $h$, and the sum tends to $t$.
