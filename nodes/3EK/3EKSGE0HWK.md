---
tag: 3EKSGE0HWK
kind: example
name: Finiteness of the domain is not expressible in independence-friendly logic
msc: ["03B60", "03C80"]
topics: [MDHDYV8QZW]
audience: research
not_instance_of:
  - target: DPMKT2KRB8
    note: no sentence of independence-friendly logic is true exactly in the finite structures, although the sentence that expresses infinity is an IF sentence
uses: [DPMKT2KRB8, 1NR3HAWG9D, GCPQGMJYEV, 4R3D37KQD8]
sources:
  - url: https://en.wikipedia.org/wiki/Independence-friendly_logic
    locator: Model-theoretic properties
  - url: https://en.wikipedia.org/wiki/Compactness_theorem
    locator: lead section
---

## Example

[[Independence-friendly logic|DPMKT2KRB8]] can say "the domain is infinite", but it cannot say "the domain is finite".
We show that no IF sentence $\varphi$ is true exactly in the finite structures of its vocabulary.

1. Suppose that $\varphi$ is true in a structure $\mathcal{M}$ if and only if the domain of $\mathcal{M}$ is finite.
2. By the Skolem semantics, $\mathcal{M} \models \varphi$ if and only if $\mathcal{M} \models \exists f_1 \cdots \exists f_k \, \psi$.
   Here $\psi$ is a first-order sentence with new function symbols $f_1, \ldots, f_k$, from the [[Skolem form|GCPQGMJYEV]] of $\varphi$.
3. For every $n \geq 1$, a structure with $n$ elements is finite, so it satisfies $\varphi$.
   So it has an expansion that satisfies $\psi$, and $\psi$ has finite models of every size.
4. Let $\delta_n$ be the first-order sentence that says "there are at least $n$ elements":
   $$\delta_n := \exists x_1 \cdots \exists x_n \bigwedge_{1 \le i < j \le n} x_i \neq x_j.$$
   Let $T = \set{\psi} \cup \set{\delta_n : n \geq 1}$.
5. A finite subset of $T$ contains only sentences $\delta_n$ with $n \leq N$, for some $N$.
   A model of $\psi$ with $N$ elements satisfies this subset, and it exists by step 3.
6. By the [[compactness theorem|1NR3HAWG9D]] of first-order logic, $T$ has a model $\mathcal{N}$.
   It satisfies every $\delta_n$, so its domain is infinite.
7. The reduct of $\mathcal{N}$ to the vocabulary of $\varphi$ satisfies $\exists f_1 \cdots \exists f_k \, \psi$, with the functions of $\mathcal{N}$ as witnesses.
   By step 2, it satisfies $\varphi$.
8. This reduct is infinite and satisfies $\varphi$, which contradicts step 1.
   So no such $\varphi$ exists.

## Remarks

### What the example shows

IF logic is not closed under classical negation.
The [[infinity sentence|4R3D37KQD8]] $\iota$ is an IF sentence, and its classical negation would express finiteness.
Full second-order logic expresses finiteness with a $\Pi^1_1$ sentence: "every injective function from the domain to itself is surjective".

The argument uses only that the sentence is $\Sigma^1_1$.
So the same proof applies to the branching quantifier sentences with a first-order matrix, and to the sentences of dependence logic.

### The dual negation of the infinity sentence

The proof also tells us something about the dual negation $\neg \iota$ of IF logic.
Suppose that $\neg \iota$ were true in every finite structure.
Then the argument above would make it true in some infinite structure $\mathcal{M}$, so Abelard would have a winning strategy for $\iota$ in $\mathcal{M}$.
But Eloise also has one, because $\mathcal{M}$ is infinite, and both players cannot have winning strategies.
So in some finite structure, $\iota$ is neither true nor false.

## Explanations

### L1 human

IF logic can say "the set is infinite", but it cannot say "the set is finite".
The reason is that an IF sentence only asks for the existence of some hidden functions.
Suppose that such functions exist on larger and larger finite sets.
Then a general theorem of logic, compactness, produces them on an infinite set too.
So a sentence that holds on all finite sets must also hold on some infinite set.
Ordinary logic has the same limit, but there it applies to both "finite" and "infinite".

### L2 human

We follow the proof with a concrete IF sentence that holds in every finite structure of even size:
$$\eta := \forall x_1 \, \exists y_1 \, \forall x_2 \, (\exists y_2 / \set{x_1, y_1}) \, \big( (x_1 = x_2 \leftrightarrow y_1 = y_2) \land y_1 \neq x_1 \land (x_2 = y_1 \to y_2 = x_1) \big).$$

1. Its Skolem form is $\exists f \, \exists g \, \forall x_1 \, \forall x_2 \, \psi$, where $\psi$ is the matrix with $y_1 = f(x_1)$ and $y_2 = g(x_2)$.
2. The matrix forces $f = g$, and then $f$ is an injective function without fixed points that is its own inverse.
3. A set with $2m$ elements has such a function: pair the elements and swap each pair.
   So $\psi$ has finite models of sizes $2, 4, 6, \ldots$.
4. Compactness, as in steps 4 to 6 of the proof, gives an infinite model of $\psi$.
5. Indeed $\eta$ is true in $\mathbb{N}$, with $f(2n) = 2n + 1$ and $f(2n + 1) = 2n$.

Check: $f(f(4)) = f(5) = 4$ and $f(4) = 5 \neq 4$, as step 2 needs.
So $\eta$ cannot say "the domain is finite and of even size", and it says "the domain is of even size or infinite".
The typical use of the argument is to show that a property is not $\Sigma^1_1$: find arbitrarily large finite models, or an infinite descending chain, and apply compactness.
Watch out: the argument fails for full second-order logic, which has the classical negation of a $\Sigma^1_1$ sentence and so expresses finiteness.
