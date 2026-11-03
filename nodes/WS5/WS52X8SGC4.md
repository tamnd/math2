---
tag: WS52X8SGC4
kind: statement
role: proposition
name: Rodrigues' rotation formula
msc: [70B10, 15B10]
uses: [0XNZWJ96HK, 0SEDGXG9S3, 05HQYM0R4G, 03RNVFDEAN, 020M04FN1H]
about: [0HFREYRSZP]
sources:
  - url: https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula
same_as:
  wikidata: Q1473494
  wikipedia: Rodrigues' rotation formula
---

## Statement

Let $k \in \R^3$ be a unit vector and let $\theta \in \R$.
Let $R$ be the [[rotation|0XNZWJ96HK]] of $\R^3$ by the angle $\theta$ about the axis $\R k$, oriented by the right-hand rule.
Then for every $v \in \R^3$,
$$R v = v \cos\theta + (k \times v) \sin\theta + k\, (k \cdot v)(1 - \cos\theta),$$
where $\times$ is the [[cross product|0SEDGXG9S3]] and $\cdot$ is the [[dot product|05HQYM0R4G]].
In matrix form, with the [[skew-symmetric matrix|03RNVFDEAN]]
$$K = \begin{pmatrix} 0 & -k_3 & k_2 \\ k_3 & 0 & -k_1 \\ -k_2 & k_1 & 0 \end{pmatrix}$$
that satisfies $K v = k \times v$, one has
$$R = I + (\sin\theta)\, K + (1 - \cos\theta)\, K^2.$$

## Remarks

Proof idea: split $v = v_\parallel + v_\perp$ with $v_\parallel = (k \cdot v) k$ along the axis and $v_\perp$ orthogonal to it.
The rotation fixes $v_\parallel$ and turns $v_\perp$ in the plane spanned by $v_\perp$ and $k \times v_\perp = k \times v$, giving $v_\perp \cos\theta + (k \times v)\sin\theta$.
Adding the two parts and using $v_\perp = v - (k \cdot v) k$ gives the formula.
The matrix form follows from $K^2 v = k \times (k \times v) = (k \cdot v) k - v$.

Example: for $k = e_3$ and $v = e_1$, the formula gives $R e_1 = (\cos\theta, \sin\theta, 0)$, the familiar plane rotation.

Since $K^3 = -K$, the matrix form equals the [[matrix exponential|020M04FN1H]] $e^{\theta K}$.
The vector $k$ must be a unit vector; for a general nonzero axis vector one first divides by its length.

## Explanations

### L1 human

If you know the axis and the angle of a turn, this formula tells you where every vector goes.
The part of the vector along the axis stays put.
The part across the axis turns in a circle, and the formula writes that circle with a cosine and a sine.

### L2 human

[[Euler's rotation theorem|2ZVG43GSKA]] says every rotation has an axis and an angle; Rodrigues' formula goes back from axis and angle to the matrix.
It shows that $SO(3)$ is the image of the exponential map on skew-symmetric matrices, the Lie algebra $\mathfrak{so}(3)$.
It is the basic tool for integrating constant [[angular velocity|2FTZ7D8Z0F]] and appears in robotics and computer graphics.
The same rotation can be computed with [[unit quaternions|EAK8KT5AMD]].
