---
tag: 14YM2HVGHA
kind: concept
name: Busy Beaver function
msc: [03D10, 68Q04]
sources:
  - url: https://en.wikipedia.org/wiki/Busy_beaver
same_as:
  wikidata: Q1427965
  wikipedia: Busy beaver
---

## Summary

The Busy Beaver function $\Sigma(n)$ is the largest number of $1$s left by a halting [[Turing machine|758EYCN27B]] with $n$ states and two symbols.
The machine starts on a blank tape.
The related function $S(n)$ is the largest number of steps such a machine can take before it halts.
Both functions are well defined, because there are only finitely many such machines.
They grow faster than every computable function, so they are not computable, which gives a concrete example of a non-computable function.

## Explanations

### L1 human

Take all small machines with a given number of states and start them on an empty tape.
Some run forever, and the others stop after a while.
Among those that stop, the busy beaver is the one that writes the most $1$s.
For one state the record is $1$ and for two states it is $4$.
The values explode quickly, and finding them requires proving that many particular machines never stop, which becomes hopeless for larger $n$.
