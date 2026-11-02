---
tag: BMDG4JQPEH
kind: object
name: Algebra of bounded operators on a Hilbert space
msc: [47B02, 46L05]
uses: [HM2HHE3J51, 06EKW1AKXF, 6HSJBJ8TTQ]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_operator
---

## Description

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]] with inner product $\ip{\cdot}{\cdot}$.
Let $B(H)$ be the set of bounded linear operators $T \colon H \to H$, with pointwise addition and scalar multiplication, composition as product, and the [[operator norm|06EKW1AKXF]]
$$\norm{T} = \sup \set{\norm{T x} : x \in H, \norm{x} \le 1}.$$
The involution is the [[adjoint|6HSJBJ8TTQ]] $T \mapsto T^*$, defined by $\ip{T x}{y} = \ip{x}{T^* y}$ for all $x, y \in H$.
With these operations $B(H)$ is a C*-algebra with unit the identity operator.

Check: $B(H)$ is complete in the operator norm because $H$ is complete, and $\norm{S T} \le \norm{S} \norm{T}$, so it is a Banach algebra.
The adjoint is conjugate linear, satisfies $(S T)^* = T^* S^*$ and $T^{**} = T$, and $\norm{T^*} = \norm{T}$.
For the C* identity, $\norm{T x}^2 = \ip{T^* T x}{x} \le \norm{T^* T} \norm{x}^2$ gives $\norm{T}^2 \le \norm{T^* T}$, and $\norm{T^* T} \le \norm{T^*} \norm{T} = \norm{T}^2$ gives the reverse inequality.

## Remarks

If $H = \C^n$, then $B(H)$ is the algebra $M_n(\C)$ of $n \times n$ complex matrices, and $T^*$ is the conjugate transpose.
By the Gelfand–Naimark theorem every C*-algebra is isometrically $*$-isomorphic to a norm-closed $*$-subalgebra of some $B(H)$.
The algebra $B(H)$ is also a von Neumann algebra: it is closed in the weak operator topology, and its commutant consists of the scalar multiples of the identity.
If $H$ is infinite-dimensional, the compact operators form a proper closed two-sided ideal of $B(H)$, and when $H$ is separable it is the only one other than $0$ and $B(H)$.

## Explanations

### L1 human

The bounded operators on a Hilbert space are the infinite-dimensional version of square matrices.
They can be added, multiplied by composition, and they have an adjoint, the analogue of the conjugate transpose.
The size of an operator is the largest factor by which it stretches a vector.
Most of operator theory studies single elements, subalgebras or subspaces of this one algebra.
