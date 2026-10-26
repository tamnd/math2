---
tag: 0N67NBKQ5T
kind: definition
name: Vector field
msc: [26B12]
defines: 0299VCW1TH
uses: [018GTRS7A4, 0S9EK5MQPE, 0TCBZMEYGN]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_field
    locator: Vector fields on subsets of Euclidean space
  - url: https://en.wikipedia.org/wiki/Vector_field
    locator: Examples
---

## Definition

Let $S \subseteq \mathbb{R}^n$.
A vector field on $S$ is a [[vector-valued function|018GTRS7A4]] $F \colon S \to \mathbb{R}^n$, $F(x) = (F_1(x), \dots, F_n(x))$.
The vector field is continuous, or of class $C^k$, if each component $F_i$ is [[continuous|0S9EK5MQPE]], or of [[class C^k|0TCBZMEYGN]], on $S$.

## Remarks

One pictures $F$ by an arrow $F(x)$ drawn with its tail at the point $x$.
For a differentiable function $f \colon U \to \mathbb{R}$ on an open set $U$, the gradient $\nabla f$ is a vector field on $U$. Such fields are gradient fields.
The field $F(x, y) = (-y, x)$ on $\mathbb{R}^2$ describes a counterclockwise rotation about the origin. The field $F(x) = x$ points away from the origin.
In $\mathbb{R}^3$ one often writes $F = P \, \mathbf{i} + Q \, \mathbf{j} + R \, \mathbf{k}$, with $P$, $Q$, $R$ the components of $F$.

## Explanations

### L1 human

A vector field attaches an arrow to each point.
Think of the wind on a weather map: at each place there is a wind direction and a wind speed.
