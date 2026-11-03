---
tag: CRQS38F4WZ
kind: statement
role: theorem
name: Real solutions from a complex eigenpair of a real matrix
msc: [34A30, 15A18]
uses: [0VJF99CZ0Z, 0N6960W0BV, 0FTH2E9TAS, 06J8TEPJPY, 08ZWFDJP3H]
sources:
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-systems.tex#L2634
    locator: ch-systems.tex:2634
---

## Statement

Let $P$ be a square matrix with real entries. Suppose $a + ib$ is a non-real eigenvalue of $P$, with $a, b \in \mathbb{R}$ and $b \ne 0$, and let $\vec{v}$ be an [[eigenvector|0N6960W0BV]] for it.

Then the [[complex conjugate|0FTH2E9TAS]] $a - ib$ is also an eigenvalue of $P$, and the conjugate vector $\overline{\vec{v}}$ is an eigenvector for it.

Moreover, the system $\vec{x}' = P\vec{x}$ has two linearly independent real-valued solutions. They are the [[real part and the imaginary part|06J8TEPJPY]] of the complex solution $\vec{v}\, e^{(a+ib)t}$:

$$\vec{x}_1 = \operatorname{Re}\big(\vec{v}\, e^{(a+ib)t}\big), \qquad \vec{x}_2 = \operatorname{Im}\big(\vec{v}\, e^{(a+ib)t}\big).$$

## Remarks

Conjugating $P\vec{v} = (a+ib)\vec{v}$ gives the first claim, because $P$ is real. The function $\vec{v}\, e^{(a+ib)t}$ solves the [[constant coefficient system|0VJF99CZ0Z]], and so do its real and imaginary parts, since $P$ is real. This is the complex case of the [[eigenvalue method|08ZWFDJP3H]].
