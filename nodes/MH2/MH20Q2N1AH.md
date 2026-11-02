---
tag: MH20Q2N1AH
kind: concept
name: Dirichlet form
msc: [31C25, 60J46]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_form
same_as:
  wikidata: Q5280765
  wikipedia: Dirichlet form
---

## Summary

A Dirichlet form is a closed, symmetric, nonnegative bilinear form on a space $L^2(X, m)$ that does not increase under truncation of functions.
The model is the classical [[Dirichlet energy|YG3W8CBB3E]] $\int \abs{\nabla u}^2 \, dx$.
Dirichlet forms correspond one to one to symmetric Markovian semigroups on $L^2(X, m)$.
By a theorem of Fukushima, a regular Dirichlet form is the energy of a symmetric [[Hunt process|Z7T669BQ9B]], so the theory joins analysis and probability.

## Explanations

### L1 human

Think of a function $u$ as a temperature profile and of $\mathcal{E}(u, u)$ as the amount of tension in it.
The energy $\int \abs{u'}^2 \, dx$ of a function on an interval is the basic example.
The key rule is that cutting a function off at $0$ and at $1$ never increases its energy.
This rule links the form to a random motion: it says that heat flow keeps temperatures between their bounds.
Dirichlet forms also make sense on graphs and fractals, where there are no derivatives.
