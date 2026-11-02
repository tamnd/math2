---
tag: JJSXXJQGEH
kind: example
name: Spin group
msc: ["22E15", "15A66", "22C05"]
instance_of: [9TFC6ADC1C]
uses: [A38B1QFK20, 0CGYNDCWRR, 3XZRRE165N, E5P8AG6CK7]
sources:
  - url: https://en.wikipedia.org/wiki/Spin_group
same_as:
  wikidata: Q2031467
  wikipedia: Spin group
---

## Example

Let $n \ge 2$ and let $\mathrm{Cl}_n$ be the real [[Clifford algebra|A38B1QFK20]] of $\R^n$ with the relations $v^2 = -\abs{v}^2$ for $v \in \R^n$.
The *spin group* $\mathrm{Spin}(n)$ is the set of products $u_1 u_2 \cdots u_{2k}$ in $\mathrm{Cl}_n$ of an even number of unit vectors $u_i \in \R^n$, with the Clifford product.
It is a group: the product of two such elements is again one.
The inverse of $u_1 \cdots u_{2k}$ is $u_{2k} \cdots u_1$, because $u_i u_i = -1$ and the number of factors is even.

For $x \in \mathrm{Spin}(n)$ and $v \in \R^n$, the element $x v x^{-1}$ lies again in $\R^n$.
Check for one unit vector $u$: $u^{-1} = -u$, and $uv = -vu$ when $v \perp u$.
So $-u v u^{-1}$ equals $v$ for $v \perp u$ and $-u$ for $v = u$, and $v \mapsto -u v u^{-1}$ is the reflection $r_u$ of $\R^n$ in the hyperplane $u^\perp$.
For $x = u_1 \cdots u_{2k}$ the signs cancel, and $v \mapsto x v x^{-1}$ is the product $r_{u_1} \cdots r_{u_{2k}}$ of $2k$ reflections, which lies in [[SO(n)|0CGYNDCWRR]].

This gives a homomorphism $\rho \colon \mathrm{Spin}(n) \to SO(n)$, $\rho(x)(v) = x v x^{-1}$.
It is surjective, because every element of $SO(n)$ is a product of an even number of reflections, and its kernel is $\set{1, -1}$.

## Remarks

$\mathrm{Spin}(n)$ is a compact connected Lie group, and $\rho$ is a two-sheeted [[covering map|3XZRRE165N]].
For $n \ge 3$ the group $\mathrm{Spin}(n)$ is simply connected, so it is the universal cover of $SO(n)$.
For $n = 2$ the group $\mathrm{Spin}(2)$ is a circle, and $\rho$ is the double cover $z \mapsto z^2$ of the circle $SO(2)$.
In low dimensions there are isomorphisms $\mathrm{Spin}(3) \cong$ [[SU(2)|E5P8AG6CK7]], $\mathrm{Spin}(4) \cong SU(2) \times SU(2)$, $\mathrm{Spin}(5) \cong \mathrm{Sp}(2)$ and $\mathrm{Spin}(6) \cong SU(4)$.
The same construction for a quadratic form of signature $(p, q)$ gives the groups $\mathrm{Spin}(p, q)$.

## Explanations

### L1 human

The spin group is a twofold cover of the rotation group: each rotation corresponds to exactly two elements of $\mathrm{Spin}(n)$, which differ by a sign.
It is built from products of unit vectors in the Clifford algebra, in which a vector squares to minus its length squared.
Each unit vector stands for a reflection, and a product of an even number of reflections is a rotation.
Physicists need the spin group because electrons and other spin $1/2$ particles change sign under a full turn, so they transform under $\mathrm{Spin}(3)$ rather than $SO(3)$.
