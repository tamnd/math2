---
tag: CDVA7EJSSD
kind: concept
name: Ambiguity function
msc: [94A12, 42A38]
sources:
  - url: https://en.wikipedia.org/wiki/Ambiguity_function
same_as:
  wikidata: Q3206297
  wikipedia: Ambiguity function
---

## Summary

The ambiguity function of a signal $f$ measures how much $f$ correlates with copies of itself shifted in time and in frequency.
In radar it describes how well a transmitted pulse lets one tell targets apart by range (time delay) and by speed (Doppler frequency shift).
It is the [[short-time Fourier transform|3DHNP5NEWH]] of $f$ with window $f$, up to a phase factor.
It is related to the [[Wigner distribution|FCHW5QGG5V]] by a two-dimensional Fourier transform.

## Explanations

### L1 human

A radar sends a pulse and listens for its echo.
The echo comes back delayed, because the target is far, and shifted in frequency, because the target moves.
The ambiguity function tells, for each delay and frequency shift, how much the shifted echo still looks like the original pulse.
A good pulse has an ambiguity function with one sharp peak at zero, so that different targets cannot be confused.
