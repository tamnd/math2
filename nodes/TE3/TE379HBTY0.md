---
tag: TE379HBTY0
kind: concept
name: Direct method in the calculus of variations
msc: [49J10, 49J45, 35A15]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_method_in_the_calculus_of_variations
same_as:
  wikidata: Q5280366
  wikipedia: Direct method in the calculus of variations
---

## Summary

The direct method proves that a functional has a minimiser without solving any equation.
One takes a minimising sequence and uses compactness to extract a subsequence that converges in a weak sense.
Lower semicontinuity then shows that the limit is a minimiser.
It is the standard existence method of the [[calculus of variations|PQ25NHV0KS]].
It explains why minimisers are first found in Sobolev spaces with their weak topologies.
It gave the first rigorous justification of Dirichlet's principle.

## Explanations

### L1 human

To show that an energy has a lowest state, take a sequence of states whose energies go down to the lowest possible value.
If the energies stay bounded, the states cannot run away, and some part of the sequence settles down to a limit.
If the energy cannot jump up in the limit, the limit is a state of lowest energy.
The key points are to choose a notion of convergence weak enough for the sequence to converge, yet strong enough for the energy to behave well.
On the real line the function $x \mapsto x^2$ illustrates the steps: any minimising sequence tends to $0$, and $0$ is the minimiser.
