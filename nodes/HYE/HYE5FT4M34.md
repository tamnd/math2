---
tag: HYE5FT4M34
kind: example
name: Non-Desarguesian plane
msc: [51A35, "51E15"]
instance_of: [DANFNN8C4Y]
not_instance_of:
  - target: HPX85PA8NX
    note: Desargues's theorem fails for two triangles in perspective
uses: [5Z19Y02MME, 3V9GYYXM1H]
sources:
  - url: https://en.wikipedia.org/wiki/Non-Desarguesian_plane
same_as:
  wikidata: Q3391357
  wikipedia: Non-Desarguesian plane
---

## Example

A *non-Desarguesian plane* is a [[projective plane|DANFNN8C4Y]] in which [[Desargues's theorem|5Z19Y02MME]] does not hold.
A concrete one is the projective completion of the [[Moulton plane|3V9GYYXM1H]].
Check: the Moulton plane has triangles $ABC$ and $A'B'C'$ in perspective from a point $O$.
In it $AB \parallel A'B'$ and $AC \parallel A'C'$, but $BC$ is not parallel to $B'C'$.
Add the line at infinity.
Then $AB \cap A'B'$ and $AC \cap A'C'$ lie on the line at infinity, but $BC \cap B'C'$ does not, so the three points are not collinear.

So this plane is not a [[Desarguesian plane|HPX85PA8NX]], and it is not isomorphic to $\mathbb{P}^2(D)$ for any division ring $D$.

## Remarks

Every projective plane of order at most $8$ is Desarguesian.
The smallest non-Desarguesian planes have order $9$.
There are exactly four projective planes of order $9$, and three of them are non-Desarguesian: the Hall plane, its dual and the Hughes plane.
The [[octonionic projective plane|S26GYRVDR5]] is a non-Desarguesian plane that is still a [[Moufang plane|7F4HSNJJH8]].
Every projective plane can be coordinatized by a [[planar ternary ring|Q0NXXFADT9]], which in a non-Desarguesian plane does not come from a division ring.

## Explanations

### L1 human

A projective plane only has to obey a few rules about points and lines.
One might expect that these rules force the plane to look like the usual plane built from numbers.
Non-Desarguesian planes show that this is false: they obey the rules, yet Desargues's theorem on triangles fails in them.
So no system of coordinates from a field, or even from a noncommutative division ring, can describe them.
