---
tag: XBTEF7WPY6
kind: concept
name: Receiver function
msc: [86A15, 86A22, 94A12]
sources:
  - url: https://en.wikipedia.org/wiki/Receiver_function
same_as:
  wikidata: Q2135141
  wikipedia: Receiver function
---

## Summary

A receiver function is a time series computed from a three-component seismogram of a distant earthquake.
It shows the response of the Earth structure directly below the station.
It is obtained by [[deconvolution|BWBB42GNEH]] of the vertical component from the horizontal components, which removes the source and the path.
What remains are the waves converted from P to S at interfaces under the station.
The delays of the converted waves after the direct P wave give the depths of interfaces such as the Moho.
Receiver functions are a main tool for mapping crustal thickness and mantle discontinuities.

## Explanations

### L1 human

When a P wave from a distant earthquake hits a boundary under a seismometer, such as the bottom of the crust, part of it turns into a slower S wave.
The S wave arrives a few seconds after the P wave, and the delay grows with the depth of the boundary.
A receiver function cleans the seismogram so that only these converted arrivals and their echoes remain.
For a crust $35$ km thick, the converted wave typically arrives about $4$ seconds after the direct P wave.
