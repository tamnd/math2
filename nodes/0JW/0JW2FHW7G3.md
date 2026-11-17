---
tag: 0JW2FHW7G3
kind: definition
name: Existential quantifier
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
defines: 0MSRQHCNN9
uses: [0T3DPBG981, 0ZGC7ZESYN, 025YZN3VJW]
sources:
  - url: https://en.wikipedia.org/wiki/Existential_quantification
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.1
  - book: isbn:9781108439534
    locator: Section 2.2
---

## Definition

Let $D$ be a set, the domain of discourse, and let $P(x)$ be a [[predicate|0T3DPBG981]] on $D$.
The existential quantification of $P$ over $D$ is the [[proposition|0ZGC7ZESYN]] $\exists x \, P(x)$, read "there exists $x$ such that $P(x)$".

1. $\exists x \, P(x)$ is true when $P(a)$ is true for at least one $a \in D$.
2. $\exists x \, P(x)$ is false when $P(a)$ is false for every $a \in D$.

An element $a \in D$ with $P(a)$ true is called a witness.
The variable $x$ is bound by the quantifier $\exists x$.
If $P$ has further free variables, as in $P(x, y)$, then $\exists x \, P(x, y)$ is a predicate in $y$, and its value at $b \in D$ is $\exists x \, P(x, b)$.
For a subset $A \subseteq D$, the restricted existential quantification is the abbreviation
$$\exists x \in A \; P(x) \quad :\Longleftrightarrow \quad \exists x \, (x \in A \land P(x)),$$
where $\land$ is the [[conjunction|025YZN3VJW]].

## Notation

Other forms are $\exists x \colon P(x)$, $\exists x, \, P(x)$ and $(\exists x) \, P(x)$; in English, "there is $x$ with $P(x)$" and "$P(x)$ for some $x$".
The restricted form is also written $(\exists x \in A) \, P(x)$, and conditions other than membership are used in the same way: $\exists \delta > 0 \; P(\delta)$ means $\exists \delta \, (\delta > 0 \land P(\delta))$.

## Remarks

When $A = \varnothing$, the statement $\exists x \in A \; P(x)$ is false for each $P$, because each instance of $x \in A \land P(x)$ has a false first conjunct.
For a finite domain $D = \{a_1, \dots, a_n\}$, the statement $\exists x \, P(x)$ is equivalent to $P(a_1) \lor \dots \lor P(a_n)$.
The definition asks for at least one witness and allows more; the [[uniqueness quantifier|0QAJHFGZZJ]] $\exists!$ asks for exactly one.
The restricted universal quantifier uses $\to$, while the restricted existential quantifier uses $\land$; with these choices, $\neg \exists x \in A \; P(x)$ is equivalent to $\forall x \in A \; \neg P(x)$.
The concept page [[existential quantifier|0MSRQHCNN9]] gives the examples, the non-examples, the first properties and the methods of proof.

## Explanations

### L1 human

"There is $x$ in a set with $P(x)$" says that at least one member of the set passes the test $P$.
One member that passes is enough, and it is called a witness.
For example, "some number in $\{3, 5, 8\}$ is even" is true, with the witness $8$, and "some number in $\{3, 5, 7\}$ is even" is false, because none of them is even.

### L2 human

We unfold $\exists x \in \mathbb{Z} \; (x^2 = 2x)$ with the definition, on the domain $D = \mathbb{R}$.

1. By the definition of the restricted form, the statement is $\exists x \, (x \in \mathbb{Z} \land x^2 = 2x)$.
2. Try $x = 2$: $2 \in \mathbb{Z}$ is true, and $2^2 = 4 = 2 \cdot 2$ is true, so the conjunction is true.
3. So $x = 2$ is a witness, and the statement is true. The integer $x = 0$ is a second witness.

A trap is to check only the predicate: for $\exists x \in \mathbb{Z} \; (x^2 = 2)$, the real number $\sqrt{2}$ satisfies $x^2 = 2$ but is not an integer, so it is not a witness, and the statement is false.
