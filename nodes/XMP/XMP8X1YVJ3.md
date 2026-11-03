---
tag: XMP8X1YVJ3
kind: statement
role: theorem
name: Levi decomposition
msc: [17B05, 17B20]
uses: [5JJYBJ6A8K, 33MD21KMNP, EY9DN7QAX1, WKSSTQ69AK, T9WAK2FH31, 1ZB13N78XW, NE2K5HAEFN, ET8Y1AR5YX, 1ZAT1Z967A]
about: [33MD21KMNP, EY9DN7QAX1]
sources:
  - url: https://en.wikipedia.org/wiki/Levi_decomposition
same_as:
  wikidata: Q6535568
  wikipedia: Levi decomposition
---

## Statement

Let $k$ be a field of [[characteristic|1ZB13N78XW]] $0$, let $\mathfrak g$ be a finite-dimensional [[Lie algebra|5JJYBJ6A8K]] over $k$, and let $\mathfrak r = \operatorname{rad}(\mathfrak g)$ be its [[radical|33MD21KMNP]].
Then there is a [[subalgebra|WKSSTQ69AK]] $\mathfrak s$ of $\mathfrak g$ such that $\mathfrak g = \mathfrak r \oplus \mathfrak s$ as vector spaces.
Every such $\mathfrak s$ is [[semisimple|EY9DN7QAX1]] and isomorphic to $\mathfrak g / \mathfrak r$, and $\mathfrak g$ is the [[semidirect product|T9WAK2FH31]] $\mathfrak r \rtimes \mathfrak s$.

## Remarks

A subalgebra $\mathfrak s$ as in the statement is a *Levi subalgebra* of $\mathfrak g$.
By a theorem of Malcev, any two Levi subalgebras are conjugate by an automorphism $\exp(\operatorname{ad} z)$ with $z$ in the [[nilradical|ET8Y1AR5YX]] of $\mathfrak g$.

Idea of the proof: by induction on $\dim \mathfrak r$ one reduces to the case where $\mathfrak r$ is abelian and is a minimal nonzero ideal.
Then $\mathfrak g$ is an extension of the semisimple Lie algebra $\mathfrak g / \mathfrak r$ by the module $\mathfrak r$.
Such an extension splits because $H^2(\mathfrak g / \mathfrak r, \mathfrak r) = 0$ by the second of [[Whitehead's lemmas|NE2K5HAEFN]], and a splitting is a Levi subalgebra.

Example: let $\mathfrak g = \mathfrak{sl}_2(k) \oplus k^2$ with the bracket $[(x, v), (y, w)] = ([x, y], xw - yv)$, where $\mathfrak{sl}_2(k)$ is the [[special linear Lie algebra|1ZAT1Z967A]].
Here $k^2$ is an abelian ideal and $\mathfrak g / k^2 \cong \mathfrak{sl}_2(k)$ is semisimple, so $\mathfrak r = k^2$ and $\mathfrak{sl}_2(k)$ is a Levi subalgebra.

## Explanations

### L1 human

Every finite-dimensional Lie algebra in characteristic $0$ splits into two pieces.
One piece is the radical, which is solvable and built from commutative layers.
The other piece is semisimple, a sum of simple Lie algebras.
The theorem says the semisimple piece can be found as a subalgebra sitting next to the radical, not only as a quotient.

### L2 human

The Levi decomposition reduces the structure theory of finite-dimensional Lie algebras in characteristic $0$ to two parts, solvable algebras and semisimple algebras.
The two parts are glued by an action of the semisimple part on the radical.
Over $\C$, semisimple algebras are classified by Dynkin diagrams, while solvable ones have no such classification.
The analogue for simply connected Lie groups is the Levi–Malcev decomposition of a group into a solvable normal subgroup and a semisimple subgroup.
The proof is a typical use of Lie algebra cohomology: an obstruction lives in a second cohomology group, and that group vanishes.
