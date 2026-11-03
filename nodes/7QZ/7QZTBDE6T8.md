---
tag: 7QZTBDE6T8
kind: definition
name: Real form
msc: ["17B20", "22E60"]
defines: 59DHW3BZTW
uses: [5JJYBJ6A8K, WKSSTQ69AK, 0XYYT5KNTX]
sources:
  - url: https://en.wikipedia.org/wiki/Real_form_(Lie_theory)
---

## Definition

Let $\mathfrak{g}$ be a [[Lie algebra|5JJYBJ6A8K]] over $\C$, and view it also as a Lie algebra over $\R$ by restriction of scalars.
A *real form* of $\mathfrak{g}$ is a real [[Lie subalgebra|WKSSTQ69AK]] $\mathfrak{g}_0 \subseteq \mathfrak{g}$ such that $\mathfrak{g} = \mathfrak{g}_0 \oplus i\mathfrak{g}_0$ as a [[direct sum|0XYYT5KNTX]] of real vector spaces.

## Remarks

Equivalently, the $\C$-linear map $\mathfrak{g}_0 \otimes_\R \C \to \mathfrak{g}$, $X \otimes z \mapsto zX$, is an isomorphism of complex Lie algebras.
Equivalently again, $\mathfrak{g}_0$ is the set of fixed points of a conjugation of $\mathfrak{g}$: a map $\sigma$ that is additive, satisfies $\sigma(zX) = \bar z \sigma(X)$, preserves brackets and has $\sigma^2 = \id$.
Example: $\mathfrak{sl}_2(\R)$ is a real form of $\mathfrak{sl}_2(\C)$; it is closed under brackets, and each complex matrix of trace $0$ is uniquely $X + iY$ with $X, Y$ real of trace $0$.
Non-example: $i\,\mathfrak{sl}_2(\R)$ satisfies the direct sum condition but is not a subalgebra, since $[ih, ie] = -[h, e] = -2e$ is real, where $h = \operatorname{diag}(1, -1)$ and $e = E_{12}$.
Real forms of Lie groups, see [[real form of a Lie group|SADNTQAY3G]], have real forms of Lie algebras as their Lie algebras.

## Explanations

### L1 human

A real form is a real Lie algebra inside a complex one that gives back the complex one when the scalars are extended to $\C$.
Different real forms of the same complex algebra can behave very differently, for example one compact and one not.
