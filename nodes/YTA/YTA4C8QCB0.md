---
tag: YTA4C8QCB0
kind: concept
name: Magari algebra
aliases: [diagonalizable-algebra]
msc: ["03G25", "03F45"]
topics: [3E7M66WW6Q]
audience: research
uses: [0XADJKM699, WJK0YA4GP2, QC9M3Q8B8Q, HACXBCM7SS, NB2BCZR40F, F6H4STF9RG, 3HD30YG3DG]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_algebra
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: Examples
---

## Summary

A Magari algebra, or diagonalizable algebra, is a [[Boolean algebra|0XADJKM699]] $B$ with a unary operation $\square \colon B \to B$ that satisfies three laws for all $x, y \in B$.
The laws are $\square 1 = 1$, $\square(x \wedge y) = \square x \wedge \square y$ and $\square(\square x \to x) = \square x$, where $a \to b$ means $\neg a \vee b$.
The third law is the algebraic form of Löb's axiom of [[provability logic|WJK0YA4GP2]].
Magari algebras are the algebraic models of the logic $\mathsf{GL}$, in the same way as Boolean algebras are the algebraic models of classical propositional logic.

## Motivation

Take the sentences of [[Peano arithmetic|HACXBCM7SS]] $\mathsf{PA}$ and identify two sentences when $\mathsf{PA}$ proves that they are equivalent.
The classes form the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of $\mathsf{PA}$, which is a Boolean algebra.
The [[provability predicate|NB2BCZR40F]] gives one more operation on the classes: the class of $\varphi$ goes to the class of $\mathrm{Prov}_{\mathsf{PA}}(\ulcorner \varphi \urcorner)$.
The [[derivability conditions|F6H4STF9RG]] and the formalized form of [[Löb's theorem|3HD30YG3DG]] say exactly that this operation obeys the three laws above.
So a Magari algebra is the abstract form of "a Boolean algebra of sentences together with provability".
The abstract form lets us use the methods of algebra, such as quotients, representations and duality, for questions about provability.

## Notation

The operation is written $\square$ in this text.
Magari wrote $\tau$ for the operation, and some later papers keep this letter.
We write $\lozenge x$ for $\neg \square \neg x$, and $x \le y$ for $x \wedge y = x$.
The names "Magari algebra" and "diagonalizable algebra" mean the same structures.

## Remarks

### Examples

- The two-element Boolean algebra $\{0, 1\}$ with $\square x = 1$ for all $x$ is a Magari algebra; see [[the two-element Magari algebra|BB0SVFTESA]].
- The [[power set|00E0YZCERH]] algebra of a finite [[strict partial order|60FNZ35H6R]] $(W, R)$ with $\square X = \{w \in W : v \in X \text{ for every } v \text{ with } wRv\}$ is a Magari algebra; see [[the Magari algebra of a finite strict partial order|RWYEYCB7TD]].
- The Lindenbaum-Tarski algebra of $\mathsf{PA}$ with $\square[\varphi] = [\mathrm{Prov}_{\mathsf{PA}}(\ulcorner \varphi \urcorner)]$ is a Magari algebra, by the [[definition|PHWAN904PT]] and the derivability conditions.
- The Lindenbaum-Tarski algebra of $\mathsf{GL}$ itself is a Magari algebra, because $\mathsf{GL}$ proves the three laws as formulas.
- Every subalgebra of a Magari algebra that is closed under $\square$ is a Magari algebra, because the three laws are equations.

### Non-examples

- The two-element Boolean algebra with $\square x = x$ is not a Magari algebra, because the third law fails at $x = 0$; see [[the identity operator is not a Magari operator|F3YQMQHKYR]].
- The power set algebra of a one-point reflexive frame $W = \{w\}$, $wRw$, is not a Magari algebra; it is the same algebra as in the previous item, since $\square X = X$ there.
- The power set algebra of the infinite chain $(\mathbb{N}, <)$, with $\square X = \{n : m \in X \text{ for every } m > n\}$, is not a Magari algebra; at $X = \emptyset$ we get $\square(\square \emptyset \to \emptyset) = \mathbb{N}$ but $\square \emptyset = \emptyset$.
- An [[interior algebra|BDEX7HET71]] with $0 \ne 1$ is not a Magari algebra, because its operator satisfies $\square x \le x$, and this law forces a Magari algebra to have $0 = 1$.

The third non-example needs a short check.
Every $n$ has a successor $n + 1$, so $\square \emptyset = \emptyset$.
Then $\square \emptyset \to \emptyset = \mathbb{N} \cup \emptyset = \mathbb{N}$, and $\square \mathbb{N} = \mathbb{N}$.

### Basic properties

The proofs are in the [[definition|PHWAN904PT]].

1. The operation is monotone: $x \le y$ implies $\square x \le \square y$.
2. The third law is equivalent to the inequality $\square(\square x \to x) \le \square x$.
3. Every Magari algebra satisfies $\square x \le \square \square x$, the algebraic form of axiom 4 of modal logic.
4. Algebraic completeness: $\mathsf{GL} \vdash \varphi$ if and only if $\varphi$ takes the value $1$ in every Magari algebra under every assignment.
5. Fixed points: if $t(x)$ is a term in which $x$ occurs only inside $\square$, then $t$ has exactly one fixed point $d = t(d)$, by the [[de Jongh-Sambin fixed-point theorem|TDDX1NHG8D]].
6. The only Magari algebra with $\square x \le x$ for all $x$ is the one-element algebra: from $\square x \le x$ we get $\square x \to x = 1$, so $\square x = \square 1 = 1$ for all $x$, and then $1 = \square 0 \le 0$.

### History

Roberto Magari introduced these algebras in the 1970s, under the name "diagonalizable algebras".
The name refers to the diagonal lemma, which gives fixed points in the algebra of $\mathsf{PA}$.
The algebras became one of the standard semantics of provability logic, next to the Kripke semantics of $\mathsf{GL}$.

### Common errors

- Reading $\square$ as an interior operator: in a Magari algebra $\square x \le x$ fails in general, for example $\square 0 = 1$ in the two-element example.
- Forgetting that $\square \square x$ need not be equal to $\square x$: the law $\square x \le \square \square x$ holds, but the reverse inequality can fail, as in the three-element chain of [[the example|RWYEYCB7TD]].
- Writing the third law as $\square(x \to \square x) = \square x$ or as $\square x \to x = 1$; both are different laws, and the second one forces $0 = 1$.

## Explanations

### L1 human

Think of a list of statements about numbers, where some statements are equivalent to others.
Besides "and", "or" and "not", there is one more way to make a new statement: "this statement can be proved".
A Magari algebra keeps track of how "can be proved" behaves with "and", "or" and "not".
For example, "the statement $1 = 1$ can be proved" is true, and "both $A$ and $B$ can be proved" means the same as "$A$ and $B$ can be proved".
The third rule is Löb's rule: if one can prove "if $A$ is provable then $A$ is true", then one can already prove $A$.
The smallest example has two elements, "false" and "true", and there "can be proved" always gives "true".

### L2 human

We work through the Boolean algebra of subsets of $W = \{0, 1\}$ with $0 R 1$ and no other relation.

1. The successors are $R[0] = \{1\}$ and $R[1] = \emptyset$.
2. The rule $\square X = \{w : R[w] \subseteq X\}$ gives $\square \emptyset = \{1\}$, $\square \{0\} = \{1\}$, $\square \{1\} = \{0, 1\}$ and $\square W = W$.
3. The first law holds, since $\square W = W$.
4. The second law holds because $R[w] \subseteq X \cap Y$ if and only if $R[w] \subseteq X$ and $R[w] \subseteq Y$.
5. The third law at $X = \emptyset$: $\square \emptyset \to \emptyset = W \setminus \{1\} = \{0\}$, and $\square \{0\} = \{1\} = \square \emptyset$.
6. The third law at $X = \{0\}$: $\square \{0\} \to \{0\} = \{0\} \cup \{0\} = \{0\}$, so $\square(\square \{0\} \to \{0\}) = \square \{0\}$.
7. The third law at $X = \{1\}$ and at $X = W$: here $\square X = W$, so $\square X \to X = X$ and both sides equal $\square X$.

The typical use is a proof that a formula is not a theorem of $\mathsf{GL}$: find a Magari algebra and an assignment that gives the formula a value other than $1$.
In this algebra, $p \mapsto \emptyset$ gives $\square p \to p$ the value $W \setminus \{1\} = \{0\} \ne W$, so $\mathsf{GL} \nvdash \square p \to p$.
A trap: $\square$ is not an interior operator, since $\square x \le x$ fails; in this algebra $\square \emptyset = \{1\} \not\subseteq \emptyset$.

### L3 human

Magari algebras form a variety, the subvariety of modal algebras defined by the Löb equation, and this variety is the equivalent algebraic semantics of $\mathsf{GL}$.
By Jónsson-Tarski duality, a modal algebra corresponds to a descriptive general frame, and the Löb equation on finite algebras corresponds to finite strict partial orders; this is the algebraic side of the [[Kripke completeness of GL|1DMFNR7FZT]].
The Lindenbaum-Tarski algebra of $\mathsf{PA}$ is a single Magari algebra that contains all the information of [[Solovay's arithmetical completeness theorem|1ZRWVDYPX0]]: the equations that hold in it are exactly the theorems of $\mathsf{GL}$.
The same algebraic method applies to the provability algebras of Japaridze's polymodal logic and to the algebras of interpretability, where a binary operation joins $\square$; see [[interpretability logic|BGKZTSQN3W]].
