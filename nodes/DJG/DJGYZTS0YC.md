---
tag: DJGYZTS0YC
kind: concept
name: Linear type system
msc: [68N15, 03B47, 68N18]
specializes: [AVVQEG0MRJ]
uses: [AVVQEG0MRJ, 2P2184B6HE]
sources:
  - url: https://en.wikipedia.org/wiki/Substructural_type_system
---

## Summary

A linear type system is a [[type system|AVVQEG0MRJ]] in which each variable must be used exactly once.
It is the type-theoretic side of [[linear logic|2P2184B6HE]].
It drops the structural rules of weakening, which allows a variable to be ignored, and of contraction, which allows it to be used twice.
Values of linear type behave like resources, such as a file handle or a block of memory, that can be neither copied nor lost.
Related substructural systems are affine types, where each variable is used at most once, and relevant types, where it is used at least once.
Rust's ownership types are close to affine types.

## Explanations

### L1 human

Think of a variable as a coin in your hand: you must spend it, and you can spend it only once.
A linear type checker enforces this rule for every variable of the program.
So a program cannot close a file twice or forget to close it, if closing is the only way to use up the file.
The function $\lambda x.\, x$ is linear, but $\lambda x.\, (x, x)$ is not, since it uses $x$ twice.
