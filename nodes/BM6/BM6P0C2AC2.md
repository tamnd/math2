---
tag: BM6P0C2AC2
kind: statement
role: lemma
name: Gödel's β-function lemma
aliases: [beta-function-lemma, godel-beta-function]
msc: ["03F30", "03D20"]
topics: [QHCRN4JVG0]
audience: grad
uses: [0FNN9B4W64, Y0JTZXBRT5, 329ZG1Z0G5, 5NVA2JRHPV]
sources:
  - wikipedia: en:8371092@r1355768245
    locator: Gödel numbering for sequences, section Accessing members > Gödel's β-function lemma
    note: adopted
    mention: wikipedia://en/8371092#TT9T
    sections: [Statement]
  - book: isbn:9780521857840
  - book: isbn:9781482237726
inventory: [2MKMSGKP7Z]
---

## Statement

Two numbers are enough to store any finite list of numbers, and the entries can be read back with remainders alone.
For $c, d, i \in \mathbb{N}$, let $\beta(c, d, i)$ be the remainder of $c$ on division by $1 + (i + 1) d$.
For every $n \in \mathbb{N}$ and every finite sequence $a_0, a_1, \ldots, a_n$ of natural numbers, there are $c, d \in \mathbb{N}$ such that
$$\beta(c, d, i) = a_i \quad \text{for } i = 0, 1, \ldots, n.$$
The graph of $\beta$ is defined by a $\Delta_0$ formula, which even represents $\beta$ in Robinson arithmetic; [[the Δ0 lemma for β|2X3BHXYR6D]] gives the formula.

## Remarks

### A pair first

Before long lists, take a pair.
Cantor's pairing function sends $(x, y)$ to one number:
$$\pi(x, y) = \frac{(x + y)(x + y + 1)}{2} + y.$$
For the pair $(3, 5)$, the sum is $8$, so
$$\pi(3, 5) = \frac{8 \cdot 9}{2} + 5 = 36 + 5 = 41.$$
To decode $41$, find the largest $w$ with $w(w + 1)/2 \le 41$, which is $w = 8$ since $8 \cdot 9 / 2 = 36$ and $9 \cdot 10 / 2 = 45$.
Then $y = 41 - 36 = 5$ and $x = w - y = 3$.
The graph $z = \pi(x, y)$ is defined by $2z = (x + y)(x + y + S0) + 2y$, which uses only $+$ and $\cdot$.

Pairs nest, so $\pi$ also codes triples and quadruples, but a list of unknown length needs a fixed number of codes for every length.
The β function solves that problem, with one more idea: the Chinese remainder theorem.

### Why the modulus has this shape

The modulus $1 + (i + 1) d$ changes with $i$, and it must.
A modulus that does not depend on $i$ would give the same remainder for every $i$, so it could store only constant lists.

The factor $d$ must also be chosen with care.
The [[proof by the Chinese remainder theorem|CXB920QH16]] takes $d$ divisible by $1, 2, \ldots, n$ and at least every $a_i$, and then the moduli are pairwise coprime.
If $d$ is too small, they need not be: for $d = 1$ the moduli are $2, 3, 4, \ldots$, and $2$ and $4$ share the factor $2$.

### What it gives you

A finite sequence of any length is coded by two numbers, with a $\Delta_0$ decoding.
This replaces coding by prime powers, whose decoding needs exponentiation, which $L_A$ does not have.

Exponentiation itself then becomes $\Sigma_1$-definable in $\mathfrak{N}$.
The equation $y = x^z$ holds exactly when some $c, d$ code a list that starts at $1$, multiplies by $x$ at each step, and ends at $y$:
$$\exists c\, \exists d\, \bigl(\beta(c, d, 0) = 1 \land \forall i < z\; \beta(c, d, i + 1) = \beta(c, d, i) \cdot x \land \beta(c, d, z) = y\bigr).$$
For $2^3 = 8$, the list is $1, 2, 4, 8$.
Since $\beta(c, d, i) \le c$, the matrix becomes $\Delta_0$ once each $\beta$ is replaced by the $\Delta_0$ formula for its graph, with quantifiers bounded by $c$.

The same pattern makes the graph of every [[primitive recursive function|5NVA2JRHPV]] $\Sigma_1$, and it is the main lemma of [[representability|BJF29XET83]].
A harder result shows that the graph of exponentiation is even $\Delta_0$-definable, although $\mathsf{I}\Delta_0$ does not prove that exponentiation is total; [[elementary function arithmetic|2JD80TE553]] takes up this point.

### Generalizations

The lemma can be proved inside [[Peano arithmetic|HACXBCM7SS]] in a formalized form: for every sequence coded by $c, d$ and every $a$, there is a code $c', d'$ of the sequence extended by $a$.
Other codings of sequences with $\Delta_0$ decoding exist.
The β function is the classical one, and it works in the language $\{0, S, +, \cdot, <\}$ without exponentiation.

## History

Gödel introduced the β function in his 1931 paper on incompleteness.
He used it to show that relations defined by primitive recursion are definable from addition and multiplication.

## Explanations

### L1 human

The lemma says that any finite list of numbers can be packed into just two numbers $c$ and $d$.
To read the $i$-th entry back, divide $c$ by $1 + (i + 1) d$ and take the remainder.
For example, $c = 27001$ and $d = 6$ store the list $2, 0, 2, 1$.
The reading uses only addition, multiplication and a bounded search, so arithmetic can talk about finite lists, and hence about computations.

### L2 human

We code the sequence $2, 0, 2, 1$, so $n = 3$.
Put $s = \max(3, 2, 0, 2, 1) = 3$ and $d = s! = 6$, so the moduli $1 + (i + 1) \cdot 6$ are $7$, $13$, $19$ and $25$.
These are pairwise coprime, and each entry is smaller than its modulus.
The Chinese remainder theorem gives $c = 27001$.
Check each remainder:
$$27001 = 3857 \cdot 7 + 2 = 2077 \cdot 13 + 0 = 1421 \cdot 19 + 2 = 1080 \cdot 25 + 1.$$
So $\beta(27001, 6, i)$ for $i = 0, 1, 2, 3$ is $2, 0, 2, 1$.

The typical use is to replace "there is a finite sequence with these properties" by "there are $c$ and $d$ with these properties".
Watch out: the code is not unique.
Every $c$ that agrees with $27001$ modulo $7 \cdot 13 \cdot 19 \cdot 25 = 43225$ works, and other $d$ work too: the pair $c = 3412752$, $d = 24$ codes the same list, as [[the Δ0 lemma for β|2X3BHXYR6D]] checks.

### L3 human

The lemma is the bridge from arithmetic to computation.
A computation is a finite sequence of states, and the β function lets a formula of $L_A$ say "there is such a sequence" with two existential quantifiers.
That is why every computably enumerable set is $\Sigma_1$-definable, and why [[representability|BJF29XET83]] reaches every recursive function.
The [[incompleteness theorems|HXHHWY3328]] then code formulas and proofs in the same way.
