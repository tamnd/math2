---
tag: VBVHWV9WCW
kind: definition
name: Minkowski space
msc: [83A05, 53B30, 53C50]
defines: G49G4R1K04
uses: [000AYPA9AJ, 0AXZNE5XNH, 01NHFZF2SK, 07EZA80NEH]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski_space
---

## Definition

*Minkowski space* is a pair $(V, \eta)$ where:

1. $V$ is a real [[vector space|000AYPA9AJ]] of dimension $4$;
2. $\eta \colon V \times V \to \R$ is a [[symmetric bilinear form|0AXZNE5XNH]];
3. $\eta$ is [[nondegenerate|01NHFZF2SK]] and has [[signature|07EZA80NEH]] $(1, 3)$, that is, one negative and three positive directions.

The form $\eta$ is the *Minkowski metric*.
Every such space has a basis $e_0, e_1, e_2, e_3$ with $\eta(e_\mu, e_\nu) = \eta_{\mu\nu}$, where $(\eta_{\mu\nu}) = \operatorname{diag}(-1, 1, 1, 1)$.
In such a basis, for $x = \sum_\mu x^\mu e_\mu$ and $y = \sum_\mu y^\mu e_\mu$,
$$\eta(x, y) = -x^0 y^0 + x^1 y^1 + x^2 y^2 + x^3 y^3.$$

## Remarks

Example: $\R^4$ with $\eta(x, y) = -x^0 y^0 + x^1 y^1 + x^2 y^2 + x^3 y^3$ is Minkowski space, written $\R^{1,3}$.
Check: $\eta$ is symmetric and bilinear, its matrix $\operatorname{diag}(-1, 1, 1, 1)$ is invertible, so $\eta$ is nondegenerate, and it has one negative and three positive eigenvalues.
Non-example: $\R^4$ with $-x^0 y^0 - x^1 y^1 + x^2 y^2 + x^3 y^3$ fails clause 3, since its signature is $(2, 2)$.
Many physics texts use the opposite sign convention $\operatorname{diag}(1, -1, -1, -1)$.
Often Minkowski space means the affine space of events whose translation space is $(V, \eta)$; it is then a flat Lorentzian manifold.
A vector $x$ is *timelike* if $\eta(x, x) < 0$, *null* (or lightlike) if $\eta(x, x) = 0$ and $x \ne 0$, and *spacelike* if $\eta(x, x) > 0$.
In physics $x^0 = ct$, where $t$ is time and $c$ is the speed of light.
