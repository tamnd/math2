---
tag: 9MB4JD02YF
kind: definition
name: Nuclear C*-algebra
msc: [46L06, 46L05]
defines: D2M4VXJ7PA
uses: [1735VGRT2P, CGY299QMC3]
sources:
  - url: https://en.wikipedia.org/wiki/Nuclear_C*-algebra
---

## Definition

Let $A$ be a [[C*-algebra|M2WFY1D3SZ]].
For a C\*-algebra $B$, let $A \odot B$ be the algebraic [[tensor product|1735VGRT2P]] of $A$ and $B$, a $*$-algebra with $(a \otimes b)^* = a^* \otimes b^*$.
A *C\*-norm* on $A \odot B$ is a norm $\gamma$ with $\gamma(xy) \le \gamma(x) \gamma(y)$, $\gamma(x^*) = \gamma(x)$ and $\gamma(x^* x) = \gamma(x)^2$.
The algebra $A$ is *nuclear* if, for every C\*-algebra $B$, there is exactly one C\*-norm on $A \odot B$.

## Remarks

There is always a smallest C\*-norm $\norm{\cdot}_{\min}$ and a largest $\norm{\cdot}_{\max}$, so $A$ is nuclear when $\norm{\cdot}_{\min} = \norm{\cdot}_{\max}$ on $A \odot B$ for all $B$.
By theorems of Choi–Effros and Kirchberg, $A$ is nuclear if and only if it has the completely positive approximation property.
This means that there are nets of [[completely positive|CGY299QMC3]] contractions $\varphi_\lambda \colon A \to M_{n_\lambda}(\C)$ and $\psi_\lambda \colon M_{n_\lambda}(\C) \to A$ with $\psi_\lambda(\varphi_\lambda(a)) \to a$ in norm for every $a \in A$.
A C\*-algebra is nuclear if and only if it is an [[amenable Banach algebra|6P9AE21Q7X]].

Example: $M_n(\C)$ is nuclear.
Take $\varphi_\lambda = \psi_\lambda$ equal to the identity map of $M_n(\C)$, which is completely positive and contractive.
Then $\psi_\lambda(\varphi_\lambda(a)) = a$, so the completely positive approximation property holds.
Commutative C\*-algebras and [[AF algebras|4Y7VENNBVK]] are also nuclear.

Non-example: let $\mathbb{F}_2$ be the free group on two generators.
For a discrete group $G$, the reduced group C*-algebra $C^*_r(G)$ is nuclear if and only if $G$ is amenable; since $\mathbb{F}_2$ is not amenable, $C^*_r(\mathbb{F}_2)$ is not nuclear.
The algebra $B(H)$ of all bounded operators on an infinite-dimensional Hilbert space is not nuclear either.
