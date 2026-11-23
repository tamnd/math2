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

We show inside $T$ that $\mathrm{Con}(T)$ implies the Gödel sentence, and then we apply the first incompleteness theorem.

Write $\square \varphi$ for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$, and write $\bot$ for the sentence $0 = S0$, so that $\mathrm{Con}(T)$ is $\neg \square \bot$.
The [[derivability conditions|F6H4STF9RG]] hold for $T$.
D1 says that $T \vdash \varphi$ gives $T \vdash \square \varphi$.
D2 says that $T \vdash \square (\varphi \to \psi) \to (\square \varphi \to \square \psi)$.
D3 says that $T \vdash \square \varphi \to \square \square \varphi$.
From D1 and D2 we get the rule (M): if $T \vdash \varphi \to \psi$, then $T \vdash \square \varphi \to \square \psi$.

1. By the [[diagonal lemma|3PRW76471J]], we fix a sentence $G$ with $T \vdash G \leftrightarrow \neg \square G$.
2. Step 1 gives $T \vdash G \to \neg \square G$, and contraposition gives $T \vdash \square G \to \neg G$.
3. We apply (M) to step 2 and get $T \vdash \square \square G \to \square \neg G$.
4. D3 gives $T \vdash \square G \to \square \square G$.
   Together with step 3, $T \vdash \square G \to \square \neg G$.
5. The formula $G \to (\neg G \to \bot)$ is a tautology, so $T$ proves it.
6. D1 applied to step 5 gives $T \vdash \square (G \to (\neg G \to \bot))$.
   Two uses of D2 then give $T \vdash \square G \to (\square \neg G \to \square \bot)$.
7. Steps 4 and 6 give $T \vdash \square G \to \square \bot$, by propositional logic.
8. By contraposition, $T \vdash \neg \square \bot \to \neg \square G$, that is, $T \vdash \mathrm{Con}(T) \to \neg \square G$.
9. Step 1 replaces $\neg \square G$ by $G$, so $T \vdash \mathrm{Con}(T) \to G$.
10. Assume that $T$ is consistent and that $T \vdash \mathrm{Con}(T)$.
    Then step 9 gives $T \vdash G$.
11. Part 1 of the [[first incompleteness theorem|X9WYNYE29C]] says that a consistent $T$ does not prove $G$.
    This contradicts step 10, so $T \nvdash \mathrm{Con}(T)$.

Next we prove the equivalence of $\mathrm{Con}(T)$ with $G$.

12. Axiom 1 of $\mathsf{Q}$ gives $T \vdash \neg (0 = S0)$, so $T \vdash \bot \to G$ by propositional logic.
13. We apply (M) to step 12 and get $T \vdash \square \bot \to \square G$.
14. By contraposition, $T \vdash \neg \square G \to \neg \square \bot$.
    With step 1 this is $T \vdash G \to \mathrm{Con}(T)$.
15. Steps 9 and 14 give $T \vdash \mathrm{Con}(T) \leftrightarrow G$.

Last, we prove the formalized form.

16. We apply (M) to step 9 and get $T \vdash \square \mathrm{Con}(T) \to \square G$.
17. With step 7, $T \vdash \square \mathrm{Con}(T) \to \square \bot$.
18. By contraposition, $T \vdash \neg \square \bot \to \neg \square \mathrm{Con}(T)$, that is, $T \vdash \mathrm{Con}(T) \to \neg \square \mathrm{Con}(T)$.

This proves the three parts of the [[second incompleteness theorem|4PZM5GJTR5]].

## Idea

Part 1 of the first theorem is the implication "if $T$ is consistent, then $T$ does not prove $G$", and $G$ says "$T$ does not prove $G$".
So the implication says "if $T$ is consistent, then $G$", and the derivability conditions let $T$ prove exactly that, in steps 2 to 9.
Once $T \vdash \mathrm{Con}(T) \to G$ is known, a proof of $\mathrm{Con}(T)$ would turn into a proof of $G$.
Step 4 is the heart of the proof: D3 lets $T$ see that a proof of $G$ yields a proof of "$G$ is provable", which is a proof of $\neg G$.

## Variants

[[Löb's theorem|3HD30YG3DG]] gives a shorter route once it is proved.
If $T \vdash \mathrm{Con}(T)$, then $T \vdash \square \bot \to \bot$, because $\neg \square \bot$ implies every implication with premise $\square \bot$.
Löb's theorem then gives $T \vdash \bot$, so $T$ is inconsistent.

The argument does not work for the [[Rosser provability predicate|Z0H1KA8ZHT]], because that predicate does not satisfy all of D1 to D3 in $T$.
This is why $T$ proves the Rosser consistency statement.

In [[provability logic|WJK0YA4GP2]], steps 1 to 9 are a derivation in the modal logic $\mathsf{K4}$ from the fixed point $G \leftrightarrow \neg \square G$.
