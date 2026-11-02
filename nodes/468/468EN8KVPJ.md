---
tag: 468EN8KVPJ
kind: definition
name: Injective algebra
msc: [08B30, 18G05]
defines: KGTA7KGP3C
uses: [KBXSZC6BV1, SCRB74SWQN, 85H7PRHDPZ]
sources:
  - url: https://en.wikipedia.org/wiki/Injective_object
---

## Definition

Fix a signature and let $\mathcal{K}$ be a class of algebras of this signature.
An algebra $A \in \mathcal{K}$ is *injective* in $\mathcal{K}$ if the following holds.
For all $B, C \in \mathcal{K}$, every [[embedding|SCRB74SWQN]] $g \colon B \to C$ and every [[homomorphism|KBXSZC6BV1]] $f \colon B \to A$, there is a homomorphism $h \colon C \to A$ with $h \circ g = f$.

## Remarks

When $\mathcal{K}$ is a variety, the embeddings are exactly the monomorphisms of the category of algebras of $\mathcal{K}$.
So in a variety, $A$ is injective in this sense exactly when it is an injective object of that category.

Example: $\Q$ is injective in the variety of abelian groups.
An abelian group is injective there exactly when it is divisible, and $\Q$ is divisible since $x = n \cdot (x/n)$ for every $x \in \Q$ and $n \ge 1$.
In the variety of modules over a ring, the injective algebras are the [[injective modules|85H7PRHDPZ]].

Non-example: $\Z$ is not injective in the variety of abelian groups.
Let $g \colon \Z \to \Q$ be the inclusion and $f = \id_{\Z}$.
A homomorphism $h \colon \Q \to \Z$ with $h(1) = 1$ would give $2 h(1/2) = 1$ in $\Z$, which is impossible.

In many varieties, such as groups, only the trivial algebra is injective.
