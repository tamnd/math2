---
tag: 6GCSRKJ0SQ
kind: proof
name: Proof of Löb's theorem
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
proves: 3HD30YG3DG
uses: [F6H4STF9RG, 3PRW76471J, NB2BCZR40F]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Löb's_theorem
    locator: Proof of Löb's theorem
  - book: isbn:9780521857840
---

## Proof

Write $\square \varphi$ for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.
The [[derivability conditions|F6H4STF9RG]] D1, D2 and D3 hold for $T$.
Rule (M): if $T \vdash \alpha \to \beta$, then $T \vdash \square \alpha \to \square \beta$.
It follows from D1 and D2.

Part 1.

1. Assume $T \vdash \square \varphi \to \varphi$.
2. By the [[diagonal lemma|3PRW76471J]], let $\psi$ satisfy $T \vdash \psi \leftrightarrow (\square \psi \to \varphi)$.
3. From step 2, $T \vdash \psi \to (\square \psi \to \varphi)$.
4. By (M) applied to step 3, $T \vdash \square \psi \to \square (\square \psi \to \varphi)$.
5. By D2, $T \vdash \square (\square \psi \to \varphi) \to (\square \square \psi \to \square \varphi)$.
6. From steps 4 and 5, $T \vdash \square \psi \to (\square \square \psi \to \square \varphi)$.
7. By D3, $T \vdash \square \psi \to \square \square \psi$.
8. From steps 6 and 7, $T \vdash \square \psi \to \square \varphi$.
9. From steps 1 and 8, $T \vdash \square \psi \to \varphi$.
10. By step 2, the right side of the equivalence is provable, so $T \vdash \psi$.
11. By D1, $T \vdash \square \psi$.
12. From steps 9 and 11, $T \vdash \varphi$.

Part 2, the formalized form.
Steps 2 to 8 did not use step 1, so $T \vdash \square \psi \to \square \varphi$ holds for every $\varphi$.

13. The formula $(\square \varphi \to \varphi) \to ((\square \psi \to \square \varphi) \to (\square \psi \to \varphi))$ is a tautology. With step 8, $T \vdash (\square \varphi \to \varphi) \to (\square \psi \to \varphi)$.
14. With step 2, $T \vdash (\square \varphi \to \varphi) \to \psi$.
15. By (M), $T \vdash \square (\square \varphi \to \varphi) \to \square \psi$.
16. With step 8, $T \vdash \square (\square \varphi \to \varphi) \to \square \varphi$.

## Idea

The sentence $\psi$ says "if I am provable, then $\varphi$".
The derivability conditions let $T$ check that a proof of $\psi$ gives a proof of $\varphi$, and the hypothesis turns that into $\varphi$ itself.
So $T$ proves exactly what $\psi$ says, hence proves $\psi$, and then $\varphi$.

## Variants

Part 1 follows from Part 2: apply D1 to the hypothesis to get $T \vdash \square (\square \varphi \to \varphi)$, so $T \vdash \square \varphi$ by Part 2, and $T \vdash \varphi$ by the hypothesis.
Another proof derives Part 1 from the second incompleteness theorem for $T + \neg \varphi$: if $T \nvdash \varphi$, then $T + \neg \varphi$ is consistent and cannot prove its own consistency, while the hypothesis lets it prove it.
In [[provability logic|WJK0YA4GP2]], the proof is a derivation in the modal logic $\mathsf{K4}$ with a fixed point for $\psi$.
