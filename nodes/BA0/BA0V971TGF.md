---
tag: BA0V971TGF
kind: concept
name: Muskingum routing method
msc: [86A05]
sources:
  - url: https://en.wikipedia.org/wiki/Routing_(hydrology)
---

## Summary

The Muskingum method is a simple model for routing a flood wave along a river reach.
It computes the outflow hydrograph at the lower end of the reach from the inflow hydrograph at the upper end.
It combines conservation of water volume with a linear relation between the water stored in the reach and a weighted mean of inflow and outflow.
Its discrete form gives each new outflow as a fixed weighted sum of two inflows and the previous outflow.
So it is easy to compute, and it is widely used in [[hydrology|2XGF4FECN5]].

## Explanations

### L1 human

When a flood enters a stretch of river, it comes out at the far end later and with a lower, broader peak.
The Muskingum method explains this with a storage idea: the river stretch holds more water when the flows through it are larger.
Water that enters and does not leave yet is stored, and the stored water drains out later.
For example, with no weight on the inflow the reach behaves like a tank that empties at a rate proportional to its content.
Then, after the inflow stops, the outflow decays exponentially.
