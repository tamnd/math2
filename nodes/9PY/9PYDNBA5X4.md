---
tag: 9PYDNBA5X4
kind: concept
name: Barcan formula
aliases: [barcan-formulas, converse-barcan-formula]
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
uses: [D2H3S12V7X, NGHWZ9Y7ZV, G989VP2NGP, 2QPT4KCM0Q, VC3A2VWXND]
sources:
  - url: https://en.wikipedia.org/wiki/Barcan_formula
    locator: The Barcan formula
  - url: https://en.wikipedia.org/wiki/Barcan_formula
    locator: Converse Barcan formula
  - url: https://en.wikipedia.org/wiki/Ruth_Barcan_Marcus
    locator: Quantified modal logic
---

## Summary

Take two worlds $w$ and $v$ with $w R v$, where $w$ has one object $1$ and $v$ has the objects $1$ and $2$.
If $1$ has the property $P$ at both worlds and $2$ lacks it, then "every object is necessarily $P$" is true at $w$, and "necessarily every object is $P$" is false there.

The Barcan formula $\mathrm{BF}$ is the following schema of [[quantified modal logic|D2H3S12V7X]], for any formula $\varphi$.
$$\forall x \, \square \varphi \to \square \, \forall x \, \varphi$$
The converse Barcan formula $\mathrm{CBF}$ is the following schema.
$$\square \, \forall x \, \varphi \to \forall x \, \square \varphi$$
We use frames with domains $(W, R, D)$ as in the semantics of [[quantified modal logic|D2H3S12V7X]], with assignments into $U = \bigcup_w D(w)$ and quantifiers at $w$ ranging over $D(w)$.
Every instance of BF is valid on $(W, R, D)$ exactly when the domains decrease, that is, $w R v$ implies $D(v) \subseteq D(w)$.
Every instance of CBF is valid on $(W, R, D)$ exactly when the domains increase, that is, $w R v$ implies $D(w) \subseteq D(v)$.
So the two schemata turn statements about what exists at each world into axioms.

## Motivation

In a Kripke model with domains, a quantifier at a world sees only the objects of that world.
The formula $\forall x \square \varphi$ speaks about the objects of the present world, while $\square \forall x \varphi$ speaks about the objects of each accessible world.
The two agree when no accessible world has new objects.
So the exchange of $\forall x$ and $\square$ is a statement about the growth of domains.
Philosophers ask whether merely possible objects exist, and BF gives this question a formal shape: it says that whatever could exist already exists.

## Notation

BF has the dual form $\lozenge \exists x \varphi \to \exists x \lozenge \varphi$.
To get it, put $\neg \varphi$ for $\varphi$ in BF and take the contrapositive.
In the same way, CBF has the dual form $\exists x \lozenge \varphi \to \lozenge \exists x \varphi$.
Increasing domains are also called expanding domains.
A frame with $D(w) = U$ for every $w$ has constant domains.

## Remarks

### Examples

1. [[The Barcan formula holds on a model with decreasing domains|F87MSJBXMQ]] checks an instance of BF on a two-world model where the domain shrinks along $R$.
2. [[The Barcan formula is derivable in quantified S5|PDGCDVGCA3]] gives a derivation that uses only the axiom B, $p \to \square \lozenge p$, of the [[Brouwerian modal logic|2QPT4KCM0Q]].
3. [[The converse Barcan formula and increasing domains|ZYYTXBXNA2]] derives CBF in $\mathsf{QK}$ and refutes it on a model where a domain shrinks.
4. With constant domains, the domains both decrease and increase, so BF and CBF are both valid.
5. When $R$ is [[symmetric|061J5VGSPT]], increasing domains are also decreasing, since $w R v$ gives $v R w$.
   On such a frame BF is valid exactly when CBF is valid.

### Non-examples

1. [[The Barcan formula fails on an S4 model with growing domains|RBTX5HWXBB]] gives a reflexive and transitive frame where a new object appears at an accessible world.
   There the instance $\forall x \square P x \to \square \forall x P x$ fails.
2. The formula $\forall x \, \lozenge \varphi \to \lozenge \forall x \, \varphi$ is not a form of BF, and it fails even with constant domains.
   Let $w$ see two worlds $u_1$ and $u_2$, with domain $\{1, 2\}$ everywhere, $I(P, u_1) = \{1\}$ and $I(P, u_2) = \{2\}$.
   Then $\forall x \lozenge P x$ holds at $w$, and no successor has $\forall x P x$.
3. The formula $\exists x \square \varphi \to \square \exists x \varphi$ is not BF either.
   It is valid on frames with increasing domains, the condition of CBF.

### Why the frame conditions hold

Assume decreasing domains and $w \models_\sigma \forall x \square \varphi$, and let $w R v$ and $d \in D(v)$.
Then $d \in D(w)$, so $w \models_{\sigma[x \mapsto d]} \square \varphi$, and $v \models_{\sigma[x \mapsto d]} \varphi$.
So $v \models_\sigma \forall x \varphi$, and BF holds at $w$.
Conversely, let $w R v$ and $d \in D(v) \setminus D(w)$, and put $I(P, u) = D(w)$ for every $u$.
Then $\forall x \square P x$ is true at $w$, and $\forall x P x$ fails at $v$ at the object $d$, so BF fails at $w$.

For CBF, assume increasing domains and $w \models_\sigma \square \forall x \varphi$, and let $d \in D(w)$ and $w R v$.
Then $d \in D(v)$, so $v \models_{\sigma[x \mapsto d]} \varphi$, and CBF holds at $w$.
Conversely, let $w R v$ and $d \in D(w) \setminus D(v)$, and put $I(P, u) = D(u)$ for every $u$.
Then $\square \forall x P x$ is true at $w$, and $\square P x$ fails at $w$ under $x \mapsto d$, because $d \notin I(P, v)$.

### What the logics prove

CBF is derivable in $\mathsf{QK}$ from instantiation, [[necessitation|G989VP2NGP]], the axiom K and generalization.
So every quantified normal modal logic with the classical quantifier rules proves CBF.
BF is derivable in $\mathsf{QKB}$, and so in $\mathsf{QS5}$, since T and 5 together give B.
BF is not derivable in $\mathsf{QS4}$.
The model of the first non-example is an $\mathsf{S4}$ frame with increasing domains, and $\mathsf{QS4}$ is sound for such frames when formulas at $w$ are evaluated under assignments into $D(w)$.
For the language without identity, $\mathsf{QK}$ plus BF is complete for the frames with constant domains.

### Watch out

Do not swap the frame conditions.
BF goes with decreasing domains, so no new object appears along $R$, and CBF goes with increasing domains, so no object disappears along $R$.
Do not expect BF from the classical quantifier rules.
Only CBF follows from them, and BF needs an extra axiom such as B, or constant domains.
A condition on frames is not a condition on one model.
If $P$ is empty at every world, the instance of BF with $P x$ is true at every world of any model, even when the domains grow.

### History

Ruth Barcan (later Ruth Barcan Marcus) stated the formula in 1946 as an axiom of the first axiomatic system of quantified modal logic.
She gave it in the dual form $\lozenge \exists x \varphi \to \exists x \lozenge \varphi$, with strict implication.
Arthur Prior showed that the formula is derivable in quantified $\mathsf{S5}$.
Saul Kripke gave in 1963 a semantics with varying domains in which both BF and CBF can fail, and the domain conditions above come from that semantics.

### Try it

First, let $W = \{w, v\}$ with $R = \{(w, v), (v, w)\}$, $D(w) = \{1\}$ and $D(v) = \{1, 2\}$.
Is BF valid on this frame, and is CBF?
Neither: $w R v$ with $2 \in D(v) \setminus D(w)$ breaks BF, and $v R w$ with $2 \in D(v) \setminus D(w)$ breaks CBF.

Second, let $R = \{(w, v)\}$, $D(w) = \{1, 2\}$, $D(v) = \{1\}$, $I(P, w) = \emptyset$ and $I(P, v) = \{1\}$.
Which of the instances of BF and CBF with $P x$ hold at $w$?
BF holds, because its antecedent $\forall x \square P x$ fails at $x \mapsto 2$.
CBF fails, because $\square \forall x P x$ holds at $w$ while $\square P x$ fails at $x \mapsto 2$.

## Explanations

### L1 human

Think of possible worlds as possible futures, each with its own list of people who exist there.
The Barcan formula says: if everyone who exists now is happy in every future, then in every future everyone is happy.
This can fail when new people are born in a future, since we said nothing about them.
So the Barcan formula holds exactly when no new objects appear as we move to accessible worlds.
For example, with $2$ people now and $3$ people in some future, the formula can fail.

### L2 human

We check BF and CBF on a frame with constant domains.

1. Let $W = \{w, v\}$, $R = \{(w, v)\}$ and $D(w) = D(v) = \{1, 2\}$.
2. Let $I(P, w) = \emptyset$ and $I(P, v) = \{1, 2\}$.
3. At $w$, $\square P x$ holds under $x \mapsto 1$ and under $x \mapsto 2$, since the only successor $v$ has $1, 2 \in I(P, v)$.
   So $w \models \forall x \square P x$.
4. At $v$, $\forall x P x$ holds, since $D(v) \subseteq I(P, v)$.
   So $w \models \square \forall x P x$, and BF holds at $w$.
5. Steps 3 and 4 give both sides at $w$, so CBF holds at $w$ as well.
6. At $v$ both formulas hold, because $v$ has no successor and every $\square$-formula is true at $v$.

The typical use of BF is as an axiom when we want one domain for all worlds.
Watch out: BF holds here because the domains are constant, not because $P$ is special.
A new object at $v$ outside $I(P, v)$ would break it.

### L3 human

BF and CBF are the simplest cases of correspondence for frames with domains.
Each is valid on a frame exactly when a first-order condition on $R$ and $D$ holds, as in [[modal correspondence theory|3RYBWYPJVD]] for propositional frames.
In the functor view of quantified modal logic, increasing domains are inclusions along $R$, and CBF says that each object has an image at every accessible world.
In $\mathsf{S5} \times \mathsf{S5}$ and in cylindric algebras, the operators $\exists x$ and $\lozenge$ commute in both directions, which is the algebraic form of BF and CBF together; see [[products of modal logics|JA2EBWVW8A]].
The debate between [[modal possibilism|RXK66SDTAR]] and [[modal actualism|9ZK5VAWDKN]] is in large part a debate about whether to accept BF.
