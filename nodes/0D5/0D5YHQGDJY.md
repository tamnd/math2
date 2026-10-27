---
tag: 0D5YHQGDJY
kind: definition
name: Subspace topology
msc: [54B05]
defines: 0WS9P12FQR
uses: [0CNQXVBHCX, 0HBRW4E6G1, 0FE8Q5S42Y]
sources:
  - url: https://en.wikipedia.org/wiki/Subspace_topology
    locator: Definition
inventory: [VRY8JPATZ4]
---

## Definition

Let $(X, \tau)$ be a [[topological space|0CNQXVBHCX]] and let $S \subseteq X$.
The subspace topology on $S$ is
$$\tau_S = \{ S \cap U : U \in \tau \}.$$
With this topology, $S$ is a subspace of $X$.

## Remarks

The set $\tau_S$ is a topology on $S$, because intersection with $S$ commutes with unions and finite [[intersections|0HBRW4E6G1]].
A set open in $S$ need not be open in $X$. For example, $[0, 1)$ is open in the subspace $[0, 1]$ of $\mathbb{R}$, because $[0, 1) = [0, 1] \cap (-1, 1)$.
For a metric space, the subspace topology is the metric topology of the [[subspace metric|0T2WYDTRP2]].
The subspace topology is the coarsest topology on $S$ for which the [[inclusion map is continuous|065J822CKN]].

## Explanations

### L1 human

A subset of a space inherits a topology: you cut each open set of the big space down to the subset.
This is how the circle and the interval get their topologies from the plane and the line.
