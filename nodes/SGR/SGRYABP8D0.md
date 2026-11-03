---
tag: SGRYABP8D0
kind: concept
name: Turbo code
msc: [94B60, 94B35, 94B10]
sources:
  - url: https://en.wikipedia.org/wiki/Turbo_code
same_as:
  wikidata: Q2164281
  wikipedia: Turbo code
---

## Summary

A turbo code is built from two [[convolutional codes|JCFC831VS2]] in parallel.
One encodes the message directly, the other encodes a scrambled copy of it.
The message is sent together with both parity streams.
It is decoded iteratively: two [[BCJR|RV2VQVS2YS]] decoders, one for each constituent code, pass soft information to each other.
Berrou, Glavieux and Thitimajshima introduced turbo codes in 1993.
They were the first practical codes to perform within a fraction of a decibel of the [[Shannon limit|PR3NJB0SKG]].
They are used in mobile telephone standards and in deep-space links.

## Explanations

### L1 human

Two simple encoders look at the same message, one in the original order and one in a shuffled order.
Each decoder alone sees only part of the evidence.
The decoders take turns: each one improves its guess about every bit and hands its new confidence to the other, which uses it as extra evidence.
After a few rounds the guesses usually agree on the sent message, even at noise levels where older codes fail.
The shuffle is important, because it makes the errors that confuse one decoder look unrelated to the other.
