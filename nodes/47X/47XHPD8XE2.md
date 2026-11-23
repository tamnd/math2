---
tag: 47XHPD8XE2
kind: definition
name: Second-order logic
msc: ["03B16", "03C85"]
topics: [MDHDYV8QZW]
defines: G6X7SZSNC5
uses: [086QKPF0A6, 983GZBQYT4, 00E0YZCERH]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_logic
---

## Definition

Let $L$ be a signature.
The formulas of second-order logic over $L$ are built like the formulas of [[first-order logic|086QKPF0A6]] over $L$, with two additions.

1. For each $n \ge 1$ there are relation variables $X, Y, \ldots$ of arity $n$, and $X(t_1, \ldots, t_n)$ is an atomic formula for terms $t_1, \ldots, t_n$.
2. If $\varphi$ is a formula and $X$ is a relation variable, then $\forall X \, \varphi$ and $\exists X \, \varphi$ are formulas.

In the standard semantics, a formula is evaluated in an $L$-[[structure|983GZBQYT4]] $\mathcal{M}$ with domain $M$.
The clauses of first-order logic apply, with three more clauses.
An assignment sends each $n$-ary relation variable to a subset of $M^n$.
The atomic formula $X(t_1, \ldots, t_n)$ is true when the tuple of the values of $t_1, \ldots, t_n$ belongs to the value of $X$.
The formula $\forall X \, \varphi$ is true when $\varphi$ is true for every value of $X$ in the [[power set|00E0YZCERH]] $\mathcal{P}(M^n)$.
The formula $\exists X \, \varphi$ is true when $\varphi$ is true for some value of $X$ in $\mathcal{P}(M^n)$.

## Remarks

### A first sentence

Over the signature $\set{0, S}$, here is a second-order sentence:
$$\forall X \, \big( (X(0) \land \forall x \, (X(x) \to X(S(x)))) \to \forall x \, X(x) \big).$$
It says that every subset of the domain that contains $0$ and is closed under $S$ is the whole domain.
In $(\mathbb{N}, 0, n \mapsto n + 1)$ it is true, because this is the principle of induction.
In the structure with domain $\mathbb{N} \cup \set{\infty}$ and $S(\infty) = \infty$ it is false.
Take $X = \mathbb{N}$: it contains $0$ and is closed under $S$, but it does not contain $\infty$.

### What is allowed and what is not

Function variables can be added in the same way.
They add no power, because a function variable can be replaced by a relation variable for its graph.
Monadic second-order logic allows only relation variables of arity $1$, that is, variables for subsets of $M$.

A formula with a quantifier over sets of subsets of $M$ is not second-order.
No clause of the definition gives such variables, and they belong to third-order logic.

### Two semantics

With the standard semantics, second-order logic has no complete effective proof system, and it does not have the compactness property.
With the [[Henkin semantics|KWEJFK5943]], the relation variables range over a chosen family of relations, and both properties return.
So a claim about "second-order logic" must say which semantics it uses.

## Explanations

### L1 human

First-order logic can say "for every element".
Second-order logic can also say "for every set of elements" and "for every relation between elements".
This makes it much more expressive.
For example, "the domain is finite" and "every bounded set of reals has a least upper bound" are each one second-order sentence.
No single first-order sentence, and no set of first-order sentences, can say either of them.
