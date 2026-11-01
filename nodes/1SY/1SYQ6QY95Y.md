---
tag: 1SYQ6QY95Y
kind: problem
name: Kirkman's schoolgirl problem
msc: [05B07, 05B05]
uses: [QHPW53E7YA]
about: [7BPSC4T4M3]
sources:
  - url: https://en.wikipedia.org/wiki/Kirkman%27s_schoolgirl_problem
same_as:
  wikidata: Q966333
  wikipedia: Kirkman's schoolgirl problem
history:
  posed_by: "Thomas Kirkman"
  first_stated: "1850"
---

## Problem

Fifteen schoolgirls go for a walk on each of seven days, in five rows of three.
Arrange the rows for the seven days so that no two girls walk in the same row on more than one day.

## Remarks

Each girl has $14$ companions and meets $2$ of them per day, so in a solution every two girls walk together exactly once.
So a solution is a [[Steiner triple system|7BPSC4T4M3]] $S(2, 3, 15)$ whose $35$ triples split into $7$ days of $5$ disjoint triples each.
A Steiner triple system with such a split into parallel classes is called a Kirkman triple system.
The problem has solutions; up to renaming the girls, there are seven different ones.
Thomas Kirkman posed the problem in 1850.
The general question, for $v$ girls with $v \equiv 3 \pmod 6$, was solved by Ray-Chaudhuri and Wilson in 1971: a Kirkman triple system of order $v$ exists for every such $v$.

## Explanations

### L1 human

The puzzle asks for a weekly walking plan in which every two of the fifteen girls walk side by side exactly once.
The numbers fit: there are $105$ pairs of girls, and each day the five rows of three cover $15$ pairs, so seven days cover $105$ pairs.
Finding an arrangement that really works is a nice exercise, and the puzzle started the theory of resolvable designs.
