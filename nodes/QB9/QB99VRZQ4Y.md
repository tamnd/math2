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

We prove the two directions separately with the rules of [[natural deduction|6KT3BJZ7D1]], and we mark the single step that uses the [[law of excluded middle|0RYYK8PG4S]].
We read $\neg \chi$ as $\chi \to \bot$, where $\bot$ is the false formula.

Direction (a): from $\varphi \to \psi$ we derive $\neg \psi \to \neg \varphi$.

1. Assume $\varphi \to \psi$, the hypothesis of direction (a).
2. Assume $\neg \psi$, since to prove an [[implication|0ZNX6DQ3EJ]] we assume its antecedent.
3. Assume $\varphi$, since to prove $\neg \varphi$ we assume $\varphi$ and derive $\bot$.
4. From steps 1 and 3, we get $\psi$ by [[modus ponens|0Y0MQYST0M]].
5. From steps 2 and 4, we get $\bot$ by the definition of [[negation|0XR7A7RSXB]].
6. Steps 3 to 5 give $\neg \varphi$ by negation introduction, and discharge the assumption $\varphi$.
7. Steps 2 to 6 give $\neg \psi \to \neg \varphi$ by implication introduction, and discharge the assumption $\neg \psi$.
   No step of direction (a) uses excluded middle, so direction (a) holds in [[intuitionistic logic|Q11N8X99FK]].

Direction (b): from $\neg \psi \to \neg \varphi$ we derive $\varphi \to \psi$.

8. Assume $\neg \psi \to \neg \varphi$, the hypothesis of direction (b).
9. Assume $\varphi$, since to prove an implication we assume its antecedent.
10. By the law of excluded middle, $\psi \lor \neg \psi$.
    This is the only classical step, `Classical.em` in Lean.
11. Case $\psi$: then $\psi$ is the required conclusion.
12. Case $\neg \psi$: with step 8, modus ponens gives $\neg \varphi$.
13. In this case, $\varphi$ from step 9 and $\neg \varphi$ from step 12 give $\bot$.
14. In this case, $\bot$ gives $\psi$ by the principle of [[explosion|TTKZGJEEK7]].
15. Both cases give $\psi$, so $\psi$ holds by [[proof by cases|0WCP0PVET6]] on the disjunction of step 10.
16. Steps 9 to 15 give $\varphi \to \psi$ by implication introduction, and discharge the assumption $\varphi$.
17. Directions (a) and (b) together give $\varphi \to \psi \equiv \neg \psi \to \neg \varphi$. $\blacksquare$

## Idea

Direction (a) is modus ponens followed by a contradiction: if $\varphi$ held, then $\psi$ would hold, against $\neg \psi$.
Direction (b) must produce the positive statement $\psi$ from negative information, and this needs a classical principle.
Here the principle is excluded middle on $\psi$, followed by a case analysis.
The same split appears in Lean: `mt` proves direction (a) with no axiom, and `not_imp_not` uses classical logic for direction (b).

## Variants

Direction (b) can use double negation elimination instead of excluded middle.
Assume $\varphi$ and $\neg \psi$.
Then $\neg \varphi$ by modus ponens, and $\bot$ with $\varphi$, so $\neg\neg \psi$ by negation introduction.
Then $\psi$ follows by [[double negation elimination|0NFAGWH84K]].
This is the form of a [[proof by contradiction|0J0XBKG64S]].

The [[truth table proof|SWH5EJP8PS]] proves both directions at once, but it gives no information about intuitionistic logic.
