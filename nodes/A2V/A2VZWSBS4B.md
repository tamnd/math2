---
tag: A2VZWSBS4B
kind: proof
name: Proof that finite subgroups of the multiplicative group of a field are cyclic
msc: ["12E20", "20K01"]
topics: [BAVE5RN4EE]
audience: ug2
proves: 0CKGBEJX6B
uses: [04C5ZBG1WT, 07C6ECNJET, 082GHNPJ53, 0ZDW0H0VX4, 0ZEPNS9BXK, 0KJVQV3E0F, 0MC0AQZSHE, N2EY1EVPRB]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Multiplicative structure
---

## Proof

Let $K$ be a [[field|04C5ZBG1WT]], and let $G$ be a finite subgroup of the [[group of units|07C6ECNJET]] $K^\times$, of order $n$.

1. Multiplication in $K$ is commutative, so $G$ is an [[abelian group|082GHNPJ53]].
2. By [[the power of the group order|0ZEPNS9BXK]], every $g \in G$ satisfies $g^n = 1$. So the [[exponent|0ZDW0H0VX4]] $e = \exp(G)$ is finite, and $e \leq n$ because $e$ is the least positive integer with this property.
3. By the definition of the exponent, every $g \in G$ satisfies $g^e = 1$. So every element of $G$ is a root in $K$ of the [[polynomial|N2EY1EVPRB]] $f = x^e - 1 \in K[x]$.
4. The polynomial $f$ is nonzero and has degree $e$, since $e \geq 1$. By [[the bound on the number of roots|0KJVQV3E0F]], $f$ has at most $e$ roots in $K$.
5. The $n$ elements of $G$ are distinct roots of $f$ by step 3. So $n \leq e$ by step 4.
6. By steps 2 and 5, $e = n$. So $G$ is a finite abelian group whose exponent equals its order.
7. By [[the theorem on exponent and order|0MC0AQZSHE]], $G$ is cyclic.
8. For the last claim, each element of $G$ is a root of $x^n - 1$ by step 2. This polynomial has at most $n$ roots in $K$, by the bound on the number of roots, and $G$ already gives $n$ of them. So $G$ is the set of all roots of $x^n - 1$ in $K$. $\blacksquare$

## Idea

The exponent of a finite abelian group is at most its order.
In a field, it cannot be smaller: all $n$ elements of $G$ are roots of $x^{\exp(G)} - 1$, and a polynomial of degree $d$ has at most $d$ roots.
So the exponent equals the order, and for a finite abelian group this means that $G$ is cyclic.

## Variants

1. The proof can avoid the word exponent. Let $h \in G$ have the largest order $m$. By Lemma B in [[the proof of the theorem on exponent and order|PPPV7NMEB5]], every $g \in G$ satisfies $g^m = 1$. So the $n$ elements of $G$ are roots of $t^m - 1$, and $n \leq m$. Since $m = |\langle h \rangle| \leq n$, the element $h$ has order $n$, so $\langle h \rangle = G$.
2. The [[counting proof|~0dc997aa]] does not use the theorem on exponent and order. It counts the elements of each order and compares the counts with the values of Euler's totient function.
