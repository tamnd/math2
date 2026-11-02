---
tag: 3BTG6VVCGZ
kind: concept
name: Loss function
msc: [62C05]
sources:
  - url: https://en.wikipedia.org/wiki/Loss_function
same_as:
  wikidata: Q1036748
  wikipedia: Loss function
---

## Summary

A loss function assigns a number to each pair of a true state of nature and an action.
The number measures the cost of taking that action in that state.
In statistics the state is an unknown parameter and the action is often an estimate.
Loss functions are the starting point of [[statistical decision theory|CPFSBBHXT5]]: averaging the loss over the data gives the risk, by which procedures are compared.

## Explanations

### L1 human

A loss function says how bad a guess is when the truth is known.
Guessing $7$ when the truth is $5$ costs $(7 - 5)^2 = 4$ under squared error loss, and $\abs{7 - 5} = 2$ under absolute error loss.
Different losses express different priorities: squared error punishes large mistakes heavily, while a $0$-$1$ loss only cares whether the answer is right.
The choice of loss changes which estimator is best.
