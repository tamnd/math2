---
tag: PAQ4ZX2TX1
kind: definition
name: Natural deduction
msc: [03F03, 03B05]
defines: 6KT3BJZ7D1
uses: [09K9MWD2QQ, QS0XVAN9BG]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_deduction
---

## Definition

Consider formulas of [[propositional logic|09K9MWD2QQ]] with the [[connectives|QS0XVAN9BG]] $\land$, $\lor$, $\to$ and the constant $\bot$ for falsity; $\neg \varphi$ abbreviates $\varphi \to \bot$.
A *natural deduction* derivation is a finite tree of formulas.
Each leaf is an assumption, and each inner node follows from its children by one of these rules:

1. $\land$-introduction: from $\varphi$ and $\psi$, infer $\varphi \land \psi$. $\land$-elimination: from $\varphi \land \psi$, infer $\varphi$, and also $\psi$.
2. $\lor$-introduction: from $\varphi$, infer $\varphi \lor \psi$ and $\psi \lor \varphi$.
3. $\lor$-elimination: from $\varphi \lor \psi$, a derivation of $\chi$ from $\varphi$, and one of $\chi$ from $\psi$, infer $\chi$, discharging $\varphi$ and $\psi$.
4. $\to$-introduction: from a derivation of $\psi$ from the assumption $\varphi$, infer $\varphi \to \psi$, discharging $\varphi$.
5. $\to$-elimination, or modus ponens: from $\varphi$ and $\varphi \to \psi$, infer $\psi$.
6. $\bot$-elimination: from $\bot$, infer any formula $\varphi$.
7. Reductio ad absurdum: from a derivation of $\bot$ from the assumption $\neg \varphi$, infer $\varphi$, discharging $\neg \varphi$.

A discharged assumption is no longer open.
One writes $\Gamma \vdash \varphi$ if some derivation has root $\varphi$ and all its open assumptions in $\Gamma$.

## Remarks

A derivation of $\vdash \varphi \land \psi \to \psi \land \varphi$: assume $\varphi \land \psi$.
By $\land$-elimination get $\psi$ and $\varphi$, and by $\land$-introduction get $\psi \land \varphi$.
Then $\to$-introduction discharges the assumption, so no open assumption remains.
The tree with the single node $p$ is a derivation of $p$, but only from the open assumption $p$; it does not show $\vdash p$.
Without rule 7, the system is natural deduction for [[intuitionistic logic|Q11N8X99FK]]; with it, the system is classical.
Quantifier rules extend the system to [[predicate logic|086QKPF0A6]].
