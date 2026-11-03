---
tag: TS89S85WZS
kind: concept
name: Limit analysis
msc: [74C05, 74G45]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_analysis
same_as:
  wikidata: Q6549440
  wikipedia: Limit analysis
---

## Summary

Limit analysis computes the collapse load of a structure made of a perfectly plastic material.
This is the load at which the structure can deform plastically without bound.
It skips the elastic–plastic history of the loading and goes straight to the collapse state.
Its two main tools are the lower bound theorem, based on admissible stress fields, and the upper bound theorem, based on admissible collapse mechanisms.
It is a central method of [[plasticity|K8BBMTN0KV]] in structural and geotechnical design.

## Explanations

### L1 human

Load a steel beam more and more and at some point it bends without stopping, like a hinge.
Limit analysis asks for that load directly.
Any stress pattern that balances the load and never exceeds the strength gives a safe load, so the true collapse load is at least as large.
Any way the structure could fold up gives a load at which it must fail, so the true collapse load is at most that large.
For a simply supported beam of span $L$ with a central load, a middle hinge gives the collapse load $4M_p/L$, where $M_p$ is the plastic moment of the section.
