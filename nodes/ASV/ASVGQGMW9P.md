---
tag: ASVGQGMW9P
kind: statement
role: proposition
name: The Yablo T-sentences are consistent but omega-inconsistent
aliases: [yablo-omega-inconsistency]
msc: ["03A05", "03F25"]
topics: [6Q4JJ2MMV8]
audience: grad
about: [99XVFR5ZN5, 4S29X1GTV4]
uses: [P3XFQC6ACX, BJF29XET83, HACXBCM7SS, 4S29X1GTV4, 1NR3HAWG9D, WP27CABPA4]
proofs: [4C40VGJHDD]
sources:
  - url: https://plato.stanford.edu/entries/self-reference/
    locator: "Self-Reference and Paradox, 1.6 Paradoxes without Self-Reference"
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 1.5 Infinite sequences"
---

## Statement

Let $\mathsf{PA}_T$ be [[Peano arithmetic|HACXBCM7SS]] in the language $\mathcal{L}_T$ with one unary predicate $T$, with induction for all formulas of $\mathcal{L}_T$.
Let $\mathrm{Sb}(a, z, u)$ be a formula of arithmetic that [[represents|BJF29XET83]] the primitive recursive function $\mathrm{sub}(a, z)$.
Here $\mathrm{sub}(a, z)$ is the code of the result of substituting the numeral $\underline{z}$ for $y$ in the formula with code $a$.
By the [[diagonal lemma with parameters|P3XFQC6ACX]], there is a formula $Y(y)$ with
$$\mathsf{PA} \vdash Y(y) \leftrightarrow \forall z\,\bigl(y < z \to \neg \tau(z)\bigr), \qquad \tau(z) := \exists u\,\bigl(\mathrm{Sb}(\ulcorner Y \urcorner, z, u) \wedge T(u)\bigr).$$
Write $Y_n$ for the sentence $Y(\underline{n})$, the $n$-th *Yablo sentence*.
It says that no later Yablo sentence is true.
Let $\mathsf{U} := \mathsf{PA}_T + \{T(\ulcorner Y_n \urcorner) \leftrightarrow Y_n : n \in \mathbb{N}\}$, the instances of the [[naive truth schema|99XVFR5ZN5]] for the Yablo sentences.
Then the following hold.

1. *(No assignment.)* No function $v \colon \mathbb{N} \to \{0, 1\}$ satisfies, for all $n$: $v(n) = 1$ if and only if $v(k) = 0$ for all $k > n$.
2. *(Consistency.)* $\mathsf{U}$ is consistent.
3. $\mathsf{U} \vdash \neg \tau(\underline{n})$ for every $n \in \mathbb{N}$.
4. $\mathsf{U} \vdash \exists z\, \tau(z)$.
5. *(ω-inconsistency.)* $\mathsf{U}$ is [[ω-inconsistent|4S29X1GTV4]], and no expansion of the [[standard model|WP27CABPA4]] is a model of $\mathsf{U}$.

## Remarks

### Why each hypothesis is needed

1. Part 2 uses that $\mathsf{U}$ has T-sentences only for the Yablo sentences. With all T-sentences, the theory is inconsistent by the [[liar paradox|KBYY281V8T]].
2. Part 5 needs the whole infinite sequence. For a finite part of the sequence, the [[compactness theorem|1NR3HAWG9D]] argument in the proof gives a model that expands $\mathcal{N}$.
3. The function $\mathrm{sub}$ must be represented in $\mathsf{PA}$, so that $\mathsf{PA}_T \vdash \tau(\underline{n}) \leftrightarrow T(\ulcorner Y_n \urcorner)$ for each $n$.

### Consequences

1. The T-sentences for the Yablo sentences have no model in which the numbers are standard. So the [[Yablo paradox|6FJXAN1ND9]] refutes the naive truth schema in the standard model.
2. In first-order arithmetic, the Yablo argument gives $\omega$-inconsistency and not inconsistency. So the formal version is weaker than the liar.

### Converse

The SEP entry on self-reference states that every finitary variant of the sequence is consistent, by compactness.
In such a variant, each sentence refers only to finitely many later sentences.

### Generalizations

[[McGee's theorem|GQW8RQVZJ4]] has the same form for a different set of axioms: a consistent theory of truth that is $\omega$-inconsistent.

## Explanations

### L1 human

Imagine an infinite line of people.
Each person says: "everyone after me is lying".
Whatever we decide about each person, some person's claim comes out wrong.
In arithmetic, this sequence of claims does not give an outright contradiction.
It gives a theory that says "some person tells the truth", but also says of each named person that this person does not.

### L2 human

1. Part 1 is the informal Yablo argument: if $v(n) = 1$, then $v(n + 1) = 0$ and all later values are $0$, which forces $v(n + 1) = 1$.
2. So every $v(n)$ is $0$, and then $v(0) = 1$, a contradiction.
3. In $\mathsf{U}$, the first step proves $\neg \tau(\underline{n})$ for each numeral separately.
4. The second step, "so every $v(n)$ is $0$", would need $\forall z\, \neg \tau(z)$. The theory does not prove this, because it has T-sentences only for numerals.

The typical use is to show that the T-sentences can fail in the standard model without being inconsistent.
The trap is to think that the formal theory proves a contradiction: it proves $\exists z\, \tau(z)$, and the witness is a nonstandard number.

### L3 human

The Yablo sequence has an acyclic but not well-founded structure of reference.
The SEP entry on self-reference reports a conjecture that every paradoxical structure of reference is either cyclic or contains a Yablo-like structure.
The $\omega$-inconsistency links the paradox to nonstandard models, as in [[McGee's theorem|GQW8RQVZJ4]].
