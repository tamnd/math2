---
tag: RMWR3MDW0T
kind: concept
name: Biological neuron model
msc: [92C20, 37N25]
sources:
  - url: https://en.wikipedia.org/wiki/Biological_neuron_model
same_as:
  wikidata: Q1651163
  wikipedia: Biological neuron model
---

## Summary

A biological neuron model is a mathematical description of the electrical activity of a nerve cell.
Most models are [[dynamical systems|BBZP1R872N]] for the membrane potential, the voltage across the cell membrane, driven by an input current.
They range from detailed conductance-based models built on ion channel data to simple threshold models that only record spike times.
They let one study how neurons turn inputs into trains of spikes, alone or in networks.

## Explanations

### L1 human

A neuron behaves like a small leaky electrical battery.
Current flowing in raises its voltage, leaks let the voltage relax back, and when the voltage gets high enough the cell fires a short pulse called a spike.
A neuron model writes these effects as equations for how the voltage changes in time.
Detailed models track the opening and closing of ion channels; simple models just say "fire and reset when the voltage crosses a threshold".
