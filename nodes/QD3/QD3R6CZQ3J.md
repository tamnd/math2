---
tag: QD3R6CZQ3J
kind: concept
name: Modified nodal analysis
msc: [94C05, 94C60]
specializes: [9NW7KCBSME]
sources:
  - url: https://en.wikipedia.org/wiki/Modified_nodal_analysis
same_as:
  wikidata: Q6889414
  wikipedia: Modified nodal analysis
---

## Summary

Modified nodal analysis extends [[nodal analysis|9NW7KCBSME]] to circuits that contain voltage sources and other elements whose current is not a function of the node voltages.
The unknowns are the node potentials together with the currents through these elements.
The resulting linear system has a block form with the nodal conductance matrix in one corner.
It is the formulation used by circuit simulators such as SPICE.

## Explanations

### L1 human

Plain nodal analysis needs every branch current to be computable from the node voltages, which is true for resistors but not for a battery.
Modified nodal analysis simply adds the current through each battery as one more unknown.
It also adds one more equation for each battery: the voltage across it is fixed.
For a battery $E$ across a resistor $R$, the unknowns are the node voltage $\varphi$ and the battery current $j$, and the equations are $\varphi / R + j = 0$ and $\varphi = E$.
