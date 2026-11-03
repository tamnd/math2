---
tag: W3N8APDEB9
kind: concept
name: Zero dynamics
msc: [93C10, 93B27, 93B18]
sources:
  - url: https://en.wikipedia.org/wiki/Zero_dynamics
same_as:
  wikidata: Q15837116
  wikipedia: Zero dynamics
---

## Summary

The zero dynamics of a nonlinear control system are the internal motions that remain when the input is chosen to keep the output identically zero.
They extend to nonlinear systems the notion of the [[zeros of a transfer function|NSGTEGWZY0]].
A system whose zero dynamics are asymptotically stable is called [[minimum phase|7PWB4YS8PA]].
This property allows exact output tracking by [[feedback linearization|1J2KTGXB34]] without internal blow-up.

## Explanations

### L1 human

Suppose a controller holds the measured output of a machine exactly at zero.
The machine may still move inside, in ways the output does not show.
These hidden motions are the zero dynamics.
If they die out, holding the output at zero is safe; if they grow, the machine falls apart while the output looks perfect.
