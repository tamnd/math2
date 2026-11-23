---
tag: B6G1P9DBF9
kind: example
name: The cancellation axiom in the standard product algebra
msc: ["03B52"]
topics: [WZP584JQ06]
audience: grad
instance_of: [YTHRDT9PDR]
uses: [DS5YPGT8GA, 7R2JBNNMT5]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 1. Fuzzy connectives based on t-norms; 5. Other notable fuzzy logics
---

## Example

We check the cancellation axiom $\neg \varphi \lor ((\varphi \to \varphi \otimes \psi) \to \psi)$ of [[product logic|DS5YPGT8GA]] in $[0, 1]_\Pi$.
Let $x$ and $y$ be the values of $\varphi$ and $\psi$, and use the residuum from [[the residua statement|7R2JBNNMT5]].

1. At $x = 0.5$, $y = 0.7$, we get $x \cdot y = 0.35$, and $0.5 \Rightarrow_\Pi 0.35 = 0.35 / 0.5 = 0.7$.
2. Then $0.7 \Rightarrow_\Pi 0.7 = 1$, so the axiom has value $\max(\neg 0.5, 1) = 1$.
3. At $x = 0$, $\neg 0 = 1$, so the axiom has value $1$ for every $y$.
4. In general, let $x > 0$ and $y < 1$.
   Then $x y < x$, so $x \Rightarrow_\Pi x y = x y / x = y$.
5. Let $x > 0$ and $y = 1$.
   Then $x \Rightarrow_\Pi x = 1 = y$.
6. In both cases $(x \Rightarrow_\Pi x y) \Rightarrow_\Pi y = y \Rightarrow_\Pi y = 1$.
7. So the axiom has value $1$ under every evaluation in $[0, 1]_\Pi$.

Two more values in $[0, 1]_\Pi$ show what product logic does not prove.

8. Contraction $p \to p \otimes p$ at $p = 0.5$ has value $0.5 \Rightarrow_\Pi 0.25 = 0.5$.
9. Double negation $\neg \neg p \to p$ at $p = 0.5$ has $\neg 0.5 = 0$ and $\neg 0 = 1$, so its value is $1 \Rightarrow_\Pi 0.5 = 0.5$.

## Remarks

Steps 4 to 7 prove that the cancellation axiom is valid in $[0, 1]_\Pi$, which is the soundness half for this axiom.
Steps 8 and 9 show that product logic proves neither contraction nor double negation, since both have value below $1$ in its standard algebra.

The disjunct $\neg \varphi$ is needed.
At $x = 0$ we get $0 \Rightarrow_\Pi 0 = 1$, and then $1 \Rightarrow_\Pi y = y$, which can be below $1$.
So without $\neg \varphi$ the formula $(\varphi \to \varphi \otimes \psi) \to \psi$ has value $0.3$ at $x = 0$, $y = 0.3$.

## Explanations

### L1 human

Multiply $0.7$ by $0.5$ to get $0.35$.
Dividing $0.35$ by $0.5$ gives $0.7$ back.
So the axiom "conjunction with $\varphi$ loses nothing" holds whenever $\varphi$ is not fully false.

### L2 human

Split on $x = 0$ and $x > 0$.
For $x = 0$, use the negation disjunct, and for $x > 0$, compute the residuum by division.
Watch out: in Łukasiewicz or Gödel logic the second disjunct can fail; see [[the non-example|VVXQ399T3V]].
