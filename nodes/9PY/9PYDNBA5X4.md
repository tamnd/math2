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

The Barcan formula is the schema of [[quantified modal logic|D2H3S12V7X]]
$$\forall x \, \square \varphi \to \square \, \forall x \, \varphi, \qquad (\mathrm{BF})$$
and the converse Barcan formula is the schema
$$\square \, \forall x \, \varphi \to \forall x \, \square \varphi, \qquad (\mathrm{CBF})$$
where $\varphi$ is any formula.
Let $(W, R, D)$ be a Kripke frame with domains, as defined on the main page of quantified modal logic, with assignments into $U = \bigcup_w D(w)$ and quantifiers at $w$ ranging over $D(w)$.
Then every instance of BF is valid on $(W, R, D)$ if and only if the domains decrease along $R$: $w R v$ implies $D(v) \subseteq D(w)$.
Every instance of CBF is valid on $(W, R, D)$ if and only if the domains increase along $R$: $w R v$ implies $D(w) \subseteq D(v)$.
The two formulas matter because they turn questions about what exists at each world into axioms, and because BF is derivable in quantified $\mathsf{S5}$.

## Motivation

In a Kripke model with domains, a quantifier at a world sees only the objects of that world.
The formula $\forall x \square \varphi$ speaks about the objects of the present world, while $\square \forall x \varphi$ speaks about the objects of each accessible world.
The two agree when every accessible world has no new objects.
So the exchange of $\forall x$ and $\square$ is a statement about the growth of domains.
Philosophers ask whether merely possible objects exist, and the Barcan formula is the formal form of this question: it says that whatever could exist already exists.

## Notation

1. BF has the equivalent dual form $\lozenge \exists x \varphi \to \exists x \lozenge \varphi$. Put $\neg \varphi$ for $\varphi$ in BF and take the contrapositive.
2. CBF has the dual form $\exists x \lozenge \varphi \to \lozenge \exists x \varphi$.
3. Some books call CBF the "Converse Barcan formula" and write BF and CBF as $\mathrm{BF}$ and $\mathrm{BF}^{-1}$.
4. A frame with domains has decreasing domains (also called anti-monotonic domains) when $w R v$ implies $D(v) \subseteq D(w)$, and increasing domains (also called expanding or monotonic domains) when $w R v$ implies $D(w) \subseteq D(v)$.

## Remarks

### Examples

1. [[The Barcan formula holds on a model with decreasing domains|F87MSJBXMQ]]: a two-world model where the domain shrinks along $R$, with the full truth check of an instance of BF.
2. [[The Barcan formula is derivable in quantified S5|PDGCDVGCA3]]: a derivation that uses only the axiom B, $p \to \square \lozenge p$, of the [[Brouwerian modal logic|2QPT4KCM0Q]].
3. [[The converse Barcan formula and increasing domains|ZYYTXBXNA2]]: a derivation of CBF in $\mathsf{QK}$, and the check that CBF fails on a model where a domain shrinks.
4. Constant domains: every frame with $D(w) = U$ for all $w$ has both decreasing and increasing domains, so BF and CBF are both valid on it.
5. Symmetric frames: when $R$ is [[symmetric|061J5VGSPT]], $w R v$ gives $v R w$, so increasing domains are also decreasing. On such a frame BF is valid if and only if CBF is valid.

### Non-examples

1. [[The Barcan formula fails on an S4 model with growing domains|RBTX5HWXBB]]: a reflexive and transitive frame where a new object appears at an accessible world. The frame is not a frame with decreasing domains, and the instance $\forall x \square P x \to \square \forall x P x$ fails.
2. The formula $\forall x \, \lozenge \varphi \to \lozenge \forall x \, \varphi$ is not a form of BF. It fails even with constant domains: take two worlds seen from $w$, each object $P$ at one of them only, and no world where all objects are $P$.
3. The formula $\exists x \square \varphi \to \square \exists x \varphi$ is not BF either. It is valid on frames with increasing domains, the condition of CBF, not the condition of BF.

### Basic properties

1. Frame condition for BF. Assume decreasing domains and $\mathfrak{M}, w \models_\sigma \forall x \square \varphi$. For $w R v$ and $d \in D(v)$ we get $d \in D(w)$, so $\mathfrak{M}, w \models_{\sigma[x \mapsto d]} \square \varphi$ and $\mathfrak{M}, v \models_{\sigma[x \mapsto d]} \varphi$. So $\mathfrak{M}, v \models_\sigma \forall x \varphi$, and BF holds at $w$. Conversely, if $w R v$ and $d \in D(v) \setminus D(w)$, put $I(P, u) = D(w)$ for every $u$; then $\forall x \square P x$ is true at $w$ and $\square \forall x P x$ is false at $w$.
2. Frame condition for CBF. Assume increasing domains and $\mathfrak{M}, w \models_\sigma \square \forall x \varphi$. For $d \in D(w)$ and $w R v$ we get $d \in D(v)$, so $\mathfrak{M}, v \models_{\sigma[x \mapsto d]} \varphi$. Conversely, if $w R v$ and $d \in D(w) \setminus D(v)$, put $I(P, u) = D(u)$ for every $u$; then $\square \forall x P x$ is true at $w$ and $\square P x$ fails at $w$ under $x \mapsto d$.
3. CBF is derivable in $\mathsf{QK}$ from instantiation, [[necessitation|G989VP2NGP]], the axiom K and generalization. So every quantified normal modal logic with the classical quantifier rules proves CBF.
4. BF is derivable in $\mathsf{QKB}$, and so in $\mathsf{QS5}$. The axiom 5, $\lozenge p \to \square \lozenge p$, together with T gives B, so the same derivation works with 5 and T.
5. BF is not derivable in $\mathsf{QS4}$. The model of the first non-example is an $\mathsf{S4}$ frame with increasing domains, and $\mathsf{QS4}$ is sound for such frames when formulas at $w$ are evaluated under assignments into $D(w)$. The sentence BF fails there.
6. $\mathsf{QK}$ plus BF is complete for the frames with constant domains.

### History

Ruth Barcan (later Ruth Barcan Marcus) stated the formula in 1946 as an axiom of the first axiomatic system of quantified modal logic, in the dual form $\lozenge \exists x \varphi \to \exists x \lozenge \varphi$ with strict implication.
Arthur Prior showed that the formula is derivable in quantified $\mathsf{S5}$.
Saul Kripke gave in 1963 a semantics with varying domains in which both BF and CBF fail, and the domain conditions of this page come from that semantics.

### Common errors

1. Swapping the frame conditions. BF goes with decreasing domains, so no new objects appear along $R$. CBF goes with increasing domains, so no object disappears along $R$.
2. Taking BF to follow from the classical quantifier rules. Only CBF follows from them; BF needs an extra axiom such as B, or constant domains.
3. Reading the condition for a frame as a condition for a model. In one model, an instance of BF can be true at every world while the domains grow. An example is the instance with $\varphi = P x$ when $P$ is empty at every world.

## Explanations

### L1 human

Think of possible worlds as possible futures, each with its own list of people who exist there.
The Barcan formula says: if everyone who exists now will be happy in every future, then in every future everyone will be happy.
This can fail when new people are born in a future, since we said nothing about them.
So the Barcan formula holds exactly when no new objects appear as we move to accessible worlds.
For example, with $2$ people now and $3$ people in some future, the formula can fail.

### L2 human

We check BF and CBF on a frame with constant domains.

1. Let $W = \{w, v\}$, $R = \{(w, v)\}$, and $D(w) = D(v) = \{1, 2\}$.
2. Let $I(P, w) = \emptyset$ and $I(P, v) = \{1, 2\}$.
3. At $w$: $\square P x$ holds under $x \mapsto 1$ and under $x \mapsto 2$, since the only successor $v$ has $1, 2 \in I(P, v)$. So $w \models \forall x \square P x$.
4. At $v$: $\forall x P x$ holds, since $D(v) = \{1, 2\} \subseteq I(P, v)$. So $w \models \square \forall x P x$, and BF holds at $w$.
5. Conversely, $w \models \square \forall x P x$ by step 4, and step 3 gives $w \models \forall x \square P x$, so CBF holds at $w$.
6. At $v$ both formulas hold, because $v$ has no successor and every $\square$-formula is true at $v$.

The typical use of BF is as an axiom when we want one domain for all worlds.
A trap: BF holds in this model because the domains are constant, not because $P$ is special; a new object at $v$ outside $I(P, v)$ would break it.

### L3 human

BF and CBF are the simplest examples of correspondence for frames with domains: each formula is valid on a frame exactly when a first-order condition on $R$ and $D$ holds, much as in [[modal correspondence theory|3RYBWYPJVD]] for propositional frames.
In the functor view of quantified modal logic, increasing domains are inclusions along $R$, and CBF expresses that each object has an image at every accessible world.
In $\mathsf{S5} \times \mathsf{S5}$ and in cylindric algebras, the two operators $\exists x$ and $\lozenge$ commute in both directions, which is the algebraic form of BF and CBF together; see [[products of modal logics|JA2EBWVW8A]].
The philosophical debate between [[modal possibilism|RXK66SDTAR]] and [[modal actualism|9ZK5VAWDKN]] is in large part a debate about whether to accept BF.
