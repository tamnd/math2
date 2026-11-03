---
tag: ZSNXTW5E2K
kind: concept
name: Flow network
msc: [90B10, 05C21, 90C35]
specializes: [0KFYGSHHF5]
sources:
  - url: https://en.wikipedia.org/wiki/Flow_network
same_as:
  wikidata: Q1412924
  wikipedia: Flow network
---

## Summary

A flow network is a [[directed graph|0KFYGSHHF5]] whose edges have capacities, together with a source vertex and a sink vertex.
A flow assigns to each edge an amount between zero and its capacity, so that at every other vertex the inflow equals the outflow.
Flow networks model the transport of goods, data or fluids, and many matching and connectivity problems reduce to them.
The [[max-flow min-cut theorem|4HMR4KQ01T]] is their central result.

## Explanations

### L1 human

Picture a system of one-way pipes, each with a largest rate at which water can pass.
Water enters at the source and leaves at the sink, and no water is stored or lost at the junctions in between.
A flow says how much water passes through each pipe per second.
For example, with pipes $s \to a$ of capacity $2$ and $a \to t$ of capacity $3$, at most $2$ units per second can reach $t$ along this route.
The natural question is how much can be sent from source to sink in total.
