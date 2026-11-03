---
tag: 7K399CMTYJ
kind: definition
name: Derivation of a Lie algebra
msc: [17B40]
defines: 57J7MHA8CN
uses: [5JJYBJ6A8K, 0NRYHJPQG2]
sources:
  - url: https://en.wikipedia.org/wiki/Derivation_(differential_algebra)
---

## Definition

Let $\mathfrak g$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $k$.
A *derivation* of $\mathfrak g$ is a $k$-[[linear map|0NRYHJPQG2]] $D \colon \mathfrak g \to \mathfrak g$ such that
$$D[x, y] = [Dx, y] + [x, Dy] \quad \text{for all } x, y \in \mathfrak g.$$
The set of derivations of $\mathfrak g$ is written $\operatorname{Der}(\mathfrak g)$.

## Remarks

Example: for $a \in \mathfrak g$, the map $\operatorname{ad}_a(y) = [a, y]$ is a derivation.
The required identity $[a, [x, y]] = [ [a, x], y] + [x, [a, y]]$ is a form of the Jacobi identity.
Such derivations are called *inner*.

Non-example: if $\operatorname{char} k \ne 2$ and $\mathfrak g$ is not abelian, the identity map is not a derivation.
For $x, y$ with $[x, y] \ne 0$, it gives $D[x, y] = [x, y]$ but $[Dx, y] + [x, Dy] = 2[x, y]$.

If $\mathfrak g$ is abelian, every linear map is a derivation, since both sides of the rule are $0$.
If $D_1$ and $D_2$ are derivations, so is $D_1 D_2 - D_2 D_1$, hence $\operatorname{Der}(\mathfrak g)$ is a Lie subalgebra of $\mathfrak{gl}(\mathfrak g)$.
The inner derivations form an ideal of $\operatorname{Der}(\mathfrak g)$.
