---
tag: P75CXH2Q2B
kind: statement
role: theorem
name: Characterizations of Galois extensions
msc: [12F10]
uses: [0NRYPM9Y27, 0CBRFQ7DVZ, 0N019F6RE9, 02NZZ1J0FH, 03J8BS7FMV, 0KMJ6919WS, 0K1SCPBNKJ, 0GS74FGFEK]
about: [0QMZAQ6QQ4]
sources:
  - url: https://en.wikipedia.org/wiki/Galois_extension
---

## Statement

Let $L/K$ be a [[finite extension|0NRYPM9Y27]], and let $\Aut(L/K)$ be the group of [[automorphisms|0K1SCPBNKJ]] of $L$ that fix $K$ pointwise.
The following are equivalent:

1. $L/K$ is [[normal|0CBRFQ7DVZ]] and [[separable|0N019F6RE9]];
2. $L$ is the [[splitting field|02NZZ1J0FH]] over $K$ of a [[separable polynomial|03J8BS7FMV]] in $K[x]$;
3. $\abs{\Aut(L/K)} = [L:K]$, where $[L:K]$ is the [[degree|0GS74FGFEK]];
4. the [[fixed field|0KMJ6919WS]] of $\Aut(L/K)$ is $K$;
5. $K$ is the fixed field of some finite group of automorphisms of $L$.

An extension with these properties is a Galois extension.

## Remarks

The implication from 1 to 2 takes the product of the distinct minimal polynomials of a basis.
From 2 to 3, one counts the extensions of the identity of $K$ to automorphisms of $L$ step by step, using that the roots are distinct.
In general $\abs{\Aut(L/K)} \le [L:K]$, and [[Artin's theorem on fixed fields|X7R15C00ET]] gives $[L:L^{G}] = \abs{G}$ for $G = \Aut(L/K)$, which links 3, 4 and 5.
From 5 to 1, every element of $L$ is a root of the separable split polynomial $\prod (x - \beta)$ over its orbit.

Example: $\Q(\sqrt[3]{2})/\Q$ is not Galois.
Its only automorphism is the identity, since the other roots of $x^3 - 2$ are not real; so condition 3 fails ($1 \ne 3$) and condition 4 fails (the fixed field is $\Q(\sqrt[3]{2})$).

Finiteness is needed for condition 3 to make sense; for infinite algebraic extensions, conditions 1 and 4 remain equivalent.

## Explanations

### L1 human

A Galois extension is a field extension with as much symmetry as possible.
This theorem lists several tests for it.
One test: each irreducible polynomial with one root in $L$ has all its roots in $L$, with no repeated roots.
Another test: count the symmetries and compare with the degree.
A third test: only the elements of $K$ are fixed by all symmetries.

### L2 human

In practice one shows that an extension is Galois by exhibiting it as a splitting field of a separable polynomial, condition 2.
One uses condition 3 or 4 to compute with the Galois group, for example to show that $\abs{\Gal(L/K)} = [L:K]$.
Condition 5 is how Galois extensions arise from group actions.
These equivalences are the input for the [[fundamental theorem of Galois theory|0T1Q8D0FW8]].
