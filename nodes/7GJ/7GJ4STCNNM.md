---
tag: 7GJ4STCNNM
kind: example
name: Complex projective space
msc: [32Q99, 51N15, 14N05]
instance_of: [JSGWAN2RJV]
uses: [ZT9A6JK8QF, 0BR3FY5Q8M, 0TVJZYB6SH]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_projective_space
same_as:
  wikidata: Q2538404
  wikipedia: Complex projective space
---

## Example

Let $n \ge 1$.
*Complex projective space* $\mathbb{CP}^n$ is the [[quotient|0BR3FY5Q8M]] of $\C^{n+1} \setminus \set{0}$ by the relation $z \sim \lambda z$ for $\lambda \in \C \setminus \set{0}$; the class of $z = (z_0, \ldots, z_n)$ is written $[z_0 : \cdots : z_n]$.
So $\mathbb{CP}^n$ is the set of complex lines through $0$ in $\C^{n+1}$.

It is a [[complex manifold|JSGWAN2RJV]] of dimension $n$.
For $i = 0, \ldots, n$, let $U_i = \set{[z] : z_i \ne 0}$ and $\varphi_i[z] = (z_0/z_i, \ldots, \widehat{z_i/z_i}, \ldots, z_n/z_i) \in \C^n$, where the hat means that the entry is left out.
Each $\varphi_i$ is a well-defined homeomorphism of $U_i$ onto $\C^n$, and the $U_i$ cover $\mathbb{CP}^n$.
On $\varphi_i(U_i \cap U_j)$ the coordinate $w$ that stands for $z_j/z_i$ is nonzero.
The components of the transition map $\varphi_j \circ \varphi_i^{-1}$ are $1/w$ and the other coordinates divided by $w$, so it is holomorphic.
The space is Hausdorff and [[compact|0TVJZYB6SH]]: it is the continuous image of the unit sphere $S^{2n+1} \subset \C^{n+1}$, since every line meets the sphere.

## Remarks

For $n = 1$ one gets the [[Riemann sphere|0J78KBPFZB]], and for $n = 2$ the [[complex projective plane|58WSWYBCWA]].
The map $S^{2n+1} \to \mathbb{CP}^n$ is a circle bundle, the [[Hopf fibration|M5AKNYC4QQ]] when $n = 1$.
The Fubini–Study metric makes $\mathbb{CP}^n$ a [[Kähler manifold|X60JG9AEQJ]].
By [[Chow's theorem|6EFEG5VJEF]], every closed complex submanifold of $\mathbb{CP}^n$ is a [[projective variety|A4H4CZ2V35]].
By the [[Kodaira embedding theorem|7G7CSM2NZ9]], a compact complex manifold embeds in some $\mathbb{CP}^N$ if and only if it carries a positive line bundle.
Since $\mathbb{CP}^n$ is compact and connected, its only holomorphic functions are the [[constants|2SM64J81YC]].

## Explanations

### L1 human

Complex projective space collects all complex lines through the origin of $\C^{n+1}$ into one space, each line becoming a single point.
Near any point it looks like $\C^n$: one coordinate is nonzero, and dividing by it gives $n$ complex numbers.
The points where that coordinate vanishes are the "points at infinity", and they make the space compact.
For $n = 1$ this is the Riemann sphere: the complex plane plus one point at infinity.
