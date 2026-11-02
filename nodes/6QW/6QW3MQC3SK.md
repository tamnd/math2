---
tag: 6QW3MQC3SK
kind: definition
name: Holomorphic automorphisms of C^n
msc: [32M17, 32H02]
defines: 2J7JB3H3FD
uses: [FX92PP3HZR, 3MQTWKBBBT, 0K1SCPBNKJ]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Definition

Let $n \ge 1$.
A *holomorphic automorphism* of $\C^n$ is a bijective [[holomorphic map|3MQTWKBBBT]] $F \colon \C^n \to \C^n$ whose inverse $F^{-1}$ is also holomorphic.
In other words, it is a [[biholomorphism|FX92PP3HZR]] of $\C^n$ onto itself.
The set of these maps, with composition as the operation, is the group $\Aut(\C^n)$.

## Remarks

Example: for an entire function $g$ on $\C$, the shear $F(z, w) = (z, w + g(z))$ is an automorphism of $\C^2$.
It is holomorphic, and $G(z, w) = (z, w - g(z))$ is holomorphic with $G \circ F = F \circ G = \id$.
Invertible affine maps $z \mapsto Az + b$, with $A$ an invertible $n \times n$ complex matrix, are automorphisms as well.

Non-example: $F(z, w) = (z, zw)$ is holomorphic on $\C^2$ but not injective, since $F(0, w) = (0, 0)$ for all $w$.

For a holomorphic map, bijectivity already implies that the inverse is holomorphic, so the last condition is automatic.
