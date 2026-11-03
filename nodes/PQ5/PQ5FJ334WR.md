---
tag: PQ5FJ334WR
kind: concept
name: Zero-order hold
msc: [93C57, 93C62]
sources:
  - url: https://en.wikipedia.org/wiki/Zero-order_hold
same_as:
  wikidata: Q2907060
  wikipedia: Zero-order hold
---

## Summary

A zero-order hold turns a sequence of numbers into a continuous-time signal by holding each value constant for one sampling period.
It is the standard model of a digital-to-analog converter, through which a computer applies its control values to a physical system.
Its use makes the effect of a continuous-time linear system between samples exactly computable, which is the basis of the [[discretization of linear systems|3Z1Z7TDPHZ]].

## Explanations

### L1 human

A computer can only output a new number at each clock tick, say every $T$ seconds.
Between ticks, the zero-order hold keeps the last number on the output wire, which gives a staircase signal.
If the computer sends $3, 1, 2$, the signal is $3$ for the first $T$ seconds, then $1$, then $2$.
The name says that the hold uses a polynomial of degree zero, a constant, on each interval.
