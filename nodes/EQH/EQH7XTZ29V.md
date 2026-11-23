---
tag: EQH7XTZ29V
kind: example
name: PA plus the consistency of PA is not conservative over PA
msc: ["03F40", "03F25"]
topics: [H8QZY0RZXZ, 8XY7JYZKFW]
audience: grad
not_instance_of:
  - target: N238J43XNE
    note: "PA + Con(PA) proves the arithmetic sentence Con(PA), which PA does not prove by the second incompleteness theorem."
  - target: TNZ995J8AP
    note: "PA + Con(PA) is not even Pi-0-1-conservative over PA, since Con(PA) is a Pi-0-1 sentence."
uses: [N238J43XNE, 0QFT7Z76N5, 4PZM5GJTR5, MFJXPAF0R0, VM8TQ70CVJ]
sources:
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: Second incompleteness theorem
  - book: isbn:9780521857840
---

## Example

Adding a true axiom to a theory can still produce new theorems in the old language.
The standard example adds to Peano arithmetic the statement that Peano arithmetic is consistent.

Let PA be [[Peano arithmetic|0QFT7Z76N5]], with a fixed [[Gödel numbering|MFJXPAF0R0]] of formulas and derivations.
Let $\mathrm{Con}(\mathsf{PA})$ be the arithmetic sentence "no number codes a derivation of $0 = 1$ from the axioms of PA", and let $T' = \mathsf{PA} + \mathrm{Con}(\mathsf{PA})$, in the same language as PA.
We show that $T'$ is a consistent extension of PA that is not a [[conservative extension|N238J43XNE]].

1. $T'$ extends PA, since it contains every axiom of PA.
2. The natural numbers with the usual operations satisfy every axiom of PA.
   By soundness PA does not prove $0 = 1$, so PA is [[consistent|VM8TQ70CVJ]].
3. Under the Gödel numbering, $\mathrm{Con}(\mathsf{PA})$ expresses the fact of step 2, so it is true in $\mathbb{N}$.
   Hence $\mathbb{N}$ is a model of $T'$, and $T'$ is consistent.
4. PA is consistent and has a decidable set of axioms, so by [[Gödel's second incompleteness theorem|4PZM5GJTR5]] PA does not prove $\mathrm{Con}(\mathsf{PA})$.
5. $T'$ proves $\mathrm{Con}(\mathsf{PA})$, since it is an axiom of $T'$.
6. So $\mathrm{Con}(\mathsf{PA})$ is a sentence of the old language that $T'$ proves and PA does not, and conservativity fails.

## Remarks

### No new symbols are needed

Here the new language equals the old one, so the failure has nothing to do with new symbols: the new axiom is itself a new arithmetic theorem.
The sentence $\mathrm{Con}(\mathsf{PA})$ has the form $\forall x\, \theta(x)$ with $\theta$ decidable, a $\Pi^0_1$ sentence, so $T'$ is not even $\Pi^0_1$-conservative over PA.

### Truth does not decide it

The theory $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is also consistent.
By step 4 PA does not prove $\mathrm{Con}(\mathsf{PA})$, and a theory $T$ fails to prove $\varphi$ exactly when $T \cup \{ \neg \varphi \}$ is consistent.
This theory is not conservative either, and its new axiom is false in $\mathbb{N}$.
So neither the truth nor the falsity of the new axiom decides conservativity; only provability in the old theory does.
The same argument works for every consistent theory $T \supseteq \mathsf{PA}$ with a decidable set of axioms and its extension $T + \mathrm{Con}(T)$.

## Explanations

### L1 human

Peano arithmetic is a list of basic laws about whole numbers.
The statement "these laws never lead to a contradiction" can be written as a statement about numbers, by coding proofs as numbers.
Gödel showed that the laws themselves cannot prove this statement.
If you add it as a new law, you get a stronger list that proves a new fact about numbers.
So the addition is not conservative, although the new law is true.

### L2 human

Compare three theories in the language of arithmetic.
All three prove $2 + 2 = 4$, so no difference appears on simple facts.
$\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$ proves $\mathrm{Con}(\mathsf{PA})$, and PA does not, by step 4.
$\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ proves $\neg \mathrm{Con}(\mathsf{PA})$, and PA does not, because PA is true in $\mathbb{N}$ and $\neg \mathrm{Con}(\mathsf{PA})$ is false there.
The typical use is as a test: an extension by a sentence of the old language that the old theory does not prove is never conservative.
Watch out for the argument that $\mathrm{Con}(\mathsf{PA})$ "says nothing new" because it is about PA rather than about numbers; under the Gödel numbering it is an ordinary arithmetic sentence.
