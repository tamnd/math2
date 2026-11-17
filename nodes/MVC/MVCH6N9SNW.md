---
tag: MVCH6N9SNW
kind: concept
name: Model
msc: ["03C07"]
topics: [NJDME6F845]
audience: ug2
uses: [983GZBQYT4, 92SWXST1ZM, K7XDVK5854, DKFGQTRYZE]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_(mathematical_logic)
  - url: https://en.wikipedia.org/wiki/Model_theory
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.2
  - url: https://builds.openlogicproject.org/
    locator: Theories and Their Models
---

## Summary

Let $L$ be a signature and let $T$ be a set of $L$-[[sentences|DKFGQTRYZE]], for example the axioms of a [[theory|92SWXST1ZM]].
An $L$-[[structure|983GZBQYT4]] $\mathcal{M}$ is a model of $T$, written $\mathcal{M} \models T$, when every sentence of $T$ is [[true|K7XDVK5854]] in $\mathcal{M}$.
The class of all models of $T$ is written $\operatorname{Mod}(T)$, and $T$ is satisfiable when $\operatorname{Mod}(T)$ is not empty.
Models give meaning to axioms: the models of the group axioms are exactly the groups, and the models of the axioms of strict linear orders are exactly the strict linear orders.

## Motivation

Mathematics often starts from axioms and then studies all the objects that satisfy them.
Group theory studies all groups, and order theory studies all orders, rather than one fixed example.
First-order logic makes this precise: the axioms are sentences, and the objects are the structures in which the sentences are true.
A model is such an object.
With models we can show that an axiom does not follow from others, by a model of the others in which it fails.
This is how the independence of the parallel postulate from the other axioms of geometry was shown.

## Notation

$\mathcal{M} \models T$ means that $\mathcal{M}$ is a model of $T$; for one sentence, $\mathcal{M} \models \sigma$ means $\mathcal{M} \models \set{\sigma}$.
$\operatorname{Mod}(T)$ or $\operatorname{Mod}_L(T)$ is the class of models of $T$; it is a proper class when $T$ has a model, because every isomorphic copy of a model is a model.
Some books use "model" for any structure, with no theory in view; this page uses "model of $T$" only.
In Mathlib, `M ⊨ T` is `FirstOrder.Language.Theory.Model`.

## Remarks

### Examples

1. Every group $(G, \cdot, e, {}^{-1})$ is a model of the three group axioms in the signature $\set{\cdot, e, {}^{-1}}$. For example $(\Z, +, 0, -)$ is a model, because addition is associative, $0$ is neutral, and $-x$ is an inverse of $x$.
2. The [[path graph on three vertices|~819ba28f]] is a model of the theory of simple graphs, $\set{\forall x \, \neg E(x, x), \ \forall x \, \forall y \, (E(x, y) \to E(y, x))}$.
3. $(\Q, <)$ is a model of the theory of [[dense linear orders without endpoints|2W4S2H4VYA]].
4. A [[non-standard model of arithmetic|1QWN5CV4CG]] is a model of Peano arithmetic with an element larger than every numeral.
5. Every structure is a model of the empty set of sentences, and of every [[valid|5SDS9T8E7J]] sentence.

### Non-examples

1. [[$(\N, \le)$ is not a model of the theory of strict linear orders|~1637f140]]: the condition that fails is irreflexivity, because $0 \le 0$.
2. $(\set{1, 2, 3}, <)$ is not a model of the theory of linear orders without endpoints: the condition that fails is $\forall x \, \exists y \, (y < x)$, because nothing is below $1$.
3. $(\N, +, 0, \id)$, with ${}^{-1}$ read as the identity map, is not a model of the group axioms: the axiom $\forall x \, (x \cdot x^{-1} = e)$ fails at $x = 1$, because $1 + 1 \neq 0$.
4. No structure is a model of $\set{\sigma, \neg \sigma}$: a sentence and its negation are never both true, by bivalence. So this set is not satisfiable.

### Basic properties

1. $\mathcal{M} \models T$ holds if and only if $T \subseteq \operatorname{Th}(\mathcal{M})$, where $\operatorname{Th}(\mathcal{M})$ is the [[theory of $\mathcal{M}$|K7XDVK5854]].
2. If $T \subseteq T'$, then $\operatorname{Mod}(T') \subseteq \operatorname{Mod}(T)$. More axioms give fewer models.
3. If $\mathcal{M} \models T$ and $\mathcal{N}$ is isomorphic to $\mathcal{M}$, then $\mathcal{N} \models T$, by [[isomorphism invariance of truth|~5166a0b3]].
4. A sentence $\sigma$ is a [[logical consequence|1HK0VYWTV7]] of $T$ exactly when every model of $T$ is a model of $\sigma$.
5. A theory with a model is consistent, by the [[soundness theorem|4A84VHDTHV]]. Conversely, every consistent theory has a model, by the [[completeness theorem|WQ1ZE255SF]].
6. A class of the form $\operatorname{Mod}(T)$ is an [[elementary class|MEC3ZMC4F1]]. Not every natural class is elementary: the class of finite groups is not, as shown in [[finiteness of a group is not first-order|3J825EJ81F]].

### History

Models of geometry were used before formal logic: Beltrami in 1868 gave a model of the hyperbolic plane inside Euclidean geometry, and Hilbert in 1899 used models to prove independence of axioms.
Tarski defined truth in a structure in 1933, and his papers "Contributions to the theory of models" (1954 and 1955) named the subject of [[model theory|HFTBG5PMXC]].

### Common errors

- Confusing a model with a theory. The theory is a set of sentences; a model is a structure, made of a set and interpretations of the symbols.
- Thinking that a theory has one model. Most theories have many non-isomorphic models; $\set{\forall x \, \neg E(x, x)}$ has all loopless directed graphs as models.
- Checking a model axiom by axiom without the right signature. A structure for $\set{<}$ is not a model of the group axioms, because the group axioms are not sentences of its signature.

## Explanations

### L1 human

A theory is a list of rules, and a model is a concrete world in which all the rules hold.
The rules "$<$ is a strict linear order with no least and no greatest element" have the integers with their usual order as a model.
The rational numbers with their usual order are another model of the same rules.
The set $\set{1, 2, 3}$ with its usual order is not a model, because $1$ is a least element.

### L2 human

We check that $(\Z, <)$ is a model of $T = \set{\forall x \, \neg (x < x), \ \forall x \, \exists y \, (y < x)}$.

1. First axiom: for each integer $a$, $a < a$ is false, so $\neg (x < x)$ holds under $x \mapsto a$. By the clause for $\forall$, the axiom is true.
2. Second axiom: for each integer $a$, the witness $y \mapsto a - 1$ gives $a - 1 < a$. By the clauses for $\exists$ and $\forall$, the axiom is true.
3. Both sentences of $T$ are true, so $(\Z, <) \models T$.

The same check fails for $(\N, <)$ at the second axiom, with $a = 0$.
The typical use is to show that a sentence $\sigma$ does not follow from $T$: find a model of $T$ in which $\sigma$ is false.
For example, $(\Z, <)$ shows that density does not follow from $T$, because no integer lies strictly between $0$ and $1$.

### L3 human

The pair of maps $T \mapsto \operatorname{Mod}(T)$ and $\mathcal{K} \mapsto \operatorname{Th}(\mathcal{K})$ is a Galois connection between sets of sentences and classes of structures.
Its closed sets on the syntax side are the theories closed under consequence, and on the semantic side the elementary classes.
The completeness theorem says that the syntactic closure, deducibility, agrees with this semantic closure.
Model theory, the later area, studies $\operatorname{Mod}(T)$ for important $T$: its sizes, its isomorphism types, and its definable sets.
