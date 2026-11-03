---
tag: D14DP6XQJ6
kind: concept
name: Modal analysis
msc: [70J10, 70J50]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_analysis
same_as:
  wikidata: Q1416137
  wikipedia: Modal analysis
---

## Summary

Modal analysis is the study of a vibrating structure through its [[normal modes|JVM27J1FTF]]: its natural frequencies, mode shapes and damping.
Mathematically, it changes coordinates to the mode shapes, so that the coupled equations $M \ddot x + K x = f(t)$ split into independent equations for single oscillators.
It is done numerically, with finite element models, or experimentally, from measured responses.
Engineers use it to keep natural frequencies of buildings, bridges, vehicles and machines away from the frequencies of the loads they meet.
See the [[definition|MSE1699MPS]].

## Explanations

### L1 human

A bridge or a car body can vibrate in many ways, which looks hopelessly complicated.
Modal analysis finds a few basic patterns of vibration, each with its own frequency.
Every vibration of the structure is a mix of these patterns, and each pattern behaves like a single mass on a spring.
So a big coupled problem becomes many small independent ones.
If a pattern has a frequency close to that of the wind or of an engine, the engineer knows that resonance is a risk.
