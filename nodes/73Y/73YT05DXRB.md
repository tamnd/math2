---
tag: 73YT05DXRB
kind: example
name: The integers with their order have no least element
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
not_instance_of:
  - target: 2RBQPV02AS
    note: no assignment satisfies the formula, because the clause for the existential quantifier finds no witness
uses: [1WTCZB4DVB, 983GZBQYT4, 0C4JS9RF5M]
sources:
  - book: isbn:9780122384523
    locator: Section 2.2
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Evaluation of truth values
---

## Example

Let $\mathcal{Z} = (\mathbb{Z}, <)$ be the [[structure|983GZBQYT4]] of the [[integers|0C4JS9RF5M]] with the usual strict order.
Let $\sigma$ be the sentence $\exists x \, \forall y \, (x < y \vee x = y)$, which says "there is a least element".
We show that $\mathcal{Z} \not\models \sigma[s]$ for every assignment $s$, by the clauses of [[satisfaction|1WTCZB4DVB]].

1. Let $s$ be any assignment.
   By the clause for $\exists x$, $\mathcal{Z} \models \sigma[s]$ holds only if some $a \in \mathbb{Z}$ gives $\mathcal{Z} \models \forall y \, (x < y \vee x = y)[s[x \mapsto a]]$.
2. Let $a \in \mathbb{Z}$ be any candidate.
   By the clause for $\forall y$, it works only if every $b \in \mathbb{Z}$ satisfies the disjunction under the assignment that sends $x$ to $a$ and $y$ to $b$.
3. Take $b = a - 1$, which is an integer.
   Then $a < a - 1$ is false, so the first disjunct fails.
4. Also $a = a - 1$ is false, so the second disjunct fails, and by the clause for $\vee$ the disjunction fails at $b = a - 1$.
5. So no candidate $a$ works, and by step 1, $\mathcal{Z} \not\models \sigma[s]$.

The sentence fails under every assignment, so no assignment satisfies $\sigma$ in $\mathcal{Z}$.

## Remarks

To show that an existential clause fails, we must refute every candidate, not just a few.
Here one rule, $b = a - 1$, refutes all candidates at once.

The answer changes with the structure.
In $(\mathbb{N}, <)$ the sentence $\sigma$ is satisfied with the witness $x \mapsto 0$, because $0 < b$ or $0 = b$ for every natural number $b$.
If we interpret $<$ on $\mathbb{Z}$ as "greater than", then $\sigma$ says "there is a greatest integer", and it fails for the same reason with $b = a + 1$.
In $\mathcal{Z}$ itself, the negation $\neg \sigma$ is satisfied by every assignment, by the clause for $\neg$.

## Explanations

### L1 human

The sentence says "some integer is smaller than or equal to all integers".
Whatever integer we pick, the integer one below it is smaller.
So no integer can be the smallest, and the sentence is false.
For the numbers $0, 1, 2, \ldots$ the same sentence is true, because $0$ is the smallest.

### L2 human

We contrast this with $(\mathbb{N}, <)$.
Take the witness $a = 0$ for $\exists x$.
For each $b \in \mathbb{N}$, either $b = 0$, and then the disjunct $x = y$ holds, or $b \geq 1$, and then the disjunct $x < y$ holds, since $0 < b$.
So the disjunction holds for every $b$, and $\sigma$ is true in $(\mathbb{N}, <)$.

The typical use is to separate two structures by a sentence.
Since $\sigma$ is true in $(\mathbb{N}, <)$ and false in $(\mathbb{Z}, <)$, these two orders are not isomorphic.
Watch out: checking a few candidates such as $a = 0$ and $a = -100$ proves nothing, and the argument must work for an arbitrary integer $a$.
