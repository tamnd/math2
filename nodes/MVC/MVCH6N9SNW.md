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

A model of a set of axioms is a structure in which every one of the axioms is true.
Take the two sentences "no element is below itself", $\forall x \, \neg (x < x)$, and "every element has something below it", $\forall x \, \exists y \, (y < x)$.
The structure $(\mathbb{Z}, <)$ makes both true, so it is a model of the pair.
The structure $(\mathbb{N}, <)$ makes the first true and the second false at $0$, so it is not a model.

In exact terms, let $L$ be a signature and let $T$ be a set of $L$-[[sentences|DKFGQTRYZE]], for example the axioms of a [[theory|92SWXST1ZM]].
An $L$-[[structure|983GZBQYT4]] $\mathcal{M}$ is a model of $T$, written $\mathcal{M} \models T$, when every sentence of $T$ is [[true|K7XDVK5854]] in $\mathcal{M}$.
The class of all models of $T$ is written $\operatorname{Mod}(T)$, and $T$ is satisfiable when it has at least one model.
The [[formal definition|CWQV9PTCB3]] states this in one line.

## Motivation

Much of mathematics starts from axioms and then studies all the objects that satisfy them.
Group theory studies all groups, and order theory all orders, rather than one fixed example.
First-order logic makes this exact: the axioms are sentences, and the objects are the structures in which the sentences are true.
The models of the group axioms are exactly the groups, and the models of the axioms of strict linear orders are exactly the strict linear orders.

Models also show what axioms do not prove.
To see that a sentence $\sigma$ does not follow from $T$, it is enough to find one model of $T$ in which $\sigma$ is false.
The independence of the parallel postulate from the other axioms of plane geometry was shown in this way, by models of non-Euclidean geometry.
The [[completeness theorem|WQ1ZE255SF]] of a later sub-area turns this into an exact match between proofs and models.

## Notation

$\mathcal{M} \models T$ means that $\mathcal{M}$ is a model of $T$, and for one sentence, $\mathcal{M} \models \sigma$ means $\mathcal{M} \models \{\sigma\}$.
$\operatorname{Mod}(T)$, or $\operatorname{Mod}_L(T)$, is the class of models of $T$.
It is a proper class when $T$ has a model, because every isomorphic copy of a model is a model.
Some books say "model" for any structure, with no theory in view, but we say "model of $T$" only.
In Mathlib, `M ⊨ T` is `FirstOrder.Language.Theory.Model`.

## Remarks

### Checking a model, axiom by axiom

To show $\mathcal{M} \models T$, we check each sentence of $T$ in $\mathcal{M}$ with the clauses of [[satisfaction|2RBQPV02AS]].
For $(\mathbb{Z}, <)$ and the two sentences of the Summary, irreflexivity holds because $a < a$ is false for every integer $a$.
The second sentence holds because each value $a$ of $x$ has the witness
$$y \mapsto a - 1, \qquad a - 1 < a.$$
Check: for $a = 0$ the witness is $-1$, and $-1 < 0$.

The [[path graph on three vertices|SG43F9BZFR]] is a model of the theory of simple graphs, $\{ \forall x \, \neg E(x, x), \ \forall x \, \forall y \, (E(x, y) \to E(y, x)) \}$, and its example checks all nine pairs.
$(\mathbb{Q}, <)$ is a model of the theory of [[dense linear orders without endpoints|2W4S2H4VYA]].
A [[nonstandard model of arithmetic|1QWN5CV4CG]] is a model of Peano arithmetic with an element larger than every numeral.

### Structures that are not models

One false axiom is enough to spoil a model.
[[$(\mathbb{N}, \leq)$ is not a model of the theory of strict linear orders|5DA671E28J]], because irreflexivity fails: $0 \leq 0$.
$(\{1, 2, 3\}, <)$ is not a model of the theory of linear orders without endpoints, because nothing is below $1$.
$(\mathbb{N}, +, 0, \operatorname{id})$, with the inverse symbol read as the identity map, is not a model of the group axioms, since $x \cdot x^{-1} = e$ fails at $x = 1$, where $1 + 1 \neq 0$.
No structure is a model of $\{\sigma, \neg \sigma\}$, since a sentence and its negation are never both true, so this set is not satisfiable.

### The rules for models

Being a model is a statement about the theory of the structure: $\mathcal{M} \models T$ exactly when $T \subseteq \operatorname{Th}(\mathcal{M})$.
More axioms give fewer models, so $T \subseteq T'$ implies $\operatorname{Mod}(T') \subseteq \operatorname{Mod}(T)$.
Every structure is a model of the empty set of sentences, and of every [[valid|5SDS9T8E7J]] sentence.
A copy of a model is a model, by [[isomorphism invariance of truth|NDTJ2E895C]].

A sentence $\sigma$ is a [[logical consequence|1HK0VYWTV7]] of $T$ exactly when every model of $T$ is a model of $\sigma$.
A theory with a model is consistent, by the [[soundness theorem|4A84VHDTHV]], and every consistent theory has a model, by the completeness theorem.

### Which classes are classes of models

A class of the form $\operatorname{Mod}(T)$ is an [[elementary class|MEC3ZMC4F1]], also called an axiomatizable class.
The groups, the fields and the strict linear orders form elementary classes.
Not every natural class is elementary.
The class of finite groups is not, as [[finiteness of a group is not first-order|3J825EJ81F]] shows with the compactness theorem.

### Watch out

A model is not a theory.
The theory is a set of sentences, and a model is a structure, made of a set and interpretations of the symbols.

A theory usually has many models that are not isomorphic.
The one axiom $\forall x \, \neg E(x, x)$ has every loopless directed graph as a model, of every size.

Check the signature first.
A structure for $\{<\}$ is not a model of the group axioms, and not a non-model either, because the group axioms are not sentences of its signature.

### History

Models of geometry came before formal logic.
Beltrami gave a model of the hyperbolic plane inside Euclidean geometry in 1868, and Hilbert used models in 1899 to prove the independence of axioms of geometry.
Tarski defined truth in a structure in 1933, and his papers "Contributions to the theory of models" of 1954 and 1955 gave [[model theory|HFTBG5PMXC]] its name.

### Try it

Is $(\mathbb{Q}, <)$ a model of $\forall x \, \forall y \, (x < y \to \exists z \, (x < z \wedge z < y))$?
Yes: for $a < b$ the witness $z \mapsto (a + b)/2$ lies strictly between them.

Is $(\mathbb{Z}, <)$ a model of the same sentence?
No: at $x \mapsto 0$ and $y \mapsto 1$ no integer lies strictly between, so the sentence does not follow from the two axioms of the Summary.

## Explanations

### L1 human

A theory is a list of rules, and a model is a concrete world in which all the rules hold.
The rules "$<$ is a strict linear order with no least and no greatest element" have the integers with their usual order as a model.
The rational numbers with their usual order are another model of the same rules.
The set $\{1, 2, 3\}$ with its usual order is not a model, because $1$ is a least element.

### L2 human

We use a model to show that commutativity does not follow from the group axioms.
The symmetric group $S_3$ is a group, so it is a model of the group axioms.
Take the transpositions $a = (1 \, 2)$ and $b = (2 \, 3)$, and compose from right to left:
$$ab = (1 \, 2 \, 3), \qquad ba = (1 \, 3 \, 2).$$
So $ab \neq ba$, and the assignment $x \mapsto a$, $y \mapsto b$ does not satisfy $x \cdot y = y \cdot x$.
Thus $S_3$ is a model of the group axioms in which $\forall x \, \forall y \, (x \cdot y = y \cdot x)$ is false, and the group axioms do not imply it.
This is the typical use of a model: one countermodel shows that a sentence is not a consequence.

### L3 human

The maps $T \mapsto \operatorname{Mod}(T)$ and $\mathcal{K} \mapsto \operatorname{Th}(\mathcal{K})$ form a Galois connection between sets of sentences and classes of structures.
Its closed sets on the side of syntax are the theories closed under consequence, and on the side of structures the elementary classes.
The completeness theorem says that the syntactic closure, deducibility, agrees with this semantic closure.
Model theory, a later area, studies $\operatorname{Mod}(T)$ for important theories $T$: the sizes of the models, their isomorphism types and their definable sets.
