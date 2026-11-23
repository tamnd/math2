---
tag: QK8QR0TEQM
kind: example
name: The Ω-rule derives the minimality axiom of ID₁
msc: ["03F15", "03F05"]
topics: [XTTKZTYDSD]
audience: research
instance_of: [5C4YBXQV15]
uses: [5C4YBXQV15, 45GQ3KQVT3, XAMKAB1BZM, CRP7Z3M9XD, 5VNT564Y2W]
sources:
  - url: https://en.wikipedia.org/wiki/Theories_of_iterated_inductive_definitions
    locator: ID<sub>1</sub>
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Table of ordinal analyses
---

## Example

### The system

Let $I$ be the even numbers, defined by "$x = 0$ or $x = y + 2$ for some $y \in I$", and let $F$ be a property with $F(0)$ and $F(y) \to F(y + 2)$.
The minimality axiom of $\mathrm{ID}_1$ says that then $F(n)$ holds for every $n \in I$, and we derive it with [[Buchholz's Ω-rule|5C4YBXQV15]], for any $I$ given by a positive formula.

Fix an $X$-positive arithmetical formula $A(X, x)$, and let $I$ be the predicate of the [[definition|45GQ3KQVT3]].
We use one-sided sequents of closed formulas in negation normal form.
The rules are: true arithmetical literals as axioms, the rules for $\wedge$, $\vee$ and $\exists$, the [[ω-rule|XAMKAB1BZM]] for $\forall$, cut, the closure rule from $\Gamma, A(I, t)$ to $\Gamma, t \in I$, and the Ω-rule.
A *P-derivation* is a derivation without cut and without the Ω-rule, whose formulas are $I$-positive.
The Ω-rule derives $\Gamma, \neg(t \in I)$ from one premise $\Gamma, \Delta$ for each P-derivation of $\Delta, t \in I$.

Let $F(x)$ be any formula, and let $C_F$ be the formula $\exists x \, (A(F, x) \wedge \neg F(x))$, which says that $F$ is not closed under $A$.
The minimality axiom for $F$ is, in one-sided form, the sequent $C_F, \forall x \, (\neg(x \in I) \vee F(x))$.
We derive it without cut.

### The derivation

1. By the ω-rule and the $\vee$-rule, it is enough to derive $C_F, \neg(n \in I), F(n)$ for each numeral $n$.
2. By the Ω-rule with side formulas $C_F, F(n)$, it is enough to derive $C_F, F(n), \Delta$ from each P-derivation $d$ of $\Delta, n \in I$.
3. We prove a stronger claim.
   Let $d$ be a P-derivation of a sequent $\Delta \cup \Pi$, where the formulas of $\Pi$ are marked.
   Then $C_F, \Delta, \Pi[F/I]$ has a derivation without cut, where $\Pi[F/I]$ replaces each atom $s \in I$ by $F(s)$.
   The proof is by induction on the height of $d$, in steps 4 to 8.
4. Axiom.
   The sequent contains a true arithmetical literal, the substitution does not change it, and so the new sequent is an axiom too.
5. The last rule acts on an unmarked formula.
   Apply the induction hypothesis to each premise, with the same marks, and then the same rule.
6. The last rule is a logical rule on a marked formula.
   Mark its minor formulas, apply the induction hypothesis, and then the same rule, since the substitution of $F$ for $I$ commutes with $\wedge$, $\vee$, $\exists$ and $\forall$.
7. The last rule is the closure rule on a marked formula $s \in I$, so its premise has the marked formula $A(I, s)$.
   The induction hypothesis gives $C_F, \Delta, \Pi'[F/I], A(F, s)$, where $\Pi'$ is the rest of $\Pi$.
8. The sequent $\neg F(s), F(s)$ has a derivation without cut, by induction on the formula $F$, with the identity for atoms $t \in I$ from the remarks.
   The $\wedge$-rule gives $C_F, \Delta, \Pi'[F/I], F(s), A(F, s) \wedge \neg F(s)$.
   The $\exists$-rule with witness $s$ gives the formula $C_F$, which is already in the sequent.
   So we get $C_F, \Delta, \Pi'[F/I], F(s)$, which is $C_F, \Delta, \Pi[F/I]$.
9. Apply the claim to $d$ with only $n \in I$ marked.
   This gives $C_F, \Delta, F(n)$, which is the premise that step 2 needs.
10. Steps 1 and 2 now give the minimality axiom $C_F, \forall x \, (\neg(x \in I) \vee F(x))$.

## Remarks

The Ω-rule replaces an axiom that quantifies over all formulas $F$: the induction on $F$-closed sets becomes an induction on the given derivation of $n \in I$.

The identity $\neg(n \in I), n \in I$ is also derivable by the Ω-rule, with $\Gamma = \{ n \in I \}$.
The premise for a P-derivation of $\Delta, n \in I$ is then $\Delta, n \in I$ itself, which that P-derivation derives.
The closure axiom of $\mathrm{ID}_1$ uses this identity: the closure rule turns $\neg A(I, n), A(I, n)$ into $\neg A(I, n), n \in I$, and the $\vee$-rule and the ω-rule finish.

Positivity is needed in steps 4 and 6, through the definition of P-derivations.
If $A(X, x)$ had a negative occurrence of $X$, P-derivations would contain atoms $\neg(s \in I)$, and the substitution would not turn them into derivable formulas.
For $\mathrm{ID}_\nu$, the $\Omega_{\mu+1}$-rule for level $\mu$ does the same with the P-derivations of the lower levels.

## Explanations

### L1 human

Suppose a set is built by rules, and a property is kept by the same rules.
Then every element of the set has the property: follow the steps that built the element, and check the property at each step.
The Ω-rule makes this idea into a rule of proof.
It says: to use the fact that $n$ is in the set, it is enough to know what to do with any proof that $n$ is in the set.
For the even numbers, a proof that $4$ is even goes $0, 2, 4$, and the property passes along the same path.

### L2 human

Let $A(X, x) = \forall y \, (\neg(y < x) \vee y \in X)$, so $I$ is the [[accessible part|CRP7Z3M9XD]] of $<$, which is $\mathbb{N}$.
We follow the claim of step 3 for a P-derivation $d$ of $1 \in I$.

1. $d$ derives $0 \in I$ from $A(I, 0)$.
   The formula $A(I, 0)$ comes by the ω-rule from the true literals $\neg(m < 0)$, with the $\vee$-rule.
2. $d$ derives $A(I, 1)$ by the ω-rule.
   The premise for $m = 0$ is $\neg(0 < 1) \vee 0 \in I$, from step 1, and the premises for $m \ge 1$ come from the true literals $\neg(m < 1)$.
3. The closure rule gives $1 \in I$.
4. The claim replaces step 1 by $A(F, 0)$ and then $F(0)$, with the help of $C_F$.
5. It replaces step 2 by $A(F, 1)$, using $F(0)$ in the premise for $m = 0$.
6. The closure step becomes $F(1)$, again with $C_F$.
   So we get $C_F, F(1)$: if $F$ is closed, then $F(1)$.

The typical use is the embedding of $\mathrm{ID}_1$ into the infinitary system, which is the first step of its ordinal analysis.
The trap is to forget that $d$ ranges over all P-derivations, also those with extra formulas $\Delta$; the extra formulas are needed later, when cuts are removed.
