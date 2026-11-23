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

When an existential sentence is valid, finitely many explicit candidates already witness it, and a truth table can check that one of them works.

We work in first-order logic without equality, over a [[signature|WDVVEYD6AT]] $\sigma$ that has at least one constant symbol.
As in the proof system $H$ of the [[soundness theorem|AVD7T7J063]], the connectives $\neg$, $\to$ and the quantifier $\forall$ are primitive, and $\lor$, $\land$, $\exists$ are abbreviations.
A closed [[term|6D3WA7N2W4]] is a term with no variables.
A quantifier-free sentence is read propositionally when each atomic sentence $R\,t_1 \cdots t_m$ is treated as a propositional variable.
Such a sentence is a [[tautology|05006AJ7DZ]] when every truth assignment to the atomic sentences makes it true.

Let $\psi$ be a quantifier-free formula whose free variables are among $x_1, \dots, x_n$.
For a tuple $\bar t = (t_1, \dots, t_n)$ of closed terms, write $\psi(\bar t)$ for the [[sentence|DKFGQTRYZE]] $\psi^{x_1 \cdots x_n}_{t_1 \cdots t_n}$, in which each $x_i$ is replaced by $t_i$.
The sentences $\psi(\bar t)$ are the ground instances of $\psi$.

**Theorem (existential form).**
The sentence $\exists x_1 \cdots \exists x_n \, \psi$ is valid if and only if there are a number $k \ge 1$ and tuples $\bar t_1, \dots, \bar t_k$ of closed terms such that the following disjunction is a tautology:
$$\psi(\bar t_1) \lor \psi(\bar t_2) \lor \cdots \lor \psi(\bar t_k).$$
A disjunction of this kind is a Herbrand disjunction for $\exists \bar x \, \psi$.

**Theorem (dual form).**
Let $\chi$ be a quantifier-free formula whose free variables are among $x_1, \dots, x_n$.
The sentence $\forall x_1 \cdots \forall x_n \, \chi$ is not [[satisfiable|QN7M1JCGT9]] if and only if there are $k \ge 1$ and tuples $\bar t_1, \dots, \bar t_k$ of closed terms such that $\chi(\bar t_1) \land \cdots \land \chi(\bar t_k)$ is false under every truth assignment.

Two proofs are given: a [[proof by propositional compactness and a Herbrand structure|8PA3V079T0]] and a [[proof by cut elimination|Y8PV0B46A6]].

## Remarks

### A first Herbrand disjunction

Take a constant $c$, a unary function symbol $f$ and a unary relation symbol $P$.
The sentence $\exists x \, (P x \to P f x)$ is valid: in any structure, either some element $a$ has $P a$ false, and then $a$ is a witness, or every element has $P$, and then every element is a witness.
Herbrand's theorem promises a finite list of closed terms that does the same job by truth tables alone.

One instance is not enough.
The instance $P t \to P f t$ contains two different atomic sentences, and the assignment with $P t$ true and $P f t$ false makes it false.
Two instances are enough, with $t_1 = c$ and $t_2 = fc$:
$$(P c \to P fc) \lor (P fc \to P ffc).$$
Check: if an assignment made both disjuncts false, the first would need $P fc$ false and the second would need $P fc$ true, which is impossible.

### Why the two forms say the same thing

Put $\chi = \neg \psi$.
In every [[structure|983GZBQYT4]], $\exists \bar x \, \psi$ is true exactly when $\forall \bar x \, \neg \psi$ is false.
So $\exists \bar x \, \psi$ is valid if and only if $\forall \bar x \, \neg \psi$ has no model.
By De Morgan's laws, $\psi(\bar t_1) \lor \cdots \lor \psi(\bar t_k)$ is a tautology if and only if $\neg \psi(\bar t_1) \land \cdots \land \neg \psi(\bar t_k)$ is false under every assignment.
For the other direction, start from $\chi$ and put $\psi = \neg \chi$; the instance $\neg \psi(\bar t) = \neg \neg \chi(\bar t)$ has the same truth value as $\chi(\bar t)$ under each assignment.

### Every sentence reduces to this case

The theorem speaks only about existential and universal sentences, but every sentence $\varphi$ can be brought to this shape.
Its [[Skolem normal form|GCPQGMJYEV]] is a universal sentence $\varphi^S = \forall \bar x \, \chi$ with $\chi$ quantifier-free, in a signature $\sigma^S$ that adds new function symbols.
The sentence $\varphi$ is satisfiable if and only if $\varphi^S$ is.
If $\sigma^S$ has no constant symbol we add one, and this keeps satisfiability, because every structure can interpret the new symbol.
So $\varphi$ is unsatisfiable exactly when some finite conjunction of ground instances of $\chi$ is false under every assignment, and we test validity of $\varphi$ by applying this to $\neg \varphi$.

For example, $\varphi = \exists x \, \forall y \, (P x \to P y)$ is valid.
Its negation is equivalent to $\forall x \, \exists y \, (P x \land \neg P y)$, with Skolem form $\forall x \, (P x \land \neg P f x)$ and an added constant $c$.
The instances for $x = c$ and $x = fc$ are $P c \land \neg P fc$ and $P fc \land \neg P ffc$.
Their conjunction contains both $\neg P fc$ and $P fc$, so it is false under every assignment, and $\varphi$ is valid.

### Theories as hypotheses

The [[compactness proof|8PA3V079T0]] also gives a version with hypotheses.
Let $T$ be a set of universal sentences $\forall \bar y \, \theta$ with $\theta$ quantifier-free.
Then $T \models \exists \bar x \, \psi$ if and only if there are finitely many ground instances $\theta_1, \dots, \theta_m$ of members of $T$ and tuples $\bar t_1, \dots, \bar t_k$ with $k \ge 1$ such that the following sentence is a tautology:
$$\theta_1 \land \cdots \land \theta_m \to \psi(\bar t_1) \lor \cdots \lor \psi(\bar t_k).$$
The proof is the one for $T = \emptyset$, with the ground instances of $T$ added to the set $\Sigma$ of that proof.

### Equality

With equality read as identity, the theorem as stated fails.
The sentence $\exists x \, (x = c)$ is valid, but each instance $t = c$ is an atomic sentence, and a disjunction of atomic sentences is never a tautology.
The remedy is to treat $=$ as an ordinary binary relation symbol $E$ and to add the equality axioms as hypotheses.
Let $\psi_E$ be $\psi$ with $=$ replaced by $E$, and let $\mathrm{Eq}$ be the set of universal closures of these formulas:

- reflexivity $E x x$, symmetry $E x y \to E y x$ and transitivity $E x y \land E y z \to E x z$;
- for each $m$-ary function symbol $f$ of $\psi$, the formula $E x_1 y_1 \land \cdots \land E x_m y_m \to E \, f x_1 \cdots x_m \, f y_1 \cdots y_m$;
- for each $m$-ary relation symbol $R$ of $\psi$, the formula $E x_1 y_1 \land \cdots \land E x_m y_m \land R x_1 \cdots x_m \to R y_1 \cdots y_m$.

Then $\exists \bar x \, \psi$ is valid in logic with equality if and only if $\mathrm{Eq} \models \exists \bar x \, \psi_E$ in logic without equality.
The version with hypotheses, for $T = \mathrm{Eq}$, now gives a Herbrand disjunction relative to ground instances of the equality axioms.
For $\exists x \, (x = c)$, the sentence $E c c \to E c c$ is a tautology, and $E c c$ is a ground instance of reflexivity.

### Equality, continued: why the reduction is correct

If $\mathcal{A}$ is a structure with true equality, we interpret $E$ as identity.
All members of $\mathrm{Eq}$ are then true, so $\mathrm{Eq} \models \exists \bar x \, \psi_E$ gives $\mathcal{A} \models \exists \bar x \, \psi$.

For the converse, let $\mathcal{B}$ be a structure with $\mathcal{B} \models \mathrm{Eq}$ and $\mathcal{B} \not\models \exists \bar x \, \psi_E$.
The axioms make $E^{\mathcal{B}}$ an equivalence relation that is a congruence for the symbols of $\psi$.
The quotient $\mathcal{B}/E$ has the classes $[b]$ as elements, with $f([b_1], \dots) = [f(b_1, \dots)]$, and with $R([b_1], \dots)$ when $R(b_1, \dots)$.
The congruence property makes these definitions independent of the representatives.
Induction on a quantifier-free $\alpha$ gives $\mathcal{B} \models \alpha_E[b_1, \dots]$ if and only if $\mathcal{B}/E \models \alpha[[b_1], \dots]$.
Every tuple of classes comes from a tuple of $\mathcal{B}$, and no tuple of $\mathcal{B}$ satisfies $\psi_E$, so $\mathcal{B}/E \not\models \exists \bar x \, \psi$.
Any expansion of $\mathcal{B}/E$ to all of $\sigma$ is then a structure with true equality in which $\exists \bar x \, \psi$ fails.

### Herbrand complexity

The Herbrand complexity of a valid sentence $\exists \bar x \, \psi$ is the least $k$ such that some Herbrand disjunction with $k$ instances is a tautology.
For $\exists x \, (P x \lor \neg P x)$ the single instance $P c \lor \neg P c$ is a tautology, so the complexity is $1$.
For $\exists x \, (P x \to P f x)$ the first computation above shows that the complexity is exactly $2$.

The complexity measures how much work the existential claim hides.
The [[proof by cut elimination|Y8PV0B46A6]] gives an upper bound.
The Herbrand complexity is at most the number of $\exists$-right inferences in any cut-free derivation of $\Rightarrow \exists \bar x \, \psi$ in the [[sequent calculus|W72CA3R9MP]] LK.

### Why each hypothesis is needed

The constant symbol is needed.
Over a signature with one unary relation symbol $P$ and no constant symbol, $\exists x \, (P x \lor \neg P x)$ is valid, because every structure has a nonempty universe.
There are no closed terms at all, so no Herbrand disjunction with $k \ge 1$ exists.

The formula $\psi$ must be quantifier-free.
The sentence $\exists x \, \forall y \, (P x \to P y)$ is valid.
If we read each instance $\forall y \, (P t \to P y)$ as one propositional variable, distinct terms give distinct variables, and a disjunction of distinct variables is never a tautology.
Skolem normal form is the correct way to handle such a sentence, as shown above.

Equality must be absent or handled by the axioms $\mathrm{Eq}$, as the example $\exists x \, (x = c)$ shows.
The number $k$ cannot be fixed at $1$, by the example $\exists x \, (P x \to P f x)$.

### The converse and what it gives you

The direction "a Herbrand disjunction is a tautology, so $\exists \bar x \, \psi$ is valid" needs none of the hypotheses, and it holds with equality and in any signature.
In every structure the atomic sentences get truth values, a tautology is true under those values, and so one instance is true and gives a witness.

The hard direction makes validity semi-decidable.
We list all finite sets of tuples of closed terms and test each disjunction by truth tables, and the search stops exactly when the sentence is valid.
The search cannot become a decision procedure, since validity is undecidable by [[Church's theorem|VA6BNNY2YC]].
[[Resolution|ZDW6N1PGJ7]] and other methods of [[automated theorem proving|A51M1KK9DJ]] rest on the theorem, and they find the terms $\bar t_i$ by [[unification|RJJ9D0WF53]] instead of listing all of them.
Along the way the compactness proof shows that a universal sentence with a model has a model whose elements are closed terms, a Herbrand structure.

### Generalizations

Herbrand normal form is the dual of Skolem normal form.
It removes the universal quantifiers of a prenex sentence with new function symbols, and a sentence is valid if and only if its Herbrand normal form is valid.
The theorem then applies to that existential sentence.
Dale Miller extended the theorem to higher-order logic in 1987, with expansion-tree proofs in place of Herbrand disjunctions.

### Watch out

A common slip is to apply the theorem to a sentence with quantifiers inside $\psi$.
For $\exists x \, \forall y \, (P x \to P y)$, the "instances" $\forall y \, (P c \to P y)$ are not quantifier-free, and no disjunction of them is a tautology.
The correct move is to Skolemize the negation first, as in the reduction above.

A second slip is to forget equality.
The sentence $c = c$ alone is not a tautology when read propositionally, so a disjunction that uses $=$ is checked by truth tables only after ground instances of $\mathrm{Eq}$ are added as hypotheses.

### Try it

First, find a Herbrand disjunction for $\exists x \, (P c \to P x)$.
The single instance $P c \to P c$ is a tautology, so $k = 1$ with $t_1 = c$.

Second, show that $\exists x \, \exists y \, (P x \to P y)$ has Herbrand complexity $1$.
Take the pair $(c, c)$: the instance $P c \to P c$ is a tautology.

## History

Jacques Herbrand proved the theorem in his doctoral thesis, Recherches sur la théorie de la démonstration, which he defended at the Sorbonne in 1930.
Gerhard Gentzen introduced the sequent calculus and the [[cut-elimination theorem|AYRZ98Y0NW]] in 1934, after Herbrand's work.
So Herbrand's own proof differs from the [[proof by cut elimination|Y8PV0B46A6]] given here.

## Explanations

### L1 human

Suppose a sentence says "there is an object with a certain property", and it is true in every possible world.
Herbrand's theorem says that we can then name finitely many candidates, built from the names in the language, and a truth table shows that one of them has the property.
Take the sentence "there is a person $x$ such that, if $x$ is happy, then the mother of $x$ is happy".
Take two candidates: Ann, and the mother of Ann.
If Ann is happy and her mother is not, the claim for the mother works, because its "if" part is false.
In every other case the claim for Ann works.
So two candidates are enough, and one candidate is not.

### L2 human

We show that $\varphi = \forall x \, P x \to \forall x \, P g x$ is valid with the dual form.
The negation $\neg \varphi$ is equivalent to $\forall x \, P x \land \exists y \, \neg P g y$, and a prenex form is $\exists y \, \forall x \, (P x \land \neg P g y)$.
A Skolem normal form replaces $y$ by a new constant $d$, so closed terms now exist:
$$\forall x \, (P x \land \neg P g d).$$
The ground instance for $x = g d$ is $P g d \land \neg P g d$.
Check: this conjunction contains an atomic sentence and its negation, so it is false under every assignment.
So $\neg \varphi$ has no model, and $\varphi$ is valid, with $k = 1$.

This is the typical use in automated reasoning: Skolemize the negation of the goal, then look for a contradictory finite set of ground instances.
The search for the right term $g d$ is the part that unification makes efficient.

### L3 human

Herbrand's theorem says that a first-order proof of an existential sentence has a finite quantifier-free core: the Herbrand disjunction with its witnessing terms.
In the sequent calculus this is the content of cut elimination for prenex sentences, and Gentzen's midsequent theorem gives a closely related form.
The model-theoretic side is the [[compactness theorem|1NR3HAWG9D]] and the term model, which also drives the Henkin proof of [[Gödel's completeness theorem|WQ1ZE255SF]].

The theorem reduces first-order validity to an infinite family of propositional problems, which explains why validity is semi-decidable and, by Church's theorem, not decidable.
The size of Herbrand disjunctions measures proof complexity, and extracting terms from proofs returns in the study of the computational content of proofs.
The [[Craig interpolation theorem|E2CBFNAVZY]] also has a proof from cut-free derivations, and it reads its interpolant off the derivation in the same way.
