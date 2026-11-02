---
tag: PWDQ80EKZ8
kind: definition
name: Antipode
msc: [16T05]
defines: PG3ECG5D0G
uses: [Q9HHVN606G, 0NRYHJPQG2]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_algebra
---

## Definition

Let $K$ be a field and let $(H, m, \eta, \Delta, \varepsilon)$ be a [[bialgebra|Q9HHVN606G]] over $K$.
An *antipode* for $H$ is a [[linear map|0NRYHJPQG2]] $S \colon H \to H$ such that
$$m \circ (S \otimes \id_H) \circ \Delta = \eta \circ \varepsilon = m \circ (\id_H \otimes S) \circ \Delta.$$

## Remarks

The *convolution* of linear maps $f, g \colon H \to H$ is $f * g = m \circ (f \otimes g) \circ \Delta$.
It makes $\End_K(H)$ an associative algebra with identity $\eta \circ \varepsilon$, and the condition says $S * \id_H = \eta \circ \varepsilon = \id_H * S$.
So $S$ is a two-sided inverse of $\id_H$, and an antipode is unique when it exists.
Example: $H = K[x]$ with $\Delta(x) = x \otimes 1 + 1 \otimes x$ and $\varepsilon(x) = 0$ has the antipode $S(x^n) = (-x)^n$.
On $x$ the check is $S(x) \cdot 1 + S(1) \cdot x = -x + x = 0 = \varepsilon(x) 1$.
Non-example: the identity map of $K[x]$ is not an antipode, since $m(\id \otimes \id)\Delta(x) = 2x \ne 0$ when the characteristic of $K$ is not $2$.
An antipode is an algebra anti-homomorphism, $S(ab) = S(b)S(a)$, and a coalgebra anti-homomorphism.
If $H$ is commutative or cocommutative, then $S \circ S = \id_H$.
