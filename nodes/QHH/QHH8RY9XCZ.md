---
tag: QHH8RY9XCZ
kind: concept
name: Schnirelmann density
msc: [11B05, 11B13]
sources:
  - url: https://en.wikipedia.org/wiki/Schnirelmann_density
same_as:
  wikidata: Q2482753
  wikipedia: Schnirelmann density
---

## Summary

The Schnirelmann density of a set $A$ of positive integers is the infimum over $n \ge 1$ of the proportion of $\set{1, \dots, n}$ that lies in $A$.
Unlike the [[natural density|RVG9Z8NYA6]], it always exists and it is very sensitive to small elements: it is $0$ whenever $1 \notin A$.
It behaves well under sums of sets, which makes it a tool for additive problems.
Schnirelmann used it to show that every integer greater than $1$ is a sum of a bounded number of [[primes|01826KMG2H]].

## Explanations

### L1 human

Look at the first $n$ positive integers and ask what fraction of them belongs to $A$.
The Schnirelmann density is the worst such fraction over all $n$.
For the odd numbers the fraction is $1$ at $n = 1$ and $1/2$ at every even $n$, so the density is $1/2$.
For the even numbers it is already $0$ at $n = 1$, so the density is $0$.
A set with positive Schnirelmann density has to start early and keep up its pace everywhere.
