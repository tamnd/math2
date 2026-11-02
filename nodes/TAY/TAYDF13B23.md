---
tag: TAYDF13B23
kind: concept
name: Algebraic statistics
msc: [62R01, 13P25, 14Q99]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_statistics
same_as:
  wikidata: Q4724018
  wikipedia: Algebraic statistics
---

## Summary

Algebraic statistics uses algebraic geometry and commutative algebra to study statistical models and procedures.
Many models for discrete data are sets of probability vectors cut out by polynomial equations.
Examples are independence models for [[contingency tables|PANSMHE0SW]], [[graphical models|Q3FQAD1BXG]] and log-linear models.
Tools such as [[polynomial ideals|096Z9MP2ME]], [[Gröbner bases|C83KPT47R0]] and [[algebraic varieties|HV6YBS0YDH]] then give information on identifiability, maximum likelihood estimation and exact tests.
A well-known example is the use of Markov bases, introduced by Persi Diaconis and Bernd Sturmfels, to sample tables with fixed margins.

## Explanations

### L1 human

Toss two coins that may be biased and record the four outcomes HH, HT, TH, TT.
If the coins are independent, the probabilities satisfy $p_{HH} p_{TT} = p_{HT} p_{TH}$.
So the independent models form a curved surface defined by one polynomial equation inside the set of all probability vectors.
Algebraic statistics studies such surfaces with the tools of algebra and uses them to answer statistical questions.
