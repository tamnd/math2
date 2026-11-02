---
tag: 4EBHAWJJ8C
kind: concept
name: Chain homotopy
msc: [18G35, 55U15]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_category_of_chain_complexes
---

## Summary

A chain homotopy between two [[chain maps|HTK9WQZJ1G]] $f, g \colon C_\bullet \to D_\bullet$ is a family of maps $h_n \colon C_n \to D_{n+1}$ with $f - g = dh + hd$.
Chain homotopic maps induce the same maps on [[homology|2J4JJJYP22]].
The notion is the algebraic shadow of a [[homotopy|4A7H5AG0NF]] between continuous maps, and it is used to define the [[homotopy category of chain complexes|9Y5Y92R4D5]].

## Explanations

### L1 human

Two chain maps can look different in each degree yet have the same effect on homology.
A chain homotopy is a certificate of this: a family of maps one degree up whose "boundary" is the difference $f - g$.
In topology, a homotopy between two maps of spaces sweeps out a cylinder, and taking chains of that cylinder gives exactly such maps $h_n$.
For example, on the complex $0 \to \Z \xrightarrow{1} \Z \to 0$ the identity is chain homotopic to zero, which matches the fact that this complex has zero homology.
