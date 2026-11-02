---
tag: AGXZ2G4MFM
kind: concept
name: Riesz mean
msc: ["40G99", "30B50"]
specializes: [8X25Q4XYMN]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_mean
same_as:
  wikidata: Q2152569
  wikipedia: Riesz mean
---

## Summary

A Riesz mean of a series $\sum a_n$ is a weighted partial sum in which the term $a_n$ is damped by a factor $(1 - \lambda_n/\omega)^{\delta}$.
Here $\lambda_n$ is a given increasing sequence and $\omega$ is a cut-off that grows to infinity.
The series is Riesz summable when these means converge.
With $\lambda_n = n$ and $\delta = 1$ the Riesz means at integer cut-offs are the [[Cesàro means|08R2V9GZF7]] of the partial sums.
Riesz means with $\lambda_n = \ln n$ are a standard tool for [[Dirichlet series|8MWTEF6462]] in analytic number theory.

## Explanations

### L1 human

A partial sum cuts a series off sharply: terms before the cut-off count fully and the rest not at all.
A Riesz mean cuts it off smoothly: terms well before the cut-off count almost fully, and terms near it count only a little.
The smooth cut-off removes much of the oscillation that makes a series diverge.
The parameter $\delta$ controls how smooth the cut-off is.
