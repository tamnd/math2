---
tag: C2CK6KSSTV
kind: concept
name: Intrinsic volume
msc: [52A39, 52A22]
sources:
  - url: https://en.wikipedia.org/wiki/Hadwiger's_theorem
---

## Summary

The intrinsic volumes $V_0(K), \dots, V_n(K)$ of a convex body $K$ in $\R^n$ are rescaled [[quermassintegrals|H1K36H9ZWB]].
The scaling makes them independent of the dimension of the ambient space.
$V_n$ is the volume, $2 V_{n-1}$ is the surface area, and $V_0$ is the Euler characteristic, equal to $1$ for every nonempty convex body.
By [[Hadwiger's theorem|7V2X68AMEY]] they span all continuous valuations on convex bodies that are invariant under rigid motions.

## Explanations

### L1 human

Intrinsic volumes are the natural sizes of a convex shape in each dimension.
For a box with sides $a, b, c$ they are $abc$ (volume), $ab + bc + ca$ (half the surface area), $a + b + c$ (a total length), and $1$.
If the box is flattened into a rectangle with sides $a, b$, one gets $0$, $ab$, $a + b$ and $1$, exactly the intrinsic volumes of the rectangle in the plane.
This independence of the surrounding space is what "intrinsic" means.
