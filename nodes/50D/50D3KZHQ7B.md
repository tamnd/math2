---
tag: 50D3KZHQ7B
kind: definition
name: Partial algebra
msc: [08A55]
defines: H7RX5729ZB
uses: [0SJ3RX9TXA, MSXX2P86CY, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_algebra
---

## Definition

Let $\Sigma$ be a signature, that is, a set of function symbols, each with an [[arity|MSXX2P86CY]] $n \ge 0$.
A *partial $\Sigma$-algebra* is a [[set|0SJ3RX9TXA]] $A$ with the following data for each symbol $f \in \Sigma$ of arity $n$.
It has a subset $\operatorname{dom}(f^A)$ of the [[Cartesian power|09CEDJYBKP]] $A^n$ and a map $f^A \colon \operatorname{dom}(f^A) \to A$.
The map $f^A$ is a *partial operation* on $A$, and $f^A(a_1, \dots, a_n)$ is defined exactly when $(a_1, \dots, a_n) \in \operatorname{dom}(f^A)$.

## Remarks

When $\operatorname{dom}(f^A) = A^n$ for every $f$, the partial algebra is an ordinary (total) algebra.

Example: the natural numbers $\N$ with subtraction, where $m - n$ is defined exactly when $m \ge n$.
The domain is $\set{(m, n) \in \N^2 : m \ge n}$, and on it $m - n \in \N$, so subtraction is a partial operation on $\N$.
It is not total, since $(0, 1)$ is not in its domain.

Non-example: subtraction on all of $\N^2$ with values in $\Z$ is not a partial operation on $\N$, since its value $0 - 1 = -1$ does not lie in the carrier $\N$.

A field $K$ with the partial operation $x \mapsto x^{-1}$ defined on $K \setminus \set{0}$ is a partial algebra for the signature $\set{+, \cdot, -, ^{-1}, 0, 1}$.
Homomorphisms, subalgebras and congruences admit several inequivalent versions for partial algebras, for example weak and strong homomorphisms, so the version in use must be stated.
