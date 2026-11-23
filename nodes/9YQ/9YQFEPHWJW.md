---
tag: 9YQFEPHWJW
kind: example
name: True arithmetic is negation complete
msc: ["03F40", "03C62"]
topics: [HXHHWY3328]
audience: grad
instance_of: [319P85G2C1]
uses: [319P85G2C1, WP27CABPA4, DKFGQTRYZE, 69TTX21TRJ, 3K1AKGXF8A]
sources:
  - url: https://en.wikipedia.org/wiki/True_arithmetic
    locator: lead section
  - book: isbn:9780521857840
---

## Example

Let $\mathrm{Th}(\mathbb{N})$ be the set of all [[sentences|DKFGQTRYZE]] of the language $\{ 0, S, +, \cdot \}$ that are true in the [[standard model|WP27CABPA4]] $\mathbb{N}$.
For example, $S0 + S0 = SS0$ is in it, and so is $\forall x \, (0 + x = x)$, but $\exists x \, (x + x = S0)$ is not, since $1$ is odd.
We use $\mathrm{Th}(\mathbb{N})$ as a set of axioms and check that it is [[negation complete|319P85G2C1]], consistent, and contains [[Robinson arithmetic|3K1AKGXF8A]].

1. Let $\varphi$ be any sentence.
   In $\mathbb{N}$ exactly one of $\varphi$ and $\neg \varphi$ is true, by the definition of satisfaction for $\neg$.
2. If $\varphi$ is true, then $\varphi$ is an axiom, and $\mathrm{Th}(\mathbb{N}) \vdash \varphi$ by a proof of one line.
3. If $\neg \varphi$ is true, then $\neg \varphi$ is an axiom, and $\mathrm{Th}(\mathbb{N}) \vdash \neg \varphi$ in the same way.
4. So $\mathrm{Th}(\mathbb{N})$ is negation complete.
5. It is consistent, because $\mathbb{N}$ is a model of it.
6. It contains the axioms of $\mathsf{Q}$, because they are true in $\mathbb{N}$.

## Remarks

The theorems of $\mathrm{Th}(\mathbb{N})$ are exactly its axioms, since a sentence that follows from true sentences is true.
The same three lines show that the theory of any structure is negation complete.

Why does this not contradict the [[first incompleteness theorem|X9WYNYE29C]]?
The theorem applies only to theories whose axioms can be checked by a program, and $\mathrm{Th}(\mathbb{N})$ fails this condition: it [[has no decidable axiom set|69TTX21TRJ]].
So the example is the extreme case that shows why the hypothesis of decidable axioms is needed.
Completeness is cheap when every truth is an axiom; the content of Gödel's theorem is that you cannot have both completeness and checkable axioms.

## Explanations

### L1 human

Take as axioms all true statements about whole numbers.
Every statement is true or false, so the statement or its negation is on the list.
This list settles every question at once.
But no computer can print the list, so nobody can use it to check a proof.

### L2 human

The argument is short because each sentence decides itself: the true one of $\varphi$ and $\neg \varphi$ is an axiom.
Compare it with $\mathsf{PA}$, whose axioms a program can list.
Every axiom of $\mathsf{PA}$ is true, so $\mathsf{PA}$ is contained in $\mathrm{Th}(\mathbb{N})$, but the Gödel sentence of $\mathsf{PA}$ lies in $\mathrm{Th}(\mathbb{N})$ and not among the theorems of $\mathsf{PA}$.
The typical use of the example is as a test case for the hypotheses of incompleteness results.
Watch out: "complete" here does not mean that we know the answers; it means only that the answers are, by definition, in the set.
