---
tag: NTQEXR0WDN
kind: definition
name: Fundamental group
msc: [55Q05, 57M05]
defines: S1XK3HXHFX
uses: [T9DG8DDE75, CCNKA8C711, G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_group
---

## Definition

Let $(X, x_0)$ be a [[pointed space|T9DG8DDE75]] and let $I = [0, 1]$.
A *loop* at $x_0$ is a continuous map $\gamma \colon I \to X$ with $\gamma(0) = \gamma(1) = x_0$.
For loops $\alpha$ and $\beta$ at $x_0$, the *concatenation* $\alpha \cdot \beta$ is the loop with $(\alpha \cdot \beta)(s) = \alpha(2s)$ for $0 \le s \le 1/2$ and $(\alpha \cdot \beta)(s) = \beta(2s - 1)$ for $1/2 \le s \le 1$.
The *fundamental group* $\pi_1(X, x_0)$ is the set of [[path homotopy|CCNKA8C711]] classes $[\gamma]$ of loops at $x_0$, with the product $[\alpha][\beta] = [\alpha \cdot \beta]$.

## Remarks

The product is well defined, and it makes $\pi_1(X, x_0)$ a [[group|G5S1M9]].
The identity is the class of the constant loop, and the inverse of $[\gamma]$ is the class of the reversed loop $s \mapsto \gamma(1 - s)$.
A pointed map $f \colon (X, x_0) \to (Y, y_0)$ induces a homomorphism $f_* \colon \pi_1(X, x_0) \to \pi_1(Y, y_0)$, $[\gamma] \mapsto [f \circ \gamma]$.
If $X$ is [[path-connected|0WB6DH499T]], the group does not depend on $x_0$ up to isomorphism.
Example: for a convex set $C \subseteq \R^n$ and $x_0 \in C$, every loop is path homotopic to the constant loop by the straight-line homotopy, so $\pi_1(C, x_0)$ is trivial.
Non-example: loops themselves, without passing to classes, do not form a group under concatenation.
Indeed $(\alpha \cdot \beta) \cdot \gamma$ and $\alpha \cdot (\beta \cdot \gamma)$ are in general different maps, which agree only up to path homotopy.
A path-connected space with trivial fundamental group is *simply connected*.
