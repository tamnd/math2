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

We build the sentence "if I am provable, then $\varphi$", show that its provability implies the provability of $\varphi$, and use the hypothesis to prove the sentence itself.

Write $\square \varphi$ for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.
The [[derivability conditions|F6H4STF9RG]] hold for $T$.
D1 says that $T \vdash \alpha$ gives $T \vdash \square \alpha$.
D2 says that $T \vdash \square (\alpha \to \beta) \to (\square \alpha \to \square \beta)$.
D3 says that $T \vdash \square \alpha \to \square \square \alpha$.
From D1 and D2 we get the rule (M): if $T \vdash \alpha \to \beta$, then $T \vdash \square \alpha \to \square \beta$.

### Part 1

1. Assume that $T \vdash \square \varphi \to \varphi$.
2. By the [[diagonal lemma|3PRW76471J]], we fix a sentence $\psi$ with $T \vdash \psi \leftrightarrow (\square \psi \to \varphi)$.
3. The direction from left to right in step 2 is $T \vdash \psi \to (\square \psi \to \varphi)$.
4. Rule (M) applied to step 3 gives $T \vdash \square \psi \to \square (\square \psi \to \varphi)$.
5. D2 gives $T \vdash \square (\square \psi \to \varphi) \to (\square \square \psi \to \square \varphi)$.
6. Steps 4 and 5 give $T \vdash \square \psi \to (\square \square \psi \to \square \varphi)$, by chaining the implications.
7. D3 gives $T \vdash \square \psi \to \square \square \psi$.
8. Steps 6 and 7 give $T \vdash \square \psi \to \square \varphi$, by propositional logic.
9. Steps 1 and 8 give $T \vdash \square \psi \to \varphi$, by chaining the implications.
10. Step 9 proves the right side of step 2, so the direction from right to left in step 2 gives $T \vdash \psi$.
11. D1 applied to step 10 gives $T \vdash \square \psi$.
12. Steps 9 and 11 give $T \vdash \varphi$, by modus ponens.

### Part 2, the formalized form

Steps 2 to 8 did not use the hypothesis of step 1, so $T \vdash \square \psi \to \square \varphi$ holds for every $\varphi$.

13. The formula $(\square \varphi \to \varphi) \to ((\square \psi \to \square \varphi) \to (\square \psi \to \varphi))$ is a tautology.
    With step 8, it gives $T \vdash (\square \varphi \to \varphi) \to (\square \psi \to \varphi)$.
14. The direction from right to left in step 2 turns this into $T \vdash (\square \varphi \to \varphi) \to \psi$.
15. Rule (M) applied to step 14 gives $T \vdash \square (\square \varphi \to \varphi) \to \square \psi$.
16. Steps 15 and 8 give $T \vdash \square (\square \varphi \to \varphi) \to \square \varphi$.

This proves both parts of [[Löb's theorem|3HD30YG3DG]].

## Idea

The sentence $\psi$ says "if I am provable, then $\varphi$".
The derivability conditions let $T$ see that a proof of $\psi$ gives a proof of $\varphi$, in steps 3 to 8.
The hypothesis turns "a proof of $\varphi$" into $\varphi$ itself, so $T$ proves exactly what $\psi$ says, and that is a proof of $\psi$.
Once $\psi$ is proved, it is provable, and what it says delivers $\varphi$.
For $\varphi := (0 = S0)$, the sentence $\psi$ is "if I am provable, then $0 = 1$", and the argument becomes the second incompleteness theorem.

## Variants

Part 1 also follows from Part 2.
Apply D1 to the hypothesis to get $T \vdash \square (\square \varphi \to \varphi)$, then Part 2 gives $T \vdash \square \varphi$, and the hypothesis gives $T \vdash \varphi$.

A second proof derives Part 1 from the [[second incompleteness theorem|4PZM5GJTR5]] for the theory $T + \neg \varphi$.
If $T \nvdash \varphi$, then $T + \neg \varphi$ is consistent.
Its consistency statement is provably equivalent to $\neg \square \varphi$, and the hypothesis gives $T + \neg \varphi \vdash \neg \square \varphi$.
So $T + \neg \varphi$ proves its own consistency, which the second theorem forbids.

In [[provability logic|WJK0YA4GP2]], steps 2 to 16 are a derivation in the modal logic $\mathsf{K4}$ from the fixed point $\psi \leftrightarrow (\square \psi \to \varphi)$.
