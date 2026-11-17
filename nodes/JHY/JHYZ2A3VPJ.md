---
tag: JHYZ2A3VPJ
kind: example
name: The proof-theoretic ordinal of ACA is ε_ε0
msc: ["03F15", "03F35"]
topics: [XTTKZTYDSD]
audience: research
instance_of: [C72RBH0CDR]
uses: [C19Z3B6V4P, DC60FYCSPM, PQSHBKCE7V, KT50SMH3EC, 7SQS69T17R, ZE54ABPMJ0, GXZZW7G54P, CNN7BK5YAW]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Table of ordinal analyses
  - url: https://en.wikipedia.org/wiki/Epsilon_number
    locator: Ordinal ε numbers
---

## Example

Let $\mathrm{ACA}$ be the system of [[second-order arithmetic|DC60FYCSPM]] with arithmetical comprehension and induction for all second-order formulas.
For a primitive recursive order $\prec$, let $\mathrm{WO}(\prec)$ be the sentence $\forall X \, \operatorname{TI}(\prec, X)$ of [[the definition|C19Z3B6V4P]].
Let $\varepsilon_\beta$ be the $\beta$-th [[epsilon number|PQSHBKCE7V]], so $\varepsilon_{\varepsilon_0} = \sup_{\beta < \varepsilon_0} \varepsilon_\beta$.
We prove the lower bound $\abs{\mathrm{ACA}} \ge \varepsilon_{\varepsilon_0}$ from cited lemmas and cite the upper bound.

1. Notation. Fix a primitive recursive notation system for the ordinals below $\varepsilon_{\varepsilon_0}$: Cantor normal forms whose atoms are $0$ and the symbols $\varepsilon_b$, where $b$ is a notation below $\varepsilon_0$. For a notation $a$, write $\prec_a$ for the order below $a$.
2. Cited lemma. $\mathrm{ACA}_0$ proves: if $\prec_a$ is a well-order, then $\prec_{\omega^a}$ is a well-order. This is the result of Girard and Hirst in [[reverse mathematics|7SQS69T17R]], read in the notation system.
3. Successor step. Fix $b$ and assume $\mathrm{WO}(\prec_{\varepsilon_b})$. Adding a top element gives $\mathrm{WO}(\prec_{\varepsilon_b + 1})$.
4. Let $t_0 = \varepsilon_b + 1$ and $t_{n+1} = \omega^{t_n}$, so that $\varepsilon_{b+1} = \sup_n t_n$. Step 2 and induction on $n$ give $\mathrm{WO}(\prec_{t_n})$ for all $n$.
5. The induction in step 4 is for the formula $\mathrm{WO}(\prec_{t_n})$, which has a set quantifier. $\mathrm{ACA}$ has this induction, and $\mathrm{ACA}_0$ does not.
6. A descending sequence below $\varepsilon_{b+1}$ starts below some $t_n$, so step 4 gives $\mathrm{WO}(\prec_{\varepsilon_{b+1}})$.
7. Limit step. If $\lambda$ is a limit and $\mathrm{WO}(\prec_{\varepsilon_\beta})$ for all $\beta < \lambda$, then $\mathrm{WO}(\prec_{\varepsilon_\lambda})$, by the argument of step 6.
8. Also $\mathrm{WO}(\prec_{\varepsilon_0})$ holds in the base case, by step 4 with $t_0 = 1$.
9. Steps 3 to 8 show that the formula $\varphi(b) := \mathrm{WO}(\prec_{\varepsilon_b})$ is progressive along the notations below $\varepsilon_0$, provably in $\mathrm{ACA}$.
10. The jump proof of [[transfinite induction in arithmetic|ZE54ABPMJ0]] uses only induction, and $\mathrm{ACA}$ has induction for all formulas. So $\mathrm{ACA}$ proves transfinite induction for $\varphi$ below each notation $a \prec \varepsilon_0$.
11. With step 9, $\mathrm{ACA} \vdash \mathrm{WO}(\prec_{\varepsilon_a})$ for each $a \prec \varepsilon_0$, so $\abs{\mathrm{ACA}} \ge \sup_{a < \varepsilon_0} \varepsilon_a = \varepsilon_{\varepsilon_0}$.
12. Upper bound (cited). The ordinal analysis of $\mathrm{ACA}$ gives $\abs{\mathrm{ACA}} \le \varepsilon_{\varepsilon_0}$, so $\abs{\mathrm{ACA}} = \varepsilon_{\varepsilon_0}$.

## Remarks

The example shows how much the induction schema adds: [[the analysis of ACA0|GXZZW7G54P]] gives $\abs{\mathrm{ACA}_0} = \varepsilon_0$, and full induction lifts this to $\varepsilon_{\varepsilon_0}$.
In step 5, $\mathrm{ACA}_0$ stops because it cannot run the induction on $n$ for a formula with a set quantifier.
The same pattern holds one level up: $\abs{\mathrm{ATR}_0} = \Gamma_0$, the [[Feferman-Schütte ordinal|CNN7BK5YAW]], and full induction gives $\abs{\mathrm{ATR}} = \Gamma_{\varepsilon_0}$, where $\Gamma_\beta$ lists the strongly critical ordinals.

## Explanations

### L1 human

ACA is a system for the natural numbers and sets of natural numbers that allows induction for every statement.
It can show that $\omega$ raised to a well-ordering is again a well-ordering, and it can repeat this step as often as induction allows.
Repeating along all ordinals below $\varepsilon_0$ gives the epsilon numbers $\varepsilon_1, \varepsilon_2, \ldots$, and in the limit $\varepsilon_{\varepsilon_0}$.
That is the proof-theoretic ordinal of ACA.

### L2 human

We go from $\varepsilon_0$ to $\varepsilon_1$ inside $\mathrm{ACA}$.

1. Assume $\mathrm{WO}(\prec_{\varepsilon_0})$. Adding a top element gives $\mathrm{WO}(\prec_{\varepsilon_0 + 1})$.
2. By the lemma, $\omega^{\varepsilon_0 + 1}$ is well-ordered, then $\omega^{\omega^{\varepsilon_0 + 1}}$, and so on.
3. Induction on $n$, for the formula "the $n$-th tower is well-ordered", gives all of them at once.
4. Their supremum is $\varepsilon_1$, so $\mathrm{WO}(\prec_{\varepsilon_1})$.

The typical use is to lift an ordinal by adding induction to a theory with a known jump lemma.
The trap: step 3 needs induction for a formula with a set quantifier, so the same proof fails in $\mathrm{ACA}_0$.
