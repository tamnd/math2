---
tag: B9C5RBFATB
kind: concept
name: Communication channel
msc: [94A40, 94A05]
sources:
  - url: https://en.wikipedia.org/wiki/Communication_channel
---

## Summary

In information theory a communication channel is a model of a medium that carries symbols from a sender to a receiver, possibly with errors.
Mathematically it is given by the probabilities of each output given each input.
The simplest and most studied model is the discrete memoryless channel, in which each use of the channel acts independently.
The main question about a channel is how fast information can pass through it reliably, which is its capacity.

## Explanations

### L1 human

A telephone line, a radio link or a hard disk all take in symbols and give out symbols, sometimes wrong ones.
The channel model forgets the physics and keeps only the chances: if I send this, what do I receive?
For example, a line that flips each bit with probability $0.1$ and leaves it alone otherwise is a channel.
[[Quantum channels|10VZYJ4552]] play the same role for quantum information.
