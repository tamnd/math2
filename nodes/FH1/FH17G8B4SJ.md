---
tag: FH17G8B4SJ
kind: concept
name: Boolean network
msc: [92C42, 94C11, 37N25]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_network
same_as:
  wikidata: Q585230
  wikipedia: Boolean network
---

## Summary

A Boolean network is a finite set of variables that are each on or off.
They are updated in discrete time by [[Boolean functions|0X05GS525E]] of the current values.
Stuart Kauffman introduced random Boolean networks in 1969 as models of gene regulation.
Since the state space is finite, every trajectory ends in a fixed point or a cycle.
These [[attractors|7FWX24X5MW]] are read as cell types or stable behaviours.
Boolean networks are the simplest discrete models of regulatory and signalling networks.

## Explanations

### L1 human

Think of a row of light bulbs, each wired to look at a few others.
At each tick, every bulb decides whether to be on or off from a fixed logical rule, such as "on if bulb 2 is on and bulb 3 is off".
With $n$ bulbs there are only $2^n$ possible patterns, so sooner or later a pattern repeats and the system cycles forever.
For example, take two bulbs with the rules "bulb 1 copies bulb 2" and "bulb 2 is the opposite of bulb 1".
Then the state goes $00, 01, 11, 10, 00$, a cycle of length $4$.
