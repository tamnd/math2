---
tag: G0DTR159RN
kind: statement
role: theorem
name: Model existence theorem
aliases: [model-existence-theorem, model-existence-lemma]
msc: ["03C07", "03B10"]
topics: [FBWW4J1XWG]
audience: ug2
about: [VM8TQ70CVJ, QN7M1JCGT9, 086QKPF0A6]
uses: [AVD7T7J063, SC0BSJ3GT6, RY8KRKR097, VM8TQ70CVJ, DKFGQTRYZE, MVCH6N9SNW, QN7M1JCGT9, 01TQB88H4C, 0G0ASKNA6Z]
history:
  first_stated: "Leon Henkin, 1949, for first-order languages of any cardinality"
  notes: "Henkin proved it with witness constants and term models."
sources:
  - wikipedia: en:12450@r1371782634
    locator: Gödel's completeness theorem, section Statement > Model existence theorem
    note: adopted
    mention: wikipedia://en/12450#2V6I
    sections: [Statement]
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem
    locator: Model existence theorem
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem
    locator: As a theorem of arithmetic
  - book: isbn:9780122384523
    locator: Section 2.5
  - url: https://builds.openlogicproject.org/
    locator: The Completeness Theorem
inventory: [WCMCVZR0SC]
---

## Statement

Let $L$ be a first-order language with equality, and let $\vdash$ be derivability in the Hilbert system $H$ of the [[soundness theorem|AVD7T7J063]].
A set of [[sentences|DKFGQTRYZE]] is [[consistent|VM8TQ70CVJ]] when it derives no pair $\psi$, $\neg \psi$.
Write $|L|$ for the [[cardinality|0G0ASKNA6Z]] of the set of symbols of $L$.

**Theorem (model existence).**

1. Every consistent set $\Gamma$ of sentences of $L$ has a [[model|MVCH6N9SNW]].
2. The model can be chosen with at most $\max(|L|, \aleph_0)$ elements. In particular, when $L$ is [[countable|01TQB88H4C]], $\Gamma$ has a model that is finite or countably infinite.
3. Part 1 is equivalent to strong completeness: for every set $\Gamma$ of sentences and every sentence $\varphi$, if $\Gamma \models \varphi$, then $\Gamma \vdash \varphi$.

The [[proof by the Henkin construction|FMZMD0GGYK]] gives all details for countable $L$, and its Variants section treats uncountable $L$.
For uncountable $L$, the proof uses the axiom of choice.

## Remarks

### Why each hypothesis is needed

- Consistency: by part 3 of the [[soundness theorem|AVD7T7J063]], a set with a model is consistent. So an inconsistent set has no model.
- The proof system must be complete enough for equality. Remove axiom group 6 from $H$. Then $\set{a = b, P(a), \neg P(b)}$ derives no contradiction, since $=$ may then be read as any reflexive relation. But it has no model.
- The bound $\max(|L|, \aleph_0)$ cannot be lowered to $|L|$. The empty language has $|L|$ finite, and the sentences "there are at least $n$ elements", for all $n \ge 1$, have only infinite models.
- Choice: for languages of every size, part 1 is equivalent in ZF to the [[Boolean prime ideal theorem|STPBXBKSZP]]. For countable $L$, no choice is needed, because the sentences can be listed.

### Consequences

- Strong completeness, part 3. If $\Gamma \models \varphi$, then $\Gamma \cup \set{\neg \varphi}$ has no model, so it is inconsistent by part 1. Fact (P5) of the [[proof of Lindenbaum's lemma|DCR0S91GYY]] then gives $\Gamma \vdash \varphi$. This is [[Gödel's completeness theorem|WQ1ZE255SF]].
- Conversely, assume strong completeness and let $\Gamma$ have no model. Then $\Gamma \models \neg \forall x \, (x = x)$ and $\Gamma \models \forall x \, (x = x)$ hold vacuously, so $\Gamma$ derives both and is inconsistent. This proves the equivalence in part 3.
- The [[compactness theorem|1NR3HAWG9D]]: a finitely satisfiable set is consistent, because a derivation uses finitely many sentences.
- A weak form of the downward [[Löwenheim-Skolem theorem|484M0TZ1S7]]: a consistent theory in a countable language has a countable model. For example, ZFC, if it is consistent, has a countable model; see [[Skolem's paradox|68QZWDXAQ4]].
- To prove that $\Gamma \nvdash \varphi$, it is enough to find a model of $\Gamma \cup \set{\neg \varphi}$, and conversely such a model exists whenever $\Gamma \nvdash \varphi$.

### Converse

The converse of part 1 holds: a set with a model is consistent, by the soundness theorem.
So for sets of sentences, consistent and [[satisfiable|QN7M1JCGT9]] are the same property.

### Generalizations

- Formulas with free variables: replace the free variables by new constants. A consistent set of formulas then has a structure and an assignment that satisfy it.
- Languages without equality: the term model needs no quotient, and the bound on the size is the same.
- Many-sorted logic and the theory of types with general models have the same theorem, with the same Henkin proof.
- Arithmetized form: for a consistent, computably axiomatized theory $T$, the Henkin construction can be carried out in Peano arithmetic. It gives a model of $T$ whose relations are defined by arithmetical formulas that are $\Delta_2$ in general, but not computable in general.
- The theorem fails for second-order logic with full semantics: no sound and effective proof system makes every consistent set satisfiable. See [[second-order logic|G6X7SZSNC5]].

## History

Kurt Gödel proved the completeness theorem in his 1929 thesis, for countable languages.
Leon Henkin published the model existence form and its proof by witness constants in 1949.
His proof works for languages of any cardinality and gives the bound on the size of the model.
Anatoly Maltsev had proved the compactness theorem for uncountable languages in 1936.

## Explanations

### L1 human

A list of axioms is consistent when no proof from it reaches a contradiction.
The theorem says that every such list describes some world in which all the axioms are true.
So "no contradiction can be proved" and "there is an example" mean the same thing.
For example, the axioms of a group with an element of order $3$ are consistent, and the group $\Z/3\Z$ satisfies them.

### L2 human

We use the theorem to show that a sentence does not follow from some axioms.

1. Let $\Gamma$ be the axioms of a partial order, and let $\varphi$ say "any two elements are comparable".
2. The theorem, in the form of part 3, says that $\Gamma \vdash \varphi$ holds if and only if $\Gamma \models \varphi$ holds.
3. The structure $\set{a, b}$ with $a \le a$, $b \le b$ and nothing else is a partial order that fails $\varphi$.
4. So $\Gamma \not\models \varphi$, and hence $\Gamma \nvdash \varphi$.

The typical use is in this direction: a model is a certificate that something is not provable.
The trap is to think that the theorem gives a useful model: the Henkin model is built from syntax and is often not the model one has in mind.

### L3 human

Part 1 says that the syntactic notion of consistency and the semantic notion of satisfiability coincide for first-order logic.
In algebraic terms, the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of a consistent theory has an ultrafilter that respects the quantifiers, and the ultrafilter gives a model.
By [[Lindström's theorem|FYZ3CJGZYV]], first-order logic is the largest regular logic with compactness and the downward Löwenheim-Skolem property, and both follow from parts 1 and 2.
The arithmetized form is a tool in the study of models of arithmetic, next to the [[incompleteness theorems|X9WYNYE29C]].
