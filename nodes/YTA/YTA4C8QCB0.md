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

A Magari algebra is a Boolean algebra of statements with one extra operation, read as "it is provable that".
The operation obeys three equations, and the third one is Löb's theorem written as algebra.

Precisely, a Magari algebra, or diagonalizable algebra, is a [[Boolean algebra|0XADJKM699]] $B$ with a map $\square \colon B \to B$ that satisfies three laws for all $x, y \in B$.
Writing $a \to b$ for $\neg a \vee b$, the laws are the following.
$$\square 1 = 1, \qquad \square(x \wedge y) = \square x \wedge \square y, \qquad \square(\square x \to x) = \square x.$$
The [[formal definition|PHWAN904PT]] states these laws and proves their first consequences.
Magari algebras are to the logic $\mathsf{GL}$ of [[provability logic|WJK0YA4GP2]] what Boolean algebras are to classical propositional logic.

## Motivation

Take the sentences of [[Peano arithmetic|HACXBCM7SS]] $\mathsf{PA}$ and identify two sentences when $\mathsf{PA}$ proves them equivalent.
The classes form the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of $\mathsf{PA}$, which is a Boolean algebra.
The [[provability predicate|NB2BCZR40F]] gives one more operation on the classes, sending the class of $\varphi$ to the class of $\mathrm{Prov}_{\mathsf{PA}}(\ulcorner \varphi \urcorner)$.

The [[derivability conditions|F6H4STF9RG]] give the first two laws for this operation.
The formalized form of [[Löb's theorem|3HD30YG3DG]] gives the third.
So a Magari algebra is what remains of "sentences together with provability" once we forget which sentences they are.
In this abstract form we can use the tools of algebra, such as subalgebras, quotients and duality, on questions about provability.

## Notation

We write $\square$ for the operation, although Magari wrote $\tau$ and some later papers keep his letter.
We write $\lozenge x$ for $\neg \square \neg x$ and $x \le y$ for $x \wedge y = x$.
The names "Magari algebra" and "diagonalizable algebra" mean the same structures.

## Remarks

### A first computation

Take $W = \{0, 1\}$ with one arrow $0 R 1$, and let $\square X$ be the set of points all of whose successors lie in $X$.
Point $1$ has no successors, so it lies in every $\square X$.
Point $0$ lies in $\square X$ exactly when $1 \in X$.
This gives the table of the operation on the four subsets of $W$.
$$\square \emptyset = \{1\}, \qquad \square \{0\} = \{1\}, \qquad \square \{1\} = W, \qquad \square W = W.$$
Check: $0 \in \square \{1\}$ because the only successor of $0$ is $1$.

The first law is the entry $\square W = W$.
The second holds because "all successors lie in $X \cap Y$" means "all successors lie in $X$ and all lie in $Y$".
For the Löb law at $X = \emptyset$, first $\square \emptyset \to \emptyset = W \setminus \{1\} = \{0\}$.
Then $\square \{0\} = \{1\} = \square \emptyset$, as the law demands.
The other three subsets work the same way, and [[the Magari algebra of a finite strict partial order|RWYEYCB7TD]] does the general case.

### Algebras that are Magari algebras

The smallest example is the two-element Boolean algebra with $\square x = 1$ for both $x$; see [[the two-element Magari algebra|BB0SVFTESA]].
It is the frame computation above for a single point with no arrows.
Every finite irreflexive transitive frame gives a Magari algebra on its subsets in the same way.

The Lindenbaum-Tarski algebra of $\mathsf{PA}$, with $\square[\varphi] = [\mathrm{Prov}_{\mathsf{PA}}(\ulcorner \varphi \urcorner)]$, is a Magari algebra by the argument of the Motivation.
The Lindenbaum-Tarski algebra of $\mathsf{GL}$ is one as well, because $\mathsf{GL}$ proves the three laws as formulas.
Every subset of a Magari algebra that is closed under the operations is again a Magari algebra, because the three laws are equations.

### Algebras that are not

The two-element Boolean algebra with $\square x = x$ fails the Löb law at $x = 0$.
There $\square(\square 0 \to 0) = \square 1 = 1$ but $\square 0 = 0$; see [[the identity operator is not a Magari operator|F3YQMQHKYR]].
It is the frame algebra of one point that sees itself.

The subsets of the infinite chain $(\mathbb{N}, <)$, with $\square X = \{n : m \in X \text{ for all } m > n\}$, fail the Löb law at $X = \emptyset$.
Every $n$ has the successor $n + 1$, so $\square \emptyset = \emptyset$.
Then $\square \emptyset \to \emptyset = \mathbb{N}$ and $\square \mathbb{N} = \mathbb{N}$, which is not $\square \emptyset$.

An [[interior algebra|BDEX7HET71]] with $0 \ne 1$ is never a Magari algebra, because its operator satisfies $\square x \le x$, and the Watch out below shows that this law forces $0 = 1$.

### First properties

The operation is monotone: $x \le y$ gives $\square x \le \square y$, by the second law applied to $x = x \wedge y$.
Given the first two laws, the Löb law is equivalent to the inequality $\square(\square x \to x) \le \square x$.
Every Magari algebra satisfies $\square x \le \square \square x$, the algebraic form of axiom 4 of modal logic.
The [[definition|PHWAN904PT]] proves all three facts.

Two deeper facts tie the algebras to logic.
The first is algebraic completeness: $\mathsf{GL} \vdash \varphi$ exactly when $\varphi$ takes the value $1$ in every Magari algebra under every assignment.
The second is about fixed points.
If $x$ occurs in a term $t(x)$ only inside $\square$, then there is exactly one $d$ with $d = t(d)$.
This is the algebraic form of the [[de Jongh-Sambin fixed-point theorem|TDDX1NHG8D]].

### History

Roberto Magari introduced these algebras in the 1970s under the name "diagonalizable algebras".
The name refers to the diagonal lemma, which produces fixed points in the algebra of $\mathsf{PA}$.

### Watch out

The operation is not an interior operator, so $\square x \le x$ is false in general.
In the two-element example $\square 0 = 1$, and $1 \not\le 0$.

In fact $\square x \le x$ for all $x$ forces the algebra to be trivial.
Take $x = 0$: then $\square 0 \le 0$, so $\square 0 = 0$.
The Löb law at $0$ reads $\square(\square 0 \to 0) = \square 0$.
Its left side is $\square(\neg 0) = \square 1 = 1$ and its right side is $0$, so $1 = 0$.

A related slip is to write the Löb law as $\square x \to x = 1$.
That is the inequality $\square x \le x$ again, so it has the same fatal effect.
The law is an equation between two boxed elements, not a claim that $\square x \to x$ is the top.

### Try it

First, in the two-point algebra of the first computation, compute $\square \square \emptyset$ and compare it with $\square \emptyset$.
The answer is $\square \{1\} = W$, which differs from $\square \emptyset = \{1\}$, so the operation is not idempotent.

Second, show that every Magari algebra satisfies $\square(\neg \square 0) = \square 0$.
Put $x = 0$ in the Löb law and use $\square 0 \to 0 = \neg \square 0$.
In the algebra of $\mathsf{PA}$ this says that $\mathsf{PA}$ proves its own consistency only if it proves $0 = 1$, which is the formalized second incompleteness theorem.

Third, does $\square x = 0$ for all $x$ make $\{0, 1\}$ a Magari algebra?
No, since the first law fails: $\square 1 = 0$.

## Explanations

### L1 human

Think of a list of statements about numbers, where we count two statements as the same if they are provably equivalent.
Besides "and", "or" and "not", there is one more way to make a new statement: "this statement can be proved".
A Magari algebra keeps track of how "can be proved" behaves with the other three.
"The statement $1 = 1$ can be proved" is always true.
"$A$ and $B$ can both be proved" means the same as "the statement '$A$ and $B$' can be proved".
The third rule is Löb's rule: if one can prove "if $A$ is provable, then $A$ is true", then one can already prove $A$.

### L2 human

The typical use is to show that a formula is not a theorem of $\mathsf{GL}$.
By algebraic completeness it is enough to find one Magari algebra and one assignment that gives the formula a value other than $1$.

Take the two-point algebra of the first computation and the formula $\square p \to p$.

1. Assign $p \mapsto \emptyset$.
2. Then $\square p$ has the value $\square \emptyset = \{1\}$.
3. So $\square p \to p$ has the value $(W \setminus \{1\}) \cup \emptyset = \{0\}$.
4. This is not $W$, so $\mathsf{GL} \nvdash \square p \to p$.

The trap is to expect $\square p \to p$ to hold because provable things "should be true".
In the algebra $\square \emptyset = \{1\}$ is not contained in $\emptyset$, and the same gap exists in arithmetic, where $\mathsf{PA}$ does not prove that provable sentences are true.

### L3 human

Magari algebras form a variety, the subvariety of modal algebras cut out by the Löb equation, and this variety is the equivalent algebraic semantics of $\mathsf{GL}$.
Under Jónsson-Tarski duality the finite Magari algebras are exactly the subset algebras of finite strict partial orders, which is the algebraic side of the [[Kripke completeness of GL|1DMFNR7FZT]].
The single algebra of $\mathsf{PA}$ already carries [[Solovay's arithmetical completeness theorem|1ZRWVDYPX0]]: the equations that hold in it are exactly the theorems of $\mathsf{GL}$.
The same method extends to provability algebras with several operators, as for [[Japaridze's polymodal logic|3EDRQJJHMT]], and to algebras with a binary operator for [[interpretability|BGKZTSQN3W]].
