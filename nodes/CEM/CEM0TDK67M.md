---
tag: CEM0TDK67M
kind: concept
name: Two-port network
msc: [94C05]
sources:
  - url: https://en.wikipedia.org/wiki/Two-port_network
same_as:
  wikidata: Q243745
  wikipedia: Two-port network
---

## Summary

A two-port network is a circuit with two pairs of terminals, an input port and an output port.
It is studied only through the voltages and currents at the ports.
For a linear two-port these four quantities satisfy two linear relations, recorded by a $2 \times 2$ [[matrix|0VD9ZSWWJG]] of parameters.
Amplifiers, filters, transmission lines and transformers are modelled as two-ports, and two-ports in cascade are handled by multiplying their transmission matrices.
[[Scattering parameters|EWRNXMPHGM]] give another description, suited to high frequencies.

## Explanations

### L1 human

Think of a box with two wires going in on the left and two wires coming out on the right.
You do not care what is inside; you only want to know how the voltage and current on the right depend on those on the left.
For a linear box, four numbers are enough to say this.
For example, put a single resistor $r$ in the top wire and a plain wire along the bottom.
This box passes the current through unchanged and lowers the voltage by $r$ times the current.
