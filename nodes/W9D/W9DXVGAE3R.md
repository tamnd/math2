---
tag: W9DXVGAE3R
kind: definition
name: Néron model
msc: [14K15, 11G10, 14L15]
defines: K0EQTBRPE3
uses: [MGM3CNJW9V, R7W03TXRS9, EXKGG9X6J0, X30G4V7VAJ, AHTE5DVX61, JDDXZ89N33]
sources:
  - url: https://en.wikipedia.org/wiki/N%C3%A9ron_model
---

## Definition

Let $R$ be a [[discrete valuation ring|MGM3CNJW9V]] with fraction field $K$.
Let $A_K$ be an [[abelian variety|R7W03TXRS9]] over $K$.
A *Néron model* of $A_K$ is an $R$-scheme $N$ with an isomorphism $N \times_R K \cong A_K$ such that:

1. $N$ is [[smooth|EXKGG9X6J0]], [[separated|X30G4V7VAJ]] and [[of finite type|AHTE5DVX61]] over $R$;
2. for every smooth $R$-scheme $Y$ and every $K$-morphism $u_K \colon Y \times_R K \to A_K$, there is a unique $R$-morphism $u \colon Y \to N$ that extends $u_K$.

Clause 2 is called the Néron mapping property.

## Remarks

A Néron model exists for every abelian variety $A_K$, and it is unique up to unique isomorphism by clause 2.
Clause 2 extends the group law of $A_K$, so $N$ is a group scheme over $R$.
Taking $Y = \operatorname{Spec} R$ in clause 2 shows that every point in $A_K(K)$ extends to a point in $N(R)$, so $N(R) = A_K(K)$.

Example: if $A_K$ extends to an [[abelian scheme|JDDXZ89N33]] $A$ over $R$, then $A$ is the Néron model of $A_K$.
This is the case of good reduction.

Non-example: let $E$ be an elliptic curve over $K$ with bad reduction, and let $W$ be the closure in $\mathbb{P}^2_R$ of a Weierstrass equation for $E$ with coefficients in $R$.
The special fibre of $W$ is a singular cubic, so $W$ is not smooth over $R$ and fails clause 1.
