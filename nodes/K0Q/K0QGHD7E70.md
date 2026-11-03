---
tag: K0QGHD7E70
kind: concept
name: Hodgkin–Huxley model
msc: [92C20, 34C60]
specializes: [RMWR3MDW0T]
sources:
  - url: https://en.wikipedia.org/wiki/Hodgkin–Huxley_model
same_as:
  wikidata: Q995215
  wikipedia: Hodgkin–Huxley model
---

## Summary

The Hodgkin–Huxley model is a system of four [[ordinary differential equations|0NT64JV96A]] that describes how action potentials are generated and propagated in a nerve cell.
It models the membrane as a capacitor in parallel with sodium, potassium and leak currents, whose conductances depend on voltage through gating variables.
Hodgkin and Huxley fitted it to measurements on the squid giant axon and published it in 1952.
It is the prototype of the conductance-based [[neuron models|RMWR3MDW0T]].

## Explanations

### L1 human

The membrane of a nerve cell has tiny gates that let sodium or potassium ions through.
When the voltage rises a little, sodium gates open fast, sodium rushes in, and the voltage shoots up: this is the spike.
More slowly, the sodium gates close and potassium gates open, and the voltage falls back.
The model writes one equation for the voltage and one for each kind of gate, and with the measured rates it reproduces the shape and speed of real spikes.
