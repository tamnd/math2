---
tag: KCGE92DJ1W
kind: concept
name: Chemical reaction network theory
msc: ["92E20", 80A30, 37N25]
sources:
  - url: https://en.wikipedia.org/wiki/Chemical_reaction_network_theory
same_as:
  wikidata: Q1069192
  wikipedia: Chemical reaction network theory
---

## Summary

Chemical reaction network theory studies the systems of [[ordinary differential equations|0NT64JV96A]] that come from networks of chemical reactions with mass-action kinetics.
Its aim is to read properties of the dynamics from the structure of the network alone, whatever the values of the rate constants.
Such properties are the number and the stability of the [[equilibria|0N8NGKDZDZ]].
Key invariants are the stoichiometric subspace, the linkage classes, weak reversibility and the deficiency.
The [[deficiency zero theorem|5JP25MVJ8Y]] is its best-known result.

## Explanations

### L1 human

A list of chemical reactions, such as $A + B \to C$ and $C \to A + B$, can be drawn as a graph whose vertices are the combinations of molecules on each side of an arrow.
With mass-action kinetics, this graph and a choice of rate constants give a system of differential equations for the concentrations.
The rate constants are usually poorly known, so one wants conclusions that hold for all of them.
The theory finds such conclusions from the shape of the graph: for example, some networks can never oscillate and always settle to a unique balance.
