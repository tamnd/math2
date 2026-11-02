---
tag: D3AC1N7PNX
kind: definition
name: Homomorphism
msc: [08A05, 03C07]
defines: KBXSZC6BV1
uses: [983GZBQYT4, WDVVEYD6AT, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Homomorphism
---

## Definition

Let $\sigma$ be a [[signature|WDVVEYD6AT]] and let $\mathbf{A}$ and $\mathbf{B}$ be $\sigma$-[[structures|983GZBQYT4]] with domains $A$ and $B$.
A *homomorphism* from $\mathbf{A}$ to $\mathbf{B}$ is a [[function|0EPAT51DXQ]] $h \colon A \to B$ such that:

1. for each function symbol $f \in \sigma$ of arity $n$ and all $a_1, \dots, a_n \in A$, $h(f^{\mathbf{A}}(a_1, \dots, a_n)) = f^{\mathbf{B}}(h(a_1), \dots, h(a_n))$;
2. for each constant symbol $c \in \sigma$, $h(c^{\mathbf{A}}) = c^{\mathbf{B}}$;
3. for each relation symbol $R \in \sigma$ of arity $n$ and all $a_1, \dots, a_n \in A$, if $(a_1, \dots, a_n) \in R^{\mathbf{A}}$ then $(h(a_1), \dots, h(a_n)) \in R^{\mathbf{B}}$.

## Remarks

Example: for the signature $\set{+, 0}$, the map $h \colon \Z \to \Z/n\Z$ that sends an integer to its residue class is a homomorphism.
Indeed, the class of $a + b$ is the sum of the classes of $a$ and $b$, and the class of $0$ is $0$.

Non-example: for the same signature, the map $x \mapsto 2x + 1$ from $\Z$ to $\Z$ fails clause 2, since $0 \mapsto 1$; it also fails clause 1, since $h(0 + 0) = 1 \ne 2 = h(0) + h(0)$.

For a signature with only function and constant symbols, clauses 1 and 2 are the whole condition; this is the notion of homomorphism of [[universal algebra|W82R6N0GM9]].
Whether a map is a homomorphism depends on the signature.
In the signature of groups $\set{\cdot, {}^{-1}, e}$ the inverse is preserved by definition, while for $\set{\cdot}$ alone it follows from the group axioms.
