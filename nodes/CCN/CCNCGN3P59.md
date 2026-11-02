---
tag: CCNCGN3P59
kind: counterexample
name: Burali-Forti paradox
msc: ["03E10", 03A05]
uses: [0YSCSX5YZC, 01CGSJ0GNQ, 0BSJ7RQ9BW, 0HE5WDQ9FJ]
sources:
  - url: https://en.wikipedia.org/wiki/Burali-Forti_paradox
same_as:
  wikidata: Q1010269
  wikipedia: Burali-Forti paradox
---

## Counterexample

Use von Neumann [[ordinals|0YSCSX5YZC]]: an ordinal is a transitive set that is [[well-ordered|01CGSJ0GNQ]] by the membership relation $\in$.
Suppose that the collection $\Omega$ of all ordinals is a [[set|0BSJ7RQ9BW]].
Every element of an ordinal is an ordinal, so $\Omega$ is transitive.
The ordinals are well-ordered by $\in$, so $\Omega$ is a transitive set well-ordered by $\in$.
Hence $\Omega$ is an ordinal, and so $\Omega \in \Omega$.
This contradicts the fact that no ordinal is an element of itself.
So the collection of all ordinals is not a set.

## Remarks

In [[naive set theory|XGAMQBSE1G]] every property defines a set, so the argument there is a paradox.
In [[Zermelo–Fraenkel set theory|0HE5WDQ9FJ]] it is a theorem: the ordinals form a proper [[class|Y48FA69563]], not a set.
In the original form, the order type of all ordinals would be an ordinal greater than every ordinal, including itself.
Cesare Burali-Forti published the argument in 1897.

## Explanations

### L1 human

Each ordinal counts the length of a well-ordered list.
If all ordinals formed one set, that set would itself be a well-ordered list, so it would have a length.
That length would be an ordinal bigger than all ordinals, which is absurd.
The way out is that "all ordinals" is too big to be a set.
