---
tag: YAQY3P8BT0
kind: example
name: Intuitionistic logic is not substructural
msc: ["03B47", "03B20"]
topics: [98QF5J4W16]
audience: research
not_instance_of:
  - target: ZZKTJY5J4T
    note: the calculus LJ has weakening, contraction and exchange, and its algebras are residuated lattices in which fusion is meet
uses: [PZX9J3VEMT, 52XCYMK0WW, NG943XNQWH, S9Z6PKTXAS]
sources:
  - url: https://en.wikipedia.org/wiki/Residuated_lattice
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Substructural_logic
    locator: lead section
---

## Example

[[Intuitionistic logic|52XCYMK0WW]] is not a substructural logic.
We check the three structural rules and then the algebraic side.

1. The calculus LJ of [[the definition|PZX9J3VEMT]] has the rules WL, CL and XL on the left.
   So it has weakening, contraction and exchange.
2. On the right, an LJ sequent has at most one formula, so contraction and exchange on the right have nothing to act on.
   Weakening on the right turns $\Gamma \Rightarrow$ into $\Gamma \Rightarrow A$.
3. A [[Heyting algebra|NG943XNQWH]] $H$ is a [[residuated lattice|S9Z6PKTXAS]] with fusion $x \cdot y = x \wedge y$, unit $1 = \top$ and residual $x \backslash y = y / x = x \to y$.
4. Residuation holds: $x \wedge y \leq z$ if and only if $y \leq x \to z$, by the definition of $\to$ in a Heyting algebra.
5. Fusion is commutative, since $x \wedge y = y \wedge x$.
   This is the algebraic form of exchange.
6. Fusion is integral, since $x \leq \top = 1$.
   This is the algebraic form of weakening.
7. Fusion is square-increasing, since $x \leq x \wedge x$.
   This is the algebraic form of contraction.

So both the calculus and the algebras have all three structural rules.

## Remarks

Conversely, a residuated lattice with $x \cdot y = x \wedge y$ and $0$ as least element is a Heyting algebra.
So intuitionistic logic is $\mathsf{FL}$ with exchange, weakening and contraction, often written $\mathsf{FL}_{ecw}$.
Classical logic is a non-example for the same reason, with Boolean algebras in place of Heyting algebras.
If we drop contraction from LJ, we get $\mathsf{FL}_{ew}$, which is substructural.

## Explanations

### L1 human

In intuitionistic logic we may reuse a hypothesis, ignore it, or reorder the hypotheses.
These are the three freedoms that substructural logics remove.
So intuitionistic logic keeps all the structure, and it is not substructural.

### L2 human

We check the algebraic form of contraction in the three-element Heyting algebra $0 < \tfrac12 < 1$.

1. Fusion is meet, so $\tfrac12 \cdot \tfrac12 = \min(\tfrac12, \tfrac12) = \tfrac12$.
2. So $x \leq x \cdot x$ holds for $x = \tfrac12$, and the same holds for $0$ and $1$.
3. In the three-element MV-algebra, fusion is $\max(0, x + y - 1)$, so $\tfrac12 \cdot \tfrac12 = 0 < \tfrac12$, and contraction fails.

The typical use is to place a logic in the family by its algebras.
A trap: the same three-element chain carries both structures, so the chain alone does not decide whether contraction holds; the fusion does.
