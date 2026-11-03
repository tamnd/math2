---
tag: BBDDJMX1CB
kind: concept
name: Bent function
msc: ["06E30", 94A60, 94A55]
specializes: [0X05GS525E]
sources:
  - url: https://en.wikipedia.org/wiki/Bent_function
same_as:
  wikidata: Q4890350
  wikipedia: Bent function
---

## Summary

A bent function is a [[Boolean function|0X05GS525E]] on $\F_2^n$ whose [[Walsh–Hadamard transform|K784BA2WHV]] has the same absolute value at every point.
Bent functions are as far as possible from all affine functions, so they have the largest possible nonlinearity.
They exist only when $n$ is even.
They are used in the design of ciphers and of sequence families with low correlation, and they correspond to certain Hadamard difference sets.
See the [[definition|9QXBBQWH0T]].

## Explanations

### L1 human

A Boolean function takes strings of $n$ bits and returns one bit.
Affine functions, such as $x_1 + x_3 + 1$ mod $2$, are the simplest ones, and they are easy to attack in a cipher.
A bent function disagrees with every affine function on nearly half of the inputs, and it does so in a perfectly even way.
The smallest example is $f(x_1, x_2) = x_1 x_2$, which agrees with each affine function of two bits on either $1$ or $3$ of the $4$ inputs.
