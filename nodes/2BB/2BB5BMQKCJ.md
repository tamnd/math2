---
tag: 2BB5BMQKCJ
kind: definition
name: Interpretability between theories
msc: ["03F25", "03B10"]
topics: [8XY7JYZKFW]
audience: grad
defines: 8H03GRMDYG
uses: [92SWXST1ZM, WDVVEYD6AT, HYJ10AF6RT, CY1TXHF6KQ, DKFGQTRYZE]
sources:
  - url: https://en.wikipedia.org/wiki/Interpretation_(model_theory)
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Interpretability
    locator: Informal definition
  - book: isbn:9780122384523
---

## Definition

An interpretation of one theory in another is a dictionary of formulas that turns every axiom of the first theory into a theorem of the second.

Let $S$ and $T$ be [[first-order theories|92SWXST1ZM]] in countable languages $L(S)$ and $L(T)$.
We assume that $L(T)$ has relation symbols and function symbols only, with constant symbols counted as $0$-ary function symbols.
A *relative interpretation* $I$ of $T$ in $S$ consists of the following [[formulas|HYJ10AF6RT]] of $L(S)$.

1. A *domain formula* $\delta(x)$ with one free variable.
2. For each $n$-ary relation symbol $R$ of $L(T)$, a formula $\varphi_R(x_1, \ldots, x_n)$.
3. For each $n$-ary function symbol $f$ of $L(T)$, a formula $\varphi_f(x_1, \ldots, x_n, y)$ for the graph of $f$.

The equality symbol of $L(T)$ is translated as the equality symbol of $L(S)$.

The *translation* $A \mapsto A^I$ sends formulas of $L(T)$ to formulas of $L(S)$.
First we unnest each atomic formula, so that it has the form $x = y$, $R(\bar x)$ or $f(\bar x) = y$ with variables only.
Then $(x = y)^I$ is $x = y$, $R(\bar x)^I$ is $\varphi_R(\bar x)$, and $(f(\bar x) = y)^I$ is $\varphi_f(\bar x, y)$.
The translation commutes with $\lnot$, $\land$, $\lor$ and $\to$, and it relativizes the quantifiers to $\delta$:
$$(\forall x \, A)^I = \forall x \, (\delta(x) \to A^I), \qquad (\exists x \, A)^I = \exists x \, (\delta(x) \land A^I).$$

The relative interpretation $I$ is an *interpretation of $T$ in $S$* when $S$ proves the following sentences.

1. $\exists x \, \delta(x)$.
2. For each $n$-ary function symbol $f$, the sentence $\forall \bar x \, \bigl(\delta(x_1) \land \cdots \land \delta(x_n) \to \exists! y \, (\delta(y) \land \varphi_f(\bar x, y))\bigr)$.
3. For each axiom $\sigma$ of $T$, the translation $\sigma^I$.

The theory $T$ is *interpretable in* $S$, and $S$ *interprets* $T$, when an interpretation of $T$ in $S$ exists.

## Notation

We write $S \rhd T$ or $T \lhd S$ for "$S$ interprets $T$", and some authors write $T \le S$ or $T \trianglelefteq S$.
We write $A^I$ or $A^\tau$ for the translation of $A$, where $\tau$ is the translation map.
In a [[structure|983GZBQYT4]] $\mathcal{M}$ of $L(S)$ the formulas of $I$ define a set with relations and functions on it, and we write $\mathcal{M}^I$ for this structure of $L(T)$.

## Remarks

### Why each condition is there

Condition 1 says that the domain is not empty.
First-order logic proves $\exists x \, (x = x)$, so a translated theorem of $T$ can assert that something exists, and the domain must supply it.

Condition 2 says that $\varphi_f$ is the graph of a total function on the domain.
Without it, the translation of the theorem $\forall x \, \exists y \, (f(x) = y)$ could fail.
For a constant symbol $c$, the formula $\varphi_c(y)$ has one free variable, and condition 2 says that it defines exactly one element of the domain.

Condition 3 is the heart of the definition, and it asks for proofs in $S$, not for truth in one model.
Unnesting is needed because a nested term such as $f(g(x))$ has no direct translation.
We replace $f(g(x)) = y$ by $\exists u \, (g(x) = u \land f(u) = y)$ and translate the pieces.

### A small example and a failure

The theory of a strict linear order without a greatest element is interpretable in [[Peano arithmetic|0QFT7Z76N5]].
Take $\delta(x) := (x = x)$ and translate $x < y$ as $\varphi_<(x, y) := \exists z \, (x + S(z) = y)$.
The axiom "for each $x$ there is $y$ with $x < y$" translates to the following sentence:
$$\forall x \, \bigl(x = x \to \exists y \, (y = y \land \exists z \, (x + S(z) = y))\bigr).$$
PA proves it with $y := S(x)$ and $z := 0$.
The axioms of irreflexivity, transitivity and totality translate to properties of $<$ that PA proves by induction.

Now try to interpret the theory of an infinite set in the theory $S$ of a set with exactly two elements.
Condition 3 fails for every choice of $\delta$.
The theory $S$ has a model with two elements, and the domain in it has at most two elements.
So the axiom "there are at least three elements" translates to a sentence false in that model, and $S$ does not prove it.

### Theorems go to theorems

The main property of an interpretation is that it carries theorems to theorems.

**Lemma.** If $I$ interprets $T$ in $S$ and $\sigma$ is a sentence of $L(T)$ with $T \vdash \sigma$, then $S \vdash \sigma^I$.

We give the semantic proof in three steps.

1. Let $\mathcal{M}$ be a [[model|MVCH6N9SNW]] of $S$.
   The set defined by $\delta$ in $\mathcal{M}$ is not empty, by condition 1, and the formulas of $I$ define on it a structure $\mathcal{M}^I$ of $L(T)$, by condition 2.
2. By induction on a formula $A$ of $L(T)$, for each tuple $\bar a$ of the domain, $\mathcal{M}^I \models A[\bar a]$ if and only if $\mathcal{M} \models A^I[\bar a]$.
   So $\mathcal{M}^I \models T$ by condition 3, hence $\mathcal{M}^I \models \sigma$ and $\mathcal{M} \models \sigma^I$.
3. Since $\mathcal{M}$ is an arbitrary model of $S$, the [[completeness theorem|WQ1ZE255SF]] gives $S \vdash \sigma^I$.

A syntactic proof also exists: by induction on a derivation in $T$, each formula $A$ with free variables $\bar x$ gives a derivation in $S$ of $\delta(\bar x) \to A^I$.
The syntactic proof is finitary, and that is why interpretations give relative consistency proofs that a finitist can accept.

### Variants

One variant allows equality of $L(T)$ to be translated by a formula $\varepsilon(x, y)$ of $L(S)$.
Then $S$ must prove that $\varepsilon$ is an equivalence relation on the domain and a congruence for each $\varphi_R$ and each $\varphi_f$, and $\mathcal{M}^I$ is the quotient of the domain by $\varepsilon$.
Another variant takes a domain of $k$-tuples, with a formula $\delta(x_1, \ldots, x_k)$.
These variants give more interpretations, and the lemma holds for them in the same form.
The concept of [[interpretability between theories|8H03GRMDYG]] comes with the local, global and weak forms of the relation and the link to consistency.

## Explanations

### L1 human

To interpret one theory in another is to show how to speak the language of the first theory with the words of the second one.
Each word of the first theory gets a definition in the second theory.
The objects of the first theory are some of the objects of the second one, picked out by a fixed property.
The definitions must turn every axiom of the first theory into a theorem of the second one.
For example, the whole numbers can be defined inside set theory: $0$ is the empty set, $1$ is $\{0\}$, $2$ is $\{0, 1\}$, and so on.

### L2 human

We see why the quantifiers must be relativized.
Interpret the theory of a nonempty set with a unary predicate $P$ that holds of everything, $\forall x \, P(x)$, in the theory $S$ of the integers with $<$.
Take $\delta(x) := (0 < x)$ and $\varphi_P(x) := (0 < x)$.
The relativized translation $\forall x \, (0 < x \to 0 < x)$ is provable.
Without relativization we would get $\forall x \, (0 < x)$, which is false for $x = 0$.

The typical use of an interpretation is a relative consistency proof: a contradiction in $T$ would translate to a contradiction in $S$.
Watch out: forgetting the relativization makes the translated axioms speak about all objects of $S$, not about the domain.
