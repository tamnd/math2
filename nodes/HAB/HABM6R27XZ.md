---
tag: HABM6R27XZ
kind: problem
name: Maxwell's demon
msc: [80A05, 82B30, 94A17]
uses: [T11MGWEKJ3, SPY89W0RJ7, ZPCGW6FGB0]
about: [T11MGWEKJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Maxwell%27s_demon
same_as:
  wikidata: Q212397
  wikipedia: Maxwell's demon
history:
  posed_by: "James Clerk Maxwell"
  first_stated: "1867"
---

## Problem

A gas at uniform temperature fills a box split into two halves by a wall with a small door.
A being, the demon, watches the molecules and works the door.
It lets fast molecules pass only from left to right, and slow molecules only from right to left.
It seems to make the right half hotter and the left half colder without doing work.
This would lower the [[entropy|SPY89W0RJ7]] of the isolated gas.
The problem is to explain why this does not violate the [[second law of thermodynamics|T11MGWEKJ3]].

## Remarks

Leo Szilard in 1929 reduced the problem to a one-molecule engine and argued that measurement by the demon must produce entropy.
The standard resolution today, due to Charles Bennett in 1982, uses [[Landauer's principle|ZPCGW6FGB0]]: measurement can in principle be done reversibly, but the demon must store its results.
To work in a cycle, it must erase its memory.
The erasure releases at least $k_B T \ln 2$ of heat per bit, which makes up for the entropy decrease of the gas.
The name "demon" was given by William Thomson, later Lord Kelvin.
Some authors still question parts of this resolution, but within statistical mechanics the second law is regarded as safe.

## Explanations

### L1 human

Maxwell imagined a tiny doorkeeper who sorts fast and slow molecules and so creates a temperature difference out of nothing.
That would let one run an engine on the heat of a single room, which the second law forbids.
The catch is information: the doorkeeper must remember what it saw, and erasing that memory produces at least as much entropy as the sorting removed.
