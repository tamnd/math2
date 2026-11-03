---
tag: 1F6MQZQ7AQ
kind: definition
name: Fourier–Stieltjes algebra
msc: [43A30, 43A35, 22D25]
defines: R8K5VH1E8K
uses: [AHV05ZBCYW, 74BPYJNZTM, JKANN4VBYH, 3PRZ02APFA, 3JA4EF163Q]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_algebra
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]].
The *Fourier–Stieltjes algebra* $B(G)$ is the set of functions $u \colon G \to \C$ of the form $u(x) = \ip{\pi(x)\xi}{\eta}$ for $x \in G$.
Here $\pi$ is a continuous [[unitary representation|74BPYJNZTM]] of $G$ on a Hilbert space $H$ and $\xi, \eta \in H$.
The norm is $\norm{u}_B = \inf \norm{\xi} \norm{\eta}$ over all such representations of $u$.
The operations are pointwise addition and multiplication.

## Remarks

The set $B(G)$ is closed under sums, by using direct sums of representations, and under products, by using tensor products.
With the norm $\norm{\cdot}_B$ it is a commutative Banach algebra with unit the constant function $1$, coming from the trivial representation.
Pairing $u$ with $f \in L^1(G)$ by $\int_G f u$ identifies $B(G)$ isometrically with the dual of the full [[group C*-algebra|JKANN4VBYH]] $C^*(G)$.
It is the linear span of the continuous [[positive-definite functions|3PRZ02APFA]] on $G$.
The [[Fourier algebra|3JA4EF163Q]] $A(G)$ is a closed ideal of $B(G)$, and $A(G) = B(G)$ exactly when $G$ is compact.

Example: $G = \Z$.
A unitary representation of $\Z$ is given by one unitary operator $U = \pi(1)$.
By the spectral theorem, $\ip{U^n \xi}{\eta} = \int_{\mathbb{T}} z^n \, d\mu(z)$ for a finite complex measure $\mu$ on the circle, and every finite measure arises in this way.
So $B(\Z)$ is the algebra of Fourier–Stieltjes coefficient sequences of finite measures on $\mathbb{T}$.

Non-example: the function $u(n) = 2^n$ on $\Z$ is not in $B(\Z)$.
Every coefficient function is bounded, since $\abs{\ip{\pi(x)\xi}{\eta}} \le \norm{\xi}\norm{\eta}$, and $u$ is unbounded.
