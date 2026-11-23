---
tag: GXZZW7G54P
kind: example
name: Ordinal analysis of ACA0
msc: ["03F15", "03F35"]
topics: [XTTKZTYDSD]
audience: research
instance_of: [C5E5TG8PGP]
uses: [57PTMS2ADY, HPA6HX3114, DC60FYCSPM, ZE54ABPMJ0, 7ANX5PDRDM]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Theories with proof-theoretic ordinal ε0
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: Arithmetical comprehension
---

## Example

Let $\mathrm{ACA}_0$ be the subsystem of [[second-order arithmetic|DC60FYCSPM]] with arithmetical comprehension and the induction axiom for sets, as in [[ACA0 is conservative over PA|HPA6HX3114]].
For a primitive recursive order $\lhd$, let $\mathrm{WF}(\lhd)$ be the sentence $\forall X \, (\operatorname{Prog}_\lhd(X) \to \forall x \, (x \in X))$, where $\operatorname{Prog}_\lhd(X)$ says that $X$ contains every $x$ whose $\lhd$-predecessors are all in $X$.
We show $\lvert \mathrm{ACA}_0 \rvert = \varepsilon_0$ by the three results of an [[ordinal analysis|57PTMS2ADY]].

1. Notation system.
   Use the Cantor normal forms below $\varepsilon_0$, as for PA.
2. Lower bound for a fixed notation $a$.
   The jump proof of [[transfinite induction in arithmetic|ZE54ABPMJ0]] needs induction for jump formulas, which are arithmetical in $X$.
   Arithmetical comprehension turns each such formula into a set, the set induction axiom applies to it, and so $\mathrm{ACA}_0$ proves $\mathrm{WF}(\prec_a)$.
3. Upper bound, conservativity (cited).
   $\mathrm{ACA}_0$ is conservative over $\mathrm{PA}(X)$, Peano arithmetic with a new predicate $X$ allowed in the induction schema, for formulas whose only set variable is $X$ free.
4. Upper bound, transfer.
   If $\mathrm{ACA}_0 \vdash \mathrm{WF}(\lhd)$, then $\mathrm{PA}(X) \vdash \operatorname{Prog}_\lhd(X) \to \forall x \, X(x)$.
   The upper bound of [[the analysis of PA|7ANX5PDRDM]] holds for $\mathrm{PA}(X)$, so the order type of $\lhd$ is below $\varepsilon_0$.
5. So $\lvert \mathrm{ACA}_0 \rvert = \varepsilon_0$.

## Remarks

Two theories with different languages have the same ordinal here, and the reason is conservativity.
The full system $\mathrm{ACA}$, with induction for all second-order formulas, proves more, and its ordinal is $\varepsilon_{\varepsilon_0}$.
The step from $\mathrm{ACA}_0$ to $\mathrm{ACA}$ adds induction, not comprehension, and the ordinal climbs through $\varepsilon_0$ further epsilon numbers.
So the subscript $0$, which marks restricted induction, changes the ordinal.

## Explanations

### L1 human

The system $\mathrm{ACA}_0$ adds sets of numbers to Peano arithmetic, but only sets that arithmetic can already describe.
Such sets let it say new things, but they do not let it prove any new facts about numbers.
So its ordinal is the same as for Peano arithmetic, namely $\varepsilon_0$.

### L2 human

Why does $\mathrm{ACA}$ go further than $\mathrm{ACA}_0$?
In $\mathrm{ACA}_0$, induction is an axiom about sets, so it applies only to properties that define a set.
Arithmetical comprehension gives sets for arithmetical properties, so arithmetical induction holds, exactly as in PA.
In $\mathrm{ACA}$, induction holds for every second-order formula, for example for "$\prec_x$ is well-founded", which has a set quantifier.
Induction on such formulas lets the jump run along longer orders, and the provable well-orders reach every ordinal below $\varepsilon_{\varepsilon_0}$.
This is the typical use: read the ordinal of a subsystem of second-order arithmetic from a conservation result.
Watch out: the same comprehension axiom with more induction gives a larger ordinal.
