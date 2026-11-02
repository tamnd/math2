---
tag: QPT5H6MM99
kind: definition
name: Abstract data type as an algebra
msc: [68Q65, 08A70]
defines: 86144NHH59
uses: [WAQJJ5GX68, HVF403PQ4H, KBXSZC6BV1, PKD440G2XW]
sources:
  - url: https://en.wikipedia.org/wiki/Abstract_data_type
---

## Definition

Let $S$ be a set of sorts and let $\Sigma$ be an $S$-sorted signature.
An *algebraic specification* is a pair $(\Sigma, E)$, where $E$ is a set of [[equations|PKD440G2XW]] between $\Sigma$-terms with variables, each side of the same sort.
A *model* of $(\Sigma, E)$ is a [[many-sorted $\Sigma$-algebra|WAQJJ5GX68]] that satisfies every equation of $E$.
A model $I$ is *initial* if for every model $A$ there is exactly one [[homomorphism|KBXSZC6BV1]] $I \to A$.
The *abstract data type* specified by $(\Sigma, E)$ is the class of initial models of $(\Sigma, E)$.

## Remarks

Initial models exist, and any two of them are isomorphic, so the abstract data type is one isomorphism class of algebras; this is the [[initial algebra semantics|HVF403PQ4H]] of the specification.
An initial model has two features.
Every element is the value of a ground term ("no junk"), and two ground terms are equal in it only if $E$ proves them equal ("no confusion").

Example: sorts $\mathrm{nat}$ and $\mathrm{bool}$; constants $\mathrm{true}, \mathrm{false} \colon \mathrm{bool}$ and $0 \colon \mathrm{nat}$; operations $s \colon \mathrm{nat} \to \mathrm{nat}$ and $\mathrm{iszero} \colon \mathrm{nat} \to \mathrm{bool}$; equations $\mathrm{iszero}(0) = \mathrm{true}$ and $\mathrm{iszero}(s(x)) = \mathrm{false}$.
The model with carriers $\N$ and $\set{\mathrm{true}, \mathrm{false}}$ is initial.
Each element is the value of a ground term, and two ground terms with the same value are equal by the equations.

Non-example: the model with one element in each sort satisfies $E$ but is not initial.
A homomorphism from it to the model above would send its single Boolean element to both $\mathrm{true}$ and $\mathrm{false}$, which is impossible.
