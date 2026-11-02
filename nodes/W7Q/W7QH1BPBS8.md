---
tag: W7QH1BPBS8
kind: concept
name: MUSCL scheme
msc: [65M08, 35L65]
specializes: [HGKN8E09RS]
sources:
  - url: https://en.wikipedia.org/wiki/MUSCL_scheme
same_as:
  wikidata: Q6719085
  wikipedia: MUSCL scheme
---

## Summary

A MUSCL scheme is a [[finite volume method|HGKN8E09RS]] for [[conservation laws|8RA7AMWSAF]] that replaces the constant cell values of [[Godunov's scheme|43HZJ7DRT0]] by limited linear reconstructions.
The name stands for Monotonic Upstream-centred Scheme for Conservation Laws, and the approach goes back to Bram van Leer.
The reconstruction gives second-order accuracy where the solution is smooth.
A [[flux limiter|NZ8XFNCKQW]] switches the slopes off near jumps, so shocks are captured without spurious oscillations.
See the [[definition|SB1TM11S5Q]].

## Explanations

### L1 human

Godunov's scheme pretends that the solution is flat inside each cell, which smears out every feature.
A MUSCL scheme draws a short straight line in each cell instead, with a slope taken from the neighbouring cells.
Near a jump such a line could overshoot, so a limiter flattens the slope there.
For data on a straight line, such as $u_j = j$, the reconstruction hits the exact value at every cell edge.
For a step from $0$ to $1$, the limiter sets the slopes to zero next to the step, and no new maximum or minimum appears.
