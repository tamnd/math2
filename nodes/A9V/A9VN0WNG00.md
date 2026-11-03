---
tag: A9VN0WNG00
kind: concept
name: Wolff algorithm
msc: [82M31, 82B20, 65C05]
specializes: [DR0E829VX6]
sources:
  - url: https://en.wikipedia.org/wiki/Wolff_algorithm
same_as:
  wikidata: Q2588971
  wikipedia: Wolff algorithm
---

## Summary

The Wolff algorithm is a single-cluster [[Monte Carlo method|DR0E829VX6]] for spin models such as the [[Ising model|R0KGM32QN6]].
It grows one cluster of aligned spins from a random seed, using the same bond probability as the [[Swendsen–Wang algorithm|5NV45XZF81]], and flips the whole cluster.
Every proposed flip is accepted, and large clusters are flipped more often because a random seed is more likely to land in them.
Near the critical point it reduces critical slowing down even more than Swendsen–Wang in many models.

## Explanations

### L1 human

Pick a random spin.
Look at its neighbours that point the same way, and add each one to a growing group with a certain probability.
Repeat from the new members until the group stops growing, then flip the whole group.
The adding probability depends on the temperature in just the right way so that the simulation stays fair.
At low temperature the groups are big, at high temperature they are small, and near the critical point their sizes vary widely, as the true magnetic regions do.
