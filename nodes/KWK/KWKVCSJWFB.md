---
tag: KWKVCSJWFB
kind: concept
name: Dirichlet space
msc: [30H99, "46E22"]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_space
same_as:
  wikidata: Q5280767
  wikipedia: Dirichlet space
---

## Summary

The Dirichlet space $\mathcal{D}$ is the Hilbert space of [[holomorphic functions|0NAHXR1FRH]] $f$ on the unit disc whose derivative is square-integrable with respect to area.
The Dirichlet integral $\int_{\mathbb{D}} \abs{f'}^2 \, dA$ is the area of the image $f(\mathbb{D})$, counted with multiplicity.
In terms of Taylor coefficients, $f = \sum a_n z^n$ lies in $\mathcal{D}$ exactly when $\sum n \abs{a_n}^2 < \infty$, so $\mathcal{D}$ is contained in the [[Hardy space|PNNNFJVF6W]] $H^2$.
It is a model space in operator theory and is linked to logarithmic [[capacity|DBQXRTC0VN]] on the circle.

## Explanations

### L1 human

A holomorphic function on the disc maps the disc onto some region, possibly covering parts of it several times.
The function is in the Dirichlet space when the total area covered, counting overlaps, is finite.
For example, any one-to-one map of the disc onto a bounded region is in the Dirichlet space.
The function $\log(1 - z)$ is in the Hardy space $H^2$ but not in the Dirichlet space, because its image has infinite area.
