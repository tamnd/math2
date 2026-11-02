---
tag: 3N66TM3TSQ
kind: concept
name: Pushforward measure
msc: [28A12, 28A20]
sources:
  - url: https://en.wikipedia.org/wiki/Pushforward_measure
same_as:
  wikidata: Q860929
  wikipedia: Pushforward measure
---

## Summary

The pushforward measure moves a [[measure|PR11BZQQPG]] along a [[measurable function|YYNCJSR0PJ]] from one space to another.
The new measure gives a set the old measure of its preimage.
In probability theory, the distribution of a random variable is the pushforward of the probability measure along the variable.
It also gives the abstract change of variables formula for integrals.

## Explanations

### L1 human

Think of the measure as sand spread over a space $X$, and of the map $f$ as a rule that moves each grain to a point of $Y$.
The pushforward is the new pile of sand on $Y$.
To weigh a region $B$ of $Y$, weigh all the grains of $X$ that land in $B$.
For example, let $X = \set{1, 2, 3, 4, 5, 6}$ with mass $1/6$ at each point, and let $f(x) = 0$ for even $x$ and $f(x) = 1$ for odd $x$.
The pushforward puts mass $1/2$ at $0$ and mass $1/2$ at $1$.
