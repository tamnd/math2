---
tag: FCGFMFM68F
kind: concept
name: Conjugate beam method
msc: [74K10, 74G05]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_beam_method
same_as:
  wikidata: Q5161152
  wikipedia: Conjugate beam method
---

## Summary

The conjugate beam method computes slopes and deflections of a beam by statics alone.
One loads an imaginary beam of the same length, the conjugate beam, with the [[bending moment|Q6XAPXMGH0]] diagram of the real beam divided by $EI$.
The shear force of the conjugate beam is then the slope of the real beam.
Its bending moment is the deflection of the real beam.
It works because deflection and moment satisfy differential equations of the same form, $w'' = -M/EI$ and $M'' = -q$.

## Explanations

### L1 human

Finding how much a beam sags normally means solving a differential equation.
Finding the bending moment of a beam under a load is easier: it is just balancing forces and turning effects.
The conjugate beam method turns the first task into the second: it pretends the curvature of the real beam is a load on a second beam.
The moment that this pretend load causes is exactly the sag of the real beam.
The supports of the pretend beam are chosen so that this works, for example a clamped end becomes a free end.
