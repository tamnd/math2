---
tag: 1NR3HAWG9D
kind: statement
role: theorem
name: Compactness theorem
aliases: [compactness-theorem, compactness-theorem-first-order-logic]
msc: ["03C07", "03B10"]
topics: [FBWW4J1XWG]
audience: ug2
uses: [DKFGQTRYZE, MVCH6N9SNW, QN7M1JCGT9, WQ1ZE255SF, G0DTR159RN, 1HK0VYWTV7, 0G0ASKNA6Z]
about: [QN7M1JCGT9]
history:
  first_stated: "Kurt Gödel, 1930, for countable languages; Anatoly Malcev, 1936, for uncountable languages"
  notes: "Gödel derived it from his completeness theorem."
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language.Theory.isSatisfiable_iff_isFinitelySatisfiable
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Compactness_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Compactness_theorem
    locator: History
  - url: https://en.wikipedia.org/wiki/Compactness_theorem
    locator: Proofs
  - book: isbn:9780122384523
    locator: Section 2.5
  - book: isbn:9780122384523
    locator: Section 2.6
  - url: https://builds.openlogicproject.org/
    locator: The Completeness Theorem
same_as:
  wikidata: Q1149458
  wikipedia: Compactness theorem
---

## Statement

If every finite part of a set of first-order sentences has a model, then the whole set has one model that satisfies all of it at once.

Let $L$ be a first-order language, given by a signature of any size, and let $\Gamma$ be a set of [[sentences|DKFGQTRYZE]] of $L$.
The set $\Gamma$ is [[satisfiable|QN7M1JCGT9]] when it has a [[model|MVCH6N9SNW]].
It is finitely satisfiable when each finite subset of $\Gamma$ is satisfiable.
Write $|L|$ for the [[cardinality|0G0ASKNA6Z]] of the set of symbols of $L$, and $\models$ for [[logical consequence|1HK0VYWTV7]].

**Theorem (compactness).**

1. The set $\Gamma$ is satisfiable if and only if $\Gamma$ is finitely satisfiable.
2. Equivalently, for every $L$-sentence $\varphi$, we have $\Gamma \models \varphi$ if and only if $\Gamma_0 \models \varphi$ for some finite $\Gamma_0 \subseteq \Gamma$.
3. If $\Gamma$ is finitely satisfiable, then $\Gamma$ has a model with at most $|L| + \aleph_0$ elements.

The theorem is proved in ZFC.
For a countable $L$ it needs no form of the axiom of choice.
There are two standard proofs: [[a proof from the completeness theorem|DFP1N4WTF9]] and [[a proof by ultraproducts|22TWAHBVWT]].

## Remarks

### A first example

Let $\lambda_n$ be the sentence that says "there are at least $n$ elements".
For $n = 3$ it reads as follows.
$$\lambda_3 = \exists x_1 \exists x_2 \exists x_3 \, (\neg\, x_1 = x_2 \land \neg\, x_1 = x_3 \land \neg\, x_2 = x_3)$$
Take the set $\Gamma = \{ \lambda_n : n \ge 2 \}$.
A finite part of $\Gamma$ mentions only $\lambda_n$ with $n \le N$ for some $N$, and a set with $N$ elements is a model of it.
So $\Gamma$ is finitely satisfiable, and compactness gives a model of all of $\Gamma$.
That model has at least $n$ elements for every $n$, so it is infinite.
Check: here we did not need compactness, since $\mathbb{N}$ is a model, but the same pattern works when no model is in sight.
[[Applications of first-order compactness|PES0S9XQZ5]] runs the pattern on arithmetic, groups, graphs and orders.

### Why each hypothesis is needed

The sentences must be first-order.
In [[second-order logic|G6X7SZSNC5]] one sentence $\mathrm{Fin}$ says that the domain is finite.
Every finite part of $\{ \mathrm{Fin} \} \cup \{ \lambda_n : n \ge 2 \}$ has a model, and the whole set has none.

The sentences must be finite strings.
In the [[infinitary logic|PQG7VAZ1R2]] $L_{\omega_1 \omega}$, the sentence $\forall x \, \bigvee_{n} x = S^n(0)$ says that every element is a numeral.
Add the sentences $\neg\, c = S^n(0)$ for all $n$.
Each finite part holds in $(\mathbb{N}, 0, S)$ with $c$ read as a large number, but the whole set has no model, since the value of $c$ must be a numeral.

The models must range over all structures, not only finite ones.
Over finite structures the set $\{ \lambda_n : n \ge 2 \}$ is finitely satisfiable and has no model.

### The role of choice

For a countable $L$, the proof from the completeness theorem lists the sentences as $\varphi_0, \varphi_1, \dots$ and needs no choice.
For an arbitrary $L$, the proof uses Zorn's lemma or the ultrafilter lemma.
Over ZF, compactness for all signatures is equivalent to the [[Boolean prime ideal theorem|STPBXBKSZP]], which is weaker than the axiom of choice.

### What it gives you

The theorem is the source of [[nonstandard models of arithmetic|1QWN5CV4CG]], of the upward [[Löwenheim-Skolem theorem|484M0TZ1S7]], and of the proofs that finiteness, torsion, connectedness and well-order are not first-order.
It also moves facts between [[characteristics|0P7CH1CND5]] of fields.
Suppose a sentence $\sigma$ of the language of rings holds in every field of characteristic $0$.
The fields of characteristic $0$ are the models of the field axioms $F$ together with the sentences $\neg\, p \cdot 1 = 0$ for all primes $p$.
By part 2, $\sigma$ follows from $F$ and finitely many of these, say for $p \le P$.
So $\sigma$ holds in every field of characteristic $p$ for every prime $p > P$.

The converse of part 1 holds in every logic: a model of $\Gamma$ is a model of each subset.
The theorem itself fails in most logics stronger than first-order logic.
By [[Lindström's theorem|FYZ3CJGZYV]], first-order logic is a maximal logic with compactness and the downward Löwenheim-Skolem property.
[[Craig's interpolation theorem|E2CBFNAVZY]] and [[Robinson's joint consistency theorem|R6AN38DNBD]] have proofs that use compactness.

### Where the name comes from

The complete theories of $L$ form a [[Stone space|ZV38HA5PAQ]], with basic open sets $\{ T : \sigma \in T \}$.
Part 1 says exactly that this space is compact: a family of basic closed sets with the finite intersection property has a common point.
The [[compactness theorem for propositional logic|4X9126SEMM]] is the special case with no quantifiers and only $0$-ary relation symbols.
Many-sorted first-order logic has the same theorem with the same proofs.

### Watch out

A common slip is to check only some finite parts.
Take $\Gamma = \{ \sigma \} \cup \{ \lambda_n : n \ge 2 \}$, where $\sigma$ is meant to say "the domain is finite".
Checking the parts $\{ \lambda_2, \dots, \lambda_N \}$ alone proves nothing, because $\sigma$ must be in the finite part too.
The correct move is to fix an arbitrary finite $\Gamma_0 \subseteq \Gamma$ and give a model of all of $\Gamma_0$.

A second slip is to read part 3 as "the model is countable".
The bound is $|L| + \aleph_0$, so a language with $\aleph_1$ constants can force a model of size $\aleph_1$.

### Try it

First, let $\Gamma$ contain the group axioms and, for a new constant $c$, the sentences $\neg\, c^n = e$ for $n \ge 1$.
Is $\Gamma$ satisfiable?
Yes: the group $(\mathbb{Z}, +)$ with $c$ read as $1$ satisfies every sentence, and compactness is not even needed.

Second, suppose $\Gamma \models \varphi$ and $\Gamma$ is infinite.
Must some finite part of $\Gamma$ already imply $\varphi$?
Yes, by part 2, although which finite part works depends on $\varphi$.

## History

Kurt Gödel proved the compactness theorem for countable languages in 1930, as a corollary of his completeness theorem.
Anatoly Malcev proved the case of uncountable languages in 1936.
Later, model theorists gave purely semantic proofs, for example by ultraproducts and Łoś's theorem.

## Explanations

### L1 human

Imagine an endless list of conditions.
Suppose that any finite handful of them can be met together by some example.
The theorem says that one single example then meets the whole list.
Take the list "at least 1 thing", "at least 2 things", "at least 3 things", and so on.
Any finite handful of these is met by a big enough finite box of things.
The whole list is met only by an infinite box, and the theorem promises that such a box exists.

### L2 human

We show that no first-order sentence $\sigma$ about graphs says "the graph is finite".
Suppose $\sigma$ holds exactly in the finite graphs, and put $\Gamma = \{ \sigma \} \cup \{ \lambda_n : n \ge 2 \}$.

1. Take a finite $\Gamma_0 \subseteq \Gamma$, and let $N$ be the largest $n$ with $\lambda_n \in \Gamma_0$, or $N = 2$ if there is none.
2. The graph with $N$ vertices and no edges is finite, so it satisfies $\sigma$, and it satisfies $\lambda_n$ for $n \le N$.
   So $\Gamma_0$ has a model.
3. By compactness, $\Gamma$ has a model $G$.
   Then $G$ satisfies $\sigma$, so it is finite, and it satisfies every $\lambda_n$, so it is infinite.
4. This contradiction shows that no such $\sigma$ exists.

The typical use is the pattern of these four steps: add infinitely many conditions, satisfy each finite part, and read off a property of the model.
Watch out: the model that compactness gives is a model of $\Gamma$, and nothing more is known about it.

### L3 human

In topological form, the theorem says that the Stone space of the Lindenbaum-Tarski algebra of sentences, whose points are the complete theories, is compact.
The ultraproduct proof leads to a characterization: a class of structures is the class of models of a set of sentences if and only if it is closed under ultraproducts and under [[elementary equivalence|P3B1V182N4]].
Compactness is the main tool of [[model theory|HFTBG5PMXC]], and with the Löwenheim-Skolem theorem it characterizes first-order logic.
In Mathlib the theorem is the declaration `FirstOrder.Language.Theory.isSatisfiable_iff_isFinitelySatisfiable`.
