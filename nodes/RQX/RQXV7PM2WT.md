---
tag: RQXV7PM2WT
kind: concept
name: Abstract logical systems
aliases: [abstract-logic, institution-theory]
msc: ["03B22", "03C95"]
topics: [H8QZY0RZXZ]
audience: research
uses: [J78Y1M4GND, A2DE66937D, 28NQ0KRHD3, DAMK8XE1FR, FYZ3CJGZYV, D9G8M42GKC]
sources:
  - url: https://en.wikipedia.org/wiki/Institution_(computer_science)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Logical_framework
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Universal_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Abstract_algebraic_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Lindstr%C3%B6m%27s_theorem
    locator: lead section
---

## Summary

An abstract logical system describes a logic by what it does, not by how its formulas are written.
Start with propositional logic and rename the variable $p$ to $r$.
The valid argument $p, p \to q \models q$ becomes $r, r \to q \models q$, which is valid again.
The reason is general: a valuation of the new variables gives a valuation of the old ones, by reading $p$ as $r$.

An abstract system keeps only general features of this kind.
Its usual ingredients are a set of sentences, a [[consequence relation|J78Y1M4GND]] on it, and a class of models with a satisfaction relation.
In the most developed form, an institution, all of these depend on a signature, the vocabulary of the logic.

An institution consists of a [[category|A2DE66937D]] $\mathbf{Sign}$ of signatures and two [[functors|28NQ0KRHD3]].
The functor $\mathrm{Sen} \colon \mathbf{Sign} \to \mathbf{Set}$ gives the sentences over each signature.
The functor $\mathrm{Mod} \colon \mathbf{Sign}^{\mathrm{op}} \to \mathbf{Cat}$ gives the models over each signature.
For each signature $\Sigma$, a satisfaction relation $\models_\Sigma$ relates $\Sigma$-models and $\Sigma$-sentences.
The data must obey the satisfaction condition.
Let $\sigma \colon \Sigma \to \Sigma'$ be a signature morphism, $M'$ a $\Sigma'$-model and $\varphi$ a $\Sigma$-sentence.
Then
$$M' \models_{\Sigma'} \mathrm{Sen}(\sigma)(\varphi) \iff \mathrm{Mod}(\sigma)(M') \models_\Sigma \varphi.$$
In words, a translated sentence is true in a model exactly when the original sentence is true in the cut-down model.

Other abstract systems are Lindström's abstract logics, the structural consequence relations of abstract algebraic logic, and logical frameworks.
A logical framework is a metalanguage in which object logics are encoded.
The abstract view matters for two reasons.
Theorems proved once for all such systems apply to every logic, and translations between logics get a precise meaning.

## Motivation

Many results of logic use only a few general features of the logic.
Examples are the Lindenbaum lemma, the basic properties of semantic consequence, and the fact that renaming symbols preserves consequence.
Computer science adds a practical need.
Specification languages use many logics, such as equational, first-order, higher-order and temporal logic, and a specification must move along changes of vocabulary.
Joseph Goguen and Rod Burstall introduced institutions to make such constructions independent of the logic.
In another direction, Per Lindström asked what singles out first-order logic among all logics, and his answer needed a precise notion of "a logic".

## Notation

For a signature morphism $\sigma \colon \Sigma \to \Sigma'$, we write $\sigma(\varphi)$ for $\mathrm{Sen}(\sigma)(\varphi)$, the translation of $\varphi$.
We write $M'|_\sigma$ for $\mathrm{Mod}(\sigma)(M')$, the reduct of $M'$.
The satisfaction condition then reads $M' \models_{\Sigma'} \sigma(\varphi) \iff M'|_\sigma \models_\Sigma \varphi$.
We write $\Gamma \models_\Sigma \varphi$ when every $\Sigma$-model that satisfies all sentences of $\Gamma$ satisfies $\varphi$.
Here $\mathbf{Sign}^{\mathrm{op}}$ is the [[opposite category|DAMK8XE1FR]].
$\mathrm{Mod}$ reverses morphisms, since a model of the larger signature can be cut down to the smaller one.
Many authors let $\mathrm{Mod}$ take values in $\mathbf{Set}$ or in classes of models, when model morphisms are not needed.

## Remarks

### Logics as consequence plus semantics

The simplest abstract system is a set $L$ with a consequence relation, as in Tarski's work.
[[Classical propositional consequence|5X683DYC8S]] is one, and derivability in any Hilbert system is another.
Adding semantics gives a set $L$, a class $K$ of models and a satisfaction relation.
The semantic consequence $\models_K$ is then a consequence relation, by the argument for any class of models.

José Meseguer's general logics combine an institution with an entailment system, a proof-theoretic consequence relation for each signature.
Soundness says that the proof-theoretic relation is contained in $\models_\Sigma$, and completeness gives the reverse inclusion.
Willem Blok and Don Pigozzi defined algebraizable logics.
In such a logic, the structural consequence relation matches an equational consequence over a class of algebras; see [[algebraic logic|QYA4H5Y7VR]].

### Institutions and translation

[[Propositional logic|4Y5D1JY6RV]] is an institution.
Its signatures are sets of variables, its models are valuations, and the reduct of $v'$ along $\sigma$ is $v' \circ \sigma$.
[[First-order logic|9J3RXB9HJG]] is another, where a reduct renames or forgets symbols but keeps the universe.
In an institution, each $\models_\Sigma$ is a consequence relation on $\mathrm{Sen}(\Sigma)$.
The satisfaction condition gives the first general theorem: translation along a signature morphism preserves consequence.

1. Let $\sigma \colon \Sigma \to \Sigma'$, and assume $\Gamma \models_\Sigma \varphi$.
2. Let $M'$ be a $\Sigma'$-model that satisfies $\sigma(\gamma)$ for every $\gamma \in \Gamma$.
3. By the satisfaction condition, $M'|_\sigma$ satisfies every $\gamma \in \Gamma$.
4. By the assumption in step 1, $M'|_\sigma \models_\Sigma \varphi$.
5. By the satisfaction condition again, $M' \models_{\Sigma'} \sigma(\varphi)$.
   Since $M'$ was arbitrary, $\sigma[\Gamma] \models_{\Sigma'} \sigma(\varphi)$.

The converse fails in general.
A morphism that sends both $p$ and $q$ to $r$ turns the non-consequence $p \not\models q$ into the consequence $r \models r$.
Institution-independent model theory, developed in Răzvan Diaconescu's book of that title, proves results such as interpolation at this level.

### Abstract logics in the sense of Lindström

An abstract logic in the sense of Lindström assigns to each vocabulary a class of sentences and a satisfaction relation with structures.
It must satisfy closure conditions such as invariance under isomorphism, renaming of symbols, reducts, Boolean operations and relativization.
This is close to an institution whose signatures are vocabularies.

[[Lindström's theorem|FYZ3CJGZYV]] says that no such logic that properly extends first-order logic has both compactness and the downward Löwenheim-Skolem property.
The two properties pull in different directions.
The [[infinitary logic|PQG7VAZ1R2]] $L_{\omega_1 \omega}$ keeps downward Löwenheim-Skolem but loses compactness.
Adding the [[generalized quantifier|MFV98WTF4G]] "there are uncountably many" gives a logic that is compact for countable sets of sentences.
It loses downward Löwenheim-Skolem, because "there are uncountably many $x$ with $x = x$" has only uncountable models.

### Universal logic and the Lindenbaum lemma

Universal logic, a project promoted by Jean-Yves Béziau, studies general structures of logics as universal algebra studies general algebras.
Its objects include consequence relations, institutions and logical matrices, and its journal is *Logica Universalis*.
A typical result is the Lindenbaum lemma for a finitary consequence relation $\vdash$.
If $\Gamma \nvdash \varphi$, there is a deductively closed $T \supseteq \Gamma$ that is maximal among the sets with $T \nvdash \varphi$.

1. Let $\mathcal{F}$ be the family of sets $\Delta \supseteq \Gamma$ with $\Delta \nvdash \varphi$, ordered by inclusion.
   It contains $\Gamma$.
2. Let $U$ be the union of a nonempty chain in $\mathcal{F}$, and suppose $U \vdash \varphi$.
   By finitarity a finite subset of $U$ yields $\varphi$, and it lies in one member of the chain.
3. By monotonicity that member yields $\varphi$, a contradiction.
   So $U \in \mathcal{F}$, and by Zorn's lemma $\mathcal{F}$ has a maximal element $T$.
4. Let $T \vdash \psi$ with $\psi \notin T$.
   By maximality $T, \psi \vdash \varphi$, and cut gives $T \vdash \varphi$, a contradiction.
   So $T$ is deductively closed.

### Logical frameworks

A logical framework is a formal system that serves as a [[metalanguage|D9G8M42GKC]] for other logics.
An object logic is encoded in it, and derivations of the object logic become objects of the framework.
The Edinburgh Logical Framework LF of Robert Harper, Furio Honsell and Gordon Plotkin is a [[dependent type|M6W6ZB4PPX]] theory.
In LF, implication and modus ponens are encoded by declarations such as
$$o : \mathrm{type}, \quad \mathrm{imp} : o \to o \to o, \quad \mathrm{pf} : o \to \mathrm{type}, \quad \mathrm{mp} : \Pi A{:}o.\, \Pi B{:}o.\, \mathrm{pf}\,(\mathrm{imp}\,A\,B) \to \mathrm{pf}\,A \to \mathrm{pf}\,B.$$
Derivations of a formula $\varphi$ correspond to terms of type $\mathrm{pf}\,\varphi$, a principle called judgments as types.
The proof assistant Isabelle, designed by Lawrence Paulson, is built in the same way on the meta-logic Isabelle/Pure.
Isabelle/HOL and Isabelle/ZF are object logics in it; see [[mathematical software and formalization|F3F5GGYHMM]].

### Watch out

Do not write $\mathrm{Mod}$ as covariant.
A signature morphism $\Sigma \to \Sigma'$ turns $\Sigma'$-models into $\Sigma$-models, so $\mathrm{Mod}$ is a functor on $\mathbf{Sign}^{\mathrm{op}}$.

Do not assume that translation reflects consequence.
It preserves consequence, but a non-injective signature morphism can create new consequences.

Not every choice of sentences gives an institution.
A [[sentence about the whole signature|T7CGA2T940]] changes its meaning when the signature grows, and it breaks the satisfaction condition.
The [[closed-world assumption|W4QZGRCDPA]] gives an inference relation that is not monotone, so it is not the semantic consequence of any class of models.
A bare set of strings, such as the language of a [[formal grammar|DP1HXZGPCM]], has no consequence relation and no semantics, so it is not a logical system.

Do not confuse the framework with the object logic.
A theorem of the framework about an encoding is a metatheorem about the object logic only after an adequacy proof for the encoding.

### History

Alfred Tarski studied consequence operations on abstract sets of sentences around 1930.
Per Lindström proved his characterization of first-order logic in 1969, using abstract logics, and this started abstract model theory.
Joseph Goguen and Rod Burstall published "Institutions: abstract model theory for specification and programming" in the *Journal of the ACM* in 1992.
Harper, Honsell and Plotkin published "A framework for defining logics", on LF, in the *Journal of the ACM* in 1993.

### Try it

Let $\sigma \colon \{ p, q \} \to \{ r \}$ send both variables to $r$.
Find $\Gamma$ and $\varphi$ with $\Gamma \not\models \varphi$ but $\sigma[\Gamma] \models \sigma(\varphi)$.
Answer: take $\Gamma = \{ p \}$ and $\varphi = q$.
The valuation $p \mapsto 1, q \mapsto 0$ shows $p \not\models q$, while $r \models r$ holds by reflexivity.

Let $\sigma \colon \Sigma \to \Sigma'$ be injective in the propositional institution.
Show that every $\Sigma$-valuation $v$ is a reduct.
Answer: put $v'(\sigma(p)) = v(p)$, which is well defined because $\sigma$ is injective, and $v'(s) = 0$ for $s$ outside the image.
Then $v' \circ \sigma = v$.

Does translation along an injective $\sigma$ reflect consequence?
Answer: yes.
If $v$ witnesses $\Gamma \not\models_\Sigma \varphi$, extend it to $v'$ as above, and the satisfaction condition shows that $v'$ witnesses $\sigma[\Gamma] \not\models_{\Sigma'} \sigma(\varphi)$.

## Explanations

### L1 human

Many different logics exist: for "and" and "or", for statements about all objects, for time, for knowledge.
Each of them has sentences, some notion of "world" in which sentences are true or false, and a rule for when one sentence follows from others.
An abstract logical system keeps only this common shape.
Then a fact proved for the shape holds for every logic at once.
A simple fact of this kind: if we rename the letters in a valid argument, it stays valid.

### L2 human

We check the satisfaction condition in a small case of the propositional institution.

1. Let $\Sigma = \{ p \}$, $\Sigma' = \{ r, s \}$ and let $\sigma \colon \Sigma \to \Sigma'$ send $p$ to $r$.
2. Take the $\Sigma$-sentence $\varphi = \neg p$, so $\sigma(\varphi) = \neg r$.
3. Take the $\Sigma'$-model $v'$ with $v'(r) = 0$ and $v'(s) = 1$.
   Its reduct is $v'|_\sigma = v' \circ \sigma$, the valuation with $p \mapsto 0$.
4. $v' \models \neg r$ holds, since $v'(r) = 0$, and $v'|_\sigma \models \neg p$ holds, since $p \mapsto 0$.
   Both sides agree.
5. The variable $s$ plays no role, because $\sigma(\varphi)$ does not mention it.

The typical use of the satisfaction condition is to move results along changes of notation, for example to rename the symbols of a theory.
A trap is to define sentences that mention the whole signature, such as "all variables are true", which break the condition.

### L3 human

Institutions are a categorical abstraction of model theory.
An institution is a functor from $\mathbf{Sign}$ into a category of "rooms", each holding sentences, models and satisfaction.
Institution morphisms and comorphisms relate different logics.
Theory morphisms, colimits of specifications, the specification language CASL and the Heterogeneous Tool Set are built on this structure.
Combining an institution with a proof system per signature gives a logic in the sense of Meseguer.
Soundness and completeness then state that the two consequence relations agree.

Lindström's approach leads to abstract model theory, where logics are compared by their model-theoretic properties.
It also leads to the study of extensions of first-order logic in [[second-order logic and extensions|MDHDYV8QZW]].
Logical frameworks connect the subject with [[type theory|Q48KGV33AH]].
The Curry-Howard correspondence and the judgments-as-types principle turn the metatheory of an object logic into type checking.
The three views agree on one lesson.
A logic is determined by its consequence relation and its semantics, and a translation between logics should preserve both.
