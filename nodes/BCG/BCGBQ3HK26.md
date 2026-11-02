---
tag: BCGBQ3HK26
kind: concept
name: Iterative functional equation
msc: [39B12, 26A18]
specializes: [SRAN4EKWS0]
sources:
  - url: https://en.wikipedia.org/wiki/Iterated_function
---

## Summary

An iterative functional equation is a [[functional equation|SRAN4EKWS0]] in one variable in which the unknown function is composed with a given map or with itself.
A typical form is $\varphi(f(x)) = g(x, \varphi(x))$, where $f$ and $g$ are given and $\varphi$ is unknown.
Such equations describe how a quantity changes under one step of an [[iterated map|AYVTR2ES5B]].
The Abel equation, the Schröder equation and the equation $\varphi(\varphi(x)) = f(x)$ for a functional square root are the main examples.

## Explanations

### L1 human

Iteration means applying the same map again and again.
An iterative functional equation asks for a function that interacts in a fixed way with one step of this process.
For example, a function $\varphi$ with $\varphi(2x) = \varphi(x) + 1$ counts how many doublings one has made, and $\varphi(x) = \log_2 x$ works on the positive numbers.
Such a function lets one ask what half a step of the process should be.
