---
tag: NBBQ02FXSD
kind: proof
name: Structure of Gentzen's consistency proof by reduction of derivations
msc: ["03F30", "03F15", "03F05"]
topics: [XTTKZTYDSD]
audience: grad
proves: QPV0HNP22S
uses: [W72CA3R9MP, AYRZ98Y0NW, 0QFT7Z76N5, KT50SMH3EC, 5NVA2JRHPV, NB2BCZR40F, 0ZHQMQ2C1N]
methods: [0J0XBKG64S, 0EFYCFHYFG, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Gentzen's_consistency_proof
    locator: Gentzen's theorem
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Upper bound
---

## Proof

This is the structure of the proof in the form of Gentzen's version of 1938.
The steps marked "cited" are lemmas whose proofs are long and are not given here.
All other steps are given in full.
We argue in $\mathrm{PRA} + \mathrm{QF}\text{-}\mathrm{TI}(\varepsilon_0)$, and every function below is [[primitive recursive|5NVA2JRHPV]].

**The formal system.**

1. Let $\mathrm{PA}_G$ be a [[sequent calculus|W72CA3R9MP]] for PA. Its initial sequents are the logical sequents $A \Rightarrow A$ and the atomic sequents that are true by the defining equations. Its rules are the structural and logical rules, cut, and induction: from $\Gamma, A(b) \Rightarrow A(b + 1), \Delta$ infer $\Gamma, A(0) \Rightarrow A(t), \Delta$.
2. (Cited, Lemma 1.) A primitive recursive translation turns each PA-proof of $A$ into a $\mathrm{PA}_G$-derivation of $\Rightarrow A$. PRA proves that the translation is correct.
3. So $\operatorname{Con}(\mathrm{PA})$ follows in PRA from the statement that no $\mathrm{PA}_G$-derivation ends with the empty sequent $\Rightarrow$. A derivation of $0 = 1$ gives a derivation of $\Rightarrow$ by one cut with the true sequent $0 = 1 \Rightarrow$.
4. Let $D(d)$ be the primitive recursive predicate "$d$ is a $\mathrm{PA}_G$-derivation of $\Rightarrow$". We must show $\forall d \, \neg D(d)$.

**The ordinal assignment.**

5. (Cited, Lemma 2.) A primitive recursive map puts each derivation into a normal shape with the same end sequent. In this shape, each eigenvariable is used only once.
6. The *degree* of a cut or of an induction is the number of logical symbols in its cut formula or its induction formula. The *height* of a sequent in a derivation is the largest degree of the cuts and inductions below it.
7. (Cited, Lemma 3.) A primitive recursive function $o$ maps derivations to notations below $\varepsilon_0$. It is defined from the top down by these rules.
   - Initial sequents get $1$, and structural rules keep the value.
   - A logical rule with one premise adds $1$. A logical rule with two premises, or a cut, takes the natural sum of the values of the premises.
   - An induction raises the value to a power of $\omega$.
   - Between a sequent and the sequent below it, the value is put through $\alpha \mapsto \omega^\alpha$ as many times as the height drops.
8. The value $o(d)$ is a notation in the standard system for [[epsilon nought|KT50SMH3EC]], so it names an ordinal below $\varepsilon_0$.

**The reduction.**

9. The *end-piece* of a derivation is the part below the lowest logical rules. It has the sequents from the end sequent upward until a logical rule is met.
10. (Cited, Lemma 4.) If $D(d)$, then the end-piece of $d$ has a step other than atomic initial sequents, structural rules and atomic cuts. Reason: in an end-piece made only of these, every sequent is true once closed terms replace the free variables. The empty end sequent is false.
11. (Cited, Lemma 5, the reduction lemma.) There is a primitive recursive function $r$ such that, for every $d$ with $D(d)$, $D(r(d))$ and $o(r(d)) \prec o(d)$. The function $r$ applies step (a), and then the first of the steps (b), (c) and (d) that is possible.
12. Step (a): if the end-piece contains a free variable that is not an eigenvariable, replace it by $0$.
13. Step (b): if the end-piece contains an induction, its term $t$ is closed after step (a), and it has a numeral value $n$. Replace the induction by a chain of cuts that joins the instances $A(0) \Rightarrow A(1)$ to $A(n-1) \Rightarrow A(n)$ of its premise.
14. Step (c): if the end-piece contains a logical initial sequent or a weakening, remove it and shorten the derivation below it.
15. Step (d): otherwise, by Lemma 4, the end-piece contains a *suitable cut*. Its cut formula is introduced by a logical rule on both sides, at the boundary of the end-piece. Replace it by cuts on the immediate subformulas, and copy the needed parts of the derivation.
16. Step (a) does not change the value, and by Lemma 3 each of the steps (b), (c) and (d) lowers it. In step (d) the derivation can grow, but the degree of the cut drops. This lowers the tower of powers in the assignment.

**The formalization.**

17. (Cited, Lemma 6.) PRA proves the facts of steps 1 to 16, as statements about codes with a free variable $d$. In particular, PRA proves $D(d) \to D(r(d)) \wedge o(r(d)) \prec o(d)$.

**The descent.**

18. [[Assume, for a contradiction|0J0XBKG64S]], that $D(d_0)$ holds for some $d_0$. Let $d_n = r^n(d_0)$, the result of $n$ reductions. This sequence is primitive recursive in $n$.
19. By step 17 and induction on $n$ in PRA, $D(d_n)$ and $o(d_{n+1}) \prec o(d_n)$ hold for all $n$.
20. So $o(d_0) \succ o(d_1) \succ o(d_2) \succ \cdots$ is a primitive recursive sequence of notations that descends for ever.
21. Let $P(x)$ say "$x \ne o(d_n)$ for all $n$". If every $y \prec x$ satisfies $P(y)$ and $x = o(d_n)$, then $o(d_{n+1}) \prec x$ contradicts $P(o(d_{n+1}))$. So $\operatorname{Prog}(P)$ holds.
22. [[Transfinite induction|0ZHQMQ2C1N]] along $\prec$ gives $\forall x \, P(x)$, and $x = o(d_0)$ gives a contradiction. This is an [[infinite descent|0EFYCFHYFG]] argument along $\prec$.
23. (Cited, Lemma 7.) The formula $P$ of step 21 has the unbounded quantifier $\forall n$. Over PRA, the conclusion of step 22 still follows from the quantifier-free schema $\mathrm{QF}\text{-}\mathrm{TI}(\varepsilon_0)$. Some books instead add the principle that no primitive recursive sequence of notations descends for ever, and stop at step 20.
24. So no $d$ satisfies $D(d)$. By step 3, $\mathrm{PRA} + \mathrm{QF}\text{-}\mathrm{TI}(\varepsilon_0) \vdash \operatorname{Con}(\mathrm{PA})$. $\blacksquare$

## Idea

Assign to each derivation an ordinal below $\varepsilon_0$ that measures how far it is from cut-free.
A derivation of the empty sequent can always be reduced, and each reduction lowers the ordinal.
A derivation of the empty sequent would therefore give an infinite descending sequence of notations, which transfinite induction excludes.
Only this last step goes beyond PRA.

## Variants

- Gentzen's version of 1936 used a different calculus and a different reduction procedure, with the same ordinal $\varepsilon_0$.
- Schütte's proof embeds PA into an infinitary sequent calculus with the [[ω-rule|XAMKAB1BZM]], where full cut elimination is possible. The [[cut-elimination theorem|AYRZ98Y0NW]] for this system raises the height of a derivation through a tower of powers of $\omega$. The bound $\varepsilon_0$ comes from the heights $\omega + k$ of embedded PA-proofs.
- Gödel's [[Dialectica interpretation|HZ17ES9PDY]] reduces the consistency of PA to the consistency of a theory of primitive recursive functionals of finite type, without ordinals.
