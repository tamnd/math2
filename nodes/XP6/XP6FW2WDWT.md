---
tag: XP6FW2WDWT
kind: statement
role: theorem
name: Trakhtenbrot's theorem
aliases: [trakhtenbrot-theorem, undecidability-of-finite-satisfiability]
msc: ["03B25", "03C13", "03D35"]
topics: [E4AVTNWE9E]
audience: grad
uses: [VA6BNNY2YC, QN7M1JCGT9, 5SDS9T8E7J, 983GZBQYT4, PPGD5KW8JC, TN9G24VABN, Z7TN2B35B0]
about: [4XRVJE0KAN, QN7M1JCGT9]
history:
  first_stated: "1950"
  notes: Proved by Boris Trakhtenbrot in 1950.
sources:
  - url: https://en.wikipedia.org/wiki/Trakhtenbrot%27s_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Finite_model_theory
    locator: lead section
---

## Statement

On finite structures, first-order logic has no algorithm for satisfiability and no complete proof system for validity.
You can search for a finite model by trying sizes $1, 2, 3, \ldots$, and that search finds every finitely satisfiable sentence, but nothing tells you when to give up.

A sentence is finitely satisfiable when it is true in some finite structure, and finitely valid when it is true in every finite structure.
There is a finite signature $L$ of relation symbols, all of arity at most $2$, with the following two properties.

1. The set of finitely [[satisfiable|QN7M1JCGT9]] $L$-sentences is [[computably enumerable|TN9G24VABN]] but not [[computable|PPGD5KW8JC]].
2. The set of finitely valid $L$-sentences is not computably enumerable.

The [[proof by encoding halting runs|1TAE4N90VW]] gives both properties.

## Remarks

### A search that never ends

Let $\sigma_\infty$ say that $<$ is irreflexive, transitive and has no greatest element.
It has the model $(\mathbb{N}, <)$, but it has no finite model, as [[a sentence with only infinite models|KH3ZG4RXAW]] shows.
On $\sigma_\infty$ the search through finite structures runs forever.
For this sentence a short argument proves that no finite model exists.
Trakhtenbrot's theorem says that no algorithm can supply such arguments for all sentences.

### Why each hypothesis is needed

The restriction to finite structures is what changes property 2.
The set of valid sentences, true in all structures, is computably enumerable by [[Gödel's completeness theorem|WQ1ZE255SF]], while the set of finitely valid sentences is not.

The signature needs a symbol of arity at least $2$.
For a signature of unary relation symbols, a sentence with a model has a finite model, by the [[finite model property of monadic logic|AS0NHQMAKA]], and finite satisfiability is decidable.

### What it gives you

The completeness theorem fails for finite structures.
No proof system with a computable set of proofs proves exactly the finitely valid sentences, since such a system would make this set computably enumerable.
The compactness theorem fails for finite structures as well, as [[finite model theory|4XRVJE0KAN]] explains.

Finite satisfiability and satisfiability are different problems, and $\sigma_\infty$ separates them.
In databases, a query language as expressive as first-order logic has an undecidable problem of finite satisfiability.
So no algorithm decides whether a query returns a nonempty answer on some finite database.

### How the two properties are linked

A set $X$ of sentences is computable if and only if $X$ and its complement are computably enumerable.
Property 2 follows from property 1 by this fact, because $\sigma$ is finitely satisfiable exactly when $\neg \sigma$ is not finitely valid.
For signatures with only unary relation symbols both sets are computable, so the theorem fails there.

### Generalizations

The theorem holds for every signature that contains at least one binary relation symbol.
The proof for one binary relation symbol codes the finitely many relations of the proof into one, and it is longer.

### Watch out

[[Church's theorem|VA6BNNY2YC]] concerns validity in all structures, and Trakhtenbrot's theorem is the finite version.
The two differ in an exact way.
Validity is computably enumerable and not decidable, while finite validity is not even computably enumerable.
Do not assume that finite structures are easier for logic because each one can be checked: the difficulty comes from the infinitely many sizes.

## History

Trakhtenbrot proved the theorem in 1950.
It is one of the founding results of finite model theory, which studies logic on finite structures.
Its proof adapts the method of Church and Turing for Church's theorem to finite structures.

## Explanations

### L1 human

Some statements of logic can be true only in an infinite world, for example "after every number there is a larger number".
For statements about finite worlds, we might hope for a computer that checks whether some finite world makes the statement true.
A computer can try worlds of size $1$, $2$, $3$ and so on, and it stops when it finds one.
Trakhtenbrot proved that no computer can recognize all the statements for which this search never stops.

### L2 human

We test two sentences in the signature $\{ < \}$ by the search over finite structures.
Let $\sigma_1$ say that $<$ is a strict linear order with a greatest element.
The structure $\{ 1 \}$ with the empty order is a model, so the search stops at size $1$.

Let $\sigma_2$ say that $<$ is a strict linear order without a greatest element.
A finite nonempty linear order has a greatest element, so $\sigma_2$ has no finite model, and the search runs forever.
Here a short proof shows that no finite model exists.
Trakhtenbrot's theorem says that no algorithm replaces such proofs in general.
For each proof system with a computable set of proofs, some sentences without finite models have no proof of this fact.

The typical use of the theorem is in [[finite model theory|4XRVJE0KAN]] and in databases, where only finite structures matter.

### L3 human

In the arithmetical hierarchy, finite satisfiability is $\Sigma^0_1$-complete and finite validity is $\Pi^0_1$-complete.
Satisfiability is $\Pi^0_1$-complete and validity is $\Sigma^0_1$-complete.
So the roles of the two problems are exchanged when we pass from all structures to finite structures.

Many classical tools of model theory fail on finite structures, and finite model theory replaces them with games, such as the [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]], and with complexity theory.
The decidable fragments of the [[classical decision problem|ZF79MZRQ8V]] usually have the finite model property, so for them satisfiability and finite satisfiability coincide.
