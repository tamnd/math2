---
tag: FQRY6M68MZ
kind: concept
name: Root pairing
msc: ["17B22", "20G07"]
sources:
  - url: https://en.wikipedia.org/wiki/Root_datum
---

## Summary

A root pairing is a family of roots in a module together with matching coroots in a dual module.
Each root and its coroot define a reflection, and these reflections permute the roots and the coroots.
It extends the notion of a root system from real Euclidean spaces to modules over any commutative ring, with no inner product.
Over the integers, with free modules of finite rank and finitely many roots, it is the same as a root datum.
Root data classify reductive algebraic groups.

## Explanations

### L1 human

In a root system the reflections come from an inner product.
A root pairing keeps the reflections but drops the inner product.
Instead, each root comes with a partner, its coroot, which lives in a dual space and tells how far to move a vector along the root.
For example, on $\Z$ with the pairing $\langle x, y \rangle = xy$, the root $1$ with coroot $2$ and the root $-1$ with coroot $-2$ form a root pairing, whose one reflection is $x \mapsto -x$.
