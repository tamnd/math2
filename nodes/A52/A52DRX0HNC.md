---
tag: A52DRX0HNC
kind: concept
name: FitzHugh–Nagumo model
msc: [92C20, 34C60, 37N25]
specializes: [RMWR3MDW0T]
sources:
  - url: https://en.wikipedia.org/wiki/FitzHugh–Nagumo_model
same_as:
  wikidata: Q502563
  wikipedia: FitzHugh–Nagumo model
---

## Summary

The FitzHugh–Nagumo model is a two-variable simplification of the [[Hodgkin–Huxley model|K0QGHD7E70]].
A fast voltage-like variable with a cubic nonlinearity is coupled to a slow linear recovery variable.
Its [[phase plane|05VDGH129F]] shows excitability, thresholds and relaxation oscillations in a form that can be analysed by hand.
It is a standard example of an excitable system in mathematical biology.

## Explanations

### L1 human

The model keeps two quantities: a voltage that can jump quickly, and a slow recovery variable that pulls the voltage back down.
At rest, a small kick dies out, but a kick above a threshold sends the voltage on a large excursion before it returns: a spike.
With enough steady input current, the spikes repeat forever, and the state goes around a closed loop.
In the plane of the two variables, this behaviour can be read off from where an S-shaped curve and a straight line cross.
