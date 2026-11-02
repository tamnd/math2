---
tag: C63RVH96TF
kind: concept
name: Latent variable model
msc: [62H25, 62H05]
specializes: [K3AMMSY8DD]
sources:
  - url: https://en.wikipedia.org/wiki/Latent_variable_model
same_as:
  wikidata: Q1806885
  wikipedia: Latent variable model
---

## Summary

A latent variable model is a statistical model that links observed variables to variables that are never observed.
The hidden variables explain the dependence between the observed ones.
Typical examples are [[factor analysis|4QQQP1Q886]], [[mixture models|C98DKQSTNC]] and hidden Markov models.
The likelihood of the observed data is obtained by integrating out the hidden variables, often with the [[expectation–maximization algorithm|11N1AXSXYK]].

## Explanations

### L1 human

Intelligence, wealth or the type of a customer cannot be measured directly, but they leave traces in things that can be measured.
A latent variable model treats such a quantity as a hidden variable and describes how it shapes the measured data.
For example, the answers of a student to many test questions are linked because they all depend on one hidden ability.
Once the ability is known, the answers are often modelled as independent of each other.
