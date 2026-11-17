---
tag: EQH7XTZ29V
kind: example
name: PA plus the consistency of PA is not conservative over PA
msc: ["03F40", "03F25"]
topics: [H8QZY0RZXZ]
audience: grad
not_instance_of:
  - target: N238J43XNE
    note: "PA + Con(PA) proves the arithmetic sentence Con(PA), which PA does not prove by the second incompleteness theorem."
uses: [N238J43XNE, 0QFT7Z76N5, 4PZM5GJTR5, MFJXPAF0R0, VM8TQ70CVJ]
sources:
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: Second incompleteness theorem
  - book: isbn:9780521857840
---

## Example

Let PA be [[Peano arithmetic|0QFT7Z76N5]], with a fixed [[Gödel numbering|MFJXPAF0R0]] of formulas and derivations.
Let $\mathrm{Con}(\mathsf{PA})$ be the arithmetic sentence "no number codes a derivation of $0 = 1$ from the axioms of PA".
Let $T' = \mathsf{PA} + \mathrm{Con}(\mathsf{PA})$, in the same language as PA.
We show that $T'$ is a consistent extension of PA that is not a [[conservative extension|N238J43XNE]].

1. $T'$ extends PA, since it contains all axioms of PA.
2. The natural numbers with the usual operations satisfy every axiom of PA. By soundness, PA does not prove $0 = 1$, so PA is [[consistent|VM8TQ70CVJ]].
3. The sentence $\mathrm{Con}(\mathsf{PA})$ expresses this fact under the Gödel numbering, so it is true in $\N$. So $\N$ is a model of $T'$, and $T'$ is consistent.
4. PA is consistent and computably axiomatized, so by [[Gödel's second incompleteness theorem|4PZM5GJTR5]], PA does not prove $\mathrm{Con}(\mathsf{PA})$.
5. $T'$ proves $\mathrm{Con}(\mathsf{PA})$, since it is an axiom of $T'$.
6. So $\mathrm{Con}(\mathsf{PA})$ is a sentence of the old language that $T'$ proves and PA does not prove. The condition of conservativity fails.

## Remarks

Here $L' = L$, so the failure has nothing to do with new symbols: the new axiom itself is a new arithmetic theorem.
The sentence $\mathrm{Con}(\mathsf{PA})$ is $\Pi^0_1$, so $T'$ is not even $\Pi^0_1$-conservative over PA.
The theory $\mathsf{PA} + \lnot\mathrm{Con}(\mathsf{PA})$ is also consistent, by step 4 and the [[consistency|VM8TQ70CVJ]] criterion "$T \nvdash \varphi$ exactly when $T \cup \set{\lnot\varphi}$ is consistent".
It is also not conservative, and it is false in $\N$.
So neither truth nor falsity of the new axiom decides conservativity; only provability in the old theory does.
The same argument works for every consistent, computably axiomatized theory $T \supseteq \mathsf{PA}$ and the extension $T + \mathrm{Con}(T)$.

## Explanations

### L1 human

Peano arithmetic is a list of basic laws about whole numbers.
The statement "these laws never lead to a contradiction" can be written as a statement about numbers, by coding proofs as numbers.
Gödel showed that the laws themselves cannot prove this statement.
If we add it as a new law, we get a stronger list that proves a new fact about numbers.
So the addition is not conservative, although the new law is true.

### L2 human

We compare three theories in the language of arithmetic.

1. PA proves $2 + 2 = 4$, and so do the two theories below; no difference appears here.
2. $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$ proves $\mathrm{Con}(\mathsf{PA})$; PA does not, by step 4.
3. $\mathsf{PA} + \lnot\mathrm{Con}(\mathsf{PA})$ proves $\lnot\mathrm{Con}(\mathsf{PA})$; PA does not, because PA is true in $\N$ and $\lnot\mathrm{Con}(\mathsf{PA})$ is false there.

The typical use is as a test: an extension by a statement independent of the old theory is never conservative.
A trap is to argue that $\mathrm{Con}(\mathsf{PA})$ "says nothing new" because it is about PA rather than about numbers; under the Gödel numbering it is an ordinary arithmetic sentence.
