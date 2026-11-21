---
tag: RK7NK2P75J
kind: statement
role: theorem
name: Chang-Łoś-Suszko theorem
aliases: [chang-los-suszko-theorem, preservation-under-unions-of-chains]
msc: ["03C40", "03C52"]
topics: [JYJHB4YBAH]
audience: grad
about: [MEC3ZMC4F1, 92SWXST1ZM]
uses: [92SWXST1ZM, MVCH6N9SNW, 676H7EGTKJ, NHCRZ74JHH, DKFGQTRYZE, 0FRXBVVR03, 1NR3HAWG9D]
history:
  notes: Jerzy Łoś and Roman Suszko announced the theorem and later published it jointly. Chen Chung Chang gave a proof in his paper On unions of chains of models, Proceedings of the American Mathematical Society 10 (1959).
sources:
  - book: isbn:9780521587136
---

## Statement

Let $L$ be a signature, and let $T$ be an $L$-[[theory|92SWXST1ZM]].
A [[sentence|DKFGQTRYZE]] is $\forall\exists$ if it has the form $\forall \bar x \, \exists \bar y \, \theta(\bar x, \bar y)$ with $\theta$ quantifier-free; either block of quantifiers may be empty.
Let $T_{\forall\exists}$ be the set of $\forall\exists$ sentences that are consequences of $T$.
A *chain* is a family $(A_i)_{i \in I}$ of $L$-structures, indexed by a nonempty [[total order|0FRXBVVR03]] $I$, with $A_i$ a [[substructure|676H7EGTKJ]] of $A_j$ for $i < j$.
Its union is the structure of the [[elementary chain theorem|NHCRZ74JHH]].
The following are equivalent.

1. The union of every chain of [[models|MVCH6N9SNW]] of $T$ is a model of $T$.
2. The union of every chain $A_0 \subseteq A_1 \subseteq \cdots$ of models of $T$, indexed by $\mathbb{N}$, is a model of $T$.
3. $T_{\forall\exists}$ has the same models as $T$.

In particular, a sentence $\varphi$ is preserved by unions of chains if and only if it is logically equivalent to a $\forall\exists$ sentence.
A proof is in [[the proof of the Chang-Łoś-Suszko theorem|AWD4GAN9YP]].

## Remarks

### Why each hypothesis is needed

- The form $\forall\exists$ cannot be replaced by $\exists\forall$. The sentence $\exists x \, \forall y \, (y \le x)$, "there is a greatest element", holds in each finite order $\set{0, \dots, n}$ but fails in their union $\mathbb{N}$.
- The class must be elementary. The torsion abelian groups are closed under unions of chains, since each element lies in one member of the chain. They are not an elementary class, because an [[ultraproduct|AX9Q86GB8M]] of the groups $\mathbb{Z}/n\mathbb{Z}$ has elements of infinite order, so they have no $\forall\exists$ axioms.
- The well-orders show that closure can fail for a natural class: the finite orders $\set{-n, \dots, 0}$ of integers form a chain whose union has no least element.

### Consequences

- [[Model complete theories|YR6HCMABTE]] have $\forall\exists$ axioms. In a model complete theory every embedding between models is elementary, so a chain of models is an elementary chain, and its union is a model.
- The theories of fields, algebraically closed fields, divisible abelian groups and dense linear orders without endpoints have $\forall\exists$ axioms, as their usual axioms show; the theorem explains why their models are closed under unions of chains.
- The theory of linear orders with a greatest element has no $\forall\exists$ axioms, by the first example above.

### Converse

The implication from 3 to 1 is part 2 of the elementary chain theorem, and 1 gives 2 at once.
So the content is the step from 2 to 3.

### Generalizations

- Relative form: a formula is preserved by unions of chains of models of $T$ if and only if it is equivalent modulo $T$ to a $\forall\exists$ formula.
- Directed unions: one may replace chains by directed families of substructures, with the same conclusion.
- The [[Łoś-Tarski theorem|9RN0KYXNT1]] is the analogue one level lower, for substructures and universal sentences; see [[preservation theorems|T69D2NS1HP]].

## History

Jerzy Łoś and Roman Suszko announced the theorem and later published it jointly.
Chen Chung Chang published a proof in 1959, in his paper "On unions of chains of models".

## Explanations

### L1 human

A chain of structures is a sequence in which each structure sits inside the next one, like the sets $\set{0}$, $\set{0, 1}$, $\set{0, 1, 2}$ and so on.
Its union collects all the elements.
A rule of the form "for every element there is another one with a property" survives the union, because the witness for an element appears at some stage and stays.
The theorem says that rules of this "for all, there is" shape are exactly the first-order rules that always survive unions of chains.

### L2 human

We check that the theory of fields is preserved by unions of chains.

1. Let $K_0 \subseteq K_1 \subseteq \cdots$ be fields, each a subfield of the next, and let $K$ be the union.
2. The ring axioms are universal; a tuple of $K$ lies in some $K_n$, where the axiom holds. So $K$ satisfies them.
3. The axiom $\forall x \, (x \ne 0 \rightarrow \exists y \, (x y = 1))$ is $\forall\exists$. A nonzero $x \in K$ lies in some $K_n$, and its inverse in $K_n$ is an inverse in $K$.
4. So $K$ is a field. For example, the union of $\mathbb{Q}(\sqrt[2^n]{2})$ over $n$ is a field.

The typical use is negative: a class of models not closed under unions of chains has no $\forall\exists$ axioms.
A trap is to think that the models of a $\forall\exists$ theory are closed under intersections or substructures; the subring $\mathbb{Z}$ of $\mathbb{Q}$ shows they are not.

### L3 human

The proof of $2 \Rightarrow 3$ builds a sandwich chain $B = B_0 \subseteq A_0 \subseteq B_1 \subseteq A_1 \subseteq \cdots$, where the $A_n$ are models of $T$ and the $B_n$ form an elementary chain.
The union is a union of models of $T$ and an elementary extension of $B$ at once.
This technique, alternating models of a theory with elementary extensions, appears again in the proof of [[Lyndon's theorem|8DJSRWME2X]] and of Robinson's test for [[model completeness|YR6HCMABTE]].
In the arithmetic hierarchy of formulas, $\forall\exists$ is the level $\Pi_2$, and the theorem says that $\Pi_2$ is the semantic level of unions of chains.
Theories with $\forall\exists$ axioms are the setting of existentially closed models, which exist for every such theory by a chain construction.
