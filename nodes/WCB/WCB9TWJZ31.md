---
tag: WCB9TWJZ31
kind: concept
name: Vector quantization
msc: [94A29, 94A34, 68P30]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_quantization
same_as:
  wikidata: Q612536
  wikipedia: Vector quantization
---

## Summary

Vector quantization replaces each point of $\R^k$ by the nearest of finitely many representative points, the codebook.
It quantizes blocks of samples together instead of one sample at a time.
Even for independent samples this can give a smaller error at the same number of bits.
One reason is that cells in several dimensions can have better shapes than cubes.
The design of good codebooks is closely related to $k$-means clustering.

## Explanations

### L1 human

Think of a map of a country with a few post offices, and send each house to the nearest post office.
The post offices are the codebook, and the regions they serve are the cells.
To store a house one only stores the number of its post office.
In image compression the "houses" are small blocks of pixels, and a list of typical blocks serves as the codebook.
