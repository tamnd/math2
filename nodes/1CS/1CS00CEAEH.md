---
tag: 1CS00CEAEH
kind: definition
name: Algebraic curve
msc: [14H99]
defines: XJM2MT4S3Y
uses: [HV6YBS0YDH, 36X2WTHYCB]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_curve
---

## Definition

Let $k$ be a field.
An *algebraic curve* over $k$ is an [[algebraic variety|HV6YBS0YDH]] over $k$ of [[dimension|36X2WTHYCB]] $1$.

## Remarks

Conventions differ on whether a curve must be irreducible, reduced, projective or smooth; each text states its choice.
For an integral variety $X$ over $k$, the dimension equals the transcendence degree of its function field over $k$.
So $X$ is a curve exactly when $k(X)$ has transcendence degree $1$.
Example: the plane curve $X \colon y^2 = x^3 - x$ in $\mathbb{A}^2_k$ is a curve.
Its function field $k(x)[y]/(y^2 - x^3 + x)$ is a finite extension of $k(x)$, so it has transcendence degree $1$.
Non-example: the affine plane $\mathbb{A}^2$ has dimension $2$, and a finite set of points has dimension $0$, so neither is a curve.
Let $k$ be algebraically closed.
Then each finitely generated field extension of $k$ of transcendence degree $1$ is the function field of exactly one smooth projective curve, up to isomorphism.
