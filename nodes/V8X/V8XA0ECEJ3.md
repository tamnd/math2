---
tag: V8XA0ECEJ3
kind: definition
name: Householder transformation
msc: [65F25, 15A23]
defines: JDH0THTVGM
uses: [025158VEYZ, 0QRBVFJ50X, 0D6RMJ10M9, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Householder_transformation
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $v \in \mathbb{K}^n$ be a vector with $v^* v = 1$, where $v^*$ is the [[conjugate transpose|0EX045E2BP]] of $v$.
The *Householder transformation* (or *Householder reflector*) defined by $v$ is the $n \times n$ matrix
$$P = I - 2 v v^*.$$

## Remarks

$P$ is Hermitian and [[unitary|0D6RMJ10M9]], and $P^2 = I$; for $\mathbb{K} = \R$ it is a symmetric [[orthogonal matrix|0QRBVFJ50X]] with determinant $-1$.
It fixes every vector orthogonal to $v$ and sends $v$ to $-v$, so it is the [[reflection|025158VEYZ]] in the hyperplane $v^\perp$.
If $x, y \in \R^n$ are distinct with $\norm{x} = \norm{y}$, then $v = (x - y)/\norm{x - y}$ gives $P x = y$.
Example: in $\R^2$, take $x = (3, 4)$ and $y = (5, 0)$; then $v = (-2, 4)/\sqrt{20}$, and
$$P = I - \frac{2}{20} \begin{pmatrix} 4 & -8 \\ -8 & 16 \end{pmatrix} = \frac{1}{5} \begin{pmatrix} 3 & 4 \\ 4 & -3 \end{pmatrix},$$
and indeed $P (3, 4)^T = (5, 0)^T$.
Non-example: $v = (2, 0)$ is not a unit vector, and $I - 2 v v^T = \begin{pmatrix} -7 & 0 \\ 0 & 1 \end{pmatrix}$ is not orthogonal.
For a nonzero $u$ that is not normalized, one writes $P = I - 2 u u^* / (u^* u)$.
In computations, $P$ is never formed: $P A = A - 2 v (v^* A)$ costs $O(n m)$ operations for an $n \times m$ matrix $A$.

## Explanations

### L1 human

A Householder transformation is a mirror reflection written as a matrix.
The unit vector $v$ points straight out of the mirror.
Reflecting twice gives back the original vector, and lengths never change.
