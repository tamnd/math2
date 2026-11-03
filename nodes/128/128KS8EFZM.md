---
tag: 128KS8EFZM
kind: definition
name: Mathematical modelling of infectious diseases
msc: [92D30]
defines: AKP63KCK02
uses: [0P97V20RW7, 0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_modelling_of_infectious_diseases
---

## Definition

A *mathematical model of an infectious disease* consists of the following data.

1. A host population and a finite set of infection states, such as susceptible, infected and recovered.
2. A state space that records how many hosts, or which hosts, are in each infection state.
3. A rule for the change of the state in time.
   The rule is deterministic, such as an [[ordinary differential equation|0P97V20RW7]], or random, such as a [[stochastic process|0QH5ENKZM1]].

*Mathematical modelling of infectious diseases* is the construction and analysis of such models to describe and predict the spread of infections.

## Remarks

Example: the [[SIR model|J5FHBDJGJA]] has three states and a system of three ordinary differential equations, so it is such a model.
The [[Reed–Frost model|DG0ZDTRKHW]] has the same states and a random rule in discrete time.

Non-example: a fitted curve of case counts against time, with no states and no transmission rule, fails clauses 1 and 3.
It may describe the data, but it is a statistical description and not a model of transmission.

Models are deterministic or stochastic, in continuous or discrete time, and homogeneous or structured by age, space or contact network.
