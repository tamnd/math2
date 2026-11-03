---
tag: ESPYW94XGR
kind: concept
name: Complexity class
msc: [68Q15]
sources:
  - url: https://en.wikipedia.org/wiki/Complexity_class
same_as:
  wikidata: Q908207
  wikipedia: Complexity class
---

## Summary

A complexity class is a set of computational problems that can be solved within a given bound on some resource.
The usual resources are [[time|T00W8RQT8E]] and [[space|FDNFGKEEJR]] on a fixed model of computation, such as the [[Turing machine|758EYCN27B]].
Classes such as P, NP and PSPACE group problems by how hard they are to solve.
The main questions of complexity theory are about inclusions between such classes.

## Explanations

### L1 human

Sort problems into boxes by the effort they need.
One box holds every yes-or-no question that a computer can answer in time bounded by a polynomial in the length of the input.
Another holds every question it can answer with memory bounded by a polynomial.
Each such box is a complexity class.
For example, "is this list of numbers sorted?" lies in the first box, since one pass through the list settles it.
