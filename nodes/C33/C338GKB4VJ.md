---
tag: C338GKB4VJ
kind: concept
name: Association scheme
msc: ["05E30"]
sources:
  - url: https://en.wikipedia.org/wiki/Association_scheme
same_as:
  wikidata: Q4810150
  wikipedia: Association scheme
---

## Summary

An association scheme is a partition of the ordered pairs of a finite set into relations with a strong regularity property.
The number of paths of two given types between two points depends only on the relation between the points.
The adjacency matrices of the relations span a matrix algebra, the Bose–Mesner algebra, which makes linear algebra available for combinatorial questions.
Association schemes came from the design of statistical experiments and are now basic in coding theory, design theory and the study of [[strongly regular graphs|C22WGRP3T8]].

## Explanations

### L1 human

Think of a finite set of points where every pair of points stands in exactly one of a few possible relations, such as "equal", "near" or "far".
The scheme is very regular.
Take two points in a given relation; the number of third points near the first and far from the second depends only on that relation.
The words of length $n$ over an alphabet, with "differ in exactly $i$ places" as the $i$-th relation, form such a scheme, called the Hamming scheme.
