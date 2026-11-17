---
tag: DEB3CF4Z2D
kind: concept
name: First-order resolution
aliases: [resolution-first-order-logic, robinson-resolution]
msc: ["03B10", "03B35"]
topics: [TTCRX3NFNY]
audience: grad
uses: [086QKPF0A6, T3SXVH3ZZC, RJJ9D0WF53, NCDZ969V7X, CS82V969DE, GCPQGMJYEV, B37TYWXS74, 0B3D4C8YF2, VZ21F10WRS, QN7M1JCGT9]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: Resolution in first-order logic
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: Factoring
  - url: https://en.wikipedia.org/wiki/Unification_(computer_science)
    locator: Occurs check
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Resolution
---

## Summary

First-order resolution is a refutation calculus for sets of [[clauses|T3SXVH3ZZC]] of [[first-order logic|086QKPF0A6]].
A clause is a finite set of literals, and it stands for the universal closure of the disjunction of its literals.
The calculus has two rules.
Binary resolution: take clauses $C \cup \{A\}$ and $D \cup \{\neg B\}$ with no common variable, where the atoms $A$ and $B$ have a most general [[unifier|RJJ9D0WF53]] (mgu) $\sigma$.
From them, derive the resolvent $(C \cup D)\sigma$.
Factoring: from a clause $C \cup \{L_1, L_2\}$, where the literals $L_1$ and $L_2$ have an mgu $\sigma$, derive the factor $(C \cup \{L_1\})\sigma$.
A refutation of a set $S$ of clauses is a finite derivation of the empty clause $\square$ from $S$.
The calculus is sound and refutation complete: $S$ has a refutation exactly when $S$ is unsatisfiable.
To show $\Gamma \models \varphi$, one turns $\Gamma \cup \{\neg\varphi\}$ into clauses and searches for a refutation.
Resolution matters because it has one rule, needs no choice of instances by hand, and is the basis of most automatic provers for first-order logic.

## Motivation

[[Herbrand's theorem|VZ21F10WRS]] reduces the unsatisfiability of a universal sentence to the unsatisfiability of finitely many ground instances.
A naive prover enumerates ground instances and tests them with propositional methods.
This wastes effort, because the prover must guess the right closed terms in advance.
Resolution delays the choice of instances.
It instantiates a clause only as far as needed to make two literals complementary, and [[unification|RJJ9D0WF53]] computes this least instantiation.
For example, $\{\neg P(x), Q(x)\}$ and $\{P(f(a))\}$ give $\{Q(f(a))\}$ with the substitution $\{x \mapsto f(a)\}$, and no other instance of the first clause is ever formed.
One resolution step with variables stands for infinitely many ground steps at once.

## Notation

A literal is an atomic formula $A$ or its negation $\neg A$.
The complement of a literal $L$ is $\overline{L}$: $\overline{A} = \neg A$ and $\overline{\neg A} = A$.
Clauses are written as sets, for example $\{\neg P(x), Q(x)\}$, and the empty clause is $\square$.
Some books write a clause as a disjunction $\neg P(x) \lor Q(x)$, and some as a sequent $P(x) \Rightarrow Q(x)$.
Substitutions are written $\{x \mapsto t, y \mapsto s\}$ and act on the right: $C\sigma$ is the result of applying $\sigma$ to every literal of $C$.
The composition $\sigma\theta$ means "first $\sigma$, then $\theta$", so $C(\sigma\theta) = (C\sigma)\theta$.
An empty substitution is written $\varepsilon$.
Robinson's original rule resolves a set of literals of one clause against a set of literals of the other clause in one step.
That rule has the same power as binary resolution plus factoring, which this page uses.

## Remarks

### From formulas to clauses

To test a finite set $\Gamma \cup \{\neg\varphi\}$ of sentences for unsatisfiability, a prover brings each sentence into clause form in four steps.

1. Prenex form: move all quantifiers to the front, after renaming bound variables apart; see [[prenex normal form|CS82V969DE]]. The result is logically equivalent to the input.
2. Skolemization: delete each $\exists y$ and replace $y$ by $f(x_1, \ldots, x_n)$, with a new function symbol $f$. Here $x_1, \ldots, x_n$ are the universal variables before $\exists y$; see [[Skolem normal form|GCPQGMJYEV]].
3. Matrix to CNF: bring the quantifier-free part into [[conjunctive normal form|0B3D4C8YF2]].
4. Clauses: each conjunct of the CNF becomes one clause, as the set of its literals, and the universal quantifiers are left implicit.

Steps 1, 3 and 4 give logically equivalent sentences.
Step 2 gives an [[equisatisfiable|B37TYWXS74]] sentence, not an equivalent one, so it is applied only after the goal is negated.
Each sentence gets its own new Skolem symbols.
Before two clauses take part in a step, their variables are renamed apart, so that no variable occurs in both.
This is sound because $\forall x\, C$ and $\forall y\, C[y/x]$ are logically equivalent.

### Unification

A unifier of two atoms $A$ and $B$ is a [[substitution|NCDZ969V7X]] $\sigma$ with $A\sigma = B\sigma$.
A unifier $\sigma$ is most general when every unifier $\theta$ has the form $\theta = \sigma\tau$ for some substitution $\tau$.
Robinson's unification algorithm decides whether two atoms are unifiable and returns an mgu when they are.
It works on a list of equations between terms, starting from the pairs of arguments in the same positions.

1. An equation $t = t$ is deleted.
2. An equation $f(s_1, \ldots, s_n) = f(t_1, \ldots, t_n)$ is replaced by $s_1 = t_1, \ldots, s_n = t_n$.
3. An equation $f(\ldots) = g(\ldots)$ with $f \neq g$ is a failure; constants count as $0$-ary function symbols.
4. An equation $x = t$ or $t = x$, with $x$ a variable and $t \neq x$, is a failure when $x$ occurs in $t$ (the occurs check).
5. Otherwise the binding $x \mapsto t$ is recorded and applied to all other equations and to the earlier bindings.

When no equation is left, the recorded bindings form an mgu.
The mgu that this algorithm returns binds only variables that occur in the two atoms.

### Soundness and refutation completeness

Soundness: every resolvent and every factor is a [[logical consequence|1HK0VYWTV7]] of its premises, read as universal closures.
For a factor, the premise $C \cup \{L_1, L_2\}$ implies its instance $(C \cup \{L_1, L_2\})\sigma$.
This instance equals the factor $(C \cup \{L_1\})\sigma$, because $L_1\sigma = L_2\sigma$.
For a resolvent, let a structure satisfy both premises, read as universal closures.
Then the instances $(C \cup \{A\})\sigma$ and $(D \cup \{\neg B\})\sigma$ hold under every assignment; fix one assignment.
Under it, $A\sigma$ and $B\sigma$ are the same atom, so $A\sigma$ is false or $\neg B\sigma$ is false.
In the first case a literal of $C\sigma$ is true, in the second case a literal of $D\sigma$ is true.
The empty clause is unsatisfiable, so a set of clauses with a refutation is unsatisfiable.

Refutation completeness: every unsatisfiable set of clauses has a refutation.
The full theorem belongs to the sub-area on completeness; here is the outline of the standard proof.

1. Herbrand step. If $S$ is unsatisfiable, then some finite set $S_0$ of ground instances of clauses of $S$ is unsatisfiable as a set of propositional clauses. This is [[Herbrand's theorem|VZ21F10WRS]], together with [[compactness|1NR3HAWG9D]] when $S$ is infinite.
2. Ground completeness. A finite unsatisfiable set of ground clauses has a refutation by ground resolution. The proof is an induction on the number of atoms; see the next paragraph.
3. Lifting. The lifting lemma below turns each ground step into a first-order step whose conclusion has the ground clause as an instance.
4. End. The ground refutation ends with $\square$, and the only clause with $\square$ as an instance is $\square$ itself.

For step 2, let $S_0$ be finite, unsatisfiable and ground, with atoms $A_1, \ldots, A_n$.
If $n = 0$, then every clause of $S_0$ is empty, and $S_0 \neq \varnothing$ because $\varnothing$ is satisfiable, so $\square \in S_0$.
If $n > 0$, set $A = A_n$.
Let $S_0^{+}$ be the set of the clauses $C \setminus \{\neg A\}$ for the clauses $C$ of $S_0$ with $A \notin C$.
This is $S_0$ with $A$ made true; it is unsatisfiable and has fewer atoms, so it has a refutation.
Put $\neg A$ back into the clauses from which it was deleted; the same steps derive $\square$ or $\{\neg A\}$ from $S_0$.
In the same way, setting $A$ false gives a derivation of $\square$ or $\{A\}$ from $S_0$.
If neither derivation gives $\square$, one more step resolves $\{A\}$ with $\{\neg A\}$ to $\square$.

The lifting lemma: let $C_1$ and $C_2$ be clauses with no common variable, and let $\theta$ be a substitution with $C_1\theta$ and $C_2\theta$ ground.
Let $D'$ be a resolvent of the ground clauses $C_1\theta$ and $C_2\theta$.
Then zero or more factoring steps turn $C_1$ and $C_2$ into clauses $C_1'$ and $C_2'$ with the following property.
Some binary resolvent $D$ of $C_1'$ and $C_2'$ satisfies $D' = D\tau$ for some substitution $\tau$.
The idea: the ground step resolves on one ground atom, and several literals of $C_1$ can map to it under $\theta$.
Factoring merges these literals first.
Then $\theta$ unifies the two literals on which $D$ is formed, and the mgu is at least as general as $\theta$.

### Examples

1. [[A chain of two syllogisms by resolution|SPE357630R]]: four clauses and three resolution steps with the mgus $\{x \mapsto a\}$, $\{y \mapsto a\}$ and $\varepsilon$.
2. [[A resolution refutation with a Skolem function|KTT1J1KHSR]]: from $\forall x\exists y\, R(x,y)$ and the symmetry of $R$ follows $\forall x\exists y\, R(y,x)$. The proof unifies terms built with the Skolem function $f$.
3. [[Factoring is needed in first-order resolution|NTB92RHJZC]]: the set $\{P(x), P(y)\}$, $\{\neg P(u), \neg P(v)\}$ is unsatisfiable, but binary resolution alone never derives $\square$ from it.
4. The sentence $\exists x\forall y\, R(x,y) \to \forall y\exists x\, R(x,y)$ is valid. Its negation gives the clauses $\{R(c, y)\}$ and $\{\neg R(u, d)\}$ with Skolem constants $c$ and $d$. The mgu $\{u \mapsto c, y \mapsto d\}$ resolves them to $\square$.
5. Horn clauses: when every clause is a [[Horn clause|QR92EZDTKF]], linear input resolution (SLD resolution) is already refutation complete. This is the proof procedure of logic programming.

### Non-examples

1. [[Unification without the occurs check|VHQXG9TYGE]]: a step that unifies $y$ with $h(g(y))$ derives $\square$ from a satisfiable set. The condition that fails is that $\sigma$ must be a unifier.
2. Resolving on two pairs of literals at once: from $\{P, Q\}$ and $\{\neg P, \neg Q\}$ one cannot derive $\square$. The set is satisfiable ($P$ true, $Q$ false); binary resolution gives only the tautologies $\{Q, \neg Q\}$ and $\{P, \neg P\}$.
3. A wrong Skolemization of $\forall x\exists y\, R(x,y)$ as $\{R(x, c)\}$ makes $y$ independent of $x$. With $\{\neg R(z, z)\}$ the mgu $\{x \mapsto c, z \mapsto c\}$ gives $\square$, although $\forall x\exists y\, R(x,y) \land \forall z\, \neg R(z,z)$ holds in $(\mathbb{N}, <)$. The correct clause $\{R(x, f(x))\}$ does not unify with $R(z,z)$, by the occurs check.

### Basic properties

1. Soundness: if $S$ has a refutation, then $S$ is unsatisfiable (see above).
2. Refutation completeness: if $S$ is unsatisfiable, then $S$ has a refutation (see above). With soundness, this makes resolution a complete test for $\Gamma \models \varphi$, like the other systems of this sub-area; compare [[equivalence of proof systems|A9AAHN4BMH]].
3. Resolution is not deductively complete. From $\{P(a)\}$ no step at all is possible, so the consequence $\{P(a), Q(b)\}$ is not derived. Consequences are proved by refuting the negated goal.
4. Ground resolution does not need factoring, because a set of literals never contains a literal twice. With variables, factoring is needed, as example 3 shows.
5. Proof search is a semi-decision procedure. A fair search finds a refutation when $S$ is unsatisfiable, but it can run forever when $S$ is satisfiable. For example, $\{P(a)\}$ and $\{\neg P(x), P(f(x))\}$ produce $P(f(a)), P(f(f(a))), \ldots$ without end.
6. No sound and complete method can stop on every satisfiable input, since validity in first-order logic is undecidable by [[Church's theorem|VA6BNNY2YC]].

### History

John Alan Robinson introduced the resolution principle and the unification algorithm in a paper in the Journal of the ACM in 1965.
A propositional form of the rule appears earlier in work of Davis and Putnam (1960) on satisfiability.
Robinson's paper made resolution the standard calculus of automated theorem proving for first-order logic.

### Common errors

1. Not renaming apart. The clauses $\{P(x)\}$ and $\{\neg P(f(x))\}$ are unsatisfiable together, but $P(x)$ and $P(f(x))$ do not unify, by the occurs check. After renaming the second clause to $\{\neg P(f(y))\}$, the mgu $\{x \mapsto f(y)\}$ gives $\square$.
2. Skolemizing the goal instead of its negation. Skolemization keeps satisfiability, not validity, so it must act on $\Gamma \cup \{\neg\varphi\}$.
3. Applying only part of the mgu. The resolvent is $(C \cup D)\sigma$, and $\sigma$ must also be applied to the literals that are not resolved on.

## Explanations

### L1 human

Resolution is a way to prove a claim by showing that its opposite leads to nonsense.
We write all facts as short "or" lists, for example "Socrates is not a man, or Socrates is mortal".
Two lists that contain a statement and its opposite can be merged into one list without that pair.
With "Socrates is a man", the list above gives "Socrates is mortal".
If we also add the opposite of the claim, "Socrates is not mortal", then the merge gives an empty list.
An empty list cannot be true, so the facts and the opposite of the claim cannot all hold.
With letters for objects, we first choose the object that makes two lists match; this choice is called unification.

### L2 human

We show that $\exists x\forall y\, R(x,y)$ implies $\forall y\exists x\, R(x,y)$ by resolution.

1. Negate the goal: $\neg\forall y\exists x\, R(x,y)$ is equivalent to $\exists y\forall x\, \neg R(x,y)$.
2. Rename bound variables: the second sentence becomes $\exists v\forall u\, \neg R(u,v)$.
3. Skolemize: $\exists x\forall y\, R(x,y)$ becomes $\forall y\, R(c,y)$, and $\exists v\forall u\, \neg R(u,v)$ becomes $\forall u\, \neg R(u,d)$. The constants $c$ and $d$ are new and distinct.
4. Clauses: $C_1 = \{R(c,y)\}$ and $C_2 = \{\neg R(u,d)\}$. They have no common variable.
5. Unify $R(c,y)$ with $R(u,d)$. The first arguments give $u \mapsto c$, and the second arguments give $y \mapsto d$.
6. The mgu is $\sigma = \{u \mapsto c, y \mapsto d\}$. Check: $R(c,y)\sigma = R(c,d) = R(u,d)\sigma$.
7. The resolvent is $(\varnothing \cup \varnothing)\sigma = \square$, so the negated goal is unsatisfiable together with the premise.

The typical use is a prover that runs this search on its own: it saturates the clause set under resolution and factoring until $\square$ appears.
A trap is the converse $\forall y\exists x\, R(x,y) \to \exists x\forall y\, R(x,y)$, which is not valid.
Its negation gives $\{R(g(y), y)\}$ and $\{\neg R(x, h(x))\}$, and the unification of $y$ with $h(g(y))$ fails by the occurs check, so no step is possible.

### L3 human

Resolution is the cut rule restricted to atoms.
Read the clause $\{\neg A_1, \ldots, \neg A_m, B_1, \ldots, B_n\}$ as the sequent $A_1, \ldots, A_m \Rightarrow B_1, \ldots, B_n$; then ground resolution is a [[sequent calculus|W72CA3R9MP]] cut on one atom.
Unification makes the cut "most general", so that one step covers all its ground instances.
The same idea of computing least instances appears in type inference and in logic programming, where SLD resolution on [[Horn clauses|QR92EZDTKF]] is the execution model.

Refinements restrict the rule and keep refutation completeness.
Ordered resolution resolves only on maximal literals for a suitable ordering, and hyperresolution combines several steps into one.
The set-of-support strategy stays complete when the clauses outside the support set are satisfiable.
For equality, resolution is extended by paramodulation and superposition; see [[rules for equality|Y90Z13AXY8]].
The propositional case is the [[Boolean satisfiability problem|3QKF32ZAKN]], where modern solvers use resolution implicitly through clause learning.

The completeness proof above connects three themes of the area: [[Herbrand's theorem|VZ21F10WRS]], [[compactness|1NR3HAWG9D]] and the [[completeness theorem|WQ1ZE255SF]].
The undecidability of first-order validity shows that the search cannot be made to stop on every satisfiable input.
Several decidable fragments of first-order logic are proved decidable by showing that a refinement of resolution terminates on them.
