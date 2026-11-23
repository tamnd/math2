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

We prove soundness with structurality, completeness with the identity valuation into the theory of $\Gamma$, and then the two remaining items.
We use the notation of [[the statement|VWJVAS3VE3]].
A homomorphism $h \colon \mathrm{Fm} \to \mathrm{Fm}$ is the same as a substitution $\sigma$, with $\sigma(p) = h(p)$ for each variable $p$, since both are fixed by their values on the variables.

First, $\Gamma \vdash \varphi$ implies $\Gamma \models_{\mathcal{K}} \varphi$.

1. Assume $\Gamma \vdash \varphi$.
   Let $T$ be closed, and let $\sigma$ be a valuation in $\langle \mathrm{Fm}, T \rangle$ with $\sigma[\Gamma] \subseteq T$.
2. Structurality gives $\sigma[\Gamma] \vdash \sigma(\varphi)$.
3. Monotonicity gives $T \vdash \sigma(\varphi)$, since $\sigma[\Gamma] \subseteq T$.
4. The set $T$ is closed, so $\sigma(\varphi) \in T$.
   Since $T$ and $\sigma$ were arbitrary, $\Gamma \models_{\mathcal{K}} \varphi$.

Second, $\Gamma \models_{\mathcal{K}} \varphi$ implies $\Gamma \vdash \varphi$.

5. Put $T = \mathrm{Cn}(\Gamma) = \{\psi : \Gamma \vdash \psi\}$.
6. The set $T$ is closed.
   If $T \vdash \chi$, then $\Gamma \cup T \vdash \chi$ by monotonicity, and cut with $\Delta = T$ gives $\Gamma \vdash \chi$, so $\chi \in T$.
7. The identity map is a valuation in $\langle \mathrm{Fm}, T \rangle$, and it sends $\Gamma$ into $T$, because reflexivity gives $\Gamma \vdash \gamma$ for each $\gamma \in \Gamma$.
8. Since $\langle \mathrm{Fm}, T \rangle \in \mathcal{K}$, the assumption gives $\varphi \in T$, that is, $\Gamma \vdash \varphi$.

Third, item 2.

9. If $\emptyset \vdash \varphi$, structurality gives $\emptyset \vdash \sigma(\varphi)$ for every $\sigma$.
   So $\sigma(\varphi) \in \mathrm{Cn}(\emptyset)$ for every valuation $\sigma$, and $\varphi$ is a tautology of $\langle \mathrm{Fm}, \mathrm{Cn}(\emptyset) \rangle$.
10. If $\varphi$ is a tautology of this matrix, take $\sigma$ to be the identity.
    Then $\varphi \in \mathrm{Cn}(\emptyset)$, so $\emptyset \vdash \varphi$.

Fourth, item 3.

11. If $\vdash$ is structural, steps 1 to 8 show that $\vdash$ equals $\models_{\mathcal{K}}$ for the class $\mathcal{K}$ of its Lindenbaum matrices.
12. Conversely, every relation $\models_{\mathcal{K}'}$ is structural, by the remarks of [[the definition of a logical matrix|AJEJS6TFWP]].

This proves the three items of the theorem.

## Idea

The formulas serve as their own truth values, and a theory serves as the set of true formulas.
Structurality makes every substitution respect $\vdash$, and that gives soundness for every Lindenbaum matrix at once.
For completeness, one matrix is enough: the identity valuation into the theory of $\Gamma$ designates $\Gamma$, so it designates $\varphi$ only if $\Gamma \vdash \varphi$.

## Variants

For a finitary logic you can use a smaller class: the closed sets that are maximal among those not containing a given formula.
Lindenbaum's lemma produces such sets, and they are enough to refute every invalid inference.
For a logic with an algebraic semantics, you then pass from $\langle \mathrm{Fm}, T \rangle$ to its quotient by the largest congruence compatible with $T$.
For classical logic and $T = \mathrm{Cn}(\emptyset)$ this quotient is a [[Boolean algebra|0XADJKM699]].
