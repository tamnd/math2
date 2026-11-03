---
tag: 21FN2KSTJZ
kind: concept
name: Linear system
msc: [93C05, 93A10]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_system
same_as:
  wikidata: Q1072174
  wikipedia: Linear system
---

## Summary

A linear system is a system whose output depends linearly on its input.
The response to a sum of inputs is the sum of the responses, and scaling the input scales the output.
This is the superposition principle.
Linear systems are the main class studied in systems and [[control theory|JXZ0GZXET1]], because the tools of linear algebra and of transforms apply to them.
Many nonlinear systems are studied through their linear approximations near an equilibrium.

## Explanations

### L1 human

Think of an ideal loudspeaker: playing two songs at once gives the sum of the two sounds, and turning up the input turns up the sound by the same factor.
A linear system behaves exactly like this.
So once one knows how it responds to a few simple inputs, one knows how it responds to all their combinations.
For example, the system with output $y(t) = 3u(t)$ is linear, but the system with output $y(t) = u(t)^2$ is not, since doubling the input multiplies the output by four.
