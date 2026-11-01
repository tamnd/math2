---
tag: PHT3TJCS90
kind: statement
role: theorem
name: Ax–Kochen theorem
msc: [12L10, 11D88, 03C60]
uses: [BT6T702C28, 2C3PAQ7H50, 0SN0MAEKYX, YZWYF7DXTW]
about: [BT6T702C28]
sources:
  - url: https://en.wikipedia.org/wiki/Ax%E2%80%93Kochen_theorem
same_as:
  wikidata: Q3526976
  wikipedia: Ax–Kochen theorem
---

## Statement

For each positive integer $d$ there is a finite set $E(d)$ of [[prime numbers|0SN0MAEKYX]] with the following property.
Let $p$ be a prime with $p \notin E(d)$, and let $\Q_p$ be the field of [[p-adic numbers|BT6T702C28]].
Let $F$ be a [[homogeneous polynomial|2C3PAQ7H50]] of degree $d$ in $n$ variables with coefficients in $\Q_p$.
If $n > d^2$, then there is $x \in \Q_p^n$ with $x \ne 0$ and $F(x) = 0$.

## Remarks

The proof is model-theoretic.
Let $\varphi$ be a first-order sentence in the language of rings.
Then $\varphi$ holds in $\Q_p$ for almost all primes $p$ if and only if it holds in the [[Laurent series field|YZWYF7DXTW]] $\F_p((t))$ for almost all $p$.
Here "almost all" means all but finitely many.
This transfer comes from ultraproducts over a nonprincipal ultrafilter on the primes.
The ultraproducts of the fields $\Q_p$ and of the fields $\F_p((t))$ are elementarily equivalent valued fields.
Both are Henselian with residue field of characteristic $0$, and they have the same residue field and the same value group.
For a fixed degree $d$, the property "every form of degree $d$ in $d^2 + 1$ variables has a nontrivial zero" is one first-order sentence.
A theorem of Lang shows that it holds in every $\F_p((t))$.
The finite exceptional set cannot be dropped in general: Terjanian found a form of degree $4$ in $18$ variables over $\Q_2$ with no nontrivial zero, while $18 > 4^2$.

## Explanations

### L1 human

Artin asked whether every homogeneous polynomial of degree $d$ in more than $d^2$ variables has a nonzero root over the $p$-adic numbers.
The answer is no in general, but Ax and Kochen proved that it is yes for all but finitely many primes $p$, the finitely many depending on $d$.
The proof compares $p$-adic numbers with power series over the finite field $\F_p$, where the answer is known, and uses logic to carry it over.

### L2 human

The theorem is a celebrated application of model theory to number theory.
The key principle is now called the Ax–Kochen–Ershov principle.
It says that the first-order theory of a Henselian valued field of residue characteristic $0$ is determined by the theories of its residue field and value group.
The original proof gives no explicit bound for the exceptional primes.
For $d = 2$ and $d = 3$ the conclusion is known to hold for all primes.
