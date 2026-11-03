---
tag: EWRNXMPHGM
kind: concept
name: Scattering parameters
msc: [94C05, 78A50]
sources:
  - url: https://en.wikipedia.org/wiki/Scattering_parameters
same_as:
  wikidata: Q2165620
  wikipedia: Scattering parameters
---

## Summary

Scattering parameters describe a linear multi-port electrical network by how waves sent into its ports are reflected and transmitted.
At each port the voltage and current are recombined into an incident wave and a reflected wave, relative to a reference impedance.
The scattering matrix maps incident waves to reflected waves.
They are the standard description at radio and microwave frequencies, where matched loads are easier to realize than open and short circuits.
They turn energy conservation into the [[unitarity|0AR68JTMDT]] of a matrix.

## Explanations

### L1 human

Send a signal into one port of a device and watch what comes back and what comes out of the other ports.
The scattering parameters are the fractions that are reflected and transmitted.
For a [[two-port network|CEM0TDK67M]], $S_{11}$ is the reflection at the input and $S_{21}$ the transmission from input to output.
A load matched to the line reflects nothing, so its reflection coefficient is $0$; an open end reflects everything with coefficient $1$.
