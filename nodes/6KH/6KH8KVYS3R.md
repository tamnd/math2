---
tag: 6KH8KVYS3R
kind: concept
name: Charlier polynomials
msc: [33C45, 42C05]
sources:
  - url: https://en.wikipedia.org/wiki/Charlier_polynomials
same_as:
  wikidata: Q5085761
  wikipedia: Charlier polynomials
---

## Summary

The Charlier polynomials $C_n(x; a)$ are the orthogonal polynomials of the [[Poisson distribution|0XB9GQTN9G]] with mean $a > 0$.
They are orthogonal for a weight on the nonnegative integers rather than on an interval.
They belong to the [[Askey scheme|RR2S05C09B]] as a limit of the [[Krawtchouk|CJGKW80KBR]] and [[Meixner polynomials|CEC3DESCFT]].

## Explanations

### L1 human

Count random events, such as calls arriving at a desk in an hour, with an average of $a$ events.
The count follows the Poisson distribution, which puts weight $e^{-a} a^x / x!$ on each whole number $x$.
The Charlier polynomials are the polynomials in $x$ that are perpendicular to each other when one averages with this weight.
The first nonconstant one is $1 - x/a$, whose average is $1 - a/a = 0$.
