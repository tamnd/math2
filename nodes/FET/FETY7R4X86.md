---
tag: FETY7R4X86
kind: concept
name: Topological data analysis
msc: [62R40, 55N31]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_data_analysis
same_as:
  wikidata: Q4460773
  wikipedia: Topological data analysis
---

## Summary

Topological data analysis studies the shape of data with tools from algebraic topology.
It turns a finite set of points, usually in a [[metric space|0VKD1TP7F3]], into a family of [[simplicial complexes|V8GZ0W1ZZ5]] indexed by a scale.
It then records how topological features such as components and loops appear and disappear as the scale grows.
The main tool is [[persistent homology|S8SNBHVPSP]], whose output, a barcode or persistence diagram, is stable under small perturbations of the data.
It is used to find clusters, loops and voids in data from biology, materials science and image analysis.

## Explanations

### L1 human

Imagine points scattered around a ring.
Draw a ball of radius $r$ around each point and watch what happens as $r$ grows.
For small $r$ the balls are separate dots; then they join into a ring with a hole; for large $r$ the hole fills in.
The hole lives for a long range of $r$, which is a strong sign that the data really lie on a circle.
Topological data analysis measures such long-lived features and ignores the short-lived ones, which are mostly noise.
