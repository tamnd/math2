---
tag: 6R0QSZ41EE
kind: proof
name: Proof that a structural logic is determined by its Lindenbaum matrices
msc: ["03B22", "03G27"]
topics: [WZP584JQ06]
audience: grad
proves: VWJVAS3VE3
uses: [AJEJS6TFWP, J78Y1M4GND]
methods: [0NTF6DMVAP, TFQ1845T84]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 3.4 Many-valuedness and rule-based approaches
---

## Proof

A homomorphism $h \colon \mathrm{Fm} \to \mathrm{Fm}$ is the same as a substitution $\sigma$, namely $\sigma(p) = h(p)$ for each variable $p$, since both are fixed by their values on the variables.

Part A: $\Gamma \vdash \varphi$ implies $\Gamma \models_{\mathcal{K}} \varphi$.

1. Assume $\Gamma \vdash \varphi$. Let $T$ be closed, and let $\sigma$ be a valuation in $\langle \mathrm{Fm}, T \rangle$ with $\sigma[\Gamma] \subseteq T$.
2. By structurality, $\sigma[\Gamma] \vdash \sigma(\varphi)$.
3. By monotonicity, $T \vdash \sigma(\varphi)$, since $\sigma[\Gamma] \subseteq T$.
4. $T$ is closed, so $\sigma(\varphi) \in T$. Hence $\Gamma \models_{\langle \mathrm{Fm}, T \rangle} \varphi$ for every closed $T$.

Part B: $\Gamma \models_{\mathcal{K}} \varphi$ implies $\Gamma \vdash \varphi$.

5. Let $T = \mathrm{Cn}(\Gamma) = \set{\psi : \Gamma \vdash \psi}$.
6. $T$ is closed: if $T \vdash \chi$, then $\Gamma \cup T \vdash \chi$ by monotonicity, and cut with $\Delta = T$ gives $\Gamma \vdash \chi$.
7. The identity map $\mathrm{id}$ is a valuation in $\langle \mathrm{Fm}, T \rangle$, and $\mathrm{id}[\Gamma] = \Gamma \subseteq T$ by reflexivity.
8. Since $\langle \mathrm{Fm}, T \rangle \in \mathcal{K}$, the assumption gives $\mathrm{id}(\varphi) = \varphi \in T$, that is, $\Gamma \vdash \varphi$.

Part C: item 2.

9. If $\emptyset \vdash \varphi$, then structurality gives $\emptyset \vdash \sigma(\varphi)$ for every $\sigma$, so $\sigma(\varphi) \in \mathrm{Cn}(\emptyset)$, and $\varphi$ is a tautology of $\langle \mathrm{Fm}, \mathrm{Cn}(\emptyset) \rangle$.
10. If $\varphi$ is a tautology of this matrix, take $\sigma = \mathrm{id}$: then $\varphi \in \mathrm{Cn}(\emptyset)$, so $\emptyset \vdash \varphi$.

Part D: item 3.

11. If $\vdash$ is structural, Parts A and B show that $\vdash$ equals $\models_{\mathcal{K}}$ for a class $\mathcal{K}$ of matrices.
12. Conversely, every $\models_{\mathcal{K}'}$ is structural, by Remark 2 of [[the definition of a logical matrix|AJEJS6TFWP]].

This proves the theorem.

## Idea

The formulas serve as their own truth values, and a theory serves as the set of true formulas.
Structurality makes every substitution respect $\vdash$, which gives soundness; the identity valuation into the theory of $\Gamma$ gives completeness.

## Variants

One can use the single bundle of matrices with closed sets $T$ that are maximal with respect to not containing a given formula; Lindenbaum's lemma produces them for finitary logics.
For a logic with an algebraic semantics, one passes from $\langle \mathrm{Fm}, T \rangle$ to the quotient by the largest congruence compatible with $T$; for classical logic this quotient is a [[Boolean algebra|0XADJKM699]].
