---
tag: Z82FS0BX8G
kind: example
name: Double negation and uniform substitution in inquisitive logic
msc: ["03B65", "03B20"]
topics: [CQM9SRN8PM]
audience: research
not_instance_of:
  - target: EX0ND8DCTN
    note: the substitution instance ¬¬?p → ?p of the valid formula ¬¬p → p is not valid in InqB, so InqB is not a substitution-closed logic
uses: [EX0ND8DCTN, Y9CNKCV26N]
sources:
  - url: https://en.wikipedia.org/wiki/Inquisitive_semantics
    locator: Basic notions
  - book: isbn:9780198814795
    locator: Ciardelli, Groenendijk and Roelofsen, Inquisitive Semantics
---

## Example

We show that $\neg\neg p \to p$ is valid in [[inquisitive logic|EX0ND8DCTN]] for an atom $p$, but its substitution instance $\neg\neg ?p \to ?p$ is not.

1. Let $s$ be any state, and let $t \subseteq s$ with $t \models \neg\neg p$.
2. The support $t \models \neg\neg p$ means that every world of $t$ makes $p$ true.
   So $t \models p$.
3. By the implication clause, $s \models \neg\neg p \to p$.
   Since $s$ was arbitrary, the formula is valid.
4. Now put $\varphi = ?p = p \vee \neg p$.
   Every world makes $p \vee \neg p$ true, so every state supports $\neg\neg ?p$.
5. The full state $W$ contains a world where $p$ is true and a world where $p$ is false.
   So $W \not\models ?p$, as [[the polar question|Y9CNKCV26N]] shows.
6. Take $t = W$ in the implication clause, where $W \models \neg\neg ?p$ and $W \not\models ?p$.
   So $W \not\models \neg\neg ?p \to ?p$.

So the valid formulas of $\mathsf{InqB}$ are not closed under uniform substitution.

## Remarks

The law $\neg\neg\varphi \to \varphi$ is valid exactly when $\varphi$ is a statement, a formula supported by its informative content.
Questions are the formulas for which it fails, so the failure of substitution is the price of having questions in the language.
The schematic fragment, the formulas all of whose instances are valid, is Medvedev's logic of finite problems.
It is closed under substitution and contains intuitionistic logic.
Classical propositional logic is not a sublogic of $\mathsf{InqB}$ in the schematic sense, because $\neg\neg\varphi \to \varphi$ and $\varphi \vee \neg\varphi$ fail for some $\varphi$.

## Explanations

### L1 human

"It is not the case that it is not raining" is the same information as "it is raining".
But "it is not the case that the question whether it rains has no answer" does not answer the question.
So a rule that is fine for statements fails for questions.
This is why inquisitive logic cannot freely substitute a question for a letter.

### L2 human

1. Test the atomic law on an arbitrary state.
   It holds because $\neg\neg p$ and $p$ have the same supporting states.
2. Replace $p$ by $?p$.
   The left side becomes valid, since $?p$ is true at every world.
3. The right side fails at the full state.

The typical use is to explain why $\mathsf{InqB}$ is axiomatized with $\neg\neg p \to p$ for atoms only.
Watch out: the logic is still closed under substitution of statements for atoms, and only questions break the law.
