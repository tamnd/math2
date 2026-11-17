---
tag: W560YMCPA3
kind: statement
role: theorem
name: Takeuti's conjecture
msc: ["03F05", "03B15"]
topics: [XTTKZTYDSD]
audience: research
uses: [G6X7SZSNC5, W72CA3R9MP, AYRZ98Y0NW, P1ABGYRQXH, SVNYKTGQ48, DC60FYCSPM, VM8TQ70CVJ, X9WYNYE29C, KWEJFK5943]
about: [AYRZ98Y0NW, G6X7SZSNC5]
history:
  first_stated: "1953"
  notes: "Takeuti stated the conjecture for his generalized logic calculus in the Japanese Journal of Mathematics 23 (1953). Tait proved the second-order case in 1966, and Takahashi (1967) and Prawitz (1968) proved the higher-order case."
sources:
  - url: https://en.wikipedia.org/wiki/Takeuti%27s_conjecture
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Cut-elimination_theorem
    locator: lead section
---

## Statement

Let $\mathrm{LK}^2$ be the classical [[sequent calculus|W72CA3R9MP]] for [[second-order logic|G6X7SZSNC5]].
Its formulas have first-order variables $x, y, \dots$ and second-order variables $X, Y, \dots$ for unary relations.
An *abstract* is an expression $T = \lambda x . B$, where $B$ is any second-order formula, and $A[T/X]$ is the result of replacing each $X(t)$ in $A$ by $B[t/x]$, after renaming bound variables when needed.
The rules of $\mathrm{LK}^2$ are the rules of the first-order calculus LK, with cut, together with the rules for the second-order quantifier:

$$\frac{\Gamma, A[T/X] \vdash \Delta}{\Gamma, \forall X \, A \vdash \Delta} \ (\forall^2 \mathrm{L}), \qquad \frac{\Gamma \vdash \Delta, A[Y/X]}{\Gamma \vdash \Delta, \forall X \, A} \ (\forall^2 \mathrm{R}),$$

where $T$ is any abstract and $Y$ is a second-order variable that does not occur free in $\Gamma$, $\Delta$ or $\forall X \, A$.
The rules for $\exists X$ are dual.

**Theorem (Takeuti's conjecture).** If a sequent $\Gamma \vdash \Delta$ has a derivation in $\mathrm{LK}^2$, then it has a derivation in $\mathrm{LK}^2$ that does not use the cut rule.

## Remarks

### Why each hypothesis is needed

- The calculus must be pure logic. Add the initial sequents $\vdash p$ and $p \vdash q$ for two propositional atoms $p$ and $q$. Then a cut on $p$ derives $\vdash q$.
  A cut-free derivation of $\vdash q$ can only use structural rules, because no logical rule ends in an atom.
  So each of its sequents has nothing on the left and only copies of $q$ on the right, and no initial sequent has this form.
  So second-order arithmetic, which has non-logical axioms, does not have cut elimination in this form.
- The theorem is about derivability, not about truth in the full semantics. In the full semantics the second-order variables range over all subsets of the domain. By [[Gödel's incompleteness theorem|X9WYNYE29C]] the set of second-order sentences that are true in all such structures is not recursively enumerable. So some of these sentences have no derivation at all, with or without cut.
- The rule $(\forall^2 \mathrm{L})$ allows every abstract $T$, also abstracts that contain $\forall X \, A$ itself. This impredicative choice gives the theorem its strength. If $T$ is restricted to second-order variables, the calculus behaves like a many-sorted first-order calculus, and the first-order [[cut-elimination theorem|AYRZ98Y0NW]] applies with the same proof.

### Consequences

- $\mathrm{LK}^2$ is consistent: a cut-free derivation of the empty sequent would end in a rule whose conclusion is empty, and no rule has such a conclusion.
- Cut-free derivations in $\mathrm{LK}^2$ do not have the usual subformula property. The formula $A[T/X]$ in $(\forall^2 \mathrm{L})$ can be longer than $\forall X \, A$, because $T$ is arbitrary. So the theorem gives less information than in first-order logic.
- Over primitive recursive arithmetic, the theorem is equivalent to the 1-consistency of [[second-order arithmetic|DC60FYCSPM]] (Wikipedia, lead section). Second-order arithmetic contains primitive recursive arithmetic, and 1-consistency implies [[consistency|VM8TQ70CVJ]]. So second-order arithmetic does not prove the theorem, by Gödel's second incompleteness theorem, if it is consistent.
- So every proof of the theorem uses principles beyond second-order arithmetic. The semantic proofs use the existence of sets of sets of natural numbers.

### Converse

The converse is true and trivial: a derivation without cut is a derivation in $\mathrm{LK}^2$.
The equivalence with the 1-consistency of second-order arithmetic is a converse in a deeper sense: the theorem also follows from that consistency statement in primitive recursive arithmetic.

### Generalizations

- Takeuti stated the conjecture for his generalized logic calculus GLC, a sequent calculus for [[higher-order logic|P1ABGYRQXH]] (simple type theory). Takahashi and Prawitz proved it for all finite types, with the same semantic method.
- Girard proved strong normalization for [[System F|SVNYKTGQ48]], the polymorphic lambda calculus. Through the correspondence between proofs and terms, this gives a syntactic proof of cut elimination for second-order intuitionistic logic, and the theorem follows as a corollary (Wikipedia, lead section).
- The theorem is also equivalent to the strong normalization of System F (same source).

## History

Gaisi Takeuti stated the conjecture in 1953 in "On a generalized logic calculus", for his calculus GLC.
Kurt Schütte reduced it to a statement about the extension of partial valuations.
William Tait proved the second-order case in 1966 by a semantic, non-constructive method based on Schütte's work.
Moto-o Takahashi (1967) and Dag Prawitz (1968) proved, independently, the case of higher-order logic.

## Explanations

### L1 human

A proof in logic often uses a lemma, and the cut rule is the rule that uses a lemma.
In first-order logic, every proof can be rewritten without lemmas, so that each step only takes apart the formulas of the conclusion.
Takeuti asked whether the same is true when one may also quantify over properties, as in "for every property $X$, if $X(a)$ then $X(b)$".
The answer is yes, but the known proofs need strong assumptions about sets.
The reason is that a property may be defined by a formula that again talks about all properties.

### L2 human

We derive the symmetry of the Leibniz equality without cut:
$$\forall X \, (X(a) \to X(b)) \vdash \forall X \, (X(b) \to X(a)).$$

1. Start from the axioms $Y(a) \vdash Y(a)$ and $Y(b) \vdash Y(b)$.
2. Negation on the right of the first gives $\vdash \neg Y(a), Y(a)$. Negation on the left of the second gives $\neg Y(b), Y(b) \vdash$.
3. Implication on the left combines them: $\neg Y(a) \to \neg Y(b), Y(b) \vdash Y(a)$.
4. Rule $(\forall^2 \mathrm{L})$ with the abstract $T = \lambda z . \neg Y(z)$ gives $\forall X \, (X(a) \to X(b)), Y(b) \vdash Y(a)$.
5. Implication on the right gives $\forall X \, (X(a) \to X(b)) \vdash Y(b) \to Y(a)$.
6. Rule $(\forall^2 \mathrm{R})$ applies, because $Y$ does not occur free on the left. This gives the sequent.

The typical use of the theorem is to show that a second-order statement is not provable, by showing that no cut-free derivation can exist.
The trap is step 4: the formula $\neg Y(a) \to \neg Y(b)$ is not a subformula of the end sequent, so a cut-free search must guess abstracts.

### L3 human

Gentzen's cut elimination for first-order logic is a finitary proof by induction on the cut rank and the height.
In the second-order case the rank argument fails: the abstract $T$ in $(\forall^2 \mathrm{L})$ can have a higher rank than $\forall X \, A$, so a reduction step can create larger cuts.
Tait, Takahashi and Prawitz avoid the syntax: a sequent with no cut-free derivation gives a partial valuation, and they extend it to a total valuation in which the rules with cut are sound.
Completeness for [[Henkin semantics|KWEJFK5943]] does not help directly, because its models come from theories that are consistent in the calculus with cut.
The extension uses sets of sets of natural numbers, and the equivalence with the 1-consistency of second-order arithmetic shows that some such strength is needed.
A finitary proof with an [[ordinal analysis|C5E5TG8PGP]] would need the ordinal of full second-order arithmetic, and no such analysis is known.
Girard's reducibility candidates, which give strong normalization for System F, are the syntactic counterpart of the semantic valuations, and they also quantify over sets of terms in an impredicative way.
