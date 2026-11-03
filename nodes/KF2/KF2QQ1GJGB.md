---
tag: KF2QQ1GJGB
kind: statement
role: theorem
name: Number of characters of a finite abelian group
msc: [20K01, 43A40]
uses: [082GHNPJ53, FPRA2KEHFF, 07CQR9BW3R, 0KVGH0J5B3]
about: [FPRA2KEHFF]
sources:
  - url: https://en.wikipedia.org/wiki/Character_group
---

## Statement

Let $G$ be a finite [[abelian group|082GHNPJ53]], and let $\widehat{G}$ be its [[character group|FPRA2KEHFF]], the group of homomorphisms $G \to \C^\times$.
Then $\abs{\widehat{G}} = \abs{G}$.

## Remarks

Proof idea: for a [[cyclic group|0KVGH0J5B3]] $\Z/n\Z$, a character is determined by the value $\chi(1)$, which can be any $n$-th root of unity, so there are exactly $n$ characters.
A character of a direct product $A \times B$ is the same as a pair of characters of $A$ and of $B$, so $\widehat{A \times B} \cong \widehat{A} \times \widehat{B}$.
By the [[classification of finite abelian groups|07CQR9BW3R]], $G$ is a product of cyclic groups, and the count follows.

Example: $G = \Z/2\Z \times \Z/2\Z$ has the four characters $(a, b) \mapsto (-1)^{\epsilon a + \eta b}$ with $\epsilon, \eta \in \set{0, 1}$.

The hypothesis that $G$ is abelian is necessary.
In general $\abs{\widehat{G}} = \abs{G / [G, G]}$, the order of the abelianization.
For $G = S_3$ this is $2$, while $\abs{S_3} = 6$.

## Explanations

### L1 human

A finite abelian group has exactly as many characters as elements.
So there are just enough waves on the group to describe every function on it.

### L2 human

Together with the [[orthogonality of characters|S6ARZ7M1YE]], the count shows that the characters form a basis of the space of functions on $G$.
It is also the first step towards the fact that $G$ is isomorphic to $\widehat{G}$.
