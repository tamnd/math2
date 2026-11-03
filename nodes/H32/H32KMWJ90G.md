---
tag: H32KMWJ90G
kind: concept
name: Maximum length sequence
msc: [94A55, 11T71, 11B37]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum-length_sequence
same_as:
  wikidata: Q1417719
  wikipedia: Maximum-length sequence
---

## Summary

A maximum length sequence, or m-sequence, is an output of a [[linear-feedback shift register|WHX90SGEJ5]] of length $L$ over $\F_q$ with period $q^L - 1$.
This is the largest possible period.
This happens exactly when the connection polynomial is [[primitive|HQ7KMZYPSQ]] and the initial state is nonzero.
Binary m-sequences look random in several precise ways: they are balanced, have the expected run statistics, and have a two-valued periodic autocorrelation.
They are used in spread-spectrum systems, ranging, acoustic measurement and as building blocks of [[Gold codes|53YA8BDBTQ]].
See the [[definition|WPMS7A9PYJ]].

## Explanations

### L1 human

A shift register with $L$ bits has $2^L$ possible states, and the all-zero state just repeats itself.
An m-sequence is produced when the register runs through all the other $2^L - 1$ states before repeating.
For $L = 3$ the output $1, 0, 0, 1, 0, 1, 1$ then repeats, with period $7$.
Over one period it has four ones and three zeros, almost a fair coin.
Shifting it and comparing with the original gives nearly as many agreements as disagreements, which makes it useful as a test signal.
