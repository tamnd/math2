---
tag: 5TKBSHY6VC
kind: example
name: Geodesic flow on a locally symmetric space
msc: ["37D40", "22E40", "53C35"]
instance_of: [96B4E2GPKJ]
illustrates: [NSYMQMHPDN]
uses: [BTYF5Y5PFY, DQB1BVQJWD, VEKV1EM77B]
sources:
  - url: https://en.wikipedia.org/wiki/Geodesic
---

## Example

Let $G = \mathrm{PSL}_2(\R)$, acting on the upper half-plane $\mathbb{H} = \set{z \in \C : \operatorname{Im} z > 0}$ by Möbius transformations $z \mapsto (az + b)/(cz + d)$.
These maps are the orientation-preserving isometries of the hyperbolic metric $\abs{dz}/\operatorname{Im} z$.
The action of $G$ on the unit [[tangent bundle|DQB1BVQJWD]] $T^1\mathbb{H}$ is free and transitive.
Let $v_0$ be the upward unit vector at $i$; then $g \mapsto g \cdot v_0$ identifies $G$ with $T^1\mathbb{H}$.
For $t \in \R$ let $a_t$ be the class of $\begin{pmatrix} e^{t/2} & 0 \\ 0 & e^{-t/2} \end{pmatrix}$.
Then $a_t \cdot i = e^t i$, and the path $t \mapsto e^t i$ is the unit-speed [[geodesic|NSYMQMHPDN]] through $v_0$, since the hyperbolic distance from $i$ to $e^t i$ is $t$ for $t \ge 0$.
As $g$ is an isometry, $g a_t \cdot v_0$ is the unit vector reached after time $t$ along the geodesic starting at $g \cdot v_0$.
So the geodesic flow on $T^1\mathbb{H}$ is the right multiplication $g \mapsto g a_t$.

Now let $\Gamma$ be a [[lattice|BTYF5Y5PFY]] in $G$, for example the [[modular group|VEKV1EM77B]] or a torsion-free cocompact lattice.
Left multiplication by $\Gamma$ commutes with right multiplication by $a_t$.
So the flow descends to $\Gamma \backslash G$, which is the unit tangent bundle of the locally symmetric surface $\Gamma \backslash \mathbb{H}$ when $\Gamma$ is torsion-free.
It is an action of the Lie group $\R$ on $\Gamma \backslash G$.
The same recipe works for a quotient $\Gamma \backslash G / K$ of a Riemannian symmetric space $G/K$.
There geodesics are orbits of one-parameter subgroups, and the flow becomes right multiplication on a homogeneous space of $G$.

## Explanations

### L1 human

On a curved surface, a geodesic flow moves every direction arrow forward along its straightest path at unit speed.
On a hyperbolic surface built from the group $\mathrm{PSL}_2(\R)$, this complicated-looking motion is just multiplication on the right by a diagonal matrix.
That turns a question in geometry into a question about groups.
Facts about group actions, such as their mixing behaviour, then say how geodesics wander over the surface.
