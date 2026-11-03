---
tag: 7MJQ2ZBQ66
kind: example
name: Hard hexagon model
msc: [82B20, 82B23]
instance_of: [PAEME5EQRM]
uses: [08ANQHHG3P, 1C5S72A9JX]
sources:
  - url: https://en.wikipedia.org/wiki/Hard_hexagon_model
same_as:
  wikidata: Q17020934
  wikipedia: Hard hexagon model
---

## Example

Let $\Lambda$ be a finite piece of the triangular lattice, a graph in which each site has six neighbours.
Let $z > 0$ be the activity.
A configuration is a set of occupied sites in which no two occupied sites are neighbours, that is, an [[independent set|08ANQHHG3P]] of the graph.
The *hard hexagon model* is the probability measure on these sets that gives a set $A$ the weight $z^{\abs{A}} / Z$, with grand partition function
$$Z = \sum_{A \text{ independent}} z^{\abs{A}}.$$
The name comes from drawing a hexagon around each occupied site: the exclusion rule says that these hexagons do not overlap.

## Remarks

It is a [[grand canonical ensemble|1C5S72A9JX]] of particles with a hard-core repulsion and no other interaction.
Baxter solved it exactly in 1980, finding the free energy in closed form in terms of $q$-series.
For small $z$ the particles are spread evenly; for large $z$ they prefer one of the three sublattices of the triangular lattice.
The transition between these regimes occurs at the activity
$$z_c = \frac{11 + 5\sqrt{5}}{2} = \varphi^5 \approx 11.09,$$
where $\varphi$ is the golden ratio.
Baxter's solution uses the [[corner transfer matrix|71KZPWHGCQ]] and identities of Rogers–Ramanujan type.

## Explanations

### L1 human

Drop coins onto the slots of a triangular grid, never letting two coins sit on neighbouring slots.
The activity $z$ controls how eager the system is to add coins.
At low $z$ the coins are scattered, and above a sharp threshold they line up on one of three interlaced sub-grids.
