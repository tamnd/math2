---
tag: CBDM280TDF
kind: definition
name: Exact sequence
msc: [18G35, 13D02, "18E10"]
defines: JB7ZBFBA9C
uses: [0310REJJY8, 0NZ8JA25WK, 0NRYHJPQG2, 0W88CEGQP1, 0S21GNW9ZB]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_sequence
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]].
Consider a finite or infinite sequence of [[$R$-modules|0NZ8JA25WK]] and $R$-[[linear maps|0NRYHJPQG2]]
$$\cdots \to M_{i-1} \xrightarrow{f_{i-1}} M_i \xrightarrow{f_i} M_{i+1} \to \cdots.$$
The sequence is *exact at* $M_i$ if $\im f_{i-1} = \ker f_i$, where $\im$ is the [[image|0S21GNW9ZB]] and $\ker$ the [[kernel|0W88CEGQP1]].
The sequence is *exact* if it is exact at every module that has both an incoming and an outgoing map.
A *short exact sequence* is an exact sequence of the form $0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$.

## Remarks

A sequence $0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$ is exact exactly when $f$ is injective, $g$ is surjective, and $\im f = \ker g$; then $C \cong B / f(A)$.
Exactness of $0 \to A \xrightarrow{f} B$ means that $f$ is injective, and exactness of $B \xrightarrow{g} C \to 0$ means that $g$ is surjective.
Exactness at $M_i$ implies $f_i \circ f_{i-1} = 0$, but not conversely.

Example: $0 \to \Z \xrightarrow{2} \Z \xrightarrow{\pi} \Z/2\Z \to 0$, with $\pi$ the reduction, is a short exact sequence of $\Z$-modules.
Multiplication by $2$ is injective, $\pi$ is onto, and $\im(2) = 2\Z = \ker \pi$.

Non-example: the sequence $\Z \xrightarrow{2} \Z \xrightarrow{\rho} \Z/4\Z$, with $\rho$ the reduction modulo $4$, is not exact at the middle term.
The image of the first map is $2\Z$, but $\ker \rho = 4\Z \ne 2\Z$.
