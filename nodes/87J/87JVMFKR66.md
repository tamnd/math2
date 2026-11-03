---
tag: 87JVMFKR66
kind: concept
name: Hindmarsh–Rose model
msc: [92C20, 37N25, 34C60]
specializes: [RMWR3MDW0T]
sources:
  - url: https://en.wikipedia.org/wiki/Hindmarsh–Rose_model
same_as:
  wikidata: Q3859862
  wikipedia: Hindmarsh–Rose model
---

## Summary

The Hindmarsh–Rose model is a three-variable polynomial [[neuron model|RMWR3MDW0T]] that produces bursting: groups of spikes separated by quiet periods.
Two fast variables generate spikes, and a third, slow adaptation variable switches the spiking on and off.
For some parameter values the bursts become irregular, and the model shows [[chaos|DBKXCGDKTD]].
It is a common test case for slow–fast analysis and for the synchronization of coupled neurons.

## Explanations

### L1 human

Some neurons fire in bursts: a rapid series of spikes, then silence, then another series.
The Hindmarsh–Rose model gets this pattern from two speeds.
A fast pair of variables can either rest or spike.
A slow third variable builds up while the neuron spikes and eventually shuts the spiking off, then decays during the silence until spiking resumes.
