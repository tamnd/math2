---
tag: ET71R6CSAZ
kind: definition
name: Amenable Banach algebra
msc: [46H20, 43A07]
defines: 6P9AE21Q7X
uses: [3J89REV9WQ, 4A82S5FVRT]
sources:
  - url: https://en.wikipedia.org/wiki/Amenable_Banach_algebra
---

## Definition

Let $A$ be a complex Banach algebra.
A *Banach $A$-bimodule* is a Banach space $X$ with bounded bilinear left and right actions $A \times X \to X$ and $X \times A \to X$ that make $X$ an $A$-bimodule.
The [[dual space|4A82S5FVRT]] $X^*$ is then a Banach $A$-bimodule with $(a \cdot f)(x) = f(x \cdot a)$ and $(f \cdot a)(x) = f(a \cdot x)$ for $a \in A$, $f \in X^*$, $x \in X$.
A bounded linear map $D \colon A \to X^*$ is a *[[derivation|3J89REV9WQ]]* if $D(ab) = a \cdot D(b) + D(a) \cdot b$ for all $a, b \in A$.
It is *inner* if there is $f \in X^*$ with $D(a) = a \cdot f - f \cdot a$ for all $a \in A$.
The algebra $A$ is *amenable* if, for every Banach $A$-bimodule $X$, every bounded derivation $A \to X^*$ is inner.

## Remarks

In cohomological terms, $A$ is amenable if and only if $H^1(A, X^*) = 0$ for every Banach $A$-bimodule $X$.

Example: $A = \C$.
Let $D \colon \C \to X^*$ be a derivation and put $u = D(1)$.
From $D(1) = D(1 \cdot 1) = 1 \cdot u + u \cdot 1$ one gets $1 \cdot u \cdot 1 = 0$.
Put $f = 1 \cdot u - u \cdot 1$.
Then $1 \cdot f - f \cdot 1 = 1 \cdot u - 2 (1 \cdot u \cdot 1) + u \cdot 1 = u = D(1)$, and by linearity $D(\lambda) = \lambda \cdot f - f \cdot \lambda$ for all $\lambda \in \C$.
So every bounded derivation is inner.

Non-example: let $\mathbb{F}_2$ be the free group on two generators, which is not an [[amenable group|CEAT9BESKK]].
By Johnson's theorem, $L^1(G)$ is amenable if and only if the locally compact group $G$ is amenable.
So $\ell^1(\mathbb{F}_2)$ is not amenable: some bounded derivation into a dual bimodule is not inner.

A C*-algebra is amenable if and only if it is [[nuclear|D2M4VXJ7PA]].
