---
tag: FPHNJ5AAYF
kind: concept
name: Generalized inverse
msc: [15A09]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_inverse
same_as:
  wikidata: Q370634
  wikipedia: Generalized inverse
---

## Summary

A generalized inverse of a matrix $A$ is a matrix $G$ with $AGA = A$.
Every matrix over a field has one, even when it is not square or not invertible.
Generalized inverses give solutions of consistent linear systems $Ax = b$ in the form $x = Gb$.
The [[Moore–Penrose inverse|0YY8VX28JR]] is a generalized inverse with three more conditions that make it unique.
The [[Drazin inverse|9FB0AZSEGM]] is a related kind of inverse for square matrices, though it does not satisfy $AGA = A$ in general.

## Explanations

### L1 human

Only some square matrices can be inverted.
A generalized inverse keeps one useful property of an inverse: applied in between, it does not change $A$.
Think of $G$ as a map that sends each vector in the image of $A$ back to one of its preimages.
For example, for $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, every matrix $G = \begin{pmatrix} 1 & a \\ b & c \end{pmatrix}$ satisfies $AGA = A$.
So a generalized inverse exists but is usually not unique.
