---
tag: WK9J5ZTZGJ
kind: example
name: Every number has a larger one, in the natural numbers and in a finite order
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
instance_of: [K7XDVK5854]
uses: [71X7TB3F98, 1WTCZB4DVB, 983GZBQYT4, 0MWKJ44V5A]
sources:
  - book: isbn:9780122384523
    locator: Section 2.2
  - url: https://builds.openlogicproject.org/
    locator: Syntax and Semantics
---

## Example

Let $\sigma$ be the sentence $\forall x \, \exists y \, (x < y)$ in the signature $\{<\}$.
We show that $\sigma$ is [[true|71X7TB3F98]] in $\mathcal{N} = (\mathbb{N}, <)$ and false in $\mathcal{F} = (\{0, 1, 2\}, <)$, both with the usual order.

First, truth in $\mathcal{N}$:

1. Let $s$ be any assignment in $\mathcal{N}$.
   By the clause for $\forall x$ of [[satisfaction|1WTCZB4DVB]], we must show $\mathcal{N} \models \exists y \, (x < y)[s[x \mapsto n]]$ for every $n \in \mathbb{N}$.
2. Let $n \in \mathbb{N}$, and take the witness $n + 1$, which is again a natural number.
3. Under the assignment that sends $x$ to $n$ and $y$ to $n + 1$, the atomic formula $x < y$ is satisfied, because $n < n + 1$.
4. By the clause for $\exists y$, step 3 gives $\mathcal{N} \models \exists y \, (x < y)[s[x \mapsto n]]$.
5. Since $n$ and $s$ were arbitrary, $\mathcal{N} \models \sigma$.

Second, falsity in $\mathcal{F}$:

1. Let $s$ be any assignment in $\mathcal{F}$, and look at the variant $s[x \mapsto 2]$.
2. The candidates for $y$ are $0$, $1$ and $2$, and none of the pairs $(2, 0)$, $(2, 1)$, $(2, 2)$ lies in the order, because $2$ is not less than $0$, $1$ or $2$.
3. So $\mathcal{F} \not\models \exists y \, (x < y)[s[x \mapsto 2]]$, by the clause for $\exists y$.
4. By the clause for $\forall x$, $\mathcal{F} \not\models \sigma[s]$.
   Since $s$ was arbitrary, $\sigma$ is false in $\mathcal{F}$, and $\mathcal{F} \models \neg \sigma$.

## Remarks

The truth value of one sentence depends on the structure, so $\sigma \in \operatorname{Th}(\mathcal{N})$ while $\neg \sigma \in \operatorname{Th}(\mathcal{F})$.
The same argument shows more.
The sentence $\sigma$ is true in every linear order without a greatest element, such as $(\mathbb{Z}, <)$ and $(\mathbb{Q}, <)$.
It is false in every nonempty finite linear order, because the greatest element has nothing above it.

Swapping the quantifiers changes the meaning.
The sentence $\exists y \, \forall x \, (x < y)$ is false in both $\mathcal{N}$ and $\mathcal{F}$, because a witness $y$ would have to satisfy $y < y$.

## Explanations

### L1 human

The sentence says "for every number there is a bigger number".
For the numbers $0, 1, 2, 3, \ldots$ it is true, because the number after $n$ is bigger than $n$.
For the numbers $0, 1, 2$ only, it is false, because nothing in the list is bigger than $2$.
So the same sentence is true in one world and false in another.

### L2 human

We show that the swapped sentence $\exists y \, \forall x \, (x < y)$ is false in every structure in which $<$ is irreflexive.
Suppose some value $b$ of $y$ satisfies $\forall x \, (x < y)$.
Then the variant $x \mapsto b$ must satisfy $x < y$, which gives
$$b < b,$$
against irreflexivity, so no witness exists and the sentence is false.

The typical use of $\sigma$ is to separate finite and infinite linear orders by one sentence.
Watch out: $\forall x \, \exists y$ lets the witness $y$ depend on $x$, and $\exists y \, \forall x$ does not.
