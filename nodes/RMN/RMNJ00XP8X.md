---
tag: RMNJ00XP8X
kind: statement
role: fact
name: Kelvin–Planck statement of the second law
msc: [80A05, 80A10]
uses: [CY4GJQGF06, S8H21RWQ86, AGRGCDWQF8, S7XFW04T3V, VECH3HZ04M]
about: [S7XFW04T3V]
sources:
  - url: https://en.wikipedia.org/wiki/Second_law_of_thermodynamics
    locator: Kelvin statement
---

## Statement

No [[cyclic process|AGRGCDWQF8]] can have as its sole result that a system absorbs [[heat|CY4GJQGF06]] from one reservoir and does an equal amount of [[work|S8H21RWQ86]].
Here a reservoir is a body held at one fixed temperature.

## Remarks

In other words, every [[heat engine|S7XFW04T3V]] that works in a cycle must give some heat to a colder reservoir; its efficiency is less than $1$.
It is equivalent to the [[Clausius statement|VECH3HZ04M]].
Suppose an engine takes heat $Q$ from a hot reservoir and turns all of it into work $W = Q$.
Let this work drive a refrigerator that takes heat $Q'$ from a cold reservoir and gives $Q' + W$ to the hot one.
The net effect is the transfer of $Q'$ from cold to hot and nothing else, which the Clausius statement forbids.
Conversely, a device that moves heat from cold to hot with no other effect can be paired with an ordinary engine between the two reservoirs.
The pair then turns heat from the hot reservoir fully into work, which the Kelvin–Planck statement forbids.

## Explanations

### L1 human

No engine running in cycles can turn heat from one source completely into work.
Some heat must always be dumped into something colder.
So one cannot power a ship just by cooling the ocean around it.

### L2 human

This statement rules out perpetual motion machines of the second kind.
It is the form of the second law used most often in proofs about cycles.
For example, the Clausius theorem $\oint \delta Q / T \le 0$ is proved by building, from a violating cycle, a machine that contradicts the Kelvin–Planck statement.
