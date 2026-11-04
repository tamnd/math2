---
tag: A2VZWSBS4B
kind: proof
name: Proof that finite subgroups of the multiplicative group of a field are cyclic
msc: ["12E20"]
proves: 0CKGBEJX6B
uses: [0QA8CHH8MG, 05THZKR9AN, 071DDFVG4J, 0FCCTFA275, 0ZEPNS9BXK, 0KJVQV3E0F, 0MC0AQZSHE]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Multiplicative structure
---

## Proof

1. Let $K$ be a [[field|0QA8CHH8MG]], and let $G$ be a finite subgroup of the [[group of units|05THZKR9AN]] $K^\times$. Let $n = \abs{G}$.
2. Multiplication in $K$ is commutative, so $G$ is an [[abelian group|071DDFVG4J]].
3. Every $g \in G$ satisfies [[$g^n = 1$|0ZEPNS9BXK]]. So some positive integer $m$ has $g^m = 1$ for all $g \in G$.
4. Let $e$ be the [[exponent|0FCCTFA275]] of $G$: the least positive integer with $g^e = 1$ for all $g \in G$. By step 3, $e \le n$.
5. Every element of $G$ is a root in $K$ of the polynomial $x^e - 1 \in K[x]$, which is nonzero of degree $e$.
6. This polynomial has [[at most $e$ roots in $K$|0KJVQV3E0F]]. The $n$ elements of $G$ are distinct roots, so $n \le e$.
7. By steps 4 and 6, the exponent $e$ equals $\abs{G} = n$.
8. A finite abelian group whose exponent equals its order [[is cyclic|0MC0AQZSHE]]. So $G$ is cyclic.

## Idea

In a field, the equation $x^e = 1$ has at most $e$ solutions. So the exponent of a finite subgroup of $K^\times$ cannot be smaller than its order. For an abelian group, exponent equal to order means that one element has the full order.
