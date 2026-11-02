---
tag: BT7D4VQ6Y0
kind: definition
name: Initial algebra semantics
msc: [08A70, 68Q55, 08B20]
defines: HVF403PQ4H
uses: [3YYKGWJJND, KBXSZC6BV1, R76EC56V9R, PKD440G2XW]
sources:
  - url: https://en.wikipedia.org/wiki/Initial_algebra
---

## Definition

Let $\Sigma$ be a signature of function symbols and let $K$ be a class of $\Sigma$-algebras.
An algebra $I \in K$ is *initial in $K$* if for every $A \in K$ there is exactly one [[homomorphism|KBXSZC6BV1]] $I \to A$.
The [[term algebra|3YYKGWJJND]] $T_\Sigma$ of ground terms is initial in the class of all $\Sigma$-algebras.
In *initial algebra semantics*, the meaning of a ground term $t$ in a $\Sigma$-algebra $A$ is $[\![t]\!]_A = h_A(t)$, where $h_A \colon T_\Sigma \to A$ is the unique homomorphism.
Let $E$ be a set of [[equations|PKD440G2XW]].
The meaning of the specification $(\Sigma, E)$ is the initial algebra of the class of $\Sigma$-algebras that satisfy $E$.
It is determined up to isomorphism.

## Remarks

Since $h_A$ is a homomorphism, $[\![f(t_1, \dots, t_n)]\!]_A = f^A([\![t_1]\!]_A, \dots, [\![t_n]\!]_A)$, so meanings are compositional.
The initial algebra of the algebras satisfying $E$ exists: it is the quotient of $T_\Sigma$ by the least congruence that contains all ground instances of the equations of $E$.

Example: let $\Sigma = \set{0, s, +}$ with arities $0, 1, 2$, and let $E$ consist of $x + 0 = x$ and $x + s(y) = s(x + y)$.
The natural numbers $\N$ with zero, successor and addition satisfy $E$.
Every ground term equals some $s^n(0)$ by $E$, and distinct numerals $s^m(0) \ne s^n(0)$ are separated in $\N$, so $\N$ is initial among the models of $E$.

Non-example: $\N$ is not initial in the class of all $\Sigma$-algebras.
In $T_\Sigma$ the terms $s(0)$ and $s(0) + 0$ are different, but in $\N$ they have the same value $1$.
A homomorphism $\N \to T_\Sigma$ would send $1$ to both terms, so there is none.

The general notion of an [[initial algebra|R76EC56V9R]] for a functor contains this one: $T_\Sigma$ is the initial algebra of the polynomial functor of $\Sigma$.
