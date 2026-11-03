---
tag: 2PQKV1KX24
kind: concept
name: Random-access machine
msc: [68Q04, 68Q25]
specializes: [YFHEG4GYHW]
sources:
  - url: https://en.wikipedia.org/wiki/Random-access_machine
same_as:
  wikidata: Q2565212
  wikipedia: Random-access machine
---

## Summary

A random-access machine, or RAM, is a [[register machine|TGDKQY6S1T]] with infinitely many numbered registers and indirect addressing.
An instruction can use the content of one register as the address of another, so any memory cell can be reached in one step.
It is the model behind the usual analysis of algorithms, where reading an array entry costs one step.
It computes the same functions as a [[Turing machine|758EYCN27B]], and the two simulate each other with polynomial overhead under the logarithmic cost measure.

## Explanations

### L1 human

A Turing machine has to walk along its tape to reach a distant cell.
A random-access machine can jump to any memory cell at once if it knows the cell's number.
This is how the memory of a real computer behaves.
For example, looking up the entry $A[i]$ of an array stored in registers costs one step, whatever $i$ is.
That is why running times of algorithms in textbooks are measured on this model.
