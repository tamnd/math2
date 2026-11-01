---
tag: 96AZPZSQKR
kind: definition
name: Quasiregular map
msc: [30C65]
defines: EGAJPZ71VW
uses: [0YF0VXKXGB, 0ZCSMYHTBP]
sources:
  - url: https://en.wikipedia.org/wiki/Quasiregular_map
---

## Definition

Let $n \ge 2$, let $\Omega \subset \R^n$ be open, and let $K \ge 1$.
A map $f \colon \Omega \to \R^n$ is *$K$-quasiregular* if:

1. $f$ is continuous.
2. $f$ lies in the Sobolev space $W^{1,n}_{\mathrm{loc}}(\Omega; \R^n)$, that is, its coordinates have locally $n$-th power integrable weak derivatives.
3. $\norm{Df(x)}^n \le K\, J_f(x)$ for almost every $x \in \Omega$.

Here $Df(x)$ is the [[Jacobian matrix|0YF0VXKXGB]] of weak derivatives, $\norm{Df(x)}$ is its operator norm, and $J_f(x) = \det Df(x)$ is the [[Jacobian determinant|0ZCSMYHTBP]].
A map is *quasiregular* if it is $K$-quasiregular for some $K \ge 1$.

## Remarks

Example: for $n = 2$, a holomorphic function $f$ on $\Omega \subset \C = \R^2$ is $1$-quasiregular.
Its Jacobian matrix is a rotation times $\abs{f'(z)}$, so $\norm{Df} = \abs{f'}$ and $J_f = \abs{f'}^2$.

Non-example: complex conjugation $f(z) = \bar z$ fails clause 3.
Here $\norm{Df} = 1$ but $J_f = -1$, so $1 \le -K$ is false.

A quasiregular homeomorphism onto its image is a [[quasiconformal map|SB8KG46NHP]].
By a theorem of Reshetnyak, a nonconstant quasiregular map is open and discrete.
