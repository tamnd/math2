---
tag: BZDZ15FMZT
kind: proof
name: Proof of the laws of propositional logic by truth tables
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
proves: A9CSGZNBV5
uses: [0JMR2HM2N2, 025YZN3VJW, 0F72FK8EKB, 029JBBF693, 05RSK4Q657, 09PKJKA6J0, 0NFAGWH84K]
methods: [05RSK4Q657, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_algebra
    locator: Laws
  - book: isbn:9781108439534
    locator: Section 1.2
---

## Proof

Two formulas are [[logically equivalent|0JMR2HM2N2]] when they have the same truth value in every row of their [[truth table|05RSK4Q657]].
For laws 1 to 7 we compute the columns of both sides and compare them.
We use the definitions of [[conjunction|025YZN3VJW]] ($a \land b$ is T only when $a$ and $b$ are both T) and of [[disjunction|0F72FK8EKB]] ($a \lor b$ is F only when $a$ and $b$ are both F).
The formula $\top$ is T in every row and $\bot$ is F in every row.

Part 1: the laws in one variable.

1. The variable $p$ has two rows, T and F.
2. Idempotent laws. In the row T, $p \land p$ and $p \lor p$ are T. In the row F, both are F. So both formulas have the column of $p$.
3. Identity laws. In the row T, $p \land \top$ is $\mathrm{T} \land \mathrm{T}$, which is T, and $p \lor \bot$ is $\mathrm{T} \lor \mathrm{F}$, which is T. In the row F, $p \land \top$ is $\mathrm{F} \land \mathrm{T}$, which is F, and $p \lor \bot$ is $\mathrm{F} \lor \mathrm{F}$, which is F. So both formulas have the column of $p$.
4. Domination laws. A disjunction with a true part is true, so $p \lor \top$ is T in both rows, like $\top$. A conjunction with a false part is false, so $p \land \bot$ is F in both rows, like $\bot$.

| $p$ | $p \land p$ | $p \lor p$ | $p \land \top$ | $p \lor \bot$ | $p \lor \top$ | $p \land \bot$ |
|---|---|---|---|---|---|---|
| T | T | T | T | T | T | F |
| F | F | F | F | F | T | F |

Part 2: the laws in two variables.

5. The variables $p$ and $q$ have four rows: TT, TF, FT and FF.
6. Commutative laws. The definitions of $\land$ and $\lor$ treat the two parts in the same way. So $p \land q$ and $q \land p$ are both T only in the row TT, and $p \lor q$ and $q \lor p$ are both F only in the row FF.
7. First absorption law. If $p$ is T, then $p \lor q$ is T, so $p \land (p \lor q)$ is T. If $p$ is F, then $p \land (p \lor q)$ is F, because a conjunction with a false part is false. So $p \land (p \lor q)$ has the column of $p$.
8. Second absorption law. If $p$ is T, then $p \lor (p \land q)$ is T. If $p$ is F, then $p \land q$ is F, so $p \lor (p \land q)$ is $\mathrm{F} \lor \mathrm{F}$, which is F. So $p \lor (p \land q)$ has the column of $p$.

| $p$ | $q$ | $p \land q$ | $q \land p$ | $p \lor q$ | $q \lor p$ | $p \land (p \lor q)$ | $p \lor (p \land q)$ |
|---|---|---|---|---|---|---|---|
| T | T | T | T | T | T | T | T |
| T | F | F | F | T | T | T | T |
| F | T | F | F | T | T | F | F |
| F | F | F | F | F | F | F | F |

Part 3: the laws in three variables.

9. The variables $p$, $q$ and $r$ have eight rows, listed in the standard order TTT, TTF, TFT, TFF, FTT, FTF, FFT, FFF.
10. Associative law for $\land$. Both $(p \land q) \land r$ and $p \land (q \land r)$ are T exactly when all three variables are T, that is, only in the row TTT.
11. Associative law for $\lor$. Both $(p \lor q) \lor r$ and $p \lor (q \lor r)$ are F exactly when all three variables are F, that is, only in the row FFF.

| $p$ | $q$ | $r$ | $p \land q$ | $(p \land q) \land r$ | $q \land r$ | $p \land (q \land r)$ | $p \lor q$ | $(p \lor q) \lor r$ | $q \lor r$ | $p \lor (q \lor r)$ |
|---|---|---|---|---|---|---|---|---|---|---|
| T | T | T | T | T | T | T | T | T | T | T |
| T | T | F | T | F | F | F | T | T | T | T |
| T | F | T | F | F | F | F | T | T | T | T |
| T | F | F | F | F | F | F | T | T | F | T |
| F | T | T | F | F | T | F | T | T | T | T |
| F | T | F | F | F | F | F | T | T | T | T |
| F | F | T | F | F | F | F | F | T | T | T |
| F | F | F | F | F | F | F | F | F | F | F |

12. First distributive law. If $p$ is F, both $p \land (q \lor r)$ and $(p \land q) \lor (p \land r)$ are F. If $p$ is T, the left side has the value of $q \lor r$, and the right side has the value of $q \lor r$ too, since $p \land q$ has the value of $q$ and $p \land r$ has the value of $r$.
13. Second distributive law. If $p$ is T, both $p \lor (q \land r)$ and $(p \lor q) \land (p \lor r)$ are T. If $p$ is F, the left side has the value of $q \land r$, and the right side has the value of $q \land r$ too, since $p \lor q$ has the value of $q$ and $p \lor r$ has the value of $r$.

| $p$ | $q$ | $r$ | $q \lor r$ | $p \land (q \lor r)$ | $(p \land q) \lor (p \land r)$ | $q \land r$ | $p \lor (q \land r)$ | $(p \lor q) \land (p \lor r)$ |
|---|---|---|---|---|---|---|---|---|
| T | T | T | T | T | T | T | T | T |
| T | T | F | T | T | T | F | T | T |
| T | F | T | T | T | T | F | T | T |
| T | F | F | F | F | F | F | T | T |
| F | T | T | T | F | F | T | T | T |
| F | T | F | T | F | F | F | F | F |
| F | F | T | T | F | F | F | F | F |
| F | F | F | F | F | F | F | F | F |

14. In each table, the two sides of each law have the same column. This proves laws 1 to 7.

Part 4: the duality principle.

15. For a formula $\varphi$ in $\neg$, $\land$, $\lor$, $\top$ and $\bot$, let $\varphi^*$ be the formula that we get when we replace each variable $p_i$ by $\neg p_i$. We claim that $\varphi^d \equiv \neg \varphi^*$, and we prove it by induction on the construction of $\varphi$.
16. If $\varphi$ is a variable $p$, then $\varphi^d = p$ and $\neg \varphi^* = \neg\neg p$. These are equivalent by the [[double negation law|0NFAGWH84K]].
17. If $\varphi$ is $\top$, then $\varphi^d = \bot$ and $\neg \varphi^* = \neg \top$, which is F in every row. The case $\varphi = \bot$ is the same with T and F exchanged.
18. If $\varphi = \neg \alpha$, then $\varphi^d = \neg \alpha^d$. By the induction hypothesis and replacement of equivalents, $\neg \alpha^d \equiv \neg \neg \alpha^*$, and $\neg\neg\alpha^* = \neg \varphi^*$ because $\varphi^* = \neg \alpha^*$.
19. If $\varphi = \alpha \land \beta$, then $\varphi^d = \alpha^d \lor \beta^d \equiv \neg \alpha^* \lor \neg \beta^*$ by the induction hypothesis. By [[De Morgan's laws|09PKJKA6J0]], this is equivalent to $\neg(\alpha^* \land \beta^*) = \neg \varphi^*$.
20. If $\varphi = \alpha \lor \beta$, the same argument with the other De Morgan law gives $\varphi^d = \alpha^d \land \beta^d \equiv \neg \alpha^* \land \neg \beta^* \equiv \neg(\alpha^* \lor \beta^*) = \neg \varphi^*$.
21. Now let $\varphi \equiv \psi$. Under a valuation $v$, the formula $\varphi^*$ has the value that $\varphi$ has under the valuation $v'$ that gives each $p_i$ the opposite of its truth value under $v$. The same holds for $\psi^*$ and $\psi$.
22. Since $\varphi$ and $\psi$ agree under $v'$, the formulas $\varphi^*$ and $\psi^*$ agree under $v$. So $\varphi^* \equiv \psi^*$, and then $\neg \varphi^* \equiv \neg \psi^*$ by the definition of [[negation|029JBBF693]].
23. By steps 15 to 20 and step 22, $\varphi^d \equiv \neg\varphi^* \equiv \neg\psi^* \equiv \psi^d$. This proves the duality principle. $\blacksquare$

## Idea

A truth table checks a law row by row, and a law in $n$ variables needs only $2^n$ rows.
Most laws need fewer checks, since one value of $p$ often fixes both sides, as in the absorption and distributive laws.
For the duality principle, De Morgan's laws show that the dual of a formula is the negation of the formula with all variables negated.
Negating all variables and then the whole formula preserves equivalence, so duals of equivalent formulas are equivalent.

## Variants

Each law can also be proved by the rules of [[natural deduction|6KT3BJZ7D1]], with one derivation for each direction.
These derivations do not use the law of excluded middle, which shows that laws 1 to 7 hold in [[intuitionistic logic|Q11N8X99FK]].
The proof of the duality principle uses the double negation law in step 16 and De Morgan's laws in steps 19 and 20.
Some classical step is necessary there, since the duality principle fails intuitionistically.
A third proof reads each law as an identity of the two-element [[Boolean algebra|0XADJKM699]] $\{0, 1\}$, with $\land$ as the minimum and $\lor$ as the maximum.
Then the laws are facts about the minimum and the maximum of numbers.
