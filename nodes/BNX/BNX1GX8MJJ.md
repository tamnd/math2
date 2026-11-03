---
tag: BNX1GX8MJJ
kind: definition
name: K-theory as a generalized cohomology theory
msc: [55N15, 55N20]
defines: 677EDH782C
uses: [H28PSZR7XG, YHK51GHK2T, 9E4JE4902G, RASZAXBHX0, WN2DCBSX1C, Q7RFNJH76Q, 5W95QFHXPR]
sources:
  - url: https://en.wikipedia.org/wiki/Cohomology
---

## Definition

Let $(X, A)$ be a pair of finite [[CW complexes|5W95QFHXPR]], with $A$ a subcomplex of $X$.
Let $X/A$ be the quotient pointed at the image of $A$, with $X/\emptyset = X_+$, the space $X$ with a disjoint base point.
For $n \ge 0$ set
$$K^{-n}(X, A) = \tilde{K}(\Sigma^n (X/A)),$$
where $\tilde{K}$ is [[reduced K-theory|RASZAXBHX0]] and $\Sigma$ is the reduced [[suspension|Q7RFNJH76Q]].
For $n > 0$ set $K^{n}(X, A) = K^{n-2}(X, A)$ inductively, which is consistent with the isomorphism $K^{-n} \cong K^{-n-2}$ of the [[Bott periodicity theorem|WN2DCBSX1C]].
*K-theory as a generalized cohomology theory* is the family of contravariant functors $(X, A) \mapsto K^n(X, A)$, $n \in \Z$, together with coboundary maps $\delta \colon K^n(A) \to K^{n+1}(X, A)$ that satisfy:

1. homotopic maps of pairs induce the same homomorphisms;
2. each pair gives a long exact sequence $\cdots \to K^n(X, A) \to K^n(X) \to K^n(A) \xrightarrow{\delta} K^{n+1}(X, A) \to \cdots$;
3. excision: for subcomplexes $A, B$ of $X$ with $X = A \cup B$, restriction gives $K^n(X, B) \cong K^n(A, A \cap B)$.

## Remarks

These are the [[Eilenberg–Steenrod axioms|YHK51GHK2T]] without the dimension axiom, so $K^*$ is a [[generalized cohomology theory|H28PSZR7XG]].
The coboundary $\delta$ comes from the Puppe sequence $A \to X \to X \cup CA \to \Sigma A \to \cdots$.

Example: for $X$ a point and $A = \emptyset$, $K^0(\text{point}) = \Z$, $K^{-1}(\text{point}) = \tilde{K}(S^1) = 0$, and $K^{-2}(\text{point}) = \tilde{K}(S^2) \cong \Z$.
So $K^n(\text{point})$ is $\Z$ for $n$ even and $0$ for $n$ odd.

Non-example: ordinary cohomology satisfies the dimension axiom $H^n(\text{point}) = 0$ for $n \ne 0$.
K-theory fails it, since $K^{-2}(\text{point}) \cong \Z$, so K-theory is not an ordinary cohomology theory.

The theory is multiplicative, and $K^*(\text{point}) \cong \Z[\beta, \beta^{-1}]$ with the Bott class $\beta$ in degree $-2$.
It is represented by the spectrum $KU$ of [[complex K-theory|9E4JE4902G]].
