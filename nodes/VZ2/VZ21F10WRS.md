---
tag: VZ21F10WRS
kind: statement
role: theorem
name: Herbrand's theorem
msc: ["03B10", "03F05", "03B35"]
topics: [FBWW4J1XWG]
audience: grad
uses: [WDVVEYD6AT, 6D3WA7N2W4, DKFGQTRYZE, 983GZBQYT4, 05006AJ7DZ, QN7M1JCGT9, GCPQGMJYEV]
about: [QN7M1JCGT9, 05006AJ7DZ]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand's_theorem
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Herbrand's_theorem
    locator: Proof sketch
  - url: https://en.wikipedia.org/wiki/Herbrand's_theorem
    locator: Generalizations of Herbrand's theorem
  - url: https://en.wikipedia.org/wiki/Jacques_Herbrand
    locator: Biography
history:
  first_stated: "Jacques Herbrand, 1930"
  notes: "Jacques Herbrand gave the theorem in his doctoral thesis, Recherches sur la théorie de la démonstration, which he defended at the Sorbonne in 1930."
same_as:
  wikidata: Q1930577
  wikipedia: Herbrand's theorem
---

## Statement

We work in first-order logic without equality, over a [[signature|WDVVEYD6AT]] $\sigma$ that has at least one constant symbol.
As in the proof system $H$ of the [[soundness theorem|~331f6430]], the connectives $\neg$, $\to$ and the quantifier $\forall$ are primitive, and $\lor$, $\land$, $\exists$ are abbreviations.
A closed [[term|6D3WA7N2W4]] is a term with no variables.
A quantifier-free sentence is read propositionally when each atomic sentence $R\,t_1 \cdots t_m$ is treated as a propositional variable.
Such a sentence is a [[tautology|05006AJ7DZ]] when every truth assignment to the atomic sentences makes it true.

Let $\psi$ be a quantifier-free formula whose free variables are among $x_1, \dots, x_n$.
For a tuple $\bar t = (t_1, \dots, t_n)$ of closed terms, write $\psi(\bar t)$ for the [[sentence|DKFGQTRYZE]] $\psi^{x_1 \cdots x_n}_{t_1 \cdots t_n}$, in which each $x_i$ is replaced by $t_i$.
The sentences $\psi(\bar t)$ are the ground instances of $\psi$.

**Theorem (existential form).**
The sentence $\exists x_1 \cdots \exists x_n \, \psi$ is valid if and only if there are a number $k \ge 1$ and tuples $\bar t_1, \dots, \bar t_k$ of closed terms such that
$$\psi(\bar t_1) \lor \psi(\bar t_2) \lor \cdots \lor \psi(\bar t_k)$$
is a tautology.

A disjunction of this kind is a Herbrand disjunction for $\exists \bar x \, \psi$.

**Theorem (dual form, equivalent).**
Let $\chi$ be a quantifier-free formula whose free variables are among $x_1, \dots, x_n$.
The sentence $\forall x_1 \cdots \forall x_n \, \chi$ is not [[satisfiable|QN7M1JCGT9]] if and only if there are $k \ge 1$ and tuples $\bar t_1, \dots, \bar t_k$ of closed terms such that $\chi(\bar t_1) \land \cdots \land \chi(\bar t_k)$ is false under every truth assignment.

Two proofs are given: a [[proof by propositional compactness and a Herbrand structure|~e4acb6a6]] and a [[proof by cut elimination|~fef865bc]].

## Remarks

### The two forms are equivalent

1. Put $\chi = \neg \psi$. In every [[structure|983GZBQYT4]] $\mathcal{A}$, the sentence $\exists \bar x \, \psi$ is true exactly when $\forall \bar x \, \neg \psi$ is false.
2. So $\exists \bar x \, \psi$ is valid if and only if $\forall \bar x \, \neg \psi$ has no model.
3. By De Morgan's laws, $\psi(\bar t_1) \lor \cdots \lor \psi(\bar t_k)$ is a tautology if and only if $\neg \psi(\bar t_1) \land \cdots \land \neg \psi(\bar t_k)$ is false under every truth assignment.
4. For the other direction, start from $\chi$ and put $\psi = \neg \chi$. The instance $\neg \psi(\bar t) = \neg\neg\chi(\bar t)$ has the same truth value as $\chi(\bar t)$ under each truth assignment.

### Arbitrary sentences and Skolem normal form

The theorem speaks about existential and universal sentences only.
Every sentence reduces to this case.
Let $\varphi$ be a $\sigma$-sentence.
Its [[Skolem normal form|GCPQGMJYEV]] is a universal sentence $\varphi^S = \forall \bar x \, \chi$ with $\chi$ quantifier-free, in a signature $\sigma^S$ that adds new function symbols to $\sigma$.
The sentence $\varphi$ is satisfiable if and only if $\varphi^S$ is satisfiable.
If $\sigma^S$ has no constant symbol, we add one; this does not change satisfiability, because every structure has an expansion for the new symbol.
The dual form now gives: $\varphi$ is unsatisfiable if and only if some finite conjunction of ground instances of $\chi$ over $\sigma^S$ is false under every truth assignment.
To test whether $\varphi$ is valid, apply this to $\neg \varphi$.

Example: the sentence $\varphi = \exists x \, \forall y \, (P x \to P y)$ is valid.
Its negation is equivalent to $\forall x \, \exists y \, (P x \land \neg P y)$.
A Skolem normal form of it is $\forall x \, (P x \land \neg P f x)$, with a new unary function symbol $f$, and we add a constant symbol $c$.
The ground instances for $x = c$ and $x = fc$ are $P c \land \neg P fc$ and $P fc \land \neg P ffc$.
Their conjunction contains both $\neg P fc$ and $P fc$, so it is false under every truth assignment.
So $\neg \varphi$ has no model, and $\varphi$ is valid.

### Theories and equality

The [[compactness proof|~e4acb6a6]] gives a version with hypotheses.
Let $T$ be a set of universal sentences $\forall \bar y \, \theta$ with $\theta$ quantifier-free.
Then $T \models \exists \bar x \, \psi$ if and only if there are finitely many ground instances $\theta_1, \dots, \theta_m$ of members of $T$ and tuples $\bar t_1, \dots, \bar t_k$ with $k \ge 1$ such that
$$\theta_1 \land \cdots \land \theta_m \to \psi(\bar t_1) \lor \cdots \lor \psi(\bar t_k)$$
is a tautology.
The proof is the same as for $T = \emptyset$: put the ground instances of $T$ into the set $\Sigma$ of that proof.

In first-order logic with equality the symbol $=$ is interpreted as identity, and the theorem as stated fails.
For example, $\exists x \, (x = c)$ is valid, but each instance $t = c$ is an atomic sentence, and a disjunction of atomic sentences is never a tautology.
The remedy is to treat $=$ as an ordinary binary relation symbol $E$ and to add the equality axioms as hypotheses.
Let $\psi_E$ be $\psi$ with $=$ replaced by $E$.
Let $\mathrm{Eq}$ be the set of universal closures of the following formulas:

- reflexivity $E x x$, symmetry $E x y \to E y x$ and transitivity $E x y \land E y z \to E x z$;
- for each $m$-ary function symbol $f$ of $\psi$: $E x_1 y_1 \land \cdots \land E x_m y_m \to E \, f x_1 \cdots x_m \, f y_1 \cdots y_m$;
- for each $m$-ary relation symbol $R$ of $\psi$: $E x_1 y_1 \land \cdots \land E x_m y_m \land R x_1 \cdots x_m \to R y_1 \cdots y_m$.

Then $\exists \bar x \, \psi$ is valid in logic with equality if and only if $\mathrm{Eq} \models \exists \bar x \, \psi_E$ in logic without equality.
The version with hypotheses, for $T = \mathrm{Eq}$, then gives a Herbrand disjunction relative to ground instances of the equality axioms.
For $\exists x \, (x = c)$, the formula $E c c \to E c c$ is a tautology, and $E c c$ is a ground instance of reflexivity.

The equivalence is checked in four steps.

1. If $\mathcal{A}$ is a structure with true equality, interpret $E$ as identity. All members of $\mathrm{Eq}$ are true, so $\mathrm{Eq} \models \exists \bar x \, \psi_E$ gives $\mathcal{A} \models \exists \bar x \, \psi$.
2. For the converse, let $\mathcal{B}$ be a structure for the symbols of $\psi$ and $E$, with $\mathcal{B} \models \mathrm{Eq}$ and $\mathcal{B} \not\models \exists \bar x \, \psi_E$. Then $E^{\mathcal{B}}$ is an equivalence relation and a congruence for the function and relation symbols of $\psi$.
3. The quotient $\mathcal{B}/E$ has the classes $[b]$ as elements, with $f([b_1], \dots) = [f(b_1, \dots)]$ and $R([b_1], \dots)$ when $R(b_1, \dots)$. The congruence property makes these well defined, and induction on quantifier-free $\alpha$ gives $\mathcal{B} \models \alpha_E[b_1, \dots]$ if and only if $\mathcal{B}/E \models \alpha[[b_1], \dots]$.
4. Every tuple of classes has the form $([b_1], \dots, [b_n])$, and no tuple of $\mathcal{B}$ satisfies $\psi_E$. So $\mathcal{B}/E \not\models \exists \bar x \, \psi$, and $\exists \bar x \, \psi$ is not valid; any expansion of $\mathcal{B}/E$ to all of $\sigma$ is a counterexample.

### Herbrand complexity

The Herbrand complexity of a valid sentence $\exists \bar x \, \psi$ is the least $k$ such that some Herbrand disjunction of $k$ instances is a tautology.

- For $\exists x \, (P x \lor \neg P x)$ with a constant $c$, the single instance $P c \lor \neg P c$ is a tautology, so the complexity is $1$.
- For $\exists x \, (P x \to P f x)$ with a constant $c$, the complexity is $2$, as the next steps show.

1. Each single instance $P t \to P f t$ has two different atomic sentences $P t$ and $P f t$. The assignment with $P t$ true and $P f t$ false makes it false. So no disjunction with $k = 1$ is a tautology.
2. Take $t_1 = c$ and $t_2 = fc$. The disjunction is $(P c \to P fc) \lor (P fc \to P ffc)$.
3. Suppose that a truth assignment makes it false. Then the first disjunct is false, so $P fc$ is false.
4. The second disjunct is false too, so $P fc$ is true. This contradicts step 3, so the disjunction is a tautology.

The [[proof by cut elimination|~fef865bc]] gives an upper bound: the Herbrand complexity is at most the number of $\exists$-right inferences in any cut-free derivation of $\Rightarrow \exists \bar x \, \psi$ in the [[sequent calculus|W72CA3R9MP]] LK.

### Why each hypothesis is needed

- A constant symbol is needed. Over the signature with one unary relation symbol $P$ and no constant symbol, $\exists x \, (P x \lor \neg P x)$ is valid, because every structure has a nonempty universe. There are no closed terms, so there is no Herbrand disjunction with $k \ge 1$.
- The formula $\psi$ must be quantifier-free. The sentence $\exists x \, \forall y \, (P x \to P y)$ is valid. If we read each instance $\forall y \, (P t \to P y)$ as one propositional variable, distinct terms give distinct variables, and a disjunction of distinct variables is never a tautology. Skolem normal form is the correct way to handle such sentences.
- Equality must be absent or handled by the axioms $\mathrm{Eq}$, as the example $\exists x \, (x = c)$ shows.
- The number $k$ cannot be fixed at $1$, by the example $\exists x \, (P x \to P f x)$ of Herbrand complexity $2$.

### Converse

The direction "a Herbrand disjunction is a tautology, so $\exists \bar x \, \psi$ is valid" needs none of the hypotheses.
It holds with equality too, and with any signature.
The reason is that in every structure the atomic sentences get truth values, and a tautology is true under those values.
The other direction is the content of the theorem and needs all the hypotheses.

### Consequences

- Validity is semi-decidable. List all finite sets of tuples of closed terms, and test each disjunction by truth tables. The search stops exactly when the sentence is valid.
- The search cannot be turned into a decision procedure. By [[Church's theorem|VA6BNNY2YC]], validity of first-order sentences is undecidable, and Skolem normal form reduces every sentence to the existential case.
- The theorem is the basis of [[resolution|ZDW6N1PGJ7]] and of other methods of [[automated theorem proving|A51M1KK9DJ]]. These methods search for the terms $\bar t_i$ with [[unification|RJJ9D0WF53]] instead of listing all of them.
- Over a signature with a constant symbol, a universal sentence with a model has a model whose elements are closed terms: a Herbrand structure. This is part of the [[compactness proof|~e4acb6a6]].

### Generalizations

- Herbrand normal form is the dual of Skolem normal form: it removes the universal quantifiers of a prenex sentence with new function symbols. A sentence is valid if and only if its Herbrand normal form is valid, and the theorem applies to that existential sentence.
- Dale Miller extended the theorem to higher-order logic in 1987, with expansion-tree proofs in place of Herbrand disjunctions.
- Herbrand disjunctions have versions with a notion of cut. These can be non-elementarily smaller than ordinary Herbrand disjunctions.

## History

Jacques Herbrand proved the theorem in his doctoral thesis, Recherches sur la théorie de la démonstration, which he defended at the Sorbonne in 1930.
The sequent calculus and the [[cut-elimination theorem|AYRZ98Y0NW]] were introduced by Gerhard Gentzen in 1934, after Herbrand's work.
So Herbrand's own proof is different from the [[proof by cut elimination|~fef865bc]] given here.

## Explanations

### L1 human

Suppose that a sentence says "there is an object with a certain property", and the sentence is true in every possible world.
Herbrand's theorem says that we can then name finitely many candidates, built from the names in the language.
For these candidates, the statement "one of them has the property" is true by a truth table alone.
Here is an instance with small numbers.
Take the sentence "there is a person $x$ such that, if $x$ is happy, then the mother of $x$ is happy".
Take two candidates: Ann, and the mother of Ann.
If Ann is happy and her mother is not, then the second candidate works.
The claim for the mother starts with "if the mother of Ann is happy", and this part is false, so the whole claim is true.
In every other case the first candidate works.
So two candidates are enough, and one candidate is not.

### L2 human

We show that $\varphi = \forall x \, P x \to \forall x \, P g x$ is valid, with the dual form.

1. The negation $\neg \varphi$ is equivalent to $\forall x \, P x \land \exists y \, \neg P g y$.
2. A prenex form is $\exists y \, \forall x \, (P x \land \neg P g y)$.
3. A Skolem normal form replaces $y$ by a new constant $d$: $\forall x \, (P x \land \neg P g d)$. Now $d$ is a constant symbol, so the closed terms exist.
4. The ground instance for $x = g d$ is $P g d \land \neg P g d$.
5. This conjunction is false under every truth assignment, so $k = 1$ already works.
6. So $\neg \varphi$ has no model, and $\varphi$ is valid.

The typical use is in automated reasoning: the prover Skolemizes the negation of the goal and looks for a contradictory finite set of ground instances.
The trap is equality: a Herbrand disjunction that uses $=$ is checked by truth tables only after the equality axioms are added, because $c = c$ alone is not a tautology.
A second trap is to expect one instance to be enough; the example $\exists x \, (P x \to P f x)$ needs two.

### L3 human

Herbrand's theorem says that a first-order proof of an existential sentence has a finite, quantifier-free core: the Herbrand disjunction, together with the witnessing terms.
In sequent calculus this is the content of cut elimination for prenex sentences; Gentzen's midsequent theorem gives a closely related form.
The model-theoretic side is the [[compactness theorem|1NR3HAWG9D]] and the term model, which also appears in the Henkin proof of [[Gödel's completeness theorem|WQ1ZE255SF]].

The theorem links logic to computation.
It reduces first-order validity to an infinite family of propositional problems, which explains why validity is semi-decidable but, by Church's theorem, not decidable.
The size of Herbrand disjunctions is a measure of proof complexity, and the same idea of extracting terms from proofs returns in the study of the computational content of proofs.
Within this topic the theorem stands next to the [[Craig interpolation theorem|E2CBFNAVZY]], which also has a proof from cut-free derivations.
