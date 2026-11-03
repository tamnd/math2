---
tag: H6TFN824YV
kind: concept
name: Quantization
msc: [94A29, 94A12, 94A34]
sources:
  - url: https://en.wikipedia.org/wiki/Quantization_(signal_processing)
same_as:
  wikidata: Q198099
  wikipedia: Quantization (signal processing)
---

## Summary

Quantization maps a continuous range of values to a finite or countable set of values.
It is the step that turns measured real numbers into numbers a computer can store.
It always loses information, and the difference between the input and its quantized value is the quantization error.
Quantization is the simplest form of lossy compression and is studied with the tools of rate–distortion theory.

## Explanations

### L1 human

Rounding to the nearest whole number is a quantizer: $2.7$ becomes $3$ and $-0.2$ becomes $0$.
A digital thermometer that shows tenths of a degree quantizes the true temperature.
The finer the steps, the smaller the error, but the more possible values must be stored.
With step $\Delta$, rounding is never off by more than $\Delta / 2$.
