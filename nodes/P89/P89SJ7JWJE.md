---
tag: P89SJ7JWJE
kind: concept
name: Uniform structure of a topological group
msc: [22A05, "54E15"]
specializes: [A54T86KS63]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_space
---

## Summary

Every [[topological group|92700QAB5Y]] carries natural [[uniform structures|A54T86KS63]] that induce its topology.
The left uniformity declares $x$ and $y$ close when $x^{-1} y$ is close to the identity, and the right uniformity uses $y x^{-1}$ instead.
These uniformities give meaning to Cauchy nets, uniform continuity and completeness without any metric.
For abelian groups the two uniformities agree.

## Explanations

### L1 human

In a metric space you can compare distances at different places: two points here are as close as two points there.
A general topological group has no metric, but it has a group law, and that is enough.
Two elements are declared close when one is obtained from the other by multiplying by an element near the identity.
For the real line under addition, this says that $x$ and $y$ are close when $y - x$ is small, which is the usual notion.
