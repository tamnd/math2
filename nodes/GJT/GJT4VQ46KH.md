---
tag: GJT4VQ46KH
kind: concept
name: Lindley equation
msc: [60K25, 90B22]
sources:
  - url: https://en.wikipedia.org/wiki/Lindley_equation
same_as:
  wikidata: Q6552558
  wikipedia: Lindley equation
---

## Summary

The Lindley equation is a recursion for the waiting times of successive customers in a single-server queue with first-come first-served discipline.
It writes the waiting time of the next customer through the waiting time of the present one, its service time and the next interarrival time.
It turns the study of the queue into the study of a [[random walk|04VZE3FZXF]] reflected at $0$.
It is the starting point of the analysis of the G/G/1 queue.

## Explanations

### L1 human

When you join a line, your wait is the wait of the person before you plus their service time, minus the time between their arrival and yours.
If this number is negative, the server was idle when you came, so your wait is $0$.
For example, if the previous customer waited $3$ minutes, was served in $2$ minutes and arrived $4$ minutes before you, you wait $3 + 2 - 4 = 1$ minute.
If instead they arrived $6$ minutes before you, you wait $0$.
