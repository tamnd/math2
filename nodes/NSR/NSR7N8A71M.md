---
tag: NSR7N8A71M
kind: concept
name: Causal system
msc: [93A10, 93C05]
sources:
  - url: https://en.wikipedia.org/wiki/Causal_system
same_as:
  wikidata: Q1523340
  wikipedia: Causal system
---

## Summary

A system is causal if its output at each time depends only on the input at that time and at earlier times.
A causal system cannot react to an input before the input arrives.
Every physical system that runs in real time is causal, so causality is a basic requirement for a model of a device or a controller.
For a [[linear time-invariant system|6J9MPVHSMF]], causality means that the [[impulse response|3X3SYVM7R5]] vanishes at negative times.

## Explanations

### L1 human

A causal system has no crystal ball: what it does now can only depend on what it has already seen.
An echo is causal, since it repeats a sound after the sound was made.
A rule such as "output today the input of tomorrow" is not causal, and no real device can carry it out in real time.
Such rules still make sense when the whole signal is recorded first, as in offline processing of a sound file.
