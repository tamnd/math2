---
tag: ~82eeef2c
kind: statement
role: theorem
name: Theorem on friends and strangers
msc: [05C55, 05D10]
uses: [~b29ee1b7]
sources:
  - url: https://en.wikipedia.org/wiki/Theorem_on_friends_and_strangers
    locator: Statement
same_as:
  wikidata: Q837506
  wikipedia: Theorem on friends and strangers
---

## Statement

Colour each edge of the [[complete graph|~b29ee1b7]] $K_6$ red or blue.
Then there are three vertices such that the three edges between them have the same colour.

## Remarks

Proof: a vertex $v$ has $5$ edges, so at least $3$ of them have one colour, say blue, by the [[pigeonhole principle|~7583255b]]. If an edge between their ends is blue, it closes a blue triangle with $v$. Otherwise these three ends form a red triangle.
The number $6$ is the least possible: $K_5$ has a colouring with no triangle of one colour.
Thus the [[Ramsey number|~88785faa]] $R(3, 3)$ is $6$.

## Explanations

### L1 human

At any party of six people, there are three people who all know each other, or three who are all strangers to each other.
With five people this can fail.
