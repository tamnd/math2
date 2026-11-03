---
tag: TGKMS42HA0
kind: conjecture
name: Global spherical shell conjecture
msc: [32J15, 32Q57]
uses: [Y4NSSJT4RC, JSGWAN2RJV, ST71ZV3FES, P9CM4GQ2T0]
about: [Y4NSSJT4RC]
sources:
  - url: https://en.wikipedia.org/wiki/Surface_of_class_VII
history:
  posed_by: "Iku Nakamura"
---

## Statement

Let $X$ be a compact complex surface, that is, a compact connected [[complex manifold|JSGWAN2RJV]] of complex dimension $2$.
Let $S^3 = \set{z \in \C^2 : \abs{z} = 1}$ be the unit [[sphere|P9CM4GQ2T0]].
A *global spherical shell* in $X$ is a holomorphic embedding $\iota \colon V \to X$ of an open neighbourhood $V$ of $S^3$ in $\C^2 \setminus \set{0}$ such that $X \setminus \iota(S^3)$ is connected.
The conjecture: every minimal [[surface of class VII|Y4NSSJT4RC]] whose second [[Betti number|ST71ZV3FES]] satisfies $b_2(X) > 0$ contains a global spherical shell.

## Remarks

Minimal means that $X$ contains no smooth rational curve of self-intersection $-1$.
Surfaces that contain a global spherical shell were introduced by Kato and are called Kato surfaces.
A primary [[Hopf surface|PNFNGBXRM3]] contains a global spherical shell, and it has $b_2 = 0$.
For $b_2 = 0$ the minimal class VII surfaces are known: they are the Hopf surfaces and the [[Inoue surfaces|GPSVJK3R4X]].
Teleman proved the conjecture for $b_2 = 1$, using gauge theory.
The general case is open.
If true, the conjecture would reduce the classification of minimal class VII surfaces with $b_2 > 0$ to that of Kato surfaces, which are much better understood.

## Explanations

### L1 human

Class VII surfaces are the compact complex surfaces with first Betti number $1$ and Kodaira dimension $-\infty$.
They are the surfaces that the Kodaira classification leaves least understood.
A global spherical shell is a thin shell around a 3-sphere, cut out of $\C^2$, that sits inside the surface without separating it.
Surfaces with such a shell can be built by hand: take a ball, blow up some points, remove a smaller ball, and glue the two boundary spheres.
The conjecture says that every minimal class VII surface with $b_2 > 0$ arises in this way.
