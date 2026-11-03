---
tag: B75K1ZJ1RE
kind: object
name: Exceptional Lie algebra G2
msc: ["17B25", "17B20"]
instance_of: [XDAXWHBNSZ]
uses: [AVVV93CASN, H59F1XBDZP, CS73JZQS66, YT1ZJ2S4EE]
sources:
  - url: https://en.wikipedia.org/wiki/G2_(mathematics)
---

## Description

The complex Lie algebra $\mathfrak{g}_2$ is the [[simple Lie algebra|XDAXWHBNSZ]] over $\C$ whose [[root system|AVVV93CASN]] has type $G_2$.
The root system $G_2$ lies in the plane $\R^2$ and has $12$ roots.
The $6$ short roots have length $1$ and angles $0^\circ, 60^\circ, \dots, 300^\circ$ with the first axis.
The $6$ long roots have length $\sqrt{3}$ and angles $30^\circ, 90^\circ, \dots, 330^\circ$.
With a short simple root $\alpha_1$ and a long simple root $\alpha_2$ at an angle of $150^\circ$, the [[Cartan matrix|H59F1XBDZP]] with entries $\langle \alpha_i, \alpha_j \rangle$ is
$$\begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix}.$$
Check: $(\alpha_1, \alpha_2) = 1 \cdot \sqrt{3} \cdot \cos 150^\circ = -3/2$, so $\langle \alpha_1, \alpha_2 \rangle = 2(-3/2)/3 = -1$ and $\langle \alpha_2, \alpha_1 \rangle = 2(-3/2)/1 = -3$.
The rank is $2$, and the dimension is the rank plus the number of roots, $2 + 12 = 14$.

## Remarks

The [[Dynkin diagram|CS73JZQS66]] of $G_2$ has two vertices joined by a triple edge, with an arrow pointing to the short root.
The [[Weyl group|YT1ZJ2S4EE]] of $G_2$ is the dihedral group of order $12$.
The algebra $\mathfrak{g}_2$ is the Lie algebra of derivations of the complex octonions, and its smallest nontrivial representation has dimension $7$.
It is the smallest of the five exceptional simple Lie algebras; the compact Lie group of this type is the [[exceptional Lie group G2|YX5FFSCR8P]].

## Explanations

### L1 human

$\mathfrak{g}_2$ is the smallest exceptional simple Lie algebra, of dimension $14$.
Its root system is a six-pointed star of short arrows inside a larger, rotated six-pointed star of long arrows.
It is the only simple Lie algebra whose roots have length ratio $\sqrt{3}$, and it describes the symmetries of the octonions.
