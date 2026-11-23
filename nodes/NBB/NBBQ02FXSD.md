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

We assign to each derivation of the empty sequent a notation below $\varepsilon_0$, show that a primitive recursive reduction always produces another such derivation with a smaller notation, and conclude by transfinite induction.
The proof follows Gentzen's version of 1938, in the form of the standard textbook presentations.
Steps marked "cited" are lemmas whose proofs are long and are not given here; all other steps are given in full.
We argue in $\mathrm{PRA} + \mathrm{QF}\text{-}\mathrm{TI}(\varepsilon_0)$, and every function below is [[primitive recursive|5NVA2JRHPV]].

**The formal system.**

1. Let $\mathrm{PA}_G$ be a [[sequent calculus|W72CA3R9MP]] for PA.
   Its initial sequents are the logical sequents $A \Rightarrow A$ and the atomic sequents that are true by the defining equations.
   Its rules are the structural and logical rules, cut, and induction: from $\Gamma, A(b) \Rightarrow A(b + 1), \Delta$ infer $\Gamma, A(0) \Rightarrow A(t), \Delta$.
2. (Cited, Lemma 1.) A primitive recursive translation turns each PA proof of $A$ into a $\mathrm{PA}_G$ derivation of $\Rightarrow A$, and PRA proves that the translation is correct.
3. A derivation of $\Rightarrow 0 = 1$ gives a derivation of the empty sequent $\Rightarrow$ by one cut with the true sequent $0 = 1 \Rightarrow$.
   So in PRA, $\operatorname{Con}(\mathrm{PA})$ follows from the statement that no $\mathrm{PA}_G$ derivation ends with $\Rightarrow$.
4. Let $D(d)$ be the primitive recursive predicate "$d$ is a $\mathrm{PA}_G$ derivation of $\Rightarrow$"; we must show $\forall d \, \neg D(d)$.

**The ordinal assignment.**

5. (Cited, Lemma 2.) A primitive recursive map puts each derivation into a regular shape with the same end sequent, in which each eigenvariable is used only once.
6. The *degree* of a cut or an induction is the number of logical symbols in its cut formula or induction formula.
   The *height* of a sequent is the largest degree of the cuts and inductions below it in the derivation.
7. (Cited, Lemma 3.) A primitive recursive function $o$ maps derivations to notations below $\varepsilon_0$, defined from the top down:
   - initial sequents get $1$, and weak structural rules keep the value;
   - a logical rule with one premise adds $1$, and a logical rule with two premises or a cut takes the natural sum $\alpha \mathbin{\#} \beta$;
   - an induction whose premise has value $\omega^{\alpha_1} + \cdots + \omega^{\alpha_k}$, with $\alpha_1$ largest, gives $\omega^{\alpha_1 + 1}$;
   - when the height drops by $k$ from a sequent to the one below, the value is put through $\alpha \mapsto \omega^\alpha$ $k$ times.
8. Each value $o(d)$ is a notation in the standard system for [[epsilon nought|KT50SMH3EC]], so it names an ordinal below $\varepsilon_0$.

**The reduction.**

9. The *end-piece* of a derivation consists of the sequents from the end sequent upward until a logical rule is met.
10. (Cited, Lemma 4.) If $D(d)$, then the end-piece of $d$ has a step other than atomic initial sequents, structural rules and atomic cuts.
    The reason is that in an end-piece made only of these, every sequent is true once closed terms replace the free variables, and the empty end sequent is false.
11. (Cited, Lemma 5, the reduction lemma.) There is a primitive recursive $r$ with $D(r(d))$ and $o(r(d)) \prec o(d)$ whenever $D(d)$.
    The function $r$ applies step (a), and then the first of the steps (b), (c) and (d) that is possible.
12. Step (a): replace each free variable in the end-piece that is not an eigenvariable by $0$.
13. Step (b): if the end-piece contains an induction, its term $t$ is closed after step (a) and has a numeral value $n$.
    Replace the induction by a chain of cuts that joins the instances $A(0) \Rightarrow A(1)$ up to $A(n-1) \Rightarrow A(n)$ of its premise.
14. Step (c): if the end-piece contains a logical initial sequent or a weakening, remove it and shorten the derivation below it.
15. Step (d): otherwise, by Lemma 4, the end-piece contains a *suitable cut*, whose cut formula is introduced by a logical rule on both sides at the boundary of the end-piece.
    Replace it by cuts on the immediate subformulas, and copy the needed parts of the derivation.
16. Step (a) does not change the value, and by Lemma 3 each of the steps (b), (c) and (d) lowers it.
    In step (d) the derivation can grow, but the degree of the cut drops, and this removes a level from a tower of powers of $\omega$ in the value.

**The formalization.**

17. (Cited, Lemma 6.) PRA proves steps 1 to 16 as statements about codes with a free variable $d$; in particular, PRA proves $D(d) \to D(r(d)) \wedge o(r(d)) \prec o(d)$.

**The descent.**

18. [[Assume, for a contradiction|0J0XBKG64S]], that $D(d_0)$ for some $d_0$, and let $d_n = r^n(d_0)$, which is primitive recursive in $n$.
19. By step 17 and induction on $n$ in PRA, $D(d_n)$ and $o(d_{n+1}) \prec o(d_n)$ for all $n$.
20. So $o(d_0) \succ o(d_1) \succ o(d_2) \succ \cdots$ is a primitive recursive sequence of notations that descends for ever.
21. Let $P(x)$ say "$x \ne o(d_n)$ for all $n$".
    If every $y \prec x$ satisfies $P(y)$ and $x = o(d_n)$, then $o(d_{n+1}) \prec x$ contradicts $P(o(d_{n+1}))$, so $\operatorname{Prog}(P)$ holds.
22. [[Transfinite induction|0ZHQMQ2C1N]] along $\prec$ gives $\forall x \, P(x)$, and $x = o(d_0)$ gives a contradiction; this is an [[infinite descent|0EFYCFHYFG]] argument along $\prec$.
23. (Cited, Lemma 7.) The formula $P$ has the unbounded quantifier $\forall n$, but over PRA the conclusion of step 22 still follows from the quantifier-free schema $\mathrm{QF}\text{-}\mathrm{TI}(\varepsilon_0)$.
    Some books instead add the principle that no primitive recursive sequence of notations descends for ever, and stop at step 20.
24. So no $d$ satisfies $D(d)$, and by step 3, $\mathrm{PRA} + \mathrm{QF}\text{-}\mathrm{TI}(\varepsilon_0) \vdash \operatorname{Con}(\mathrm{PA})$. $\blacksquare$

## Idea

Give each derivation an ordinal below $\varepsilon_0$ that measures how far it is from being cut-free.
A derivation of the empty sequent can always be reduced, and each reduction lowers the ordinal.
So a derivation of the empty sequent would give an infinite descending sequence of notations, and transfinite induction excludes that.
Only this last step goes beyond PRA, and it is exactly the step that PA cannot take for itself.

## Variants

Gentzen's version of 1936 used a different calculus and a different reduction procedure, with the same ordinal $\varepsilon_0$.

Schütte's proof embeds PA into an infinitary sequent calculus with the [[ω-rule|XAMKAB1BZM]], where full cut elimination is possible.
The [[cut-elimination theorem|AYRZ98Y0NW]] for that system raises the height of a derivation through a tower of powers of $\omega$, and embedded PA proofs have heights below $\omega \cdot 2$, so the cut-free heights stay below $\varepsilon_0$.

Gödel's [[Dialectica interpretation|HZ17ES9PDY]] reduces the consistency of PA to the consistency of a theory of primitive recursive functionals of finite type, without ordinals.
