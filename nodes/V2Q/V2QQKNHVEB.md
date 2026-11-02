---
tag: V2QQKNHVEB
kind: example
name: Pin group
msc: ["22E15", "15A66", "22C05"]
instance_of: [9TFC6ADC1C]
uses: [A38B1QFK20, 0TKYAEJ8N7, JJSXXJQGEH]
sources:
  - url: https://en.wikipedia.org/wiki/Pin_group
same_as:
  wikidata: Q7194770
  wikipedia: Pin group
---

## Example

Let $n \ge 1$, let $\varepsilon \in \set{1, -1}$, and let $\mathrm{Cl}$ be the real [[Clifford algebra|A38B1QFK20]] of $\R^n$ with the relations $v^2 = \varepsilon \abs{v}^2$ for $v \in \R^n$.
Let $\alpha$ be the automorphism of $\mathrm{Cl}$ with $\alpha(v) = -v$ for $v \in \R^n$.
The *pin group* is the set of all products $u_1 u_2 \cdots u_k$ in $\mathrm{Cl}$ of unit vectors $u_i \in \R^n$, with any number $k \ge 0$ of factors.
It is a group under the Clifford product, since $u_i^{-1} = \varepsilon u_i$.

For $x$ in the pin group and $v \in \R^n$, set $\rho(x)(v) = \alpha(x) v x^{-1}$.
Check for one unit vector $u$: $uv = -vu$ when $v \perp u$, so $\rho(u)(v) = -u v u^{-1}$ equals $v$ for $v \perp u$ and $-u$ for $v = u$.
So $\rho(u)$ is the reflection of $\R^n$ in the hyperplane $u^\perp$.
Since every element of the [[orthogonal group|0TKYAEJ8N7]] $O(n)$ is a product of reflections, $\rho$ is a surjective homomorphism onto $O(n)$, and its kernel is $\set{1, -1}$.

## Remarks

The two signs $\varepsilon = 1$ and $\varepsilon = -1$ give two groups, written $\mathrm{Pin}^+(n)$ and $\mathrm{Pin}^-(n)$, which are not isomorphic in general.
For $n = 1$, with unit vectors $\pm e_1$, one sign gives $\set{\pm 1, \pm e_1}$ with $e_1^2 = 1$, a Klein four-group, and the other gives the same set with $e_1^2 = -1$, a cyclic group of order $4$.
In both cases the products of an even number of unit vectors form the [[spin group|JJSXXJQGEH]] $\mathrm{Spin}(n)$, a subgroup of index $2$.
For $n \ge 2$ the pin groups are compact Lie groups with two connected components, and they are double covers of $O(n)$.

## Explanations

### L1 human

The pin group is to the full orthogonal group what the spin group is to the rotation group.
It doubles the group of all rotations and reflections, so that every such map corresponds to two elements that differ by a sign.
A single unit vector of the Clifford algebra stands for the reflection in the plane perpendicular to it.
Because a reflection can be lifted with either sign convention, there are two different pin groups.
