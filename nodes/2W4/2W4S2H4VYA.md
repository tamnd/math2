---
tag: 2W4S2H4VYA
kind: example
name: Dense linear order
msc: [03C35, 03C10, 06A05]
instance_of: [1JJCGNX240]
uses: [0FRXBVVR03, 0NCJ5WXN6Z, 0D3WA36K2Q, ZR7Y5C235P, 7FDDXV3JK7]
sources:
  - url: https://en.wikipedia.org/wiki/Dense_order
---

## Example

A [[linear order|0FRXBVVR03]] $(D, <)$ is *dense* if for all $a < b$ in $D$ there is $c \in D$ with $a < c < b$.
The theory $\mathrm{DLO}$ of dense linear orders without endpoints is a theory in the signature $\set{<}$.
It says that $<$ is a dense linear order on a set with at least two elements.
It also says that there is no least and no greatest element.
The [[rational numbers|0NCJ5WXN6Z]] and the real numbers with their usual order are models.

$\mathrm{DLO}$ is $\aleph_0$-categorical: any two countable models are [[order isomorphic|0D3WA36K2Q]].
Check, by Cantor's back-and-forth argument: list the elements of two countable models $A$ and $B$, and build a chain of finite order-preserving partial maps.
At odd steps, send the next element of $A$ to an element of $B$ in the same position relative to the finite image.
This element exists because $B$ is dense and has no endpoints.
At even steps, do the same from $B$ back to $A$.
The union of the chain is an isomorphism from $A$ onto $B$.

## Remarks

Since $\mathrm{DLO}$ has no finite models, the [[Łoś–Vaught test|ZR7Y5C235P]] shows that it is complete; it is also decidable.
It has [[quantifier elimination|7FDDXV3JK7]].
It is not $\kappa$-categorical for any uncountable $\kappa$.
For $\kappa = 2^{\aleph_0}$, compare $\R$ with the order $\R + \Q$, a copy of $\R$ followed by a copy of $\Q$.
Both are dense without endpoints and have size $2^{\aleph_0}$.
They are not isomorphic.
In $\R$ every nonempty set with an upper bound has a least upper bound.
In $\R + \Q$ the copy of $\R$ is bounded above but has no least upper bound.

## Explanations

### L1 human

In a dense order, between any two elements there is a third, like the rational numbers on the number line.
Every countable dense order without a first or last element is a copy of the rational numbers.
This makes the theory of such orders one of the simplest examples in model theory.
It is complete, it has only one countable model, and every formula reduces to comparisons between the variables.
