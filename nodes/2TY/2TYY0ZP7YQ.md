---
tag: 2TYY0ZP7YQ
kind: concept
name: Robinson forcing
aliases: [robinson-forcing, model-theoretic-forcing, infinite-forcing, finite-forcing, generic-model]
msc: ["03C25"]
topics: [1A9JSC5YG8]
audience: research
uses: [92SWXST1ZM, MVCH6N9SNW, 676H7EGTKJ, G8TRE2KSRV, 6M98MCW575, 68GG7QKN7C, F2DTWW9HP7]
sources:
  - url: https://en.wikipedia.org/wiki/Forcing_(mathematics)
  - book: isbn:9780521587136
---

## Summary

Let $T$ be an [[inductive|G8TRE2KSRV]] [[theory|92SWXST1ZM]] in a signature $L$, and let $T_\forall$ be its set of universal consequences.
*Infinite forcing* defines, for a [[model|MVCH6N9SNW]] $M$ of $T_\forall$ and a sentence $\varphi$ with parameters in $M$ built from atomic formulas with $\neg$, $\land$ and $\exists$, a relation $M \Vdash \varphi$:

- for atomic $\varphi$, $M \Vdash \varphi$ if $M \models \varphi$;
- $M \Vdash \varphi \land \psi$ if $M \Vdash \varphi$ and $M \Vdash \psi$, and $M \Vdash \exists x \, \varphi(x)$ if $M \Vdash \varphi(a)$ for some $a \in M$;
- $M \Vdash \neg \varphi$ if no model $N \supseteq M$ of $T_\forall$ has $N \Vdash \varphi$.

$M$ is *infinitely generic* if $M \Vdash \varphi \iff M \models \varphi$ for all such $\varphi$.
*Finite forcing* does the same with finite sets of atomic and negated atomic sentences, consistent with $T$, in place of structures, and gives the *finitely generic* models.
The method produces well-behaved [[existentially closed models|6M98MCW575]] even when $T$ has no model companion.

## Motivation

The e.c. models of an inductive theory always exist, but they can have very different theories, as for groups.
One would like a canonical subclass of e.c. models that behaves like the models of a model companion.
Forcing gives two such classes, by deciding each sentence along a chain of extensions, as Cohen's [[forcing|F2DTWW9HP7]] decides statements about a generic set.
When the [[model companion|68GG7QKN7C]] exists, both classes are its models, so forcing is a generalization of the model companion.

## Notation

One writes $T^F$ for the theory of the infinitely generic models, the *infinite forcing companion*, and $T^f$ for the theory of the finitely generic models, the *finite forcing companion*.
Some books replace the atomic clause of finite forcing by $T \cup p \vdash \varphi$.

## Remarks

### Examples

- [[Algebraically closed fields are infinitely generic|3TAHEB9Z2Z]]: since $\mathrm{ACF}$ is model complete, forcing and truth agree in it.
- [[Dense linear orders are infinitely generic|9NGY6NCJGE]], by the same argument for $\mathrm{DLO}$.
- If $T$ has a model companion $T^*$, then $T^f = T^F = T^*$.
- For the theory of groups, the infinitely generic groups are e.c. groups, but their class is not elementary, since its theory would be a model companion.

### Non-examples

- [[The rational field is not infinitely generic|PE6618GS47]]: it satisfies $\neg \exists x \, (x^2 = 2)$ without forcing it.
- A model of $T_\forall$ that is not e.c. is never generic, since generic models are e.c.

### Basic properties

- Forcing is monotone: if $M \subseteq N$ and $M \Vdash \varphi$, then $N \Vdash \varphi$.
- Every model of $T_\forall$ is a [[substructure|676H7EGTKJ]] of an infinitely generic model, and every infinitely generic model is e.c.
- If $M \subseteq N$ are infinitely generic, then $M \preceq N$.
- In a countable signature, finitely generic models exist and are e.c., and they can be built with the omitting types theorem or the Baire category theorem.
- $T^f$ and $T^F$ have the same universal consequences as $T$.

### History

Abraham Robinson adapted Cohen's forcing from set theory to model theory, in a finite and an infinite version.
The two versions give the finite and the infinite forcing companions of a theory.

### Common errors

- Confusing infinitely generic with e.c. Every infinitely generic model is e.c., and the two notions agree when the model companion exists. In general, infinite genericity is the extra condition that forcing agrees with truth.
- Assuming that $T^f = T^F$ without proof. The two companions agree when $T$ has a model companion, but they are defined by different relations, and in general one must compare them.

## Explanations

### L1 human

Forcing is a way to build a model one step at a time, while deciding every question about it.
At each step one asks whether a statement can still be made true in a larger model.
If it cannot, one decides that it is false forever.
The models built in this way are "generic": they are closed under solving equations and they decide every statement in the most stable way.

### L2 human

We see the negation clause for fields, with conditions that are integral domains.

1. Let $\varphi$ be $\exists x \, (x \cdot x = 2)$. The field $\Q(\sqrt 2)$ forces $\varphi$, since $\sqrt 2 \cdot \sqrt 2 = 2$ is atomic and true there.
2. So $\Q$ does not force $\neg \varphi$, because $\Q(\sqrt 2) \supseteq \Q$ forces $\varphi$.
3. $\Q$ does not force $\varphi$ either, since $2$ has no square root in $\Q$.
4. An algebraically closed field $K$ forces $\varphi$ directly, since it has a square root of $2$.

So $\Q$ leaves $\varphi$ undecided, while generic fields decide it, and decide it in agreement with truth.
The typical use of forcing is to single out a class of e.c. models with a common theory.
A trap is the negation clause: $M \Vdash \neg \varphi$ is stronger than $M \not\Vdash \varphi$.

### L3 human

Robinson forcing replaces the model companion when it does not exist.
For an inductive theory $T$, every model of $T_\forall$ embeds into an infinitely generic model, and an infinitely generic model that is a substructure of another one is an elementary substructure.
So the infinitely generic models behave like the models of a model companion, except that they need not form an elementary class.
For groups and for arithmetic, the generic models are a source of e.c. structures with strong closure properties, and the finite version connects with Baire category arguments and omitting types.
