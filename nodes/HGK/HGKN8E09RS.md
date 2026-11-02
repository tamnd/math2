---
tag: HGKN8E09RS
kind: concept
name: Finite volume method
msc: [65M08, 65N08, 35L65]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_volume_method
same_as:
  wikidata: Q1401936
  wikipedia: Finite volume method
---

## Summary

The finite volume method discretizes a [[conservation law|8RA7AMWSAF]] by dividing the domain into small control volumes and keeping the average of the solution in each.
The [[divergence theorem|0JX86PSSA9]] turns the change of each average into a sum of fluxes through the faces of the volume.
Each flux is computed once and used by the two volumes that share the face, so the scheme conserves the total amount exactly.
This makes it the standard method for shocks in gas dynamics and for transport in fluid mechanics; [[Godunov's scheme|43HZJ7DRT0]] is a classical example.
See the [[definition|CAB1ARHH31]].

## Explanations

### L1 human

Split a pipe into short sections and keep track of how much water each section holds.
The amount in a section changes only by what flows in or out through its two ends.
Whatever leaves one section through a wall enters the neighbour through the same wall, so no water is created or lost.
A finite volume method computes these flows from the amounts in the neighbouring sections and updates the amounts step by step.
