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

First-order resolution proves a claim by deriving a contradiction from its negation, with a single rule that cancels a literal against its opposite.
Variables are handled by [[unification|RJJ9D0WF53]], which finds the least instance that makes two literals clash.
Here is a complete refutation of the three [[clauses|T3SXVH3ZZC]] $\{ \neg P(x), Q(x) \}$, $\{ P(a) \}$ and $\{ \neg Q(a) \}$:
$$\{ \neg P(x), Q(x) \},\ \{ P(a) \} \;\vdash\; \{ Q(a) \} \quad \text{with } \sigma = \{ x \mapsto a \}, \qquad \{ Q(a) \},\ \{ \neg Q(a) \} \;\vdash\; \square.$$
Check: $P(x)\sigma = P(a)$, so the first step cancels $\neg P(a)$ against $P(a)$ and keeps $Q(x)\sigma = Q(a)$.
The empty clause $\square$ cannot be true, so "every $P$ is a $Q$, and $a$ is a $P$" forces "$a$ is a $Q$".

In general, a clause is a finite set of literals, read as the universal closure of their disjunction.
The calculus has two rules.
Binary resolution takes clauses $C \cup \{ A \}$ and $D \cup \{ \neg B \}$ with no common variable, where the atoms $A$ and $B$ have a most general unifier (mgu) $\sigma$, and derives the resolvent $(C \cup D)\sigma$.
Factoring takes a clause $C \cup \{ L_1, L_2 \}$ in which the literals $L_1$ and $L_2$ have an mgu $\sigma$, and derives the factor $(C \cup \{ L_1 \})\sigma$.
A refutation of a set $S$ of clauses is a finite derivation of $\square$ from $S$.
The calculus is sound and refutation complete: $S$ has a refutation exactly when $S$ is unsatisfiable.

## Motivation

[[Herbrand's theorem|VZ21F10WRS]] reduces the unsatisfiability of a universal sentence to the unsatisfiability of finitely many ground instances of its matrix.
A naive prover lists ground instances and tests them with propositional methods, but it must guess the right closed terms in advance.
Resolution delays that choice.
It instantiates a clause only as far as needed to make two literals clash, and unification computes this least instantiation.
So one resolution step with variables stands for infinitely many ground steps at once.

This makes resolution the basis of most automatic provers for first-order logic.
To show $\Gamma \models \varphi$, a prover turns $\Gamma \cup \{ \neg\varphi \}$ into clauses and searches for a refutation.
Logic programming runs on a restricted form of the same rule.

## Notation

A literal is an atom $A$ or its negation $\neg A$, and its complement is $\overline{A} = \neg A$ and $\overline{\neg A} = A$.
Clauses are written as sets, and $\square$ is the empty clause.
Some books write a clause as a disjunction $\neg P(x) \lor Q(x)$, and some as a sequent $P(x) \Rightarrow Q(x)$.
Substitutions are written $\{ x \mapsto t, y \mapsto s \}$ and act on the right, so $C\sigma$ applies $\sigma$ to every literal of $C$.
The composition $\sigma\theta$ means "first $\sigma$, then $\theta$", and $\varepsilon$ is the empty substitution.
Robinson's original rule resolves a set of literals of one clause against a set of literals of the other in one step, and it has the same power as binary resolution plus factoring.

## Remarks

### From formulas to clauses

A prover brings each sentence of $\Gamma \cup \{ \neg\varphi \}$ into clause form in four steps.

1. Rename bound variables apart and move all quantifiers to the front, as in [[prenex normal form|CS82V969DE]].
2. Skolemize: delete each $\exists y$ and replace $y$ by $f(x_1, \ldots, x_n)$ for a new function symbol $f$, where $x_1, \ldots, x_n$ are the universal variables before $\exists y$; see [[Skolem normal form|GCPQGMJYEV]].
3. Bring the quantifier-free matrix into [[conjunctive normal form|0B3D4C8YF2]].
4. Turn each conjunct into the clause of its literals, and leave the universal quantifiers implicit.

Steps 1, 3 and 4 give logically equivalent sentences.
Step 2 gives only an [[equisatisfiable|B37TYWXS74]] sentence, so it is applied after the goal is negated, and each sentence gets its own new Skolem symbols.
Before two clauses meet in a step, their variables are renamed apart.
This is sound because $\forall x\, C$ and $\forall y\, C[y/x]$ are logically equivalent.

### Unification

A unifier of atoms $A$ and $B$ is a [[substitution|NCDZ969V7X]] $\sigma$ with $A\sigma = B\sigma$.
It is most general when every unifier $\theta$ has the form $\sigma\tau$ for some $\tau$.
Robinson's algorithm decides whether two atoms unify, and it returns an mgu when they do.
It works on a list of equations, starting with the pairs of arguments in matching positions.

1. Delete an equation $t = t$.
2. Replace $f(s_1, \ldots, s_n) = f(t_1, \ldots, t_n)$ by $s_1 = t_1, \ldots, s_n = t_n$.
3. Fail on $f(\ldots) = g(\ldots)$ with $f \neq g$, where constants count as $0$-ary function symbols.
4. Fail on $x = t$ or $t = x$ when $x$ is a variable, $t \neq x$, and $x$ occurs in $t$; this is the occurs check.
5. Otherwise record the binding $x \mapsto t$, and apply it to the other equations and to the earlier bindings.

When no equation is left, the bindings form an mgu.
For example, $P(x, f(y))$ and $P(g(z), f(a))$ give the equations $x = g(z)$ and $f(y) = f(a)$, and the mgu $\{ x \mapsto g(z), y \mapsto a \}$.

### Worked refutations

The [[chain of two syllogisms|SPE357630R]] refutes four clauses in three steps, with the mgus $\{ x \mapsto a \}$, $\{ y \mapsto a \}$ and $\varepsilon$.

The [[refutation with a Skolem function|KTT1J1KHSR]] shows that $\forall x\, \exists y\, R(x,y)$ and the symmetry of $R$ give $\forall x\, \exists y\, R(y,x)$.
Unification finds the witness term $f(c)$ on its own.

The valid sentence $\exists x\, \forall y\, R(x,y) \to \forall y\, \exists x\, R(x,y)$ needs one step.
Its negation gives the clauses $\{ R(c, y) \}$ and $\{ \neg R(u, d) \}$ with Skolem constants $c$ and $d$.
The mgu $\{ u \mapsto c, y \mapsto d \}$ makes both atoms $R(c,d)$, and the resolvent is $\square$.

When every clause is a [[Horn clause|QR92EZDTKF]], linear input resolution, called SLD resolution, is already refutation complete.
This is the proof procedure of logic programming.

### Where the rule needs care

The [[step without the occurs check|VHQXG9TYGE]] binds $y$ to $h(g(y))$ and derives $\square$ from a satisfiable set.
The condition that fails is that $\sigma$ must be a unifier.

The [[factoring example|NTB92RHJZC]] shows that $\{ P(x), P(y) \}$ and $\{ \neg P(u), \neg P(v) \}$ are unsatisfiable, but binary resolution alone never reaches $\square$ from them.

Resolving on two pairs of literals at once is not a rule.
The clauses $\{ P, Q \}$ and $\{ \neg P, \neg Q \}$ are satisfiable, with $P$ true and $Q$ false, and binary resolution gives only the tautologies $\{ Q, \neg Q \}$ and $\{ P, \neg P \}$.

A wrong Skolemization of $\forall x\, \exists y\, R(x,y)$ as $\{ R(x, c) \}$ makes $y$ independent of $x$.
With $\{ \neg R(z, z) \}$ the mgu $\{ x \mapsto c, z \mapsto c \}$ gives $\square$, yet $\forall x\, \exists y\, R(x,y) \land \forall z\, \neg R(z,z)$ holds in $(\mathbb{N}, <)$.
The correct clause $\{ R(x, f(x)) \}$ does not unify with $R(z,z)$, by the occurs check.

### Why resolution is sound

Every factor and every resolvent is a [[logical consequence|1HK0VYWTV7]] of its premises, read as universal closures.
A factor is an instance $(C \cup \{ L_1, L_2 \})\sigma$ of its premise, and that instance equals $(C \cup \{ L_1 \})\sigma$ because $L_1\sigma = L_2\sigma$.

For a resolvent, let a structure satisfy both premises.
Then the instances $(C \cup \{ A \})\sigma$ and $(D \cup \{ \neg B \})\sigma$ hold under every assignment, so fix one.
Since $A\sigma = B\sigma$, either $A\sigma$ is false or $\neg B\sigma$ is false.
In the first case some literal of $C\sigma$ is true, and in the second case some literal of $D\sigma$ is true.
The empty clause is unsatisfiable, so a set of clauses with a refutation is unsatisfiable.

### Refutation completeness

Every unsatisfiable set $S$ of clauses has a refutation.
The full theorem belongs to the sub-area on completeness, and the standard proof has four steps.

1. Herbrand step: some finite set $S_0$ of ground instances of clauses of $S$ is unsatisfiable as a set of propositional clauses, by [[Herbrand's theorem|VZ21F10WRS]] and, for infinite $S$, [[compactness|1NR3HAWG9D]].
2. Ground step: a finite unsatisfiable set of ground clauses has a refutation by ground resolution.
3. Lifting: each ground step lifts to a first-order step whose conclusion has the ground clause as an instance.
4. End: the ground refutation ends with $\square$, and the only clause with $\square$ as an instance is $\square$ itself.

### Refutation completeness, continued

The ground step goes by induction on the number $n$ of atoms in $S_0$.
If $n = 0$, every clause of $S_0$ is empty, and $S_0$ is not the empty set, because the empty set is satisfiable, so $\square \in S_0$.
If $n > 0$, pick an atom $A$, and form $S_0^{+}$ from the clauses without $A$ by deleting $\neg A$ from them.
This is $S_0$ with $A$ made true, so it is unsatisfiable with fewer atoms, and it has a refutation.
Putting $\neg A$ back, the same steps derive $\square$ or $\{ \neg A \}$ from $S_0$, and in the same way setting $A$ false gives $\square$ or $\{ A \}$.
If neither gives $\square$, one more step resolves $\{ A \}$ with $\{ \neg A \}$.

The lifting lemma says this.
Let $C_1$ and $C_2$ have no common variable, let $C_1\theta$ and $C_2\theta$ be ground, and let $D'$ be a resolvent of them.
Then factoring turns $C_1$ and $C_2$ into $C_1'$ and $C_2'$ with a binary resolvent $D$ such that $D' = D\tau$ for some $\tau$.
Factoring merges the literals that $\theta$ sends to the same ground atom, and the mgu is at least as general as $\theta$.

### What resolution does not do

Resolution is not deductively complete.
From $\{ P(a) \}$ no step is possible, so the consequence $\{ P(a), Q(b) \}$ is never derived, and consequences are proved by refuting the negated goal.

Ground resolution never needs factoring, because a set never contains a literal twice, but with variables factoring is needed.

Proof search is only a semi-decision procedure.
A fair search finds a refutation when $S$ is unsatisfiable, but it can run forever when $S$ is satisfiable.
For example, $\{ P(a) \}$ and $\{ \neg P(x), P(f(x)) \}$ produce $P(f(a)), P(f(f(a))), \ldots$ without end.
No sound and complete method can stop on every satisfiable input, because validity in first-order logic is undecidable by [[Church's theorem|VA6BNNY2YC]].
With soundness and completeness, resolution decides the same consequences as the other calculi; compare the [[equivalence of proof systems|A9AAHN4BMH]].

### Watch out

Rename the clauses apart before each step.
The clauses $\{ P(x) \}$ and $\{ \neg P(f(x)) \}$ are unsatisfiable together, but $P(x)$ and $P(f(x))$ do not unify, by the occurs check.
After renaming the second clause to $\{ \neg P(f(y)) \}$, the mgu $\{ x \mapsto f(y) \}$ gives $\square$.

Skolemize the negation of the goal, never the goal.
Skolemization keeps satisfiability, not validity, so it must act on $\Gamma \cup \{ \neg\varphi \}$.

Apply the whole mgu to the whole resolvent.
The resolvent is $(C \cup D)\sigma$, and $\sigma$ also acts on the literals that are not resolved on.

### History

John Alan Robinson introduced the resolution principle and the unification algorithm in a paper in the Journal of the ACM in 1965.
A propositional form of the rule appears earlier, in the work of Davis and Putnam of 1960 on satisfiability.
Robinson's paper made resolution the standard calculus of automated theorem proving for first-order logic.

### Try it

First, find an mgu of $Q(x, g(x))$ and $Q(a, y)$.
The equations $x = a$ and $g(x) = y$ give $x \mapsto a$ and then $y \mapsto g(a)$, so the mgu is $\{ x \mapsto a, y \mapsto g(a) \}$.

Second, write $\forall x\, \exists y\, (P(x) \to Q(y))$ in clause form.
Skolemizing $y$ as $f(x)$ gives $\forall x\, (\neg P(x) \lor Q(f(x)))$, which is the single clause $\{ \neg P(x), Q(f(x)) \}$.

## Explanations

### L1 human

Resolution proves a claim by showing that its opposite leads to nonsense.
We write all facts as short "or" lists, such as "Socrates is not a man, or Socrates is mortal".
Two lists that contain a statement and its opposite merge into one list without that pair.
With "Socrates is a man", the list above gives "Socrates is mortal".
If we add the opposite of the claim, "Socrates is not mortal", the merge gives an empty list.
An empty list cannot be true, so the facts and the opposite of the claim cannot all hold.
With letters for objects, we first choose the object that makes two lists match, and that choice is called unification.

### L2 human

We show that $\exists x\, \forall y\, R(x,y)$ implies $\forall y\, \exists x\, R(x,y)$ by resolution.

1. Negate the goal: $\neg\forall y\, \exists x\, R(x,y)$ is equivalent to $\exists y\, \forall x\, \neg R(x,y)$, which we rename to $\exists v\, \forall u\, \neg R(u,v)$.
2. Skolemize: the premise becomes $\forall y\, R(c,y)$ and the negated goal becomes $\forall u\, \neg R(u,d)$, with new distinct constants $c$ and $d$.
3. The clauses are $C_1 = \{ R(c,y) \}$ and $C_2 = \{ \neg R(u,d) \}$, and they share no variable.
4. Unify $R(c,y)$ with $R(u,d)$: the first arguments give $u \mapsto c$, and the second give $y \mapsto d$.
5. Check: with $\sigma = \{ u \mapsto c, y \mapsto d \}$, both atoms become $R(c,d)$, and the resolvent is $\square$.

A prover runs this search on its own, saturating the clause set under resolution and factoring until $\square$ appears.
Watch out for the converse $\forall y\, \exists x\, R(x,y) \to \exists x\, \forall y\, R(x,y)$, which is not valid.
Its negation gives $\{ R(g(y), y) \}$ and $\{ \neg R(x, h(x)) \}$, and unification fails on $y = h(g(y))$ by the occurs check, so no step is possible.

### L3 human

Resolution is the cut rule restricted to atoms.
Read the clause $\{ \neg A_1, \ldots, \neg A_m, B_1, \ldots, B_n \}$ as the sequent $A_1, \ldots, A_m \Rightarrow B_1, \ldots, B_n$; then ground resolution is a [[sequent calculus|W72CA3R9MP]] cut on one atom.
Unification makes the cut most general, so that one step covers all its ground instances.
The same idea of computing least instances appears in type inference and in logic programming, where SLD resolution on Horn clauses is the execution model.

Refinements restrict the rule and keep refutation completeness.
Ordered resolution resolves only on literals that are maximal for a suitable ordering, and hyperresolution combines several steps into one.
For equality, resolution is extended by paramodulation and superposition; see [[rules for equality|Y90Z13AXY8]].
The propositional case is the [[Boolean satisfiability problem|3QKF32ZAKN]], where modern solvers use resolution implicitly through clause learning.
The completeness proof ties together [[Herbrand's theorem|VZ21F10WRS]], compactness and the [[completeness theorem|WQ1ZE255SF]].
