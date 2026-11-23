---
tag: 6KBJX91N7G
kind: statement
role: theorem
name: Unique readability theorem
aliases: [unique-parsing-theorem, unique-readability-lemma]
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
about: [TT7WT5HPN9]
uses: [TFDYXS3K1N]
proofs: [68PGHXRTPQ]
sources:
  - url: https://en.wikipedia.org/wiki/Well-formed_formula
    locator: Propositional calculus
  - url: https://en.wikipedia.org/wiki/Polish_notation
    locator: Polish notation for logic
  - book: isbn:9780122384523
    locator: Chapter 1
  - book: isbn:9781447145578
    locator: Chapter 1
---

## Statement

Every propositional formula can be read in exactly one way: its last building step, its main connective and its immediate parts are fixed by the string.

Let $P$ be a set of variables, and let $\mathrm{Form}$ be the set of [[propositional formulas|TT7WT5HPN9]] over $P$, as in the [[definition|TFDYXS3K1N]].
Each formula $\varphi \in \mathrm{Form}$ has exactly one of the following three forms:

1. $\varphi$ is a variable $p \in P$;
2. $\varphi = (\neg \psi)$ for a formula $\psi$;
3. $\varphi = (\psi \circ \chi)$ for formulas $\psi$, $\chi$ and a binary connective $\circ \in \{ \land, \lor, \to, \leftrightarrow \}$.

In addition, in form 2 the formula $\psi$ is unique, and in form 3 the connective $\circ$ and the formulas $\psi$ and $\chi$ are unique.

## Remarks

### A first reading

Take $\varphi = ((p \to q) \land (\neg p))$.
It starts with a left bracket followed by a left bracket, not by $\neg$, so it has form 3.
Remove the outer brackets and count open brackets from the left:
$$(p \to q) \land (\neg p) \qquad \text{the count returns to } 0 \text{ after } (p \to q).$$
So $\psi = (p \to q)$, the connective is $\land$, and $\chi = (\neg p)$.
The theorem says that no other split works: no shorter or longer initial piece of $(p \to q) \land (\neg p)$ is a formula followed by a connective and a formula.
The [[proof by counting brackets|68PGHXRTPQ]] shows why: a nonempty proper initial segment of a formula always has more left than right brackets, so it is never a formula itself.

### Why recursion needs the theorem

A definition by recursion has one clause for each formation rule.
For a [[truth valuation|H31CS3HK5P]] one clause is $\bar v((\varphi \land \psi)) = \min(\bar v(\varphi), \bar v(\psi))$.
If one string could be written both as $(\varphi \land \psi)$ and as $(\varphi' \lor \psi')$, the clauses could give it two different values, and they would define a relation, not a function.
The theorem rules this out, so the clauses define exactly one function on $\mathrm{Form}$.

In general, let $A$ be a set, $g \colon P \to A$, $h_\neg \colon A \to A$, and $h_\circ \colon A \times A \to A$ for each binary connective $\circ$.
Then exactly one $F \colon \mathrm{Form} \to A$ extends $g$ and satisfies
$$F((\neg \varphi)) = h_\neg(F(\varphi)), \qquad F((\varphi \circ \psi)) = h_\circ(F(\varphi), F(\psi)).$$
Truth values, subformulas, the set of variables, depth and the parse tree are all defined this way.

### Why the brackets are needed

The hypothesis hidden in the theorem is the shape of the formation rules: each connective comes with its own pair of brackets.
Without brackets, the string $p \land q \lor r$ can be built as $(p \land q) \lor r$ and as $p \land (q \lor r)$.
At $p = 0$ and $r = 1$ the first reading has the value $(0 \land q) \lor 1 = 1$ and the second has the value $0 \land (q \lor 1) = 0$.
So the string would have no well-defined truth value.

The theorem also needs the variables, connectives and brackets to be distinct single symbols.
If some variable were written as the string $(\neg p)$, that string would have forms 1 and 2 at once.

### The converse and the variants

The converse is part of the definition: every string of forms 1 to 3, with $\psi$ and $\chi$ formulas, is a formula by the formation rules.

The theorem survives several changes of notation.
It holds when negation is written $\neg \varphi$ without brackets, since the symbol $\neg$ in first place already marks form 2.
It holds in Polish notation, with weights in place of brackets: give each variable weight $1$, the letter $N$ weight $0$ and each binary letter weight $-1$.
A string is then a formula exactly when its total weight is $1$ and each nonempty proper initial segment has weight at most $0$, as [[reading Polish notation|MJ6FMPYEF2]] shows.
So the Polish formulas form a [[prefix code|GNB3T6TD0M]]: no formula is a proper prefix of another.
The same theorem, with the same proof, holds for the terms and formulas of [[first-order logic|086QKPF0A6]].

### Watch out

The theorem is not only about brackets in print.
It is the reason why truth values and every other recursive function on formulas are well defined.
A typical slip is to split a formula at the first connective that you read, as in $((p \land q) \to r)$, where the first connective $\land$ sits inside a bracket and the main connective is $\to$.

### Try it

Find $\psi$, $\circ$ and $\chi$ for $((\neg p) \leftrightarrow (q \lor r))$.
The count returns to $0$ after $(\neg p)$, so $\psi = (\neg p)$, $\circ = \leftrightarrow$ and $\chi = (q \lor r)$.

Why can a formula of form 2 never also have form 3?
Its second symbol is $\neg$, while the second symbol of form 3 is the first symbol of a formula, which is a variable or a left bracket.

## History

Jan Łukasiewicz introduced his prefix notation in 1924, and it needs no brackets because of the Polish version of the theorem.
Textbooks of mathematical logic prove the bracketed version by counting brackets, as Enderton does in his chapter on sentential logic.

## Explanations

### L1 human

The theorem says that each formula can be read in only one way.
In school arithmetic, $2 + 3 \times 4$ needs a rule (multiply first) to have one meaning.
In formulas each connective comes with its own pair of brackets, so no rule is needed.
For example, $((p \land q) \lor r)$ is an "or" of two parts, and nothing else.
Because the reading is unique, the truth value of a formula is fixed once the letters have values.

### L2 human

We compute the depth of $\varphi = ((p \to q) \land (\neg p))$ by recursion, and the theorem guarantees one answer.
The clauses are $d(p) = 0$, $d((\neg \psi)) = d(\psi) + 1$ and $d((\psi \circ \chi)) = \max(d(\psi), d(\chi)) + 1$.
The theorem gives the unique split $\psi = (p \to q)$ and $\chi = (\neg p)$, so
$$d(\varphi) = \max(d((p \to q)), d((\neg p))) + 1 = \max(1, 1) + 1 = 2 .$$
Check: the parse tree has root $\land$, two inner nodes $\to$ and $\neg$, and leaves at distance $2$ from the root.
Every recursive function on formulas is computed in the same way, from the parts that the theorem provides.

### L3 human

In algebraic terms, the theorem says that the formula algebra is free.
The operations $\varphi \mapsto (\neg \varphi)$ and $(\varphi, \psi) \mapsto (\varphi \circ \psi)$ are injective, their images are pairwise disjoint, and the images do not contain the variables.
These conditions, with generation by $P$, characterize the absolutely free algebra, and the recursion principle is its universal property.
In the theory of formal languages, the theorem says that the context-free grammar of formulas is unambiguous.
The Polish weight test is the basis of stack evaluation of prefix and postfix expressions.
