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

Let $\varphi$ and $\psi$ be first-order [[sentences|DKFGQTRYZE]] in a language with equality.
The non-logical symbols of a sentence are the relation, function and constant symbols of its [[signature|WDVVEYD6AT]] that occur in it; $=$ is a logical symbol.
Assume $\varphi \models \psi$, in the sense of [[logical consequence|1HK0VYWTV7]].

**Theorem (Craig).** There is a sentence $\theta$ such that:

1. $\varphi \models \theta$ and $\theta \models \psi$;
2. every non-logical symbol of $\theta$ occurs both in $\varphi$ and in $\psi$.

Such a $\theta$ is an interpolant of $\varphi$ and $\psi$.
Two proofs are given: [[a proof from Robinson's joint consistency theorem|~a657d74c]] and [[an outline of a proof by the cut-free sequent calculus|~ca2164eb]].

## Remarks

### Why each hypothesis is needed

- The condition on symbols is the content of the theorem. Without it, $\theta = \varphi$ always works.
- Arbitrary structures: over finite structures only, the theorem fails. Let $\varphi(P)$ say that $<$ is a linear order, the first element is in $P$, and $P$ alternates along successors.
- In a finite linear order, such a $P$ exists and is unique. The order has even length iff its last element is not in $P$.
- So $\varphi(P) \land \neg P(\mathrm{last})$ entails $\varphi(P') \to \neg P'(\mathrm{last})$ over finite structures. An interpolant in $\set{<}$ would define "even length" for finite linear orders, which no first-order sentence does.
- First-order logic: the theorem fails in some extensions of first-order logic, and holds in others. So it is a property of the logic, not of the notion of consequence alone.

### Consequences

- The [[Beth definability theorem|RJBDSA2ETP]]: a relation that is implicitly definable by a theory is explicitly definable in the language of the theory.
- [[Robinson's joint consistency theorem|~6d43779a]], by [[this proof|~1df8300a]].
- If $\varphi$ and $\psi$ share no non-logical symbol, then $\theta$ is a sentence of pure equality. For example, $P(a) \land \neg P(b) \models \exists x \, \exists y \, \neg (x = y)$, and the interpolant is $\exists x \, \exists y \, \neg (x = y)$ itself.
- If $\varphi$ is not satisfiable, $\theta$ can be $\neg \forall x \, (x = x)$. If $\psi$ is valid, $\theta$ can be $\forall x \, (x = x)$.
- Interpolants are computed in software verification, where they summarize what one part of a system tells another.

### Converse

The converse holds: if a sentence $\theta$ satisfies $\varphi \models \theta$ and $\theta \models \psi$, then $\varphi \models \psi$, because logical consequence is transitive.

### Generalizations

- [[Lyndon's interpolation theorem|BRDT1BT7WW]]: each relation symbol that occurs positively in $\theta$ occurs positively in both $\varphi$ and $\psi$, and the same for negative occurrences.
- Theories: if $T_1 \cup T_2$ has no model, then some sentence $\theta$ in the common symbols satisfies $T_1 \models \theta$ and $T_2 \models \neg \theta$. This is the separation form of [[Robinson's theorem|~6d43779a]].
- Formulas: for formulas $\varphi$ and $\psi$, treat the free variables as new constants. Then $\theta$ may contain the free variables common to both.
- The [[propositional Craig interpolation theorem|TRS2HY57EG]] is the case of propositional logic, with the common propositional variables in place of the common symbols.
- Many-sorted logic, intuitionistic predicate logic and the infinitary logic $L_{\omega_1 \omega}$ also have interpolation theorems.

## History

William Craig proved the theorem in 1957.
Abraham Robinson had published his joint consistency theorem in 1956, and the two results imply each other.
Roger Lyndon proved the refinement with positive and negative occurrences in 1959.

## Explanations

### L1 human

Suppose fact A implies fact B, and A and B talk partly about different things.
The theorem says that there is a middle fact C that uses only the words A and B have in common.
A implies C, and C implies B.
For example, "Ann is a tall doctor" implies "someone is tall or rich", and "Ann is tall" is a middle fact that uses only the shared words.

### L2 human

We find an interpolant for $\varphi = \forall x \, (P(x) \to Q(x)) \land P(a)$ and $\psi = Q(a) \lor R(a)$.

1. The common non-logical symbols are $Q$ and $a$. The symbol $P$ occurs only in $\varphi$, and $R$ only in $\psi$.
2. From $\varphi$, instantiate $x$ by $a$: $P(a) \to Q(a)$, and with $P(a)$ we get $Q(a)$. So $\varphi \models Q(a)$.
3. $Q(a) \models Q(a) \lor R(a)$, by the truth table of $\lor$.
4. So $\theta = Q(a)$ is an interpolant.

The typical use is to prove a definability result: an implication between two copies of a theory gives a definition in the common language.
The trap is to forget that equality is always shared: the interpolant may say how many elements there are, even when $\varphi$ and $\psi$ have no common symbol.

### L3 human

Interpolation says that the consequence relation of first-order logic factors through the common language.
In algebraic terms, the Lindenbaum-Tarski algebras of the languages $L_1 \cap L_2$, $L_1$, $L_2$ form a square that satisfies an amalgamation property.
Proof-theoretically, interpolants come from cut-free proofs, and their size can be bounded by the size of the proof.
Model-theoretically, interpolation is equivalent to Robinson's joint consistency theorem, and in abstract model theory it is one of the properties that compare logics.
