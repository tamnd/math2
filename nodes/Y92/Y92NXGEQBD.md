---
tag: Y92NXGEQBD
kind: definition
name: Second-order arithmetic
msc: [03F35, 03B30]
defines: DC60FYCSPM
uses: [0QFT7Z76N5, 3K1AKGXF8A, 92SWXST1ZM, HYJ10AF6RT]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
---

## Definition

The language of second-order arithmetic has number variables $n, m, x, y, \ldots$ and set variables $X, Y, \ldots$.
It has the constants $0$ and $1$, the operations $+$ and $\cdot$, and the relation $<$ on numbers.
It also has the membership relation $n \in X$ between a number and a set.
*Second-order arithmetic* $\mathsf{Z}_2$ is the [[theory|92SWXST1ZM]] in this two-sorted first-order language with these axioms:

1. the basic axioms: the axioms of a discretely ordered commutative semiring with least element $0$ and successor $n + 1$, in the style of [[Robinson arithmetic|3K1AKGXF8A]];
2. the induction axiom: $\forall X\, \big( (0 \in X \wedge \forall n\, (n \in X \to n + 1 \in X)) \to \forall n\, (n \in X) \big)$;
3. the comprehension scheme: $\exists X\, \forall n\, (n \in X \leftrightarrow \varphi(n))$ for every [[formula|HYJ10AF6RT]] $\varphi(n)$ in which $X$ does not occur free.

## Remarks

Example: the full structure, with number domain $\N$ and set domain the power set of $\N$, is a model of $\mathsf{Z}_2$.
Each clause holds because every subset of $\N$ is available, and ordinary induction holds in $\N$.

Non-example: the structure with number domain $\N$ and set domain the computable subsets of $\N$ satisfies clauses 1 and 2 but not clause 3.
The formula $\varphi(e)$ that says "program $e$ halts on input $e$" uses only number quantifiers, and the set it defines is the halting problem, which is not computable.

Subsystems are obtained by restricting comprehension and induction to classes of formulas, for example arithmetical comprehension in $\mathsf{ACA}_0$.
Despite the name, $\mathsf{Z}_2$ is a first-order theory: its models may have a set domain smaller than the full power set.
Together with clause 2, the comprehension scheme proves induction for every formula, so the first-order [[Peano axioms|0QFT7Z76N5]] are provable in $\mathsf{Z}_2$.
