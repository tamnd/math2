---
tag: P6QNEK44RX
kind: statement
role: theorem
name: Lie's third theorem
msc: ["22E60", "22E15"]
uses: [7JBRGCVJRB, SNA3DVPK0C, S1XK3HXHFX, SWW2993CVJ]
about: [7JBRGCVJRB]
sources:
  - url: https://en.wikipedia.org/wiki/Lie%27s_third_theorem
same_as:
  wikidata: Q15080987
  wikipedia: Lie's third theorem
---

## Statement

Let $\mathfrak{g}$ be a finite-dimensional [[Lie algebra|5JJYBJ6A8K]] over $\R$.
Then there is a connected and simply connected real [[Lie group|7JBRGCVJRB]] $G$ whose Lie algebra is isomorphic to $\mathfrak{g}$.
Here the Lie algebra of $G$ is the algebra of [[left-invariant vector fields|SNA3DVPK0C]] on $G$.
Such a group $G$ is unique up to isomorphism of Lie groups.

## Remarks

One proof uses Ado's theorem: $\mathfrak{g}$ is isomorphic to a Lie subalgebra of $\mathfrak{gl}_n(\R)$ for some $n$.
The connected Lie subgroup of $GL_n(\R)$ with Lie algebra $\mathfrak{g}$ is then a Lie group with Lie algebra $\mathfrak{g}$, and its [[universal covering group|SWW2993CVJ]] is simply connected.
Uniqueness follows because a Lie algebra isomorphism between Lie algebras of simply connected groups integrates to a Lie group isomorphism.
Example: the Lie algebra $\R$ with zero bracket gives $G = \R$; the circle group has the same Lie algebra but is not simply connected, since its [[fundamental group|S1XK3HXHFX]] is $\Z$.
The group $G$ need not be a group of matrices: the universal cover of $SL_2(\R)$ has no faithful finite-dimensional representation.
In infinite dimension the analogue fails: there are Banach Lie algebras that are not the Lie algebra of any Banach Lie group.

## Explanations

### L1 human

A Lie algebra is a vector space with a bracket, the infinitesimal shadow of a Lie group.
The theorem says that every such shadow, in finite dimension, really comes from a group.
Among all groups with the given shadow there is a best one, the simply connected one, and it is unique.

### L2 human

With the correspondence between homomorphisms, this theorem shows that taking the Lie algebra is an equivalence between connected simply connected Lie groups and finite-dimensional real Lie algebras.
Every other connected Lie group with Lie algebra $\mathfrak{g}$ is a quotient $G / \Gamma$ of the simply connected one by a discrete central subgroup $\Gamma$.
So classifying connected Lie groups reduces to classifying Lie algebras and the discrete subgroups of the centres of the simply connected groups.
The name comes from Lie's work, where the third of his fundamental theorems was a local result about infinitesimal transformations.
