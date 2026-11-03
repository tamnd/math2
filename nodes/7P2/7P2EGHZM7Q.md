---
tag: 7P2EGHZM7Q
kind: concept
name: Cohesive zone model
msc: [74R10, 74R20, 74A45]
sources:
  - url: https://en.wikipedia.org/wiki/Cohesive_zone_model
same_as:
  wikidata: Q17007169
  wikipedia: Cohesive zone model
---

## Summary

A cohesive zone model describes fracture as a gradual separation of two surfaces that still attract each other.
Ahead of the physical crack tip there is a zone where the crack faces carry tractions that depend on their opening, through a traction–separation law.
The tractions decrease to zero at a critical opening, and the area under the law is the fracture energy.
This removes the stress singularity of linear elastic [[fracture mechanics|SNRXGRZWR5]] and is widely used in finite element simulations of crack growth.

## Explanations

### L1 human

When two pieces of tape are peeled apart, they do not separate at a sharp line.
Near the peel front, the glue is stretched and still pulls the two sides together, and only further back is it fully broken.
A cohesive zone model treats every crack this way.
It says how strongly the faces pull on each other as a function of how far apart they are.
The crack is fully open only where they no longer pull at all.
