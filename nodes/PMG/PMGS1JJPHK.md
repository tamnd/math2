---
tag: PMGS1JJPHK
kind: concept
name: Lattice Boltzmann method
msc: [76M28, 82C40, 65M75]
sources:
  - url: https://en.wikipedia.org/wiki/Lattice_Boltzmann_methods
same_as:
  wikidata: Q1807064
  wikipedia: Lattice Boltzmann methods
---

## Summary

The lattice Boltzmann method is a numerical method for fluid flow that evolves particle distributions on a lattice instead of solving the [[Navier–Stokes equations|18KXZHVF4M]] directly.
At each time step, populations of fictitious particles stream to neighbouring lattice sites.
Then they relax towards a local equilibrium, as in the [[BGK collision operator|YQRS1ZMRAC]].
Their moments, density and momentum, approximate a solution of the weakly compressible Navier–Stokes equations at low [[Mach number|GFHJ858AN1]].
The method is local and simple, so it suits parallel computers and complex geometries such as porous media.
See the [[definition|HM1VPNV8J6]].

## Explanations

### L1 human

Imagine a grid where at each node a few groups of particles wait, one group for each direction to a neighbouring node.
In each step, every group hops to the neighbour in its direction.
Then, at each node, the groups mix so that their numbers move towards an equilibrium set by the local density and velocity.
Repeating these two simple steps, the average motion of the particles behaves like a real fluid.
In two dimensions a common choice uses nine directions: rest, four along the axes, and four along the diagonals.
