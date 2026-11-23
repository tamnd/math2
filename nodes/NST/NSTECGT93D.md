---
tag: NSTECGT93D
kind: statement
role: theorem
name: Büchi arithmetic
msc: ["03B25", "03D05"]
topics: [E4AVTNWE9E]
audience: research
about: [0MWKJ44V5A, 18WVBDCS38, 1DQ1M6ZWS4]
uses: [086QKPF0A6, 0MWKJ44V5A, 1DQ1M6ZWS4, 18WVBDCS38, W65B6BKZRY, SFMYM96C1B, 4W0E9G7PPV, HWC687ES0Q]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%BCchi_arithmetic
    locator: Büchi arithmetic and automata
  - url: https://en.wikipedia.org/wiki/Cobham%27s_theorem
    locator: Formulation in logic
same_as:
  wikidata: Q5005255
  wikipedia: Büchi arithmetic
history:
  first_stated: "1960"
  notes: "Büchi stated a version in 1960 that needed correction; the form with V_k is due to Bruyère and is surveyed by Bruyère, Hansel, Michaux and Villemaire (1994)."
---

## Statement

A finite automaton that reads binary digits can check $x + y = z$, because it only has to remember a carry bit.
Büchi arithmetic is the logic that matches such automata exactly: addition, plus a function that finds the last nonzero digit of a number.

Fix an integer $k \ge 2$ and the digit set $\Sigma_k = \{ 0, 1, \ldots, k - 1 \}$.
Define $V_k \colon \mathbb{N} \to \mathbb{N}$ by $V_k(0) = 1$, and for $x \ge 1$ let $V_k(x)$ be the largest power of $k$ that divides $x$.
For example $V_2(20) = 4$ and $V_3(20) = 1$.
Büchi arithmetic of base $k$ is the structure $(\mathbb{N}, +, V_k)$ of the [[natural numbers|0MWKJ44V5A]], in the [[first-order|086QKPF0A6]] language with $+$, $V_k$ and equality.

For $n \ge 1$, read a word $w = c_0 c_1 \cdots c_{L-1}$ over the alphabet $\Sigma_k^n$ as $n$ parallel tracks of digits, least significant digit first.
Its value $\operatorname{val}(w) \in \mathbb{N}^n$ has $i$-th component $\sum_{j < L} c_j^{(i)} k^j$, where $c_j^{(i)}$ is the $i$-th component of the column $c_j$.
Every tuple has infinitely many representations, because columns of zeros at the end do not change the value.
A relation $X \subseteq \mathbb{N}^n$ is $k$-automatic, or $k$-recognizable, when the language $L_X$ of all words $w$ over $\Sigma_k^n$ with $\operatorname{val}(w) \in X$ is a [[regular language|18WVBDCS38]].

Let $k \ge 2$ and $n \ge 1$.

1. Definable equals automatic.
   A relation $X \subseteq \mathbb{N}^n$ is [[definable|1DQ1M6ZWS4]] in $(\mathbb{N}, +, V_k)$ by a first-order formula without parameters exactly when $X$ is $k$-automatic.
2. Effectiveness.
   An algorithm takes a formula $\varphi(x_1, \ldots, x_n)$ and returns a finite automaton that recognizes $L_X$ for the relation $X$ defined by $\varphi$.
3. Decidability.
   The theory $\operatorname{Th}(\mathbb{N}, +, V_k)$ is [[decidable|HWC687ES0Q]].

The [[proof|WX2B2GTGJX]] proves the direction from definable to automatic and part 3 in full, and gives the other direction in outline.

## Remarks

### A first decision

Is every number $x$ with $V_2(x) = x$ and $x > 2$ divisible by $4$?
The formula $V_2(x) = x$ says that $x$ is a power of $2$, since a number equals the largest power of $2$ that divides it only when it is itself a power of $2$.
An automaton for the sentence accepts the binary words, least significant digit first, of the form $0^p 1 0^r$ with $p \ge 2$, and it checks that the first two digits are $0$.
Every such word has two leading zeros, so the sentence is true.
Check: $8$ is $0001$ in this order, and $8 = 4 \cdot 2$.

### Why each hypothesis is needed

The function $V_k$ is needed for the direction from automatic to definable.
Without it, the definable subsets of $\mathbb{N}$ are those of [[Presburger arithmetic|4W0E9G7PPV]], which are eventually periodic.
The set of powers of $k$ is $k$-automatic, but it is not eventually periodic, because its gaps grow without bound.

The base must be fixed.
For two bases $k$ and $l$ that are not powers of a common integer, Villemaire proved that the theory of $(\mathbb{N}, +, V_k, V_l)$ is undecidable.

Multiplication cannot be added.
If $x \cdot y = z$ were $k$-automatic, then by part 1 it would be definable in $(\mathbb{N}, +, V_k)$, and part 3 would decide the theory of $(\mathbb{N}, +, \cdot)$, which is undecidable by [[Gödel's incompleteness theorems|X9WYNYE29C]].

### What it gives you

Every relation definable in $(\mathbb{N}, +)$ is $k$-automatic for every $k \ge 2$, since $(\mathbb{N}, +)$ is a reduct of $(\mathbb{N}, +, V_k)$.
This gives an automata proof of the decidability of Presburger arithmetic.

The set of $n$ whose binary digit sum is odd is $2$-automatic, since a two-state automaton tracks the parity of the number of digits $1$.
So it is definable in $(\mathbb{N}, +, V_2)$, and it gives the [[Thue-Morse sequence|7JZVT385PC]].

If $k$ and $l$ are powers of a common integer, then $(\mathbb{N}, +, V_k)$ and $(\mathbb{N}, +, V_l)$ define the same relations.

### The converse and the conventions

The theorem is an equivalence, so it contains its own converse.
It does not matter whether one uses all representations or only the shortest ones.
The shortest representations are the words of $L_X$ that do not end with a column of zeros, and this language is regular when $L_X$ is.
Conversely, $L_X$ comes from the shortest representations by appending any number of zero columns, which keeps a language regular.
The reading direction does not matter either, because the reversal of a regular language is regular.

### Watch out

The choice $V_k(0) = 1$ is common, but some authors use $V_k(0) = 0$.
Both give the same definable relations, because $0$ is definable by $x + x = x$.

Do not confuse "the largest power of $k$ dividing $x$" with "the largest power of $k$ below $x$".
For example $V_2(12) = 4$, while the largest power of $2$ below $12$ is $8$.

### Generalizations

Call $k, l \ge 2$ multiplicatively independent when $k^a \ne l^b$ for all integers $a, b \ge 1$.
A set $X \subseteq \mathbb{N}$ is eventually periodic when there are $N_0$ and $p \ge 1$ with $x \in X \Leftrightarrow x + p \in X$ for all $x \ge N_0$.
Cobham's theorem says that for multiplicatively independent $k$ and $l$, a set $X \subseteq \mathbb{N}$ is both $k$-automatic and $l$-automatic exactly when it is eventually periodic.

Semenov's theorem extends this to all dimensions.
For multiplicatively independent $k$ and $l$, a relation $X \subseteq \mathbb{N}^n$ is both $k$-automatic and $l$-automatic exactly when it is definable in $(\mathbb{N}, +)$.
In logical terms, a relation definable both in $(\mathbb{N}, +, V_k)$ and in $(\mathbb{N}, +, V_l)$ is already definable in $(\mathbb{N}, +)$.

The same method works for every structure whose domain and relations are given by finite automata on words.
Such structures are called automatic structures, and their first-order theories are decidable by the same proof.

### Try it

Is the set of even numbers definable in $(\mathbb{N}, +, V_2)$?
Yes, already in $(\mathbb{N}, +)$, by $\exists y \, (x = y + y)$, and its automaton checks that the first digit, if there is one, is $0$.

Is the set of powers of $3$ $2$-automatic?
No: the numbers $2$ and $3$ are multiplicatively independent, the set is $3$-automatic, and it is not eventually periodic, so Cobham's theorem rules it out.

## History

Büchi stated the connection between automata and definability in arithmetic in 1960, as a by-product of his work on [[monadic second-order logic|AK66XQ59Z3]] on words.
His original formulation used a different predicate and needed a correction.
The correct form with $V_k$ is due to Véronique Bruyère, and the survey of Bruyère, Hansel, Michaux and Villemaire (1994) gives a complete account.
Alan Cobham proved his theorem in 1969, and Alexei Semenov proved the form for all dimensions in 1977.

## Explanations

### L1 human

Write numbers in base $2$, with the last digit first, and stack several numbers on top of each other.
A finite automaton is a machine with a fixed, finite memory that reads the stacked digits from left to right.
To check $3 + 5 = 8$, the machine needs to remember only one carry bit.
Büchi arithmetic is the language of addition together with "the largest power of $2$ that divides $x$".
The theorem says that this language describes exactly the relations that such machines can check.
So every question in this language can be answered by building a machine and looking at it.

### L2 human

We run the automaton for $x + y = z$ in base $2$ on $3 + 5 = 8$.
The states are the carries $0$ and $1$, and column $(a, b, d)$ takes carry $c$ to carry $c'$ when $a + b + c = d + 2c'$.

1. Write $3 = 11$, $5 = 101$ and $8 = 0001$, least significant digit first.
   Pad to length 4, so the columns are $(1,1,0)$, $(1,0,0)$, $(0,1,0)$ and $(0,0,1)$.
2. Start with carry $0$.
   For the column $(1,1,0)$, $1 + 1 + 0 = 0 + 2 \cdot 1$, so the new carry is $1$.
3. For the column $(1,0,0)$, $1 + 0 + 1 = 0 + 2 \cdot 1$, so the carry stays $1$.
4. For the column $(0,1,0)$, $0 + 1 + 1 = 0 + 2 \cdot 1$, so the carry stays $1$.
5. For the column $(0,0,1)$, $0 + 0 + 1 = 1 + 2 \cdot 0$, so the carry becomes $0$.
6. The run ends with carry $0$, so the automaton accepts, and indeed $3 + 5 = 8$.

The typical use is a decision procedure: a sentence about $+$ and powers of $k$ becomes an automaton, and one checks whether its language is empty.
Watch out: the run must end with carry $0$, since a final carry $1$ means that $z$ is missing a digit.

### L3 human

The theorem identifies the relations definable in $(\mathbb{N}, +, V_k)$ with the relations recognized by finite automata on base-$k$ representations.
It is the arithmetic form of the [[Büchi-Elgot-Trakhtenbrot theorem|AK66XQ59Z3]]: a number with its digits is a word, and $V_k$ lets first-order logic speak about digit positions, as set quantifiers do in monadic second-order logic.
The Cobham-Semenov theorem then says that two multiplicatively independent bases share only the Presburger-definable relations.
Automatic structures, $k$-automatic sequences and the decision procedures for combinatorics on words all grow from this correspondence.
