---
tag: Y1DVDH3EYH
kind: example
name: Intuitionistic propositional logic is algebraizable
msc: ["03G27", "03G10"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [CESWST3NWA]
uses: [XADWEW9TNP, Q11N8X99FK, NG943XNQWH, QC9M3Q8B8Q, X3EQTPS85Z]
sources:
  - url: https://en.wikipedia.org/wiki/Abstract_algebraic_logic
  - book: isbn:9781848902077
---

## Example

Let $\vdash$ be [[intuitionistic propositional logic|Q11N8X99FK]] in $\land, \lor, \to, \bot$, and let $K$ be the class of [[Heyting algebras|NG943XNQWH]].
Put $E(x) = \set{x \approx x \to x}$ and $\Delta(x, y) = \set{x \to y, y \to x}$, as in [[the classical case|X3EQTPS85Z]].
We check [[the definition|XADWEW9TNP]].

1. (A1), soundness. The axioms take the value $1$ in every Heyting algebra, and $a = 1$, $a \to b = 1$ give $b = a \wedge (a \to b) \le b$, so $b = 1$.
2. (A1), completeness. Let $\Gamma \nvdash \varphi$, and let $T$ be the theory of $\Gamma$. On formulas put $\alpha \sim \beta$ iff $T \vdash \alpha \to \beta$ and $T \vdash \beta \to \alpha$.
3. The quotient $\mathrm{Fm}/{\sim}$ is a Heyting algebra, the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of $T$, and its top is the class of $T$.
4. The quotient map sends each $\gamma \in \Gamma$ to $1$ but sends $\varphi$ to another element, since $\varphi \notin T$. So $E[\Gamma] \not\models_K E(\varphi)$.
5. (A2). In a Heyting algebra $a \to b = 1$ iff $a \le b$. So $a \to b = 1$ and $b \to a = 1$ iff $a = b$.

So intuitionistic logic is [[algebraizable|CESWST3NWA]], with the Heyting algebras as equivalent algebraic semantics.

## Remarks

1. By [[the isomorphism theorem|8ZFJ67HTWR]], the intermediate logics correspond to the varieties of Heyting algebras, in the reverse order.
2. Unlike the classical case, no single finite Heyting algebra suffices for step 2. One can use the Lindenbaum-Tarski algebra; for finite $\Gamma$, the finite Heyting algebras suffice, by the finite model property.
3. The same $E$ and $\Delta$ work for every axiomatic extension, with the corresponding variety of Heyting algebras.

## Explanations

### L1 human

Intuitionistic logic has its own algebras, the Heyting algebras, and it matches them as closely as classical logic matches Boolean algebras.

### L2 human

1. Take $\Gamma = \emptyset$ and $\varphi = p \lor \lnot p$.
2. In the three-element Heyting algebra $0 < \frac{1}{2} < 1$, put $p = \frac{1}{2}$.
3. Then $\lnot p = p \to 0 = 0$, so $p \lor \lnot p = \frac{1}{2} \ne 1$.
4. By (A1), $\nvdash p \lor \lnot p$ in intuitionistic logic.

The typical use: to show that a formula is not intuitionistically provable, find a small Heyting algebra and a valuation that does not give $1$.
The trap: Heyting algebras use $a \to b$ as the relative pseudocomplement, not as $\lnot a \lor b$.
