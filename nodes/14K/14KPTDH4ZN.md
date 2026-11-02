---
tag: 14KPTDH4ZN
kind: definition
name: Finitely based algebra
msc: [08B05]
defines: YGYZAQ12MZ
uses: [9Q008GMZSW, PKD440G2XW, AJNZJD8442]
sources:
  - url: https://en.wikipedia.org/wiki/Variety_(universal_algebra)
---

## Definition

Let $A$ be an algebra of a signature with only function symbols.
The algebra $A$ is *finitely based* if it has a finite [[equational basis|9Q008GMZSW]].
That is, there is a finite set $\Sigma$ of [[identities|PKD440G2XW]] satisfied by $A$ such that every identity of $A$ holds in all algebras satisfying $\Sigma$.
A [[variety|AJNZJD8442]] is *finitely based* if it is the class of all algebras satisfying some finite set of identities.

## Remarks

An algebra is finitely based exactly when the variety it generates is finitely based.
An algebra is finitely based exactly when its equational theory is the set of consequences of finitely many identities.
Every two-element algebra of finite signature is finitely based, by a theorem of Lyndon, while Lyndon also found a finite algebra that is not finitely based.

Example: the group $(\Z, +, -, 0)$ is finitely based.
It generates the variety of abelian groups, so the identities $x + (y + z) \approx (x + y) + z$, $x + 0 \approx x$, $x + (-x) \approx 0$ and $x + y \approx y + x$ form an equational basis.

Non-example: the six-element Brandt monoid $B_2^1$ is not finitely based as a semigroup, by a theorem of Perkins.
It consists of the four $2 \times 2$ matrix units, the zero matrix and the identity matrix, under multiplication.
