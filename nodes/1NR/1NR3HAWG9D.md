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
  first_stated: "Kurt Gödel, 1930, for countable languages; Anatoly Maltsev, 1936, for uncountable languages"
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

Let $L$ be a first-order language, given by a signature, and let $\Gamma$ be a set of first-order [[sentences|DKFGQTRYZE]] of $L$.
A set of sentences is [[satisfiable|QN7M1JCGT9]] when it has a [[model|MVCH6N9SNW]], and finitely satisfiable when each of its finite subsets is satisfiable.

**Theorem (compactness).**

1. $\Gamma$ is satisfiable if and only if $\Gamma$ is finitely satisfiable.
2. Equivalently, for every sentence $\varphi$ of $L$: $\Gamma \models \varphi$ if and only if $\Gamma_0 \models \varphi$ for some finite $\Gamma_0 \subseteq \Gamma$.
3. If $\Gamma$ is finitely satisfiable, then $\Gamma$ has a model with at most $\max(|L|, \aleph_0)$ elements.

Here $\models$ is [[logical consequence|1HK0VYWTV7]] and $|L|$ is the [[cardinality|0G0ASKNA6Z]] of the set of symbols of $L$.
Two proofs are given: [[a proof from the completeness theorem|~e8fafa0d]] and [[a proof by ultraproducts|~e411426e]].

## Remarks

### Why each hypothesis is needed

- First-order logic: in [[second-order logic|G6X7SZSNC5]] one sentence $\mathrm{Fin}$ says that the universe is finite. Together with the sentences "there are at least $n$ elements", every finite part has a model, but the whole set has none.
- Arbitrary structures: over finite structures only, the theorem fails. The set of sentences "there are at least $n$ elements", for $n \ge 1$, is finitely satisfiable in finite structures, but it has no finite model.
- Finitary sentences: in the infinitary logic $L_{\omega_1 \omega}$, the sentence $\forall x \, \bigvee_{n} x = S^n(0)$ together with $\neg(c = S^n(0))$ for all $n$ is finitely satisfiable in $\N$, but not satisfiable.
- Choice: in ZF, the theorem for languages of every size is equivalent to the [[Boolean prime ideal theorem|STPBXBKSZP]]. For countable languages it is provable in ZF.

### Consequences

- [[Applications of first-order compactness|~23a8e9a5]] collects the standard uses: nonstandard models, the finiteness of a property, and transfer between characteristics.
- If a theory has finite models of every size, then it has an infinite model. So "the universe is finite" is not expressible by a set of first-order sentences.
- [[Nonstandard models of arithmetic|1QWN5CV4CG]]: the sentences true in $\N$, plus $c > \underline{n}$ for a new constant $c$ and each numeral $\underline{n}$, have a model with an element above all numerals.
- The upward [[Löwenheim-Skolem theorem|484M0TZ1S7]]: a theory with an infinite model has models of every infinite cardinality at least $|L|$.
- A sentence true in every field of characteristic $0$ is true in every field of characteristic $p$, for all but finitely many primes $p$.
- [[Craig's interpolation theorem|E2CBFNAVZY]] and [[Robinson's joint consistency theorem|~6d43779a]] have proofs by compactness.

### Converse

The direction "satisfiable implies finitely satisfiable" holds in every logic, since a model of $\Gamma$ is a model of each subset.
The theorem itself is not a property of every logic; by [[Lindström's theorem|FYZ3CJGZYV]], first-order logic is the largest regular logic with compactness and the downward Löwenheim-Skolem property.

### Generalizations

- Topological form: the space of complete theories of $L$, with the Stone topology, is compact. The theorem is equivalent to this compactness, which gives the name.
- The [[propositional compactness theorem|4X9126SEMM]] is the special case of quantifier-free sentences with $0$-ary relation symbols.
- Many-sorted logic has the same theorem, with the same proofs.
- Infinitary logic: let $\kappa$ be an uncountable cardinal. Suppose that in $L_{\kappa \kappa}$, every set of sentences whose subsets of size less than $\kappa$ are satisfiable is satisfiable. This property is the definition of a strongly compact cardinal $\kappa$.

## History

Kurt Gödel proved the compactness theorem for countable languages in 1930, as a corollary of his completeness theorem.
Anatoly Maltsev proved the case of uncountable languages in 1936.
Later proofs were purely semantic, for example by ultraproducts and Łoś's theorem.

## Explanations

### L1 human

Imagine an infinite list of conditions.
Suppose that every finite selection of them can be met at once by some example.
The theorem says that one example then meets the whole infinite list at once.
For example, "there are at least $1$ thing", "there are at least $2$ things", and so on, can all hold together, in an infinite world.

### L2 human

We show that no first-order sentence $\sigma$ in the language of graphs says "the graph is finite".

1. Suppose $\sigma$ holds exactly in the finite graphs.
2. Let $\lambda_n$ say "there are at least $n$ vertices", and let $\Gamma = \set{\sigma} \cup \set{\lambda_n : n \ge 1}$.
3. A finite part of $\Gamma$ mentions $\lambda_n$ for $n \le N$ only. A graph with $N$ vertices and no edges satisfies it.
4. By compactness, $\Gamma$ has a model. That graph satisfies $\sigma$, so it is finite, and it satisfies every $\lambda_n$, so it is infinite.
5. This contradiction shows that no such $\sigma$ exists.

The typical use is this pattern: add infinitely many conditions, check finite parts, and conclude that a model exists.
The trap is to check only some finite parts, for example the parts $\set{\lambda_1, \dots, \lambda_N}$ without $\sigma$.

### L3 human

The theorem says that the Stone space of the Lindenbaum-Tarski algebra of sentences, whose points are the complete theories, is compact.
The ultraproduct proof leads to a characterization: a class of structures is the class of models of a set of sentences iff it is closed under ultraproducts and elementary equivalence.
Compactness is the main tool of [[model theory|HFTBG5PMXC]], and with Löwenheim-Skolem it characterizes first-order logic.
In Mathlib the theorem is the declaration `FirstOrder.Language.Theory.isSatisfiable_iff_isFinitelySatisfiable`.
