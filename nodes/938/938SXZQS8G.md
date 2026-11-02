---
tag: 938SXZQS8G
kind: concept
name: Dual Radon transform
msc: [44A12, 92C55]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Radon_transform
---

## Summary

The dual Radon transform, or back-projection, acts on functions $g$ on the set of hyperplanes.
Its value at a point $x$ of $\R^n$ is the integral of $g$ over all hyperplanes through $x$.
It is the formal adjoint of the [[Radon transform|VJNZJ352PC]] for the natural measures.
It is not the inverse of the Radon transform, but the [[Radon inversion formula|HN93ST5CBT]] writes the inverse as the dual transform composed with a filter.
In tomography this is the back-projection step of [[filtered back-projection|SJQDDY9FMX]].

## Explanations

### L1 human

Each line measurement of a scanner says how much material lies along that line, but not where on the line.
Back-projection smears each measured value back uniformly along its line.
Adding the smears of all lines through a point gives the value of the dual transform there.
For example, if every line carries the value $1$, then every point receives the same total.
The resulting picture is a blurred version of the true one, and a filter removes the blur.
