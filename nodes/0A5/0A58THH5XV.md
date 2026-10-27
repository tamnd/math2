---
tag: 0A58THH5XV
kind: definition
name: Boolean function
msc: ["06E30", 94C11]
defines: 0X05GS525E
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_function
    locator: lead section
inventory: [E1GBCX18PB]
---

## Definition

Let $n$ be a natural number.
A Boolean function of $n$ variables is a function $f : \{0, 1\}^n \to \{0, 1\}$.

## Remarks

There are $2^n$ inputs, so there are $2^{2^n}$ Boolean functions of $n$ variables.
A truth table lists the values of a Boolean function on all inputs.
Every Boolean function is given by a formula in [[disjunctive normal form|06S4WGSEQA]], and also by one in [[conjunctive normal form|07C4A8Y18K]].

## Explanations

### L1 human

A Boolean function takes some bits as input and returns one bit.
The logic gates and, or and not are Boolean functions, and a digital circuit computes a Boolean function.
