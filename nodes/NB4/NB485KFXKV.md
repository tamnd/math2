---
tag: NB485KFXKV
kind: concept
name: Reflection principles
msc: ["03F40", "03F30", "03F25"]
topics: [HXHHWY3328]
audience: research
uses: [NB2BCZR40F, F6H4STF9RG, 4NBAX3VRQ7, 4PZM5GJTR5, 3HD30YG3DG, MPSCREYC3M, 4A84VHDTHV, 7CVJCQKY41]
sources:
  - url: https://en.wikipedia.org/wiki/Reflection_principle
    locator: For arithmetic
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: Second incompleteness theorem
---

## Summary

Consider the sentence "if $\mathsf{PA}$ proves $0 = 1$, then $0 = 1$".
Since $0 = 1$ is false, the sentence says exactly that $\mathsf{PA}$ does not prove $0 = 1$, which is the consistency of $\mathsf{PA}$.
A reflection principle makes the same claim for every sentence at once: whatever the theory proves is true.

Exactly: let $T$ be a consistent theory of arithmetic with a decidable set of axioms that contains $\mathsf{PA}$, and let $\mathrm{Prov}_T$ be its [[provability predicate|NB2BCZR40F]].
The local reflection principle $\mathrm{Rfn}(T)$ is the schema of the sentences
$$\mathrm{Prov}_T(\ulcorner \varphi \urcorner) \to \varphi,$$
one for each sentence $\varphi$.
The uniform reflection principle $\mathrm{RFN}(T)$ is the schema of the sentences
$$\forall x \, \bigl(\mathrm{Prov}_T(\ulcorner \varphi(\dot{x}) \urcorner) \to \varphi(x)\bigr),$$
one for each formula $\varphi(x)$ with one free variable.
For a class $\Gamma$ of formulas, such as $\Pi_1$ or $\Sigma_1$, the schemas $\mathrm{Rfn}_\Gamma(T)$ and $\mathrm{RFN}_\Gamma(T)$ keep only the instances with $\varphi$ in $\Gamma$.

## Motivation

By [[Gödel's second incompleteness theorem|4PZM5GJTR5]], $T$ does not prove $\mathrm{Con}(T)$.
Yet anyone who accepts the axioms of $T$ as true also accepts that every theorem of $T$ is true, and so accepts more than $T$ proves.
The [[consistency statement|4NBAX3VRQ7]] records one consequence of this belief: the false sentence $0 = 1$ is not a theorem.
The reflection principles record the whole belief, one sentence or one formula at a time.
They express the [[soundness|4A84VHDTHV]] of $T$ as far as arithmetic can express it, since truth itself is not definable.

This makes them a measuring tool.
Adding reflection to a weak theory gives the natural stronger theories, and Kreisel and Lévy showed, for example, that $\mathsf{PA}$ has the same theorems as primitive recursive arithmetic plus uniform reflection for it.
Iterating reflection leads to the [[Turing and Feferman progressions|F7Z4BV2KHD]] and to ordinal analysis.

## Notation

For a formula $\varphi(x)$, the expression $\ulcorner \varphi(\dot{x}) \urcorner$ is a term with the variable $x$ whose value at $x = n$ is the code of the sentence $\varphi(\underline{n})$.
It is built from the substitution and numeral functions of the [[arithmetization of syntax|6M12VR1GT6]].
$\mathrm{Rfn}$ is local and $\mathrm{RFN}$ is uniform in most recent texts, but some authors use other letters, so check the convention of each book.
$\mathrm{Rfn}_{\Pi_n}(T)$ and $\mathrm{RFN}_{\Sigma_n}(T)$ refer to the levels of the [[arithmetical hierarchy|7CVJCQKY41]].
A uniform principle for several free variables quantifies over all of them, and over $\mathsf{PA}$ it follows from the one-variable form by coding a tuple as one number.

## Remarks

### Consistency is the smallest case

Take the instance of $\mathrm{Rfn}(T)$ for the sentence $0 = S0$:
$$\mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner) \to 0 = S0.$$
The axiom $Sx \ne 0$ of $\mathsf{Q}$ gives $\neg (0 = S0)$, and $A \to B$ together with $\neg B$ is equivalent to $\neg A$.
So the instance is equivalent over $\mathsf{Q}$ to $\neg \mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$, which is $\mathrm{Con}(T)$.

More is true: over $T$, the single sentence $\mathrm{Con}(T)$ already proves every instance of $\mathrm{Rfn}_{\Pi_1}(T)$, and even of $\mathrm{RFN}_{\Pi_1}(T)$.
The proof is worked out in [[consistency as Π1 reflection|JHGJ6APMRF]].
So at the level $\Pi_1$ reflection collapses to consistency.

### What reflection proves

The Gödel sentence $G$ of $T$ satisfies $T \vdash \neg G \to \mathrm{Prov}_T(\ulcorner G \urcorner)$, by its fixed point property.
With the instance $\mathrm{Prov}_T(\ulcorner G \urcorner) \to G$ of $\mathrm{Rfn}(T)$ this gives $\neg G \to G$, and so $G$.
So one instance of reflection proves the sentence that $T$ cannot prove.

Uniform reflection is stronger still.
[[Uniform reflection over PRA|DGQRT1BVJ3]] proves the whole induction schema, which is the easy half of the Kreisel-Lévy theorem: $\mathsf{PRA} + \mathrm{RFN}(\mathsf{PRA})$ and $\mathsf{PA}$ have the same theorems.
The other half, that $\mathsf{PA}$ proves each instance of $\mathrm{RFN}(\mathsf{PRA})$, uses [[partial truth predicates|Y2MF1EZAM7]] and cut elimination, and we do not prove it here.

If all axioms of $T$ are true in $\mathbb{N}$, then every instance of $\mathrm{RFN}(T)$ is true in $\mathbb{N}$.
The reason is that every theorem of $T$ is then true, including each $\varphi(\underline{n})$ that $T$ proves.

### What reflection is not

The schema $\varphi \to \mathrm{Prov}_T(\ulcorner \varphi \urcorner)$ points the other way.
It claims completeness, not soundness, and for a sound $T$ its instance for the Gödel sentence is false; see [[the completeness schema|R1M4RR5WR1]].

The [[derivability condition|F6H4STF9RG]] $\mathrm{Prov}_T(\ulcorner \varphi \urcorner) \to \mathrm{Prov}_T(\ulcorner \mathrm{Prov}_T(\ulcorner \varphi \urcorner) \urcorner)$ is not a reflection principle either.
Its conclusion is again a statement about provability, and $T$ proves every instance of it, while $T$ does not prove $\mathrm{Rfn}(T)$.

### The rules you can use

When $x$ does not occur in $\varphi$, the uniform instance for $\varphi$ is logically equivalent to the local one, so $\mathrm{RFN}(T)$ implies $\mathrm{Rfn}(T)$.

[[Löb's theorem|3HD30YG3DG]] says that $T$ proves $\mathrm{Prov}_T(\ulcorner \varphi \urcorner) \to \varphi$ only when $T$ proves $\varphi$.
So $T$ proves just the instances of local reflection that it does not need.
In particular $T$ does not prove the instance for $0 = S0$, and $T + \mathrm{Rfn}(T)$ is a proper extension of $T$.

All instances of $\mathrm{Rfn}_{\Sigma_1}(T)$ are true in $\mathbb{N}$ exactly when every $\Sigma_1$ sentence that $T$ proves is true.
This is the property of [[1-consistency|4S29X1GTV4]].

### Watch out

Do not think that $\mathrm{Rfn}_{\Sigma_1}(T)$ is equivalent to $\mathrm{Con}(T)$.
Take $\sigma := \mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$, a $\Sigma_1$ sentence.
Inside $T + \mathrm{Con}(T)$ the conclusion $\sigma$ is false, so the instance $\mathrm{Prov}_T(\ulcorner \sigma \urcorner) \to \sigma$ is equivalent there to $\neg \mathrm{Prov}_T(\ulcorner \sigma \urcorner)$.
Since $\sigma$ is equivalent to $\neg \mathrm{Con}(T)$, the formalized deduction theorem turns this into $\mathrm{Con}(T + \mathrm{Con}(T))$.
If $T + \mathrm{Con}(T)$ is consistent, the second incompleteness theorem says that it does not prove this sentence.
So local $\Sigma_1$ reflection is strictly stronger than consistency.

Do not think that a reflection principle is one sentence.
It is a schema, and only its $\Pi_1$ part collapses to the single sentence $\mathrm{Con}(T)$.

### History

Turing (1939) and Feferman (1962) added consistency and reflection statements along ordinal notations, in the work on progressions of theories.
Kreisel and Lévy made reflection principles a standard tool in their paper of 1968, "Reflection principles and their use for establishing the complexity of axiomatic systems".
That paper proved that $\mathsf{PA}$ is equivalent to $\mathsf{PRA}$ plus uniform reflection for $\mathsf{PRA}$.

### Try it

Write the instance of $\mathrm{Rfn}(\mathsf{PA})$ for the sentence $\forall x \, (0 + x = x)$, and say whether $\mathsf{PA}$ proves it.
It is $\mathrm{Prov}_{\mathsf{PA}}(\ulcorner \forall x \, (0 + x = x) \urcorner) \to \forall x \, (0 + x = x)$, and $\mathsf{PA}$ proves it, because $\mathsf{PA}$ proves the conclusion by induction.

Does $\mathsf{PA}$ prove the instance for $0 = S0$?
No: that instance is equivalent to $\mathrm{Con}(\mathsf{PA})$, and the second incompleteness theorem applies.

## Explanations

### L1 human

A reflection principle is a new axiom that says "every statement this theory proves is true".
For the statement "$2 + 2 = 4$" it says "if the theory proves $2 + 2 = 4$, then $2 + 2 = 4$", which is harmless.
For the false statement "$0 = 1$" it says "the theory does not prove $0 = 1$", which is the consistency of the theory.
Gödel showed that a good theory cannot prove its own consistency, so these new axioms always add something.

### L2 human

We check that one instance of local reflection proves the Gödel sentence $G$ of $T$.
By the diagonal lemma, $T \vdash G \leftrightarrow \neg \mathrm{Prov}_T(\ulcorner G \urcorner)$, so
$$T \vdash \neg G \to \mathrm{Prov}_T(\ulcorner G \urcorner).$$
Add the instance $\mathrm{Prov}_T(\ulcorner G \urcorner) \to G$ and chain the two implications:
$$T + \mathrm{Rfn}(T) \vdash \neg G \to G.$$
Since $(\neg G \to G) \to G$ is a tautology, $T + \mathrm{Rfn}(T) \vdash G$.
This is the typical use of reflection: it settles sentences that $T$ leaves open, in a controlled way.
Watch out: $T + \mathrm{Rfn}(T)$ is a new theory, and it does not prove its own reflection principle, by the second incompleteness theorem again.

### L3 human

Reflection principles form a hierarchy.
At the bottom, $\mathrm{Rfn}_{\Pi_1}(T)$, $\mathrm{RFN}_{\Pi_1}(T)$ and $\mathrm{Con}(T)$ are equivalent over $T$; above them come the local and uniform principles for $\Sigma_n$ and $\Pi_n$, and the full schemas at the top.
Later work studies the restricted principles with the algebraic methods of [[provability logic|WJK0YA4GP2]].
Iterating consistency or reflection along ordinal notations is one route to [[ordinal analysis|XTTKZTYDSD]]: a theory is measured by how far the iteration over a weak base must go to prove the same $\Pi_1$ sentences.
Feferman showed that iterated uniform reflection proves every true arithmetic sentence along suitable notations; see [[Turing and Feferman progressions|F7Z4BV2KHD]].
In set theory the word "reflection" means something else, the Lévy-Montague reflection of truth to sets, and the two ideas should not be confused.
