---
tag: WHX90SGEJ5
kind: concept
name: Linear-feedback shift register
msc: [94A55, 11B37, 11T71]
sources:
  - url: https://en.wikipedia.org/wiki/Linear-feedback_shift_register
same_as:
  wikidata: Q681101
  wikipedia: Linear-feedback shift register
---

## Summary

A linear-feedback shift register (LFSR) is a device that produces a sequence over a [[finite field|0ZXZ82FTX2]].
Each new term is a fixed linear combination of the previous $L$ terms.
So its output is a solution of a [[linear recurrence with constant coefficients|0NDVHBVBXB]].
LFSRs are cheap to build in hardware and produce long sequences with good statistical properties, such as [[maximum length sequences|H32KMWJ90G]].
They are used in pseudo-random number generation, stream ciphers, spread-spectrum communication and error-detecting codes.
See the [[definition|CYP0N13QVX]].

## Explanations

### L1 human

Picture a row of $L$ boxes, each holding a bit.
At each clock tick, the bit in the last box is output and everything moves one box along.
The empty first box gets the sum mod $2$ of the bits in some chosen boxes.
For example, with two boxes and the rule "new bit = sum of both bits", starting from $1, 1$ the output is $1, 1, 0, 1, 1, 0, \dots$.
The output looks irregular for well-chosen rules, but it always repeats eventually, because there are only finitely many states.
