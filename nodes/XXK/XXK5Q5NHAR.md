---
tag: XXK5Q5NHAR
kind: proof
name: Proof of the basic theorems of the Hilbert system L
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
proves: Y060MF2NZ7
uses: [1MGMQX43B8, 9X08XK5RV2, 0Y0MQYST0M]
methods: [0NTF6DMVAP]
sources:
  - book: isbn:9781482237726
    locator: Chapter 1
  - url: https://en.wikipedia.org/wiki/Deduction_theorem
    locator: Helpful theorems
---

## Proof

We derive T1 directly from the axioms, and for each other law we derive the consequent from the antecedents and then remove them with the deduction theorem.

We use three general facts about derivations in the [[Hilbert system|1MGMQX43B8]] L.
(F1) If $\Gamma \subseteq \Gamma'$ and $\Gamma \vdash \varphi$, then $\Gamma' \vdash \varphi$, because a derivation from $\Gamma$ is also a derivation from $\Gamma'$.
(F2) If $\vdash \varphi$, then $\varphi$ may be written as a line of any derivation, because a derivation of $\varphi$ can be inserted before that line.
(F3) The [[deduction theorem|9X08XK5RV2]]: $\Gamma \cup \{ \varphi \} \vdash \psi$ holds if and only if $\Gamma \vdash \varphi \to \psi$.

To keep substitutions apart from the formulas $\varphi$, $\psi$, $\chi$ of the statement, we write the axiom schemas with the letters $\alpha$, $\beta$, $\gamma$:
$$\begin{array}{ll} \text{(A1)} & \alpha \to (\beta \to \alpha), \\ \text{(A2)} & (\alpha \to (\beta \to \gamma)) \to ((\alpha \to \beta) \to (\alpha \to \gamma)), \\ \text{(A3)} & (\neg \beta \to \neg \alpha) \to ((\neg \beta \to \alpha) \to \beta). \end{array}$$
When we use an earlier law T$k$ at an instance, the substitution is simultaneous.
We write MP $i, j$ for [[modus ponens|0Y0MQYST0M]] applied to line $i$, the formula $\alpha$, and line $j$, the formula $\alpha \to \beta$.
"Hyp" marks a hypothesis.

**T1.** The following five lines derive $\varphi \to \varphi$ from no hypotheses.

1. $\varphi \to ((\varphi \to \varphi) \to \varphi)$, by A1 with $\alpha := \varphi$, $\beta := \varphi \to \varphi$.
2. $(\varphi \to ((\varphi \to \varphi) \to \varphi)) \to ((\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi))$, by A2 with $\alpha := \varphi$, $\beta := \varphi \to \varphi$, $\gamma := \varphi$.
3. $(\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi)$, by MP 1, 2.
4. $\varphi \to (\varphi \to \varphi)$, by A1 with $\alpha := \varphi$, $\beta := \varphi$.
5. $\varphi \to \varphi$, by MP 4, 3.

**T2.** We derive $\varphi$ from $\{ \neg \neg \varphi \}$.

1. $\neg \neg \varphi$, Hyp.
2. $\neg \neg \varphi \to (\neg \varphi \to \neg \neg \varphi)$, by A1 with $\alpha := \neg \neg \varphi$, $\beta := \neg \varphi$.
3. $\neg \varphi \to \neg \neg \varphi$, by MP 1, 2.
4. $(\neg \varphi \to \neg \neg \varphi) \to ((\neg \varphi \to \neg \varphi) \to \varphi)$, by A3 with $\alpha := \neg \varphi$, $\beta := \varphi$.
5. $(\neg \varphi \to \neg \varphi) \to \varphi$, by MP 3, 4.
6. $\neg \varphi \to \neg \varphi$, by T1 for the formula $\neg \varphi$ and (F2).
7. $\varphi$, by MP 6, 5.
8. So $\{ \neg \neg \varphi \} \vdash \varphi$, and (F3) with $\Gamma = \emptyset$ gives $\vdash \neg \neg \varphi \to \varphi$.

**T3.** We derive $\neg \neg \varphi$ from $\{ \varphi \}$.

1. $\varphi$, Hyp.
2. $\varphi \to (\neg \neg \neg \varphi \to \varphi)$, by A1 with $\alpha := \varphi$, $\beta := \neg \neg \neg \varphi$.
3. $\neg \neg \neg \varphi \to \varphi$, by MP 1, 2.
4. $\neg \neg \neg \varphi \to \neg \varphi$, by T2 for the formula $\neg \varphi$ and (F2).
5. $(\neg \neg \neg \varphi \to \neg \varphi) \to ((\neg \neg \neg \varphi \to \varphi) \to \neg \neg \varphi)$, by A3 with $\alpha := \varphi$, $\beta := \neg \neg \varphi$.
6. $(\neg \neg \neg \varphi \to \varphi) \to \neg \neg \varphi$, by MP 4, 5.
7. $\neg \neg \varphi$, by MP 3, 6.
8. So $\{ \varphi \} \vdash \neg \neg \varphi$, and (F3) gives $\vdash \varphi \to \neg \neg \varphi$.

**T4.** We derive $\psi$ from $\{ \neg \varphi, \ \varphi \}$.

1. $\neg \varphi$, Hyp.
2. $\varphi$, Hyp.
3. $\neg \varphi \to (\neg \psi \to \neg \varphi)$, by A1 with $\alpha := \neg \varphi$, $\beta := \neg \psi$.
4. $\neg \psi \to \neg \varphi$, by MP 1, 3.
5. $\varphi \to (\neg \psi \to \varphi)$, by A1 with $\alpha := \varphi$, $\beta := \neg \psi$.
6. $\neg \psi \to \varphi$, by MP 2, 5.
7. $(\neg \psi \to \neg \varphi) \to ((\neg \psi \to \varphi) \to \psi)$, by A3 with $\alpha := \varphi$, $\beta := \psi$.
8. $(\neg \psi \to \varphi) \to \psi$, by MP 4, 7.
9. $\psi$, by MP 6, 8.
10. So $\{ \neg \varphi, \ \varphi \} \vdash \psi$.
    Then (F3) gives $\{ \neg \varphi \} \vdash \varphi \to \psi$, and (F3) again gives $\vdash \neg \varphi \to (\varphi \to \psi)$.

**T5.** We derive $\psi$ from $\{ \neg \psi \to \neg \varphi, \ \varphi \}$.

1. $\neg \psi \to \neg \varphi$, Hyp.
2. $\varphi$, Hyp.
3. $(\neg \psi \to \neg \varphi) \to ((\neg \psi \to \varphi) \to \psi)$, by A3 with $\alpha := \varphi$, $\beta := \psi$.
4. $(\neg \psi \to \varphi) \to \psi$, by MP 1, 3.
5. $\varphi \to (\neg \psi \to \varphi)$, by A1 with $\alpha := \varphi$, $\beta := \neg \psi$.
6. $\neg \psi \to \varphi$, by MP 2, 5.
7. $\psi$, by MP 6, 4.
8. So $\{ \neg \psi \to \neg \varphi, \ \varphi \} \vdash \psi$, and (F3) used twice gives $\vdash (\neg \psi \to \neg \varphi) \to (\varphi \to \psi)$.

**T6.** We derive $\neg \neg \psi$ from $\{ \varphi \to \psi, \ \neg \neg \varphi \}$, and then use T5.

1. $\varphi \to \psi$, Hyp.
2. $\neg \neg \varphi$, Hyp.
3. $\neg \neg \varphi \to \varphi$, by T2 and (F2).
4. $\varphi$, by MP 2, 3.
5. $\psi$, by MP 4, 1.
6. $\psi \to \neg \neg \psi$, by T3 for the formula $\psi$ and (F2).
7. $\neg \neg \psi$, by MP 5, 6.
8. So $\{ \varphi \to \psi, \ \neg \neg \varphi \} \vdash \neg \neg \psi$, and (F3) gives $\{ \varphi \to \psi \} \vdash \neg \neg \varphi \to \neg \neg \psi$.
9. T5 with $\neg \psi$ in place of $\varphi$ and $\neg \varphi$ in place of $\psi$ gives $\vdash (\neg \neg \varphi \to \neg \neg \psi) \to (\neg \psi \to \neg \varphi)$.
10. By (F1) and MP with steps 8 and 9, $\{ \varphi \to \psi \} \vdash \neg \psi \to \neg \varphi$.
11. Then (F3) gives $\vdash (\varphi \to \psi) \to (\neg \psi \to \neg \varphi)$.

**T7.** We derive $\psi$ from $\{ \varphi, \ \varphi \to \psi \}$, and then use T6.

1. $\varphi$, Hyp.
2. $\varphi \to \psi$, Hyp.
3. $\psi$, by MP 1, 2.
4. So $\{ \varphi, \ \varphi \to \psi \} \vdash \psi$, and (F3) gives $\{ \varphi \} \vdash (\varphi \to \psi) \to \psi$.
5. T6 with $\varphi \to \psi$ in place of $\varphi$ gives $\vdash ((\varphi \to \psi) \to \psi) \to (\neg \psi \to \neg (\varphi \to \psi))$.
6. By (F1) and MP with steps 4 and 5, $\{ \varphi \} \vdash \neg \psi \to \neg (\varphi \to \psi)$.
7. Then (F3) gives $\vdash \varphi \to (\neg \psi \to \neg (\varphi \to \psi))$.

**T8.** We derive $\psi$ from $\{ \varphi \to \psi, \ \neg \varphi \to \psi \}$.

1. $\varphi \to \psi$, Hyp.
2. $\neg \varphi \to \psi$, Hyp.
3. $(\varphi \to \psi) \to (\neg \psi \to \neg \varphi)$, by T6 and (F2).
4. $\neg \psi \to \neg \varphi$, by MP 1, 3.
5. $(\neg \varphi \to \psi) \to (\neg \psi \to \neg \neg \varphi)$, by T6 with $\neg \varphi$ in place of $\varphi$, and (F2).
6. $\neg \psi \to \neg \neg \varphi$, by MP 2, 5.
7. $(\neg \psi \to \neg \neg \varphi) \to ((\neg \psi \to \neg \varphi) \to \psi)$, by A3 with $\alpha := \neg \varphi$, $\beta := \psi$.
8. $(\neg \psi \to \neg \varphi) \to \psi$, by MP 6, 7.
9. $\psi$, by MP 4, 8.
10. So $\{ \varphi \to \psi, \ \neg \varphi \to \psi \} \vdash \psi$, and (F3) used twice gives $\vdash (\varphi \to \psi) \to ((\neg \varphi \to \psi) \to \psi)$.

**HS.** Assume $\Gamma \vdash \varphi \to \psi$ and $\Gamma \vdash \psi \to \chi$.

1. By (F1), $\Gamma \cup \{ \varphi \} \vdash \varphi \to \psi$ and $\Gamma \cup \{ \varphi \} \vdash \psi \to \chi$.
2. The formula $\varphi$ is a hypothesis, so $\Gamma \cup \{ \varphi \} \vdash \varphi$.
3. By MP with steps 2 and 1, $\Gamma \cup \{ \varphi \} \vdash \psi$.
4. By MP with step 3 and the second derivation of step 1, $\Gamma \cup \{ \varphi \} \vdash \chi$.
5. Then (F3) gives $\Gamma \vdash \varphi \to \chi$.

This proves T1 to T8 and HS for all formulas $\varphi$, $\psi$ and $\chi$.

## Idea

T1 is a direct derivation from A1 and A2, and it is the only part that does not use the deduction theorem.
For every other law we play the same game: assume the antecedents, reach the consequent with modus ponens, and give the assumptions back with the deduction theorem.
The axiom A3 is the only source of negation laws.
It gives the double negation laws T2 and T3 first, and the contraposition laws T5 and T6 are built from them.
Then T7 is T6 applied to modus ponens, and T8 is A3 fed with two contrapositions.

## Variants

The same laws can be derived without the deduction theorem, by expanding each use of it with the construction in its proof; the derivations then become much longer.
With Łukasiewicz's third axiom $(\neg \varphi \to \neg \psi) \to (\psi \to \varphi)$ in place of A3, T5 is an axiom instance, and the order of the derivations changes.
Another route uses the [[completeness theorem for propositional logic|81ZNY1XKYJ]], since each of T1 to T8 is a [[tautology|05006AJ7DZ]].
That route is circular here, because the standard proofs of completeness for L use T1 to T8.
