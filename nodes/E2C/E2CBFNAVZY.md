---
tag: E2CBFNAVZY
kind: statement
role: theorem
name: Craig interpolation theorem
aliases: [craig-interpolation, craig-interpolation-theorem, interpolation-theorem]
msc: ["03C40", "03B10"]
topics: [FBWW4J1XWG]
audience: ug3
uses: [DKFGQTRYZE, 1HK0VYWTV7, WDVVEYD6AT]
about: [1HK0VYWTV7]
history:
  first_stated: "William Craig, 1957"
  notes: "Lyndon refined it in 1959."
sources:
  - url: https://en.wikipedia.org/wiki/Craig_interpolation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Craig_interpolation
    locator: Proof of Craig's interpolation theorem
  - url: https://en.wikipedia.org/wiki/Craig_interpolation
    locator: Applications
  - url: https://builds.openlogicproject.org/
    locator: Interpolation
same_as:
  wikidata: Q1052021
  wikipedia: Craig interpolation
---

## Statement

When one sentence implies another, the reason can always be written as a third sentence that speaks only about the symbols the two sentences share.
For example, $\forall x \, (P(x) \to Q(x)) \land P(a)$ implies $Q(a) \lor R(a)$, and the sentence $Q(a)$, which uses only the shared symbols $Q$ and $a$, sits between them.

Let $\varphi$ and $\psi$ be first-order [[sentences|DKFGQTRYZE]] in a language with equality.
The non-logical symbols of a sentence are the relation, function and constant symbols of its [[signature|WDVVEYD6AT]] that occur in it, and $=$ counts as a logical symbol.
Assume $\varphi \models \psi$, in the sense of [[logical consequence|1HK0VYWTV7]].

**Theorem (Craig).** There is a sentence $\theta$ such that:

1. $\varphi \models \theta$ and $\theta \models \psi$;
2. every non-logical symbol of $\theta$ occurs both in $\varphi$ and in $\psi$.

Such a $\theta$ is an interpolant of $\varphi$ and $\psi$.
Two proofs are given: [[a proof from Robinson's joint consistency theorem|JP8J5RJM6W]] and [[an outline of a proof by the cut-free sequent calculus|KJ7PEGF7YN]].

## Remarks

### A first interpolant

Take $\varphi = \forall x \, (P(x) \to Q(x)) \land P(a)$ and $\psi = Q(a) \lor R(a)$.
The symbol $P$ occurs only in $\varphi$, the symbol $R$ occurs only in $\psi$, and the shared symbols are $Q$ and $a$.
We look for a sentence in $Q$ and $a$ alone.
Instantiate the universal sentence at $a$ and use modus ponens:
$$P(a) \to Q(a), \quad P(a) \quad \text{give} \quad Q(a).$$
So $\varphi \models Q(a)$, and $Q(a) \models Q(a) \lor R(a)$ by the truth table of $\lor$.
Check: the interpolant $\theta = Q(a)$ mentions neither $P$ nor $R$.

The interpolant is the part of the information in $\varphi$ that $\psi$ can "hear".
Everything that $\varphi$ says about $P$ is private, and only its effect on the shared vocabulary passes through $\theta$.

### Why each hypothesis is needed

The condition on symbols is the content of the theorem, since without it $\theta = \varphi$ always works.

The theorem needs arbitrary structures, and it fails over finite structures only.
Let $\varphi(P)$ say that $<$ is a linear order, the first element lies in $P$, and $P$ alternates along immediate successors.
In a finite linear order such a $P$ exists and is unique, and the order has even length if and only if its last element is not in $P$.
So over finite structures $\varphi(P) \land \neg P(\mathrm{last})$ entails $\varphi(P') \to \neg P'(\mathrm{last})$, where $P'$ is a new symbol.
An interpolant in the language $\{ < \}$ would be a first-order sentence that defines "even length" among finite linear orders, and no first-order sentence does that.

The theorem is a property of the logic.
It holds in some extensions of first-order logic and fails in others.
In full second-order logic it holds for a cheap reason: if $P$ is the only symbol private to $\varphi$, then $\exists P \, \varphi$ is an interpolant.

### What it gives you: Beth definability

The main consequence is the [[Beth definability theorem|RJBDSA2ETP]]: a relation that a theory pins down implicitly has an explicit definition in the other symbols.
Here is a small case in the language $\{ P, Q, R \}$ of unary relation symbols.
Let $T(P)$ be the conjunction of three axioms:
$$\forall x \, (P x \to Q x), \qquad \forall x \, (Q x \land \neg R x \to P x), \qquad \forall x \, (P x \to \neg R x).$$
Two models of $T$ with the same $Q$ and $R$ have the same $P$, so $T$ defines $P$ implicitly.
With a copy $P'$ of $P$ and a new constant $c$, this gives the implication $T(P) \land P c \models T(P') \to P' c$.
The shared symbols are $Q$, $R$ and $c$, and $\theta = Q c \land \neg R c$ is an interpolant.
Check: the first and third axioms of $T(P)$ give $\theta$ from $P c$, and the second axiom of $T(P')$ gives $P' c$ from $\theta$.
Replacing $c$ by $x$ gives the explicit definition $T \models \forall x \, (P x \leftrightarrow Q x \land \neg R x)$.

### Other consequences

[[Robinson's joint consistency theorem|R6AN38DNBD]] follows from interpolation, by [[a short proof|V36AHEN7ZE]], and the two theorems are equivalent.

If $\varphi$ and $\psi$ share no non-logical symbol, then $\theta$ is a sentence of pure equality.
For example, $P(a) \land \neg P(b) \models \exists x \, \exists y \, \neg (x = y)$, and the conclusion itself is an interpolant, since it uses no non-logical symbol.
If $\varphi$ is unsatisfiable, $\theta$ can be $\neg \forall x \, (x = x)$, and if $\psi$ is valid, $\theta$ can be $\forall x \, (x = x)$.
Interpolants are also computed in software verification, where they summarize what one part of a system tells another.

### The converse and generalizations

The converse is true: if some $\theta$ has $\varphi \models \theta$ and $\theta \models \psi$, then $\varphi \models \psi$, because logical consequence is transitive.

[[Lyndon's interpolation theorem|BRDT1BT7WW]] sharpens the symbol condition: a relation symbol that occurs positively in $\theta$ occurs positively in both $\varphi$ and $\psi$, and the same holds for negative occurrences.
For theories, if $T_1 \cup T_2$ has no model, then some sentence $\theta$ in the common symbols has $T_1 \models \theta$ and $T_2 \models \neg \theta$.
For formulas, we treat the free variables as new constants, and $\theta$ may then contain the free variables common to both.
The [[propositional Craig interpolation theorem|TRS2HY57EG]] is the case of propositional logic, with the common variables in place of the common symbols.
Many-sorted logic, intuitionistic predicate logic and the infinitary logic $L_{\omega_1 \omega}$ also have interpolation theorems.

### Watch out

Equality is always shared, because it is a logical symbol.
A student who finds no common non-logical symbol may conclude that there is no interpolant, and that is wrong.
In the example $P(a) \land \neg P(b) \models \exists x \, \exists y \, \neg (x = y)$ the interpolant counts elements, and it uses only $=$.

A second slip is to put a private constant into the interpolant.
For $P(a) \models \exists x \, P(x)$ the sentence $P(a)$ is not an interpolant, because $a$ does not occur in $\psi$.
The correct interpolant is $\exists x \, P(x)$, which binds the private constant by a quantifier.

### Try it

First, find an interpolant for $R(a, a) \land P(a) \models \exists y \, R(y, y) \lor Q(b)$.
The only shared symbol is $R$, so the constant $a$ must be bound, and $\theta = \exists z \, R(z, z)$ works.

Second, find an interpolant for $P(a) \land Q(a) \models P(a) \lor S$, where $S$ is a sentence letter.
The shared symbols are $P$ and $a$, and $\theta = P(a)$ works.

## History

William Craig proved the theorem in 1957.
Abraham Robinson had published his joint consistency theorem in 1956, and the two results imply each other.
Roger Lyndon proved the refinement with positive and negative occurrences in 1959.
Evert Beth published his definability theorem in 1953, and Craig's theorem gave it a short new proof.

## Explanations

### L1 human

Suppose fact A implies fact B, and A and B talk partly about different things.
The theorem says that there is a middle fact C that uses only the words that A and B have in common.
A implies C, and C implies B.
For example, "Ann is a tall doctor" implies "Ann is tall or rich".
The middle fact "Ann is tall" uses only words of both sides.
Here "doctor" belongs only to A and "rich" belongs only to B, and C needs neither of them.

### L2 human

We find an interpolant for $\varphi = \forall x \, (P x \to Q x) \land \exists x \, P x$ and $\psi = \exists x \, (Q x \lor R x)$.
The shared symbol is $Q$ alone, so the interpolant can say only something about $Q$.
From $\varphi$, take a witness $a$ for $\exists x \, P x$, and the first conjunct gives $Q a$:
$$\varphi \models \exists x \, Q x.$$
In the other direction, a witness for $\exists x \, Q x$ is also a witness for $\exists x \, (Q x \lor R x)$:
$$\exists x \, Q x \models \psi.$$
Check: $\theta = \exists x \, Q x$ contains no $P$ and no $R$.

This is the typical shape: the interpolant forgets the private symbol $P$ by keeping only what it forces about $Q$.
When the private part is a constant, as in the first example, the interpolant must quantify it away.

### L3 human

Interpolation says that the consequence relation of first-order logic factors through the common language.
In algebraic terms, the Lindenbaum-Tarski algebras of the languages $L_1 \cap L_2$, $L_1$ and $L_2$ satisfy an amalgamation property.
In proof theory, interpolants come from cut-free proofs, and the [[sequent calculus proof|KJ7PEGF7YN]] bounds their size by the size of the proof.
In model theory, interpolation is equivalent to Robinson's joint consistency theorem, and in abstract model theory it is one of the properties used to compare logics.
The [[Herbrand theorem|VZ21F10WRS]] is a second result that reads explicit information off a cut-free derivation.
