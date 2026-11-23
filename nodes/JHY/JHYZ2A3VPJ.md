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

The system $\mathrm{ACA}$ of [[second-order arithmetic|DC60FYCSPM]] has arithmetical comprehension and induction for all second-order formulas.
Its weaker version $\mathrm{ACA}_0$ has induction only for sets, and [[its ordinal is ε0|GXZZW7G54P]].
We show that full induction lifts the ordinal to $\varepsilon_{\varepsilon_0}$.

For a primitive recursive order $\prec$, let $\mathrm{WO}(\prec)$ be the sentence $\forall X \, \operatorname{TI}(\prec, X)$ of [[the definition|C19Z3B6V4P]].
Let $\varepsilon_\beta$ be the $\beta$-th [[epsilon number|PQSHBKCE7V]], counted from $\varepsilon_0$, so that $\varepsilon_{\varepsilon_0} = \sup_{\beta < \varepsilon_0} \varepsilon_\beta$.
We prove the lower bound $\lvert \mathrm{ACA} \rvert \ge \varepsilon_{\varepsilon_0}$ from a cited lemma, and we cite the upper bound.

### Notation and the cited lemma

Fix a primitive recursive notation system for the ordinals below $\varepsilon_{\varepsilon_0}$: Cantor normal forms whose atoms are $0$ and symbols $\varepsilon_b$ for notations $b$ below $\varepsilon_0$.
For a notation $a$, write $\prec_a$ for the order restricted to the notations below $a$.
We cite a theorem of Girard in [[reverse mathematics|7SQS69T17R]], read in the notation system: $\mathrm{ACA}_0$ proves that if $\prec_a$ is a well-order, then so is $\prec_{\omega^a}$.

### The climb through the epsilon numbers

1. Successor step.
   Fix $b$ and assume $\mathrm{WO}(\prec_{\varepsilon_b})$.
   Adding one top element gives $\mathrm{WO}(\prec_{\varepsilon_b + 1})$.
2. Put $t_0 = \varepsilon_b + 1$ and $t_{n+1} = \omega^{t_n}$, so that $\varepsilon_{b+1} = \sup_n t_n$.
   The cited lemma and induction on $n$ give $\mathrm{WO}(\prec_{t_n})$ for all $n$.
3. The induction in step 2 is for the formula $\mathrm{WO}(\prec_{t_n})$, which has a set quantifier.
   $\mathrm{ACA}$ has this induction, and $\mathrm{ACA}_0$ does not.
4. A descending sequence below $\varepsilon_{b+1}$ starts below some $t_n$, so step 2 gives $\mathrm{WO}(\prec_{\varepsilon_{b+1}})$.
5. Limit step.
   If $\lambda$ is a limit and $\mathrm{WO}(\prec_{\varepsilon_\beta})$ holds for all $\beta < \lambda$, then $\mathrm{WO}(\prec_{\varepsilon_\lambda})$ holds, by the argument of step 4.
6. Base case.
   Step 2 with $t_0 = 1$ gives $\mathrm{WO}(\prec_{\varepsilon_0})$.
7. Steps 1 to 6 show, inside $\mathrm{ACA}$, that the formula $\varphi(b) := \mathrm{WO}(\prec_{\varepsilon_b})$ is progressive along the notations below $\varepsilon_0$.

### The value

Gentzen's proof of [[transfinite induction in arithmetic|ZE54ABPMJ0]] uses only induction on formulas, and $\mathrm{ACA}$ has induction for all formulas.
So $\mathrm{ACA}$ proves transfinite induction for $\varphi$ below each notation $a \prec \varepsilon_0$.
With step 7 this gives $\mathrm{ACA} \vdash \mathrm{WO}(\prec_{\varepsilon_a})$ for each $a \prec \varepsilon_0$, so $\lvert \mathrm{ACA} \rvert \ge \sup_{a < \varepsilon_0} \varepsilon_a = \varepsilon_{\varepsilon_0}$.
For the upper bound we cite the ordinal analysis of $\mathrm{ACA}$, which gives $\lvert \mathrm{ACA} \rvert \le \varepsilon_{\varepsilon_0}$, so $\lvert \mathrm{ACA} \rvert = \varepsilon_{\varepsilon_0}$.

## Remarks

The example shows how much the induction schema adds on top of comprehension.
In $\mathrm{ACA}_0$ the climb stops at step 3, because the theory cannot run an induction on a formula with a set quantifier.
Each epsilon number is reached by one such induction, and Gentzen's argument then strings them together along every ordinal below $\varepsilon_0$.

The same pattern holds one level up.
The [[Feferman-Schütte ordinal|CNN7BK5YAW]] $\Gamma_0$ is the ordinal of $\mathrm{ATR}_0$, and full induction gives $\lvert \mathrm{ATR} \rvert = \Gamma_{\varepsilon_0}$, where $\Gamma_\beta$ lists the strongly critical ordinals.

## Explanations

### L1 human

ACA is a system for numbers and sets of numbers that allows induction for every statement.
It can show that $\omega$ raised to a well-ordering is again a well-ordering, and it can repeat this step as often as induction allows.
Repeating along all ordinals below $\varepsilon_0$ gives the epsilon numbers $\varepsilon_1, \varepsilon_2, \ldots$, and in the limit $\varepsilon_{\varepsilon_0}$.
That limit is the proof-theoretic ordinal of ACA.

### L2 human

We go from $\varepsilon_0$ to $\varepsilon_1$ inside $\mathrm{ACA}$.

1. Assume $\mathrm{WO}(\prec_{\varepsilon_0})$, and add a top element to get $\mathrm{WO}(\prec_{\varepsilon_0 + 1})$.
2. By the lemma, $\omega^{\varepsilon_0 + 1}$ is well-ordered, then $\omega^{\omega^{\varepsilon_0 + 1}}$, and so on.
3. Induction on $n$, for the formula "the $n$-th tower is well-ordered", gives all of them at once.
4. Their supremum is $\varepsilon_1$, so $\mathrm{WO}(\prec_{\varepsilon_1})$.

The typical use is to lift an ordinal by adding induction to a theory that has a known jump lemma.
Watch out: step 3 needs induction for a formula with a set quantifier, so the same proof fails in $\mathrm{ACA}_0$.
