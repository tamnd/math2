---
tag: ZETPP2VJFJ
kind: definition
name: Many-sorted algebra
msc: [08A68, 68Q65]
defines: WAQJJ5GX68
uses: [0SJ3RX9TXA, 0EPAT51DXQ, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Many-sorted_logic
---

## Definition

Let $S$ be a [[set|0SJ3RX9TXA]], whose elements are called *sorts*.
An *$S$-sorted signature* $\Sigma$ is a set of operation symbols, each with a type $s_1 \cdots s_n \to s$, where $n \ge 0$ and $s_1, \dots, s_n, s \in S$.
A *many-sorted $\Sigma$-algebra* $A$ consists of:

1. a set $A_s$ for each sort $s \in S$, the carrier of sort $s$;
2. for each symbol $f$ of type $s_1 \cdots s_n \to s$, a [[function|0EPAT51DXQ]] $f^A \colon A_{s_1} \times \cdots \times A_{s_n} \to A_s$ on the [[Cartesian product|09CEDJYBKP]].

A *homomorphism* $h \colon A \to B$ of $\Sigma$-algebras is a family of maps $h_s \colon A_s \to B_s$ with $h_s(f^A(a_1, \dots, a_n)) = f^B(h_{s_1}(a_1), \dots, h_{s_n}(a_n))$ for every symbol $f$ of type $s_1 \cdots s_n \to s$ and all $a_i \in A_{s_i}$.

## Remarks

Example: let $S = \set{\mathrm{scalar}, \mathrm{vector}}$, with symbols $+ \colon \mathrm{vector}\,\mathrm{vector} \to \mathrm{vector}$, $\cdot \colon \mathrm{scalar}\,\mathrm{vector} \to \mathrm{vector}$, and the field operations on the sort $\mathrm{scalar}$.
A vector space $V$ over a field $K$ gives an algebra with $A_{\mathrm{scalar}} = K$ and $A_{\mathrm{vector}} = V$; each operation sends arguments of the right sorts to the right sort.

Non-example: the same data with a map $K \times V \to K$ in place of scalar multiplication fails clause 2, since the value of $\cdot$ must lie in the carrier of sort $\mathrm{vector}$.

With one sort, a many-sorted algebra is an ordinary algebra.
Birkhoff and Lipson called these structures *heterogeneous algebras*.
Some authors require each carrier $A_s$ to be nonempty.
