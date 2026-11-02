---
tag: BW7FEZ8WM1
kind: concept
name: Automatic differentiation
msc: [65D25, 68W30]
sources:
  - url: https://en.wikipedia.org/wiki/Automatic_differentiation
same_as:
  wikidata: Q787371
  wikipedia: Automatic differentiation
---

## Summary

Automatic differentiation computes exact values of [[derivatives|0V1EJCT8G6]] of a function given as a computer program.
It applies the [[chain rule|0RXX2PT1MQ]] to each elementary operation of the program.
So its only errors are rounding errors, unlike [[numerical differentiation|NVH3F8FTYS]].
In forward mode it propagates directional derivatives along with the values; in reverse mode it propagates sensitivities backwards from the outputs.
Reverse mode computes the gradient of a scalar function at a small constant multiple of the cost of the function.
The backpropagation algorithm of machine learning is a special case of reverse mode.

## Explanations

### L1 human

A program computes a complicated function by a long chain of simple steps: additions, multiplications, sines, exponentials.
The derivative of each simple step is known, and the chain rule says how to combine them.
Automatic differentiation lets the computer carry along the derivative next to each intermediate value.
For example, for $f(x) = x \sin x$ at $x = 1$, it keeps the pairs $(1, 1)$ for $x$ and $(\sin 1, \cos 1)$ for $\sin x$, and the product rule gives the pair $(\sin 1, \sin 1 + \cos 1)$, whose second entry is $f'(1)$.
