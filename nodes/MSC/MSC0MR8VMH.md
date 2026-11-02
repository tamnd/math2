---
tag: MSC0MR8VMH
kind: concept
name: Parametric model
msc: [62A01, 62F99]
specializes: [K3AMMSY8DD]
sources:
  - url: https://en.wikipedia.org/wiki/Parametric_model
same_as:
  wikidata: Q7135228
  wikipedia: Parametric model
---

## Summary

A parametric model is a [[statistical model|K3AMMSY8DD]] whose laws are described by finitely many real numbers, the parameters.
Inference in such a model reduces to learning a point of a subset of $\R^k$.
Most classical theory, such as maximum likelihood and the Cramér–Rao bound, is developed for parametric models.

## Explanations

### L1 human

A parametric model is a family of distributions that you can tune with a few knobs.
The normal distributions form such a family: two knobs, the mean $\mu$ and the variance $\sigma^2$, fix the whole bell curve.
Learning from data then means finding good settings of the knobs.
A model with "any distribution at all" has no finite set of knobs, and it is called nonparametric.
