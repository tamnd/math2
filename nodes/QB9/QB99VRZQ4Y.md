---
tag: QB99VRZQ4Y
kind: proof
name: Proof of the law of contraposition by rules of inference
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: ug1
proves: 04T1CT7212
uses: [0Y0MQYST0M, 0XR7A7RSXB, 0ZNX6DQ3EJ, 0RYYK8PG4S, TTKZGJEEK7, 6KT3BJZ7D1]
methods: [0NTF6DMVAP, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Contraposition
    locator: lead section
  - book: isbn:9781447145578
    locator: Chapter 1
---

## Proof

We prove the two directions separately, with the rules of [[natural deduction|6KT3BJZ7D1]].
We read $\neg \chi$ as "$\chi$ leads to a contradiction", that is, $\chi \to \bot$, where $\bot$ is the false formula.
We mark the single step that uses the [[law of excluded middle|0RYYK8PG4S]].

Direction (a): from $\varphi \to \psi$ we derive $\neg \psi \to \neg \varphi$.

1. Assume $\varphi \to \psi$. Reason: hypothesis of direction (a).
2. Assume $\neg \psi$, in order to prove $\neg \varphi$. Reason: to prove an [[implication|0ZNX6DQ3EJ]], we assume its antecedent.
3. Assume $\varphi$, in order to reach a contradiction. Reason: to prove $\neg \varphi$, we assume $\varphi$ and derive $\bot$.
4. From steps 1 and 3 we get $\psi$. Reason: [[modus ponens|0Y0MQYST0M]].
5. From steps 2 and 4 we get $\bot$. Reason: $\neg \psi$ and $\psi$ together give a contradiction, by the definition of [[negation|0XR7A7RSXB]].
6. Steps 3 to 5 give $\neg \varphi$ and discharge the assumption $\varphi$. Reason: negation introduction.
7. Steps 2 to 6 give $\neg \psi \to \neg \varphi$ and discharge the assumption $\neg \psi$. Reason: implication introduction.

No step of direction (a) uses excluded middle, so direction (a) holds in [[intuitionistic logic|Q11N8X99FK]].

Direction (b): from $\neg \psi \to \neg \varphi$ we derive $\varphi \to \psi$.

8. Assume $\neg \psi \to \neg \varphi$. Reason: hypothesis of direction (b).
9. Assume $\varphi$, in order to prove $\psi$. Reason: to prove an implication, we assume its antecedent.
10. We have $\psi \lor \neg \psi$. Reason: the law of excluded middle. This is the only classical step.
11. Case 1: $\psi$ holds. Then $\psi$ is the required conclusion.
12. Case 2: $\neg \psi$ holds. Together with step 8, this gives $\neg \varphi$. Reason: modus ponens.
13. In case 2, $\varphi$ from step 9 and $\neg \varphi$ from step 12 give $\bot$. Reason: definition of negation.
14. In case 2, $\bot$ gives $\psi$. Reason: the principle of [[explosion|TTKZGJEEK7]].
15. Both cases give $\psi$. Reason: [[proof by cases|0WCP0PVET6]], applied to the disjunction of step 10.
16. Steps 9 to 15 give $\varphi \to \psi$ and discharge the assumption $\varphi$. Reason: implication introduction.

Directions (a) and (b) together give $\varphi \to \psi \equiv \neg \psi \to \neg \varphi$.
$\blacksquare$

## Idea

Direction (a) is modus ponens followed by a contradiction: if $\varphi$ held, then $\psi$ would hold, against $\neg \psi$.
Direction (b) must produce the positive statement $\psi$ from negative information, and this needs a classical principle.
Here it is excluded middle on $\psi$, followed by a case analysis.
The same split appears in Lean: `mt` proves direction (a) with no axiom, and `not_imp_not` uses classical logic for direction (b).

## Variants

Direction (b) can use double negation elimination instead of excluded middle.
Assume $\varphi$ and $\neg \psi$; then $\neg \varphi$ by modus ponens, and $\bot$ with $\varphi$; so $\neg\neg \psi$ by negation introduction; then $\psi$ by [[double negation elimination|0NFAGWH84K]].
This is the form of a [[proof by contradiction|0J0XBKG64S]].
The [[truth table proof|SWH5EJP8PS]] proves both directions at once, but it gives no information about intuitionistic logic.
