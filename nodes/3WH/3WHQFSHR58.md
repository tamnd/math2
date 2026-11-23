---
tag: 3WHQFSHR58
kind: concept
name: Monadic second-order logic
aliases: [mso, mso-logic]
msc: ["03B16", "03C85", "03D05", "68Q45"]
topics: [MDHDYV8QZW]
audience: grad
uses: [G6X7SZSNC5, 086QKPF0A6, 983GZBQYT4, 18WVBDCS38]
sources:
  - url: https://en.wikipedia.org/wiki/Monadic_second-order_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Monadic_second-order_logic
    locator: Variants
  - url: https://en.wikipedia.org/wiki/Monadic_second-order_logic
    locator: Decidability and complexity of satisfiability
  - url: https://en.wikipedia.org/wiki/Büchi–Elgot–Trakhtenbrot_theorem
    locator: Theorem statement
  - url: https://en.wikipedia.org/wiki/Courcelle's_theorem
    locator: Formulations
  - url: https://en.wikipedia.org/wiki/Büchi_automaton
    locator: lead section
---

## Summary

Monadic second-order logic lets a sentence say "there is a set of elements such that ...", but never "there is a relation such that ...".
Here is a first thing it can say that ordinary first-order logic cannot.
A word $a_1 a_2 \cdots a_n$ has even length exactly when some set $X$ of positions contains position $1$, contains exactly one of any two neighboring positions, and misses position $n$.
For the word $abab$ the set is $X = \{ 1, 3 \}$, and [[the even-length example|PD8MWX6JDM]] checks the sentence step by step.

In exact terms, monadic second-order logic (MSO) is the fragment of [[second-order logic|G6X7SZSNC5]] in which every quantified second-order variable is unary.
Its formulas use the symbols of a vocabulary, element variables $x, y, \ldots$, set variables $X, Y, \ldots$, the new atomic formulas $X(x)$, and the connectives of [[first-order logic|086QKPF0A6]].
The quantifiers are $\exists x$, $\forall x$, $\exists X$ and $\forall X$.
In the full (standard) semantics on a [[structure|983GZBQYT4]] $\mathcal{M}$, a set variable ranges over all subsets of the domain of $\mathcal{M}$, and $X(x)$ means that the element $x$ lies in the set $X$.
The vocabulary may contain relation symbols of any arity, and only the quantified variables are restricted to sets.
On words and trees, MSO has exactly the power of finite [[automata|KTX2S6J2E6]], so it is a strong logic that algorithms can still handle.

## Motivation

First-order logic cannot say that a word has even length, or that a finite graph is connected.
Each of these properties needs a quantifier over sets: a set of positions that alternates along the word, or a set of vertices that is closed under edges.
Full second-order logic can say both, but it quantifies over relations of every arity, and that is too much.
On words it already defines languages that no finite automaton recognizes, such as $\{ a^n b^n : n \ge 1 \}$.

MSO keeps only the quantifiers over sets, and this restriction pays off.
By the [[Büchi-Elgot-Trakhtenbrot theorem|AK66XQ59Z3]], the languages of finite words that MSO defines are exactly the [[regular languages|18WVBDCS38]].
So a question about an MSO sentence on words becomes a question about an automaton, and algorithms answer those.
The same idea gives [[Büchi's theorem on S1S|YPDXVTH5JR]] for infinite words, [[Rabin's tree theorem|PXKKP038RG]] for infinite trees, and [[Courcelle's theorem|DD4JB8XJ5A]] for graphs of bounded [[treewidth|CD2XB4Y1SF]].
In computer science, this link between logic and automata is the basis of the automatic verification of finite-state systems.

## Notation

The atomic formula $X(x)$ is also written $Xx$ or $x \in X$.
A word $w = a_1 \cdots a_n$ over a finite alphabet $\Sigma$ is read as the structure with domain $\{ 1, \ldots, n \}$, the usual order $<$, and one unary relation $P_a = \{ i : a_i = a \}$ for each letter $a \in \Sigma$.
Some books use the successor relation in place of $<$, and each is MSO-definable from the other.
On graphs, $\mathrm{MSO}_1$ quantifies over sets of vertices, and $\mathrm{MSO}_2$ also quantifies over sets of edges.
Existential MSO (EMSO, or monadic $\Sigma^1_1$) consists of the sentences $\exists X_1 \cdots \exists X_k \, \varphi$ with $\varphi$ first-order.
Weak MSO lets set variables range over finite sets only.
The names S1S and S2S denote the MSO theories of $(\mathbb{N}, \mathrm{succ})$ and of the infinite binary tree with its two successor functions, and WS1S and WS2S are their weak versions.

## Remarks

### Sets of vertices in a graph

On a [[graph|00C0BR7D7H]] with edge relation $E$, a set quantifier can guess a part of the graph, and a first-order formula then checks the part.
A graph is [[bipartite|0ZVQKTRKVQ]] exactly when it satisfies the sentence below, where $X$ is one side of the bipartition:
$$\beta := \exists X \, \forall x \, \forall y \, \bigl( E(x, y) \to (X(x) \leftrightarrow \neg X(y)) \bigr).$$
A graph is [[connected|0KWFFMDF8T]] exactly when no set $X$ with a vertex inside and a vertex outside is closed under edges.
In symbols:
$$\gamma := \forall X \, \bigl( (\exists x \, X(x) \land \exists y \, \neg X(y)) \to \exists x \, \exists y \, (X(x) \land \neg X(y) \land E(x, y)) \bigr).$$
Check: on the graph with vertices $1, 2, 3$ and the one edge $\{ 1, 2 \}$, the set $X = \{ 3 \}$ has a vertex inside and a vertex outside, and no edge leaves it, so $\gamma$ is false, and the graph is indeed not connected.

Colorings fit the same pattern.
The EMSO sentence $\exists R \, \exists G \, \exists B \, \varphi$ with a first-order $\varphi$ defines the [[3-colorable graphs|0XHZW0VCPR]], as [[the three-colorability example|EHH5XEB6BG]] proves.
With edge sets the logic says more.
A graph with at least three vertices is Hamiltonian exactly when some set of edges has exactly two of its edges at each vertex and forms a connected subgraph.
That condition is an $\mathrm{MSO}_2$ sentence.

### What MSO cannot say

The language $\{ a^n b^n : n \ge 1 \}$ is not MSO-definable on words, because it is not regular, as [[the a^n b^n non-example|EHV16FB3Z8]] shows with the pumping lemma.
MSO can check the shape $a^+ b^+$, but it cannot compare the lengths of two long blocks.

Over the empty vocabulary, "the domain has an even number of elements" is not MSO-definable on finite sets.
A game with set moves, an extension of the [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]], shows that two large enough pure sets satisfy the same MSO sentences of a given quantifier rank.
The same property is definable on finite linear orders, as the even-length sentence shows, because the order gives the alternating set a path to follow.

Hamiltonicity is $\mathrm{MSO}_2$-definable but not $\mathrm{MSO}_1$-definable, so the two variants of MSO on graphs differ in power.
Connectivity of finite graphs is not EMSO-definable, by a theorem of Fagin.
Its complement is EMSO-definable: some set $X$ is nonempty, misses a vertex, and is closed under edges.

### The bridge to automata

The Büchi-Elgot-Trakhtenbrot theorem says that a language of finite words is regular exactly when it is MSO-definable, and both directions are effective.
From an automaton to a sentence, we guess the run with one set variable for each state, as the even-length sentence does with its two states.
From a sentence to an automaton, we build automata by induction on the formula, and the [[closure properties of regular languages|446KZ8HJ5F]] under union, complement and projection handle $\lor$, $\neg$ and $\exists X$.

First-order logic with $<$ defines exactly the [[star-free languages|K83HS1C5WG]] on words, a theorem of McNaughton and Papert.
The words of even length over a one-letter alphabet form a regular language that is not star-free, so this language separates first-order logic from MSO.

Satisfiability of MSO on finite words is decidable, because emptiness of finite automata is decidable, but no algorithm of elementary time complexity decides it.
On infinite words, S1S is decidable by a translation into [[Büchi automata|92DM43HQZT]], and on finite trees MSO matches the [[tree automata|TQWGW9X8VF]].
The topic [[automata on infinite words and trees|HQJP210CHQ]] treats these automata in full.
By Courcelle's theorem, each fixed $\mathrm{MSO}_2$ property is decidable in linear time on graphs of treewidth at most $k$, for each fixed $k$.

### Where MSO sits

MSO is stronger than first-order logic and weaker than full second-order logic.
The even-length sentence separates the first pair.
On finite pure sets, "even size" separates the second pair, since second-order logic says it with a binary relation that pairs the elements and MSO cannot say it.

On arbitrary structures MSO keeps the failures of second-order logic.
Its satisfiability problem is undecidable already because first-order logic is a fragment of it.
Under [[Henkin semantics|KWEJFK5943]], where set variables range over a chosen family of subsets, MSO becomes a two-sorted first-order logic, and completeness and compactness hold again.
All the results above use the full semantics.

### Watch out

Do not confuse MSO with the [[monadic predicate calculus|SERN6CRVWW]].
The monadic predicate calculus allows only unary symbols in the vocabulary and has no set quantifiers, while MSO keeps every vocabulary and restricts only the quantified variables.
For example, the sentence $\gamma$ for connectivity uses the binary symbol $E$, so it lies outside the monadic predicate calculus.

Do not speak of "MSO on graphs" without saying $\mathrm{MSO}_1$ or $\mathrm{MSO}_2$.
Hamiltonicity separates the two, and Courcelle's theorem is usually stated for $\mathrm{MSO}_2$.

Do not think that MSO is decidable in general.
Decidability holds on special classes, such as words, trees and graphs of bounded treewidth, and it fails on the class of all finite graphs.

### History

Büchi in 1960 and Elgot in 1961 proved that MSO on finite words defines exactly the regular languages, and Trakhtenbrot found the same result independently.
Büchi introduced Büchi automata in 1962 to decide S1S, and Rabin proved the decidability of S2S in 1969.
Thatcher and Wright extended the automata method to finite trees in 1968, and Courcelle proved his theorem on graphs of bounded treewidth in 1990.
Fagin showed in 1975 that connectivity is not in monadic NP, the class of properties that EMSO defines.

### Try it

Is "the number of $a$'s in the word is even" MSO-definable on words over $\{ a, b \}$?
Yes: a two-state automaton recognizes it, and in the sentence, $X$ is the set of positions where the number of $a$'s read so far is odd.

Does the triangle with vertices $1, 2, 3$ satisfy the bipartiteness sentence $\beta$?
No: the edges $\{ 1, 2 \}$ and $\{ 2, 3 \}$ force $X(1) \leftrightarrow X(3)$, and the edge $\{ 1, 3 \}$ forces the opposite.

## Explanations

### L1 human

Ordinary logic talks about single objects: "there is a vertex", "every position".
Monadic second-order logic can also talk about groups of objects: "there is a set of vertices".
This is enough to say things that ordinary logic cannot say.
For example, a word has even length when we can mark every second letter, starting with the first, and the last letter stays unmarked.
For the word "abab" we mark the letters in positions 1 and 3, and position 4 is unmarked, so the length 4 is even.
On words, the properties that this logic can express are exactly the properties that a machine with finitely many states can check.

### L2 human

We test the bipartiteness sentence $\beta$ on two small graphs.

1. Take the 4-cycle with vertices $1, 2, 3, 4$ and edges $12$, $23$, $34$, $41$.
2. Choose $X = \{ 1, 3 \}$.
   Each edge joins a vertex of $X$ to a vertex outside $X$, so the first-order part holds, and $\beta$ is true.
3. Take the triangle with vertices $1, 2, 3$ and edges $12$, $23$, $13$, and suppose that some set $X$ works.
4. The edges $12$ and $23$ give $X(1) \leftrightarrow \neg X(2)$ and $X(2) \leftrightarrow \neg X(3)$, so $X(1) \leftrightarrow X(3)$.
5. The edge $13$ gives $X(1) \leftrightarrow \neg X(3)$, which contradicts step 4.
   So no set $X$ works, and $\beta$ is false.

The typical use of MSO follows the pattern of $\beta$: guess one or more sets, then check a first-order condition on them.
Colorings, bipartitions, matchings and paths all fit this pattern.
Watch out: not every graph property of this kind is in EMSO.
Connectivity needs a universal set quantifier, and Fagin proved that no EMSO sentence defines it.

### L3 human

MSO sits between [[first-order logic|086QKPF0A6]] and full [[second-order logic|G6X7SZSNC5]], and it is the natural logic when a structure is built from a finite skeleton such as a word, a tree or a tree decomposition.
On such structures the set quantifier corresponds to the projection of an automaton, and the Büchi-Elgot-Trakhtenbrot theorem, Büchi's theorem on S1S and Rabin's tree theorem are three stages of one correspondence between logic and automata.
Courcelle's theorem transfers the tree case to graphs of bounded treewidth, and [[Seese's theorem|RT898AFHWT]] gives a converse for the decidability of $\mathrm{MSO}_2$ theories.

In [[finite model theory|4XRVJE0KAN]], EMSO is the monadic part of [[Fagin's theorem|BG8Q0BYSQ3]].
Fagin's proof that monadic NP differs from its complement is a proved analogue of the open question whether NP equals co-NP.
In philosophy, Boolos read MSO as [[plural quantification|DZVEFDYYZX]] over objects, so that a set variable becomes "some things" and no sets are needed.
