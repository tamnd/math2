---
tag: YET20Q6WW6
kind: concept
name: Banzhaf power index
msc: [91B12, 91A12]
sources:
  - url: https://en.wikipedia.org/wiki/Banzhaf_power_index
same_as:
  wikidata: Q2742375
  wikipedia: Banzhaf power index
---

## Summary

The Banzhaf power index measures the voting power of each member of a committee that decides by a voting rule, such as a weighted majority.
A voter's power is counted by the number of winning coalitions in which her vote is decisive.
It shows that voting power is not proportional to voting weight.
It is named after John F. Banzhaf III, who applied it to weighted voting systems.

## Explanations

### L1 human

A vote matters when switching it would change the result.
The Banzhaf index counts, for each voter, how many winning groups would lose if she left them.
Take three parties with $2$, $1$ and $1$ seats and a quota of $3$ seats.
The big party is decisive in three winning groups and each small party in one.
So the big party has $3/5$ of the power, although it has only half of the seats.
