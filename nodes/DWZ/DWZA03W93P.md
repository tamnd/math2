---
tag: DWZA03W93P
kind: definition
name: C-infinity ring
msc: [58A03, 18F40, 51K10]
defines: 4EJED0YZBB
uses: [0V33BNKZ9S, F45VQ47GPV, NTJ94H2CNS, 0310REJJY8, 7SWSRGDT4A]
sources:
  - url: https://en.wikipedia.org/wiki/Synthetic_differential_geometry
---

## Definition

A *$C^\infty$-ring* is a set $A$ together with, for each $n \ge 0$ and each [[smooth function|0V33BNKZ9S]] $f \colon \R^n \to \R$, a map $\Phi_f \colon A^n \to A$, such that both conditions hold.

1. For each $n$ and each coordinate projection $\pi_i \colon \R^n \to \R$, $(x_1, \dots, x_n) \mapsto x_i$, one has $\Phi_{\pi_i}(a_1, \dots, a_n) = a_i$.
2. For smooth $f \colon \R^n \to \R$ and $g_1, \dots, g_n \colon \R^m \to \R$, and $h = f \circ (g_1, \dots, g_n)$, one has
$$\Phi_h(a) = \Phi_f\big(\Phi_{g_1}(a), \dots, \Phi_{g_n}(a)\big) \quad \text{for all } a \in A^m.$$

A morphism of $C^\infty$-rings is a map $\phi \colon A \to B$ with $\phi(\Phi_f(a_1, \dots, a_n)) = \Phi_f(\phi(a_1), \dots, \phi(a_n))$ for all $f$ and $a_i$.

## Remarks

Equivalently, a $C^\infty$-ring is a model of the [[Lawvere theory|NTJ94H2CNS]] whose $n$-ary operations are the smooth maps $\R^n \to \R$.
In other words, it is a product-preserving functor to sets from the category of the spaces $\R^n$ with smooth maps.
Using $f(x, y) = x + y$, $f(x, y) = xy$ and the constant functions, every $C^\infty$-ring is a [[commutative ring|0310REJJY8]] and an $\R$-algebra.

Example: for a [[smooth manifold|F45VQ47GPV]] $M$, let $A = C^\infty(M)$ and $\Phi_f(a_1, \dots, a_n) = f \circ (a_1, \dots, a_n)$.
Clause 1 holds since $\pi_i \circ (a_1, \dots, a_n) = a_i$, and clause 2 is associativity of composition.
The ring of [[germs of smooth functions|7SWSRGDT4A]] at a point is a $C^\infty$-ring in the same way.
The ring $\R[\varepsilon]/(\varepsilon^2)$ is a $C^\infty$-ring with $\Phi_f(a + b\varepsilon) = f(a) + f'(a) b \varepsilon$ for $n = 1$, and the analogous formula with the gradient for larger $n$; clause 2 is the chain rule.

Non-example: on $A = \R$, the rule $\Phi_f(a_1, \dots, a_n) = f(0, \dots, 0)$ fails clause 1, since $\Phi_{\pi_1}(a) = 0 \ne a$ for $a \ne 0$.
