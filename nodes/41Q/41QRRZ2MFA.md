---
tag: 41QRRZ2MFA
kind: proof
name: Proof outline of Parsons's theorem by Herbrand analysis
msc: ["03F30", "03F05"]
topics: [8XY7JYZKFW]
audience: research
proves: 2VYJXZZDGB
uses: [MESZ87G9ET, W72CA3R9MP, AYRZ98Y0NW, 5NVA2JRHPV, 0WCP0PVET6, HZ17ES9PDY, A4WR995XZP]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand%27s_theorem
    locator: Generalizations of Herbrand's theorem
  - url: https://en.wikipedia.org/wiki/Cut-elimination_theorem
    locator: lead section
---

## Proof

We reduce the derivation to one in which every formula is $\Sigma_1$, and then read off primitive recursive witnesses by induction on the derivation, following the method of [[Herbrand analysis|MESZ87G9ET]].
We cite one result, free-cut elimination, without proof.

### The setting

We formulate $\mathrm{I}\Sigma_1$ as a [[sequent calculus|W72CA3R9MP]] in the language of $\mathsf{PRA}$.
Its initial sequents are $A \Rightarrow A$ for atomic $A$, and quantifier-free sequents for equality and for the defining equations of $\mathsf{PRA}$.
Its rules are the logical and structural rules of classical sequent calculus, the cut rule, and the $\Sigma_1$ induction rule.
The induction rule infers $\Gamma, A(0) \Rightarrow A(t), \Delta$ from $\Gamma, A(a) \Rightarrow A(a + 1), \Delta$, for a $\Sigma_1$ formula $A$ and a variable $a$ not free in the conclusion.
Here a *$\Sigma_1$ formula* is a formula $\exists z \, \chi$ with $\chi$ quantifier-free, or a quantifier-free formula.

**Cited result (C), free-cut elimination.** A derivation of a sequent of $\Sigma_1$ formulas can be transformed into a derivation of the same sequent in which every cut formula is $\Sigma_1$.
Full [[cut elimination|AYRZ98Y0NW]] is not available, because cuts on induction formulas cannot be removed in general.

### Reduction to Σ1 derivations

1. Assume that $\mathrm{I}\Sigma_1 \vdash \forall x \, \exists y \, \varphi(x, y)$.
   Then $\mathrm{I}\Sigma_1 \vdash \exists y \, \varphi(a, y)$ for a tuple $a$ of fresh variables, by instantiation.
2. The sequent calculus derives every theorem of $\mathrm{I}\Sigma_1$, since the induction rule derives the induction axioms.
   So it derives $\Rightarrow \exists y \, \varphi(a, y)$.
3. By (C), some derivation of this sequent has only $\Sigma_1$ cut formulas.
4. In that derivation every formula is a subformula instance of the end sequent, of an initial sequent, of a cut formula or of an induction formula.
   All of these are $\Sigma_1$, so every formula in the derivation is $\Sigma_1$.

### The witnessing lemma

For a sequent $\Gamma \Rightarrow \Delta$ of the derivation, write the formulas of $\Gamma$ as $\exists u_j \, \gamma_j$ and those of $\Delta$ as $\exists v_i \, \theta_i$, with dummy quantifiers on quantifier-free formulas.
**Lemma.** There are primitive recursive $f_i$ such that $\mathsf{PRA}$ proves $\bigwedge_j \gamma_j(w_j) \to \bigvee_i \theta_i(f_i(w))$, where $w$ lists the $w_j$ and all free variables of the sequent are extra arguments.
We prove the lemma by induction on the derivation, one case for each kind of rule.

5. Initial sequents are quantifier-free, so dummy witnesses work, and $\mathsf{PRA}$ proves the sequent itself.
6. A propositional rule has a quantifier-free principal formula, because a $\Sigma_1$ formula with a quantifier is not a conjunction, disjunction, implication or negation.
   The side formulas keep their witnesses.
7. A rule with two premises gives witnesses $f_i$ and $f'_i$ for $\Delta$, and a [[definition by cases|0WCP0PVET6]] chooses between them.
   For $\wedge$ on the right, from $\Gamma \Rightarrow A, \Delta$ and $\Gamma \Rightarrow B, \Delta$, we take $f_i$ if $A$ is false and $f'_i$ otherwise.
8. This choice is correct.
   If $A \wedge B$ is false, then $A$ is false and the first premise gives $\bigvee_i \theta_i(f_i)$, or $B$ is false and the second gives $\bigvee_i \theta_i(f'_i)$.
   The left rules for $\vee$ and $\to$ are treated in the same way.

### The witnessing lemma, structural and quantifier rules

9. Weakening on the right adds a formula with the witness $0$.
   Contraction on the left uses one input witness twice.
10. Contraction on the right of $\exists v \, \theta$, with witnesses $f$ and $f'$, uses $g = f$ if $\theta(f)$ is true and $g = f'$ otherwise.
11. The right $\exists$ rule infers $\exists v \, \theta(v)$ from $\theta(t)$, and the witness is the term $t$.
12. The left $\exists$ rule infers $\exists u \, \gamma(u)$ from $\gamma(b)$ with eigenvariable $b$.
    We substitute the input witness $w$ for $b$ in the functions of the premise.
13. A cut on $C = \exists z \, \chi$ has a left premise that gives $c$ with $\chi(c)$ or $\bigvee_i \theta_i(f_i)$.
    Its right premise gives $f'_i(w)$ from any witness $w$ of $C$.
    We take $g_i = f'_i(c)$ if $\chi(c)$ is true and $g_i = f_i$ otherwise.

### The witnessing lemma, the induction rule

14. For the induction rule with $A(a) = \exists z \, \chi(z, a)$, the premise gives a function $g$ with
    $$\chi(w, a) \to \chi(g(a, w), a + 1) \vee \bigvee_i \theta_i(f_i(a, w)).$$
15. Let $w_0$ be the input witness for $A(0)$, and define $h(0) = w_0$ and $h(b + 1) = g(b, h(b))$ by [[primitive recursion|5NVA2JRHPV]].
16. By bounded search, let $c^*$ be the least $c < t$ with $\neg \chi(h(c + 1), c + 1)$.
    If no such $c$ exists, then $h(t)$ is a witness for $A(t)$.
17. Otherwise $\chi(h(c^*), c^*)$ is true, by the input assumption $\chi(w_0, 0)$ when $c^* = 0$ and by the minimality of $c^*$ when $c^* > 0$.
    But $\chi(g(c^*, h(c^*)), c^* + 1)$ is false, so the premise at $a = c^*$ gives $\bigvee_i \theta_i(f_i(c^*, h(c^*)))$, and these are witnesses for $\Delta$.
18. Bounded search, definition by cases and primitive recursion preserve primitive recursiveness, so every $f_i$ built in steps 5 to 17 is primitive recursive.
    Each case argument uses only quantifier-free induction, so it is a proof in $\mathsf{PRA}$.

### Conclusion

19. We apply the lemma to the end sequent $\Rightarrow \exists y \, \varphi(a, y)$, whose antecedent is empty.
20. It gives a primitive recursive $f$ with $\mathsf{PRA} \vdash \varphi(a, f(a))$, which is the statement of [[Parsons's theorem|2VYJXZZDGB]].

## Idea

After free-cut elimination, a proof of a $\Sigma_1$ formula contains only $\Sigma_1$ formulas, so every existential quantifier in it can carry a witness.
We then read the proof as a program.
A cut composes two programs, a two-premise rule becomes a test, and an induction becomes a primitive recursion followed by a bounded search for the first step that fails.
The only cited result is free-cut elimination, and everything else is a direct check of the rules.

## Variants

Parsons, Mints and Takeuti proved the theorem independently, before the proof by Herbrand analysis, and the outline above does not follow their proofs.
The [[Dialectica interpretation|HZ17ES9PDY]] gives another route.
It interprets $\mathrm{I}\Sigma_1$ in the fragment of [[Gödel's system T|A4WR995XZP]] with the recursor at type $0$ only, and that fragment defines exactly the primitive recursive functions.
There are also model-theoretic proofs.
They start from a model of $\mathsf{PRA}$ with an element $a$ such that $\varphi(a, t(a))$ fails for every primitive recursive term $t$, and build a model of $\mathrm{I}\Sigma_1$ in which $\exists y \, \varphi(a, y)$ fails.
