---
tag: RQ3JKGWD03
kind: concept
name: Volterra series
msc: [93C10, 45G10]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_series
same_as:
  wikidata: Q3957891
  wikipedia: Volterra series
---

## Summary

A Volterra series writes the output of a nonlinear, time-invariant system with memory as a sum of multiple integrals of the input.
The first term is a [[convolution|2Z29JN3VES]] with an impulse response, as for a linear system.
The next terms involve products of two, three or more past values of the input, weighted by kernels of several variables.
It plays for nonlinear operators the role that the [[Taylor series|0Z49YH6ZWY]] plays for functions.
It is used to model and identify nonlinear systems in engineering and biology.

## Explanations

### L1 human

A linear system remembers its past inputs and adds them up with fixed weights.
A nonlinear system may also multiply past inputs with each other, for example the input a second ago times the input two seconds ago.
The Volterra series lists all these effects: first the single inputs, then the pairs, then the triples, each with its own weights.
For example, squaring the output of a simple linear filter gives a system whose series has only a second order term.
