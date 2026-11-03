---
tag: ZXKS5FADM1
kind: concept
name: Theil index
msc: [91B82, 62P20, 94A17]
sources:
  - url: https://en.wikipedia.org/wiki/Theil_index
same_as:
  wikidata: Q1655361
  wikipedia: Theil index
---

## Summary

The Theil index is a measure of income inequality built from the entropy of information theory.
It is the gap between the largest possible entropy of income shares, reached at perfect equality, and the actual entropy.
It equals $0$ for perfect equality and $\ln n$ when one of $n$ people has everything.
Its main advantage is that total inequality splits exactly into inequality within groups and inequality between groups.

## Explanations

### L1 human

Give each person a share of the total income.
If all shares are equal, the shares are as spread out as possible, and the Theil index is $0$.
The more the income is concentrated, the larger the index.
For two people with incomes $1$ and $4$, the index is about $0.19$; if one of them had everything, it would be $\ln 2 \approx 0.69$.
