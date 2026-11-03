---
tag: DGC6BEAEEP
kind: definition
name: Matrix coefficient
msc: ["22D10", "43A65", "22C05"]
defines: J85Q7QGGHS
uses: [G5S1M9, WYGRXCG2RN, 74BPYJNZTM, HM2HHE3J51, 07JBSZE0V4]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_coefficient
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $\pi$ be a [[representation|WYGRXCG2RN]] of $G$ on a complex vector space $V$.
Let $v \in V$, and let $\ell$ be a linear functional on $V$, taken continuous when $V$ is a topological vector space.
The *matrix coefficient* of $\pi$ attached to $v$ and $\ell$ is the function $c_{v, \ell} \colon G \to \C$ given by
$$c_{v, \ell}(g) = \ell(\pi(g) v).$$
When $\pi$ is a [[unitary representation|74BPYJNZTM]] on a [[Hilbert space|HM2HHE3J51]] $\mathcal{H}$, one usually takes $\ell = \ip{\cdot}{w}$, so that $c_{v, w}(g) = \ip{\pi(g) v}{w}$ for $v, w \in \mathcal{H}$.

## Remarks

If $\dim V = n$ and $e_1, \dots, e_n$ is a basis with dual basis $e_1^*, \dots, e_n^*$ in the [[dual space|07JBSZE0V4]], then $\pi_{ij}(g) = e_i^*(\pi(g) e_j)$ is the $(i, j)$ entry of the matrix of $\pi(g)$.
Every matrix coefficient of $\pi$ is a linear combination of the $\pi_{ij}$, because $c_{v, \ell}$ is linear in $v$ and in $\ell$.
The left and right translates of a matrix coefficient of $\pi$ are again matrix coefficients of $\pi$: $c_{v, \ell}(h g) = c_{\pi(g) v, \ell}(h)$.

Example: let $G = \mathrm{SO}(2)$ act on $\R^2 \subset \C^2$ by rotations $r_\theta = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$.
With $v = e_1$ and $\ell = e_2^*$, the matrix coefficient is $\theta \mapsto \sin \theta$.

Non-example: on the circle group $\R / 2\pi\Z$, the matrix coefficients of the finite-dimensional continuous representations are exactly the trigonometric polynomials.
The function $\theta \mapsto \abs{\sin \theta}$ has infinitely many nonzero Fourier coefficients, so it is not a matrix coefficient of any finite-dimensional continuous representation.
