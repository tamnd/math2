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

Fix an integer $k \ge 2$ and the digit set $\Sigma_k = \set{0, 1, \ldots, k - 1}$.
Define $V_k \colon \N \to \N$ by $V_k(0) = 1$, and for $x \ge 1$ let $V_k(x)$ be the largest power of $k$ that divides $x$.
For example $V_2(20) = 4$ and $V_3(20) = 1$.
Büchi arithmetic of base $k$ is the structure $(\N, +, V_k)$ of the [[natural numbers|0MWKJ44V5A]], in the [[first-order|086QKPF0A6]] language with $+$, $V_k$ and equality.

For $n \ge 1$, read a word $w = c_0 c_1 \cdots c_{L-1}$ over the alphabet $\Sigma_k^n$ as $n$ parallel tracks of digits, least significant digit first.
Its value is the tuple
$$\operatorname{val}(w) = \Bigl( \sum_{j < L} c_j^{(1)} k^j, \; \ldots, \; \sum_{j < L} c_j^{(n)} k^j \Bigr) \in \N^n,$$
where $c_j^{(i)}$ is the $i$-th component of the column $c_j$.
Every tuple has infinitely many representations, because columns of zeros at the end do not change the value.
A relation $X \subseteq \N^n$ is $k$-automatic, or $k$-recognizable, when the language
$$L_X = \set{w \in (\Sigma_k^n)^* : \operatorname{val}(w) \in X}$$
is a [[regular language|18WVBDCS38]].

**Theorem.** Let $k \ge 2$ and $n \ge 1$.

1. A relation $X \subseteq \N^n$ is [[definable|1DQ1M6ZWS4]] in $(\N, +, V_k)$ by a first-order formula without parameters if and only if $X$ is $k$-automatic.
2. There is an algorithm that takes a formula $\varphi(x_1, \ldots, x_n)$ and returns a finite automaton that recognizes $L_X$ for the relation $X$ defined by $\varphi$.
3. The theory $\operatorname{Th}(\N, +, V_k)$ is [[decidable|HWC687ES0Q]].

The [[proof|WX2B2GTGJX]] proves the direction from definable to automatic and part 3 in full, and gives the other direction in outline.

## Remarks

### Why each hypothesis is needed

- The function $V_k$ is needed for the direction from automatic to definable. Without it, the definable subsets of $\N$ are those of [[Presburger arithmetic|4W0E9G7PPV]], which are ultimately periodic. The set of powers of $k$ is $k$-automatic, but it is not ultimately periodic, because its gaps grow without bound.
- The base must be fixed. For two bases $k$ and $l$ that are not powers of a common integer, the theory of $(\N, +, V_k, V_l)$ is undecidable, a result of Villemaire. The Cobham-Semenov theorem below shows that the two kinds of automata see different sets.
- Multiplication cannot be added. The relation $x \cdot y = z$ is not $k$-automatic for any $k$: otherwise part 2 would decide the theory of $(\N, +, \cdot)$, which is undecidable by [[Gödel's incompleteness theorems|X9WYNYE29C]].

### Consequences

1. The set of powers of $k$ is defined by the formula $V_k(x) = x$, since $V_k(x) = x$ holds exactly when $x$ is a power of $k$.
2. Every relation definable in $(\N, +)$ is $k$-automatic for every $k \ge 2$, since $(\N, +)$ is a reduct of $(\N, +, V_k)$. This gives an automata proof of the decidability of Presburger arithmetic.
3. The set of $n$ whose binary digit sum is odd is $2$-automatic: a two-state automaton tracks the parity of the number of digits $1$. So it is definable in $(\N, +, V_2)$. This set gives the [[Thue-Morse sequence|7JZVT385PC]].
4. If $k$ and $l$ are powers of a common integer, then $(\N, +, V_k)$ and $(\N, +, V_l)$ define the same relations.
5. The notion of a $k$-automatic relation does not depend on the reading direction. The reversal of a regular language is regular, so reading the most significant digit first gives the same class.

### Converse

The theorem is an equivalence, so it is its own converse.
It also does not matter whether one uses all representations or only the shortest one.
The shortest representations form $L_X$ minus the words that end with a column of zeros, together with the empty word when $0 \cdots 0 \in X$; this language is regular when $L_X$ is.
Conversely $L_X$ is obtained from the shortest representations by appending any number of zero columns, which keeps a language regular.

### Generalizations

1. Cobham's theorem (1969). Call $k, l \ge 2$ multiplicatively independent when $k^a \ne l^b$ for all integers $a, b \ge 1$. For multiplicatively independent $k$ and $l$, a set $X \subseteq \N$ is both $k$-automatic and $l$-automatic if and only if $X$ is ultimately periodic. Ultimately periodic means that there are $N_0$ and $p \ge 1$ with $x \in X \Leftrightarrow x + p \in X$ for all $x \ge N_0$.
2. Semenov's theorem (1977) extends this to all dimensions. For multiplicatively independent $k$ and $l$, a relation $X \subseteq \N^n$ is both $k$-automatic and $l$-automatic if and only if $X$ is definable in $(\N, +)$.
3. In the language of logic, the Cobham-Semenov theorem says: a relation definable both in $(\N, +, V_k)$ and in $(\N, +, V_l)$ is already definable in $(\N, +)$. For $n = 1$ this is Cobham's theorem, since the subsets of $\N$ definable in $(\N, +)$ are the ultimately periodic sets.
4. The same method works for every structure whose domain and relations are given by finite automata on words. Such structures are called automatic structures, and their first-order theories are decidable by the same proof.

## History

Büchi stated the connection between automata and definability in arithmetic in 1960, as a by-product of his work on [[monadic second-order logic|AK66XQ59Z3]] on words.
His original formulation used a different predicate and needed a correction.
The correct form with $V_k$ is due to Véronique Bruyère, and the survey of Bruyère, Hansel, Michaux and Villemaire (1994) gives a complete account.
Alan Cobham proved his theorem in 1969, and Alexei Semenov proved the multidimensional form in 1977.

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

1. Write $3 = 11$, $5 = 101$ and $8 = 0001$, least significant digit first. Pad to length 4: the columns are $(1,1,0)$, $(1,0,0)$, $(0,1,0)$, $(0,0,1)$.
2. Start with carry $0$. Column $(1,1,0)$: $1 + 1 + 0 = 0 + 2 \cdot 1$, so the new carry is $1$.
3. Column $(1,0,0)$: $1 + 0 + 1 = 0 + 2 \cdot 1$, so the carry stays $1$.
4. Column $(0,1,0)$: $0 + 1 + 1 = 0 + 2 \cdot 1$, so the carry stays $1$.
5. Column $(0,0,1)$: $0 + 0 + 1 = 1 + 2 \cdot 0$, so the carry becomes $0$.
6. The run ends with carry $0$, so the automaton accepts, and indeed $3 + 5 = 8$.

The typical use is a decision procedure: a sentence about $+$ and powers of $k$ is turned into an automaton, and one checks whether its language is empty.
A trap is the convention for $V_k(0)$: the choice $V_k(0) = 1$ is common, but some authors use $V_k(0) = 0$; both give the same definable relations, because $0$ is definable by $x + x = x$.

### L3 human

The theorem identifies the relations definable in $(\N, +, V_k)$ with the relations recognized by finite automata on base-$k$ representations.
It is the arithmetic form of the [[Büchi-Elgot-Trakhtenbrot theorem|AK66XQ59Z3]]: a number with its digits is a word, and $V_k$ lets first-order logic speak about digit positions, as set quantifiers do in monadic second-order logic.
The Cobham-Semenov theorem then says that two multiplicatively independent bases share only the Presburger-definable relations.
Automatic structures, $k$-automatic sequences and the decision procedures for combinatorics on words all grow from this correspondence.
