---
tag: 26RWFX4H2H
kind: definition
name: Forgetful functor
msc: ["18A22", "08C05"]
defines: WV3BPYCHVG
uses: [A2DE66937D, 28NQ0KRHD3, KBXSZC6BV1]
sources:
  - url: https://en.wikipedia.org/wiki/Forgetful_functor
---

## Definition

Let $\sigma$ be an algebraic signature and let $K$ be a class of $\sigma$-algebras.
Let $\mathcal{K}$ be the [[category|A2DE66937D]] whose objects are the members of $K$ and whose morphisms are the [[homomorphisms|KBXSZC6BV1]] between them.
The *forgetful functor* $U \colon \mathcal{K} \to \mathbf{Set}$ is the [[functor|28NQ0KRHD3]] that sends each algebra $A$ to its underlying set.
It sends each homomorphism $f \colon A \to B$ to the same map $f$ between the underlying sets.

More generally, let $\sigma' \subseteq \sigma$.
The functor that sends a $\sigma$-algebra to its reduct to the operations of $\sigma'$, and each homomorphism to itself, is also called forgetful.

## Remarks

$U$ is a functor because the identity homomorphism is the identity map and the composite of homomorphisms is their composite as maps.
It is faithful: two homomorphisms $A \to B$ with the same underlying map are equal.

Example: the forgetful functor $\mathbf{Ring} \to \mathbf{Ab}$ keeps the addition of a ring and drops its multiplication and unit.
A ring homomorphism is additive, so it is sent to a group homomorphism.

Non-example: consider the functor $\mathbf{Grp} \to \mathbf{Set}$ that sends a group $G$ to the set of its subgroups, and a homomorphism $f$ to $H \mapsto f(H)$.
It is a functor, but not a forgetful functor.
It does not send $G$ to its underlying set.

The term is also used informally for functors such as $\mathbf{Top} \to \mathbf{Set}$, which forget a topology rather than operations.
