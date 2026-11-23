---
tag: KJ7PEGF7YN
kind: proof
name: Outline of a proof of Craig's interpolation theorem by the cut-free sequent calculus
msc: ["03C40", "03F05"]
topics: [FBWW4J1XWG]
audience: grad
proves: E2CBFNAVZY
uses: [W72CA3R9MP, AYRZ98Y0NW, WQ1ZE255SF, DKFGQTRYZE]
methods: [12MQ2NJ29A, 0WCP0PVET6, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Craig_interpolation
    locator: Proof of Craig's interpolation theorem
  - url: https://builds.openlogicproject.org/
    locator: Interpolation
---

## Proof

We split every sequent of a cut-free proof of $\varphi \Rightarrow \psi$ into a side of $\varphi$ and a side of $\psi$, and we build an interpolant for each split by induction on the proof, from the axioms down.

This is an outline for a relational language without equality, constants or function symbols.
The connectives include the constants $\top$ (true) and $\bot$ (false), with the axioms $\bot \Rightarrow$ and $\Rightarrow \top$.
We use the [[sequent calculus|W72CA3R9MP]] LK without the cut rule.

1. Let $\varphi \models \psi$.
   By [[Gödel's completeness theorem|WQ1ZE255SF]] and [[cut elimination|AYRZ98Y0NW]], the sequent $\varphi \Rightarrow \psi$ has a cut-free proof.
2. A split of a sequent $\Gamma \Rightarrow \Delta$ writes it as $\Gamma_1, \Gamma_2 \Rightarrow \Delta_1, \Delta_2$.
   Side 1 is $(\Gamma_1, \Delta_1)$, and side 2 is $(\Gamma_2, \Delta_2)$.
3. We claim that for every split of a sequent with a cut-free proof, some formula $C$ makes both $\Gamma_1 \Rightarrow \Delta_1, C$ and $C, \Gamma_2 \Rightarrow \Delta_2$ provable.
   Also, every relation symbol and free variable of $C$ occurs on both sides.
4. We prove the claim by induction on the cut-free proof.
5. For an axiom $A \Rightarrow A$ with both copies on side 1, we take $C = \bot$.
   With both copies on side 2, we take $C = \top$.
6. For an axiom $A \Rightarrow A$ with the left $A$ on side 1 and the right $A$ on side 2, we take $C = A$.
   In the opposite case, we take $C = \neg A$, since $\Rightarrow A, \neg A$ and $\neg A, A \Rightarrow$ are provable.
7. For a one-premise propositional or structural rule, the principal formula stays on its side, and the interpolant of the premise works.
8. For a two-premise rule with interpolants $C_1$, $C_2$ of the premises, we take $C_1 \lor C_2$ when the principal formula is on side 1, and $C_1 \land C_2$ when it is on side 2.
   For example, $\land$R on side 1 gives $\Gamma_1 \Rightarrow \Delta_1, A \land B, C_1 \lor C_2$ from the two premises, and $\lor$L gives $C_1 \lor C_2, \Gamma_2 \Rightarrow \Delta_2$.
9. For $\forall$ on the right and $\exists$ on the left, the eigenvariable occurs only in the principal formula, so it is not in $C$, and the interpolant of the premise works.
10. For $\forall$ on the left with premise $A(y), \Gamma \Rightarrow \Delta$ and the principal formula $\forall x \, A$ on side 1, let $C$ be an interpolant of the premise.
11. If $y$ occurs on side 1 of the conclusion, or does not occur in $C$, then $C$ works.
    Otherwise, $y$ occurs on side 1 of the premise only in $A(y)$.
12. In that case we take $\forall y \, C$.
    From $\Gamma_1, A(y) \Rightarrow \Delta_1, C$, the left rule for $\forall$ and then the right rule for $\forall$ give $\Gamma_1, \forall x \, A \Rightarrow \Delta_1, \forall y \, C$.
13. The right rule is allowed, because $y$ does not occur in $\Gamma_1, \forall x \, A, \Delta_1$.
    On side 2, the left rule for $\forall$ turns $C, \Gamma_2 \Rightarrow \Delta_2$ into $\forall y \, C, \Gamma_2 \Rightarrow \Delta_2$.
14. If the principal formula of this rule is on side 2, we take $\exists y \, C$ instead, by the dual argument.
    The rule for $\exists$ on the right is dual to steps 10 to 14.
15. We apply the claim to $\varphi \Rightarrow \psi$ with $\varphi$ on side 1 and $\psi$ on side 2.
    Then $\varphi \Rightarrow C$ and $C \Rightarrow \psi$ are provable.
16. By soundness, $\varphi \models C$ and $C \models \psi$.
    The symbols of $C$ occur in both $\varphi$ and $\psi$, and $C$ has no free variables, because $\varphi$ and $\psi$ have none.
17. If $\varphi$ and $\psi$ share a relation symbol $R$, we replace $\top$ by $\forall \bar x \, (R \bar x \to R \bar x)$ and $\bot$ by its negation.
    Otherwise $C$ is built from $\top$ and $\bot$ alone and is equivalent to one of them, and with equality we can write it as $\forall x \, (x = x)$ or its negation.

## Idea

A cut-free proof has the subformula property: every formula in it is a part of the end sequent.
So we can follow the proof from the axioms down and build the interpolant step by step, and at each step the interpolant only uses what both sides share.
The axioms are where information crosses from one side to the other, which is why an axiom with one copy of $A$ on each side contributes $A$ itself.
The quantifier rules need care, because a variable that leaves one side must be bound in the interpolant.
For $P \land Q \Rightarrow P \lor S$ with $0$-ary relation symbols, the proof starts from the crossing axiom $P \Rightarrow P$ and adds $Q$ and $S$ by weakening, so the method returns the interpolant $P$.

## Variants

With equality, constants and function symbols, the same method works with more cases.
Terms that occur on one side only are bound by quantifiers, as in step 12.

The method gives [[Lyndon's interpolation theorem|BRDT1BT7WW]] with only bookkeeping added: by induction, each relation symbol occurs in $C$ with a sign that it has on both sides.

The size of $C$ is bounded by the size of the cut-free proof.
Cut-free proofs can be much longer than proofs with cut, so this bound can be large.
The [[model-theoretic proof|JP8J5RJM6W]] uses Robinson's theorem and gives no bound on $\theta$.
