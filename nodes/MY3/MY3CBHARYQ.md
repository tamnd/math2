---
tag: MY3CBHARYQ
kind: example
name: Wallpaper group
msc: [20H15, 52C22]
instance_of: [7KTJKFQT2N]
sources:
  - url: https://en.wikipedia.org/wiki/Wallpaper_group
---

## Example

A wallpaper group is a [[crystallographic group|7KTJKFQT2N]] of dimension $2$: a discrete group of isometries of the plane $\R^2$ with compact quotient.
A concrete one, called $p4$, is the group $\Gamma$ of all maps
$$v \mapsto R^k v + t, \qquad k \in \set{0, 1, 2, 3}, \ t \in \Z^2,$$
where $R(x, y) = (-y, x)$ is the rotation by a quarter turn about the origin.
The set $\Gamma$ is a group, because $R$ maps $\Z^2$ onto itself, so composites and inverses of such maps have the same form.
It is discrete, because its elements have only four linear parts and their translation parts lie in $\Z^2$.
The quotient is compact, because every orbit meets the unit square $[0, 1]^2$, already under the translations alone.
The translation subgroup is $\Z^2$, of index $4$, as part 1 of the [[Bieberbach theorems|YE87R5CDJY]] predicts.

## Remarks

Up to isomorphism, and also up to affine change of coordinates, there are exactly $17$ wallpaper groups.

## Explanations

### L1 human

A wallpaper group is the symmetry group of a pattern that repeats in two directions across the whole plane, like tiles on a bathroom floor.
The pattern $p4$ is a grid of square tiles each marked with a pinwheel, so it can be turned by a quarter turn but not reflected.
Although such patterns come in endless designs, only $17$ different symmetry groups occur.
