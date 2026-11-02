---
tag: PDFK69ZMST
kind: statement
role: theorem
name: CW approximation
msc: [55P10, 57Q05]
uses: [5W95QFHXPR, 4Q3WY1RX91, XZG6MTSWCN, 6P1E2FJPSD, 0CNQXVBHCX]
about: [5W95QFHXPR, 4Q3WY1RX91]
sources:
  - url: https://en.wikipedia.org/wiki/CW_complex
---

## Statement

Let $X$ be a [[topological space|0CNQXVBHCX]].

1. There are a [[CW complex|5W95QFHXPR]] $Z$ and a [[weak homotopy equivalence|4Q3WY1RX91]] $f \colon Z \to X$.
2. Let $f' \colon Z' \to X$ be another weak homotopy equivalence from a CW complex $Z'$.
   Then there is a [[homotopy equivalence|XZG6MTSWCN]] $h \colon Z \to Z'$ such that $f' \circ h$ is homotopic to $f$.

The pair $(Z, f)$ is called a *CW approximation* of $X$.

## Remarks

Part 1 is proved by building $Z$ one dimension at a time.
For each path component one starts with a point.
At stage $n$ one attaches cells to make the map surjective on $\pi_n$ and further cells to kill the kernel on $\pi_n$.
Part 2 uses the fact that a weak homotopy equivalence $f' \colon Z' \to X$ induces a bijection $[Z, Z'] \to [Z, X]$ for every CW complex $Z$, together with the [[Whitehead theorem|6P1E2FJPSD]].

Example: the Warsaw circle $W$ has all homotopy groups trivial, so the inclusion of a point is a weak homotopy equivalence and a point is a CW approximation of $W$.
The space $W$ itself is not contractible, so a weak equivalence need not be a homotopy equivalence when the source or target is not a CW complex.

## Explanations

### L1 human

Many spaces are not CW complexes, but homotopy groups and singular homology cannot tell the difference.
The theorem says every space has a CW complex shadow with the same homotopy groups, mapped into it.
That shadow is unique up to homotopy equivalence.

### L2 human

CW approximation lets one prove results about singular homology and homotopy groups for CW complexes only and then extend them to all spaces.
It also shows that the homotopy category of CW complexes is equivalent to the category of all spaces with weak homotopy equivalences inverted.
Functorial versions are given by the geometric realization of the singular simplicial set, $\abs{\operatorname{Sing} X} \to X$.
