---
tag: B0K18PWN2A
kind: concept
name: Restricted isometry property
msc: [94A12, 41A46, 15B52]
sources:
  - url: https://en.wikipedia.org/wiki/Restricted_isometry_property
same_as:
  wikidata: Q17099734
  wikipedia: Restricted isometry property
---

## Summary

A matrix has the restricted isometry property of order $s$ when it nearly preserves the length of every vector with at most $s$ nonzero entries.
The size of the distortion is measured by the restricted isometry constant $\delta_s$.
If $\delta_{2s}$ is small, $s$-sparse vectors can be recovered stably from their images by $\ell^1$ minimization.
This is the basis of compressed sensing.
Computing $\delta_s$ exactly is hard, but random Gaussian matrices have small constants with high probability.

## Explanations

### L1 human

A wide [[matrix|0VD9ZSWWJG]] must squash some vectors to zero, because it maps a big space into a small one.
The restricted isometry property says that it still keeps the lengths of all sparse vectors almost unchanged.
If this holds for all $2s$-sparse vectors, then two different $s$-sparse vectors cannot have the same image.
They even stay well separated after the map.
For example, the identity matrix keeps every length exactly, so $\delta_s = 0$ for every $s$.
A matrix with two equal columns sends $e_1 - e_2$, which has only two nonzero entries, to $0$, so it fails the property of order $2$.
