---
tag: C6RVY7R8S6
kind: example
name: Power-law fluid
msc: [76A05]
instance_of: [8DT9MB9V6R]
sources:
  - url: https://en.wikipedia.org/wiki/Power-law_fluid
same_as:
  wikidata: Q970142
  wikipedia: Power-law fluid
---

## Example

A *power-law fluid* (Ostwald–de Waele fluid) has two constants, the consistency $K > 0$ and the flow index $n > 0$.
In a simple shear flow with shear rate $\dot\gamma > 0$ its shear stress is
$$\tau = K \dot\gamma^{\,n}.$$
Its apparent viscosity is $\eta(\dot\gamma) = \tau / \dot\gamma = K \dot\gamma^{\,n - 1}$.
For $n = 1$ this is the constant $K$, and the fluid is Newtonian.
For $n \ne 1$ the apparent viscosity depends on $\dot\gamma$, so the fluid is a [[non-Newtonian fluid|8DT9MB9V6R]].
If $n < 1$ the viscosity decreases as $\dot\gamma$ grows (shear-thinning, or pseudoplastic); if $n > 1$ it increases (shear-thickening, or dilatant).

## Remarks

In a general flow one writes $\tau = 2 K \dot\gamma^{\,n-1} D$, where $D$ is the strain rate tensor and $\dot\gamma = \sqrt{2 \, \tr(D^2)}$.
For $n < 1$ the model predicts infinite viscosity at zero shear rate, so it is only used over a limited range of shear rates.

## Explanations

### L1 human

Many fluids get thinner when they are stirred faster, like paint or blood, and a few get thicker.
The power-law fluid is the simplest formula for this: stress is a power of the shear rate.
The exponent $n$ tells which case you are in, with $n = 1$ giving an ordinary fluid like water.
