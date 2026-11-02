---
tag: MFDEMR9GMM
kind: definition
name: Configuration
msc: [05B30, 51A20, "51E30"]
defines: Q2QFXPP9EE
uses: [FGKNAFNHA3, CX07CWPCDX]
sources:
  - url: https://en.wikipedia.org/wiki/Configuration_(geometry)
---

## Definition

Let $p, \ell, \gamma, \pi$ be positive integers.
A *configuration* $(p_\gamma\ \ell_\pi)$ is a finite [[incidence structure|FGKNAFNHA3]] of points and lines such that:

1. there are $p$ points and $\ell$ lines;
2. each point lies on exactly $\gamma$ lines;
3. each line contains exactly $\pi$ points;
4. two distinct points lie on at most one common line.

## Remarks

Clause 4 says that the structure is a [[partial linear space|CX07CWPCDX]]; it is equivalent to saying that two distinct lines meet in at most one point.
Counting incident point-line pairs in two ways gives $p \gamma = \ell \pi$.
When $p = \ell$, and hence $\gamma = \pi = k$, the configuration is *symmetric* and is written $(p_k)$.
A *geometric* configuration is one whose points and lines are points and lines of the real (or another) projective plane, with incidence as in the plane.

Example: the complete quadrilateral, made of $4$ lines in the real plane with no three concurrent and their $6$ intersection points, is a $(6_2\ 4_3)$ configuration.
Each line meets the other three lines in $3$ distinct points, each point lies on $2$ of the lines, and $6 \cdot 2 = 4 \cdot 3$.

Non-example: a triangle together with one median has $4$ points and $4$ lines.
The vertex the median starts from lies on $3$ of the lines, but each other point lies on only $2$, so clause 2 fails.
