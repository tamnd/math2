---
tag: NP473H6VVV
kind: concept
name: Gene regulatory network
msc: [92C42, 92C40]
sources:
  - url: https://en.wikipedia.org/wiki/Gene_regulatory_network
same_as:
  wikidata: Q1502576
  wikipedia: Gene regulatory network
---

## Summary

A gene regulatory network is a collection of genes and their products in which some products switch the expression of other genes on or off.
Mathematically it is a [[directed graph|0KFYGSHHF5]] whose edges carry a sign for activation or repression, together with a dynamical model of expression levels.
Common dynamical models are systems of ordinary differential equations with Hill functions and Boolean networks.
Feedback loops in the network explain switches, memory and oscillations in cells.

## Explanations

### L1 human

Each gene makes a protein, and some of these proteins bind to DNA and change how much of other proteins is made.
Draw an arrow from gene A to gene B if the protein of A affects B, with a plus for "turns on" and a minus for "turns off".
Two genes that turn each other off form a switch: the cell settles with one gene on and the other off, and it remembers which.
Three genes that turn each other off in a ring can make protein levels rise and fall in a cycle, like a clock.
