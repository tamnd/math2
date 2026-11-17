---
tag: 4S9W7VVKT9
kind: proof
name: Proof of the second incompleteness theorem
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
proves: 4PZM5GJTR5
uses: [F6H4STF9RG, 3PRW76471J, X9WYNYE29C, 4NBAX3VRQ7, NB2BCZR40F]
methods: [0NTF6DMVAP, 0BB5TPGQ1N]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Bernays_provability_conditions
    locator: Use in proving Gödel's incompleteness theorems
  - book: isbn:9780521857840
---

## Proof

Write $\square \varphi$ for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$ and $\bot$ for the sentence $0 = S0$.
So $\mathrm{Con}(T)$ is $\neg \square \bot$.
The [[derivability conditions|F6H4STF9RG]] D1, D2 and D3 hold for $T$.
From D1 and D2: if $T \vdash \varphi \to \psi$, then $T \vdash \square \varphi \to \square \psi$.
We call this rule (M).

1. By the [[diagonal lemma|3PRW76471J]], let $G$ satisfy $T \vdash G \leftrightarrow \neg \square G$.
2. From step 1, $T \vdash \square G \to \neg G$, by contraposition.
3. By (M) applied to step 2, $T \vdash \square \square G \to \square \neg G$.
4. By D3, $T \vdash \square G \to \square \square G$. With step 3, $T \vdash \square G \to \square \neg G$.
5. The formula $G \to (\neg G \to \bot)$ is a tautology, so $T$ proves it.
6. By D1 applied to step 5, $T \vdash \square (G \to (\neg G \to \bot))$. By D2 twice, $T \vdash \square G \to (\square \neg G \to \square \bot)$.
7. From steps 4 and 6, $T \vdash \square G \to \square \bot$.
8. By contraposition, $T \vdash \neg \square \bot \to \neg \square G$, that is, $T \vdash \mathrm{Con}(T) \to \neg \square G$.
9. With step 1, $T \vdash \mathrm{Con}(T) \to G$.
10. Assume $T$ is consistent and $T \vdash \mathrm{Con}(T)$. By step 9, $T \vdash G$.
11. Part 1 of the [[first incompleteness theorem|X9WYNYE29C]] says that a consistent $T$ does not prove $G$. This contradicts step 10, so $T \nvdash \mathrm{Con}(T)$.

The converse implication.

12. $T \vdash \neg (0 = S0)$, by axiom 1 of $\mathsf{Q}$. So $T \vdash \bot \to G$.
13. By (M) applied to step 12, $T \vdash \square \bot \to \square G$.
14. By contraposition and step 1, $T \vdash \neg \square G \to \neg \square \bot$, so $T \vdash G \to \mathrm{Con}(T)$.
15. Steps 9 and 14 give $T \vdash \mathrm{Con}(T) \leftrightarrow G$.

## Idea

The proof of part 1 of the first theorem shows "if $T$ is consistent, then $G$ is not provable", and $G$ says "$G$ is not provable".
The derivability conditions let $T$ carry out this proof about itself, which gives $T \vdash \mathrm{Con}(T) \to G$.
So a proof of $\mathrm{Con}(T)$ in $T$ would give a proof of $G$, which part 1 forbids.

## Variants

[[Löb's theorem|3HD30YG3DG]] gives a shorter route: if $T \vdash \mathrm{Con}(T)$, then $T \vdash \square \bot \to \bot$, so $T \vdash \bot$ by Löb's theorem.
The proof by the [[Rosser provability predicate|Z0H1KA8ZHT]] does not work, because that predicate fails D2 or D3.
Rule (M) applied to step 9 gives $T \vdash \square \mathrm{Con}(T) \to \square G$.
With step 7, $T \vdash \square \mathrm{Con}(T) \to \square \bot$, which is the formalized version $T \vdash \mathrm{Con}(T) \to \neg \square \mathrm{Con}(T)$.
