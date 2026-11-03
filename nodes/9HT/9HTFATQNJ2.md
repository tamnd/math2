---
tag: 9HTFATQNJ2
kind: concept
name: Kendall's notation
msc: [60K25, 90B22]
sources:
  - url: https://en.wikipedia.org/wiki/Kendall%27s_notation
same_as:
  wikidata: Q1738700
  wikipedia: Kendall's notation
---

## Summary

Kendall's notation is the standard short code for a queueing model, written $A/S/c$ or, in full, $A/S/c/K/N/D$.
The first three fields give the law of the times between arrivals, the law of the service times, and the number of servers.
The optional fields give the capacity, the size of the population of customers, and the service discipline.
David G. Kendall introduced the three-letter form in 1953.
It lets one name a model of [[queueing theory|P64V0HTE78]], such as the [[M/M/1 queue|GTFRPF5J2K]], in a few symbols.

## Explanations

### L1 human

Queue models differ in a few basic choices: how customers arrive, how long they are served, and how many clerks there are.
Kendall's notation writes these choices as letters and numbers separated by slashes.
For example, M/M/1 means random (Poisson) arrivals, random exponential service times and one clerk.
M/D/3 means random arrivals, service times that are always the same, and three clerks.
