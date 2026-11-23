---
tag: QMN8CHHE9Y
kind: proof
name: Proof of the ordinal analysis of Π¹₁ comprehension
msc: ["03F15", "03F35"]
topics: [XTTKZTYDSD]
audience: research
proves: 2MGJJTSRFD
methods: [0NTF6DMVAP, 0ASJVEFA9J, 0J0XBKG64S]
uses: [5VNT564Y2W, 45GQ3KQVT3, CRP7Z3M9XD, E7WEFRMQTB, XAMKAB1BZM, 5C4YBXQV15, AYRZ98Y0NW, 0A7KV2WB7A]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Table of ordinal analyses
  - url: https://en.wikipedia.org/wiki/Buchholz_psi_functions
    locator: Ordinal notation
  - url: https://en.wikipedia.org/wiki/Theories_of_iterated_inductive_definitions
    locator: Proof-theoretic ordinals
---

## Proof

We prove part (a) in full from two cited facts about $\mathrm{ID}_n$, and we give parts (b) and (c) as a chain of cited lemmas from Buchholz's method of $\Omega_{\mu+1}$-rules.
Write $o(a)$ for the ordinal of a term $a \in \mathrm{OT}$ in Buchholz's notation, and $\tau$ for the term of $\psi_0(\Omega_\omega)$.

### Part (a): interpreting the theories ID_n

1. Let $A(X, x)$ be an $X$-positive arithmetical formula, possibly with set parameters, and let $I = \{ x : \forall X \, (\forall y \, (A(X, y) \to y \in X) \to x \in X) \}$.
   The defining formula is $\Pi^1_1$, so $I$ is a set by $\Pi^1_1$-comprehension.
2. The set $I$ is closed under $A$.
   Let $A(I, x)$ hold, and let $X$ be closed under $A$.
   Then $I \subseteq X$ by the definition of $I$, so $A(X, x)$ holds by [[monotonicity|0A7KV2WB7A]] of positive formulas, so $x \in X$, and hence $x \in I$.
3. The set $I$ is contained in every class defined by a formula and closed under $A$.
   After the interpretation, a formula of $\mathrm{ID}_n$ is arithmetical with set parameters, so it defines a set by arithmetical comprehension, and the definition of $I$ applies to this set.
4. A proof in $\mathrm{ID}_n$ uses finitely many predicates $P_A$.
   For each of them and each stage $0, 1, \dots, n - 1$, apply step 1, with the sets of the earlier stages as parameters.
   The induction axioms of $\mathrm{ID}_n$ hold, because each formula defines a set and $\Pi^1_1\text{-}\mathrm{CA}_0$ has induction for sets, and transfinite induction along a finite order is ordinary induction.
5. So $\Pi^1_1\text{-}\mathrm{CA}_0$ proves the interpretation of each theorem of [[ID_n|5VNT564Y2W]], for each $n \ge 1$.

### Part (a): from accessibility to well-ordering

6. Cited fact 1 (Buchholz, Pohlers): $\lvert \mathrm{ID}_n \rvert = \psi_0(\Omega_{n+1})$, and for each term $a$ with $o(a) < \psi_0(\Omega_{n+1})$ there is a proof in $\mathrm{ID}_n$ that $a$ lies in the [[accessible part|CRP7Z3M9XD]] $\mathrm{Acc}$ of $\prec$.
7. Cited fact 2: $\lvert \mathrm{ID}_{<\omega} \rvert = \psi_0(\Omega_\omega)$, the supremum of the ordinals $\psi_0(\Omega_{n+1})$.
8. Let $a \prec \tau$.
   Then $o(a) < \psi_0(\Omega_\omega)$, so $o(a) < \psi_0(\Omega_{n+1})$ for some $n \ge 1$, by step 7.
9. By steps 5 and 6, $\Pi^1_1\text{-}\mathrm{CA}_0$ proves $a \in \mathrm{Acc}^*$, where $\mathrm{Acc}^*$ is the set of step 1 for $A(X, x) = \forall y \, (y \prec x \to y \in X)$.
10. A set is closed under this operator exactly when it is progressive, as in $\mathrm{WO}(a)$.
    Steps 2 and 3 make $\mathrm{Acc}^*$ a fixed point, so $y \in \mathrm{Acc}^*$ for all $y \prec a$, and every progressive $X$ contains $\mathrm{Acc}^*$ by its definition.
11. So $\Pi^1_1\text{-}\mathrm{CA}_0$ proves $\forall y \, (y \prec a \to y \in X)$ for every progressive $X$, which is $\mathrm{WO}(a)$.

### Parts (b) and (c): the cited lemmas

The lemmas of steps 12 to 16 come from Buchholz's method, first developed for $\mathrm{ID}_\nu$ in Lecture Notes in Mathematics 897 (1981), and we state them without proof.

12. Embedding lemma (cited): each derivation in $\Pi^1_1\text{-}\mathrm{CA}_0$ of a $\Pi^1_1$ sentence translates into a derivation in an infinitary sequent calculus with the [[ω-rule|XAMKAB1BZM]] and, for each $\mu < \omega$, an $\Omega_{\mu+1}$-rule.
    The height and the cut rank of the translation are given by terms of $\mathrm{OT}$ below $\Omega_\omega$.
13. Predicative cut elimination (cited): cuts of a fixed rank can be removed, with the height growing from $\alpha$ to $\omega^\alpha$, as in [[cut elimination|AYRZ98Y0NW]] for the ω-rule.
14. Collapsing lemma (cited): a derivation of height $\alpha$ that uses the $\Omega_{\mu+1}$-rule, with an end sequent of low complexity, becomes a derivation of height $\psi_\mu(\alpha)$ without that rule.
    This is where [[Buchholz's functions|E7WEFRMQTB]] enter.
15. Applying steps 13 and 14 finitely often, from the highest level $\mu$ down to $\mu = 0$, gives a cut-free derivation of each $\Pi^1_1$ theorem with the ω-rule alone, of height $o(b)$ for some term $b \prec \tau$.
16. Boundedness lemma (cited): if $\mathrm{WO}(a)$ has a cut-free ω-derivation of height $\beta$, then $o(a)$ is at most an ordinal computed from $\beta$ by a fixed function that maps ordinals below $\psi_0(\Omega_\omega)$ to ordinals below $\psi_0(\Omega_\omega)$.

### Parts (b) and (c): the upper bound

17. Proof of (b): if $\Pi^1_1\text{-}\mathrm{CA}_0$ proved $\mathrm{WO}(\tau)$, step 15 would give a cut-free derivation of height $o(b) < \psi_0(\Omega_\omega)$.
    Step 16 would then give $o(\tau) < \psi_0(\Omega_\omega)$, against $o(\tau) = \psi_0(\Omega_\omega)$.
18. For (c), the infinitary derivations of steps 12 to 15 have primitive recursive codes, and the reduction steps act primitive recursively on the codes.
19. A derivation of $0 = 1$ in $\Pi^1_1\text{-}\mathrm{CA}_0$ would reduce to a cut-free derivation of the false atomic sentence $0 = 1$, and no rule of the cut-free calculus ends in a false atomic sentence.
20. The termination of this reduction is an instance of quantifier-free transfinite induction along $\prec$ below $\tau$, so primitive recursive arithmetic with this induction proves $\mathrm{Con}(\Pi^1_1\text{-}\mathrm{CA}_0)$.
21. Steps 11, 17, 19 and 20 give parts (a), (b) and (c) of the [[statement|2MGJJTSRFD]].

## Idea

The lower bound reduces $\Pi^1_1$-comprehension to finitely iterated inductive definitions: each inductively defined set is the intersection of all closed sets, which is a $\Pi^1_1$ definition.
The upper bound translates proofs into infinitary derivations, where impredicative comprehension is handled by rules that quantify over all derivations of a lower level.
Cut elimination removes ordinary cuts, and the collapsing functions $\psi_\mu$ remove the impredicative rules one level at a time.
The resulting heights are below $\psi_0(\Omega_\omega)$, and a derivation of small height cannot prove the well-foundedness of a long ordering.

## Variants

Takeuti's original proof of 1967 reduces derivations of a finite Gentzen-style calculus directly and measures them with ordinal diagrams.
It gives part (c) with ordinal diagrams in place of Buchholz's notation.

Pohlers's method of [[local predicativity|5C4YBXQV15]] replaces the $\Omega_{\mu+1}$-rules by a semantic hierarchy of levels and gives the same ordinals.

Buchholz later introduced operator-controlled derivations, in which an operator on sets of ordinals records which ordinals may appear.
They make the collapsing lemma shorter, and Rathjen used them for much stronger theories.
