---
tag: TGBB6EC1J2
kind: definition
name: Lie algebroid
msc: [53D17, 58H05, 17B66]
defines: PS9XRYDJAW
uses: [F45VQ47GPV, P4DZM975BV, WY6K3P4YCG, 68FGQEBD6J, 5JJYBJ6A8K]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebroid
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]], and let $C^\infty(M)$ be the ring of smooth real functions on $M$.
Let $A \to M$ be a smooth real [[vector bundle|P4DZM975BV]].
Write $\Gamma(A)$ for the space of smooth sections of $A$ and $TM$ for the [[tangent bundle|WY6K3P4YCG]].
A *Lie algebroid* structure on $A$ is a pair $([\cdot, \cdot], \rho)$ such that:

1. $[\cdot, \cdot]$ is a real [[Lie algebra|5JJYBJ6A8K]] bracket on $\Gamma(A)$;
2. $\rho \colon A \to TM$ is a morphism of vector bundles over the identity of $M$, called the *anchor*;
3. for all $X, Y \in \Gamma(A)$ and $f \in C^\infty(M)$, the Leibniz rule $[X, fY] = f[X, Y] + (\rho(X) f)\, Y$ holds.

Here $\rho(X)$ is the vector field $p \mapsto \rho(X_p)$, and $\rho(X) f$ is the derivative of $f$ along it.

## Remarks

Example: $A = TM$ with $\rho = \id$ and the [[Lie bracket of vector fields|68FGQEBD6J]].
Clause 3 is the identity $[X, fY] = f[X, Y] + X(f)\, Y$, which follows from the product rule when both sides act on a function.

Example: a finite-dimensional real Lie algebra $\mathfrak{g}$ is a Lie algebroid over a point, with $\rho = 0$; then $C^\infty(M) = \R$ and clause 3 is bilinearity.

Non-example: $A = TM$ with the Lie bracket of vector fields and the anchor $\rho = 0$ fails clause 3 when $\dim M \ge 1$, because $[X, fY] - f[X, Y] = X(f)\, Y$ is nonzero for suitable $X$, $Y$ and $f$.

The axioms imply that $\rho$ preserves brackets: $\rho([X, Y]) = [\rho(X), \rho(Y)]$ for all sections $X$ and $Y$.
