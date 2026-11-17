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

Monadic second-order logic (MSO) is the fragment of [[second-order logic|G6X7SZSNC5]] in which every quantified second-order variable is unary.
Its formulas use the symbols of a vocabulary, first-order variables $x, y, \ldots$ for elements, set variables $X, Y, \ldots$, the atomic formulas $X(x)$, and the connectives of [[first-order logic|086QKPF0A6]].
The quantifiers $\exists x$, $\forall x$, $\exists X$ and $\forall X$ bind both kinds of variable.
In the full (standard) semantics on a [[structure|983GZBQYT4]] $\mathcal{M}$, a set variable ranges over all subsets of the domain of $\mathcal{M}$, and $X(x)$ means that the element $x$ lies in the set $X$.
The vocabulary may contain relation symbols of any arity; only the quantified variables are restricted to sets.
MSO matters because it is strong enough to express connectivity, colourings and the parity of a length, and weak enough that on words and trees it has the same power as finite [[automata|KTX2S6J2E6]].

## Motivation

[[First-order logic|086QKPF0A6]] cannot say that a word has even length, or that a finite graph is connected.
Each of these properties needs a quantifier over sets: a set of positions that alternates along the word, or a set of vertices that is closed under edges.
Full second-order logic can say both, but it quantifies over relations of every arity.
On words it already defines languages that no finite automaton recognises, such as $\set{a^n b^n : n \geq 1}$.
MSO keeps only quantifiers over sets.
On words this restriction gives a logic whose definable languages are exactly the [[regular languages|18WVBDCS38]], so many questions about MSO become questions about automata, which algorithms can answer.
The same restriction leads to decidable theories of infinite words and trees, and to fast algorithms on graphs of bounded [[treewidth|CD2XB4Y1SF]].

## Notation

The atomic formula $X(x)$ is also written $Xx$ or $x \in X$.
A word $w = a_1 a_2 \cdots a_n$ over a finite alphabet $\Sigma$ is read as the structure with domain $\set{1, \ldots, n}$, the usual order $<$, and one unary relation $P_a = \set{i : a_i = a}$ for each letter $a \in \Sigma$.
Some books use the successor relation $S(x, y)$ in place of $<$; each is MSO-definable from the other.
On graphs, $\mathrm{MSO}_1$ quantifies over sets of vertices, and $\mathrm{MSO}_2$ also quantifies over sets of edges.
Existential MSO (EMSO, or monadic $\Sigma^1_1$) is the set of sentences $\exists X_1 \cdots \exists X_k\, \varphi$ with $\varphi$ first-order.
Weak MSO (WMSO) lets set variables range over finite sets only.
The names S1S and S2S denote the MSO theories of $(\mathbb{N}, \mathrm{succ})$ and of the infinite binary tree with its two successor functions; WS1S and WS2S are their weak versions.

## Remarks

### Examples

- Even length of a word: the sentence $\exists X$ ("the first position is in $X$, membership alternates along the word, and the last position is not in $X$") defines the words of even length; see [[this example|PD8MWX6JDM]].
- Connectivity of a graph: a [[graph|00C0BR7D7H]] with edge relation $E$ is [[connected|0KWFFMDF8T]] if and only if it satisfies the $\mathrm{MSO}_1$ sentence below. It says that no set $X$ with a vertex inside and a vertex outside is closed under edges.
$$\forall X \bigl( (\exists x\, X(x) \land \exists y\, \neg X(y)) \to \exists x \exists y\, (X(x) \land \neg X(y) \land E(x, y)) \bigr)$$
- Three-colourability: the EMSO sentence $\exists R \exists G \exists B\, \varphi$ with a first-order $\varphi$ defines the [[3-colourable graphs|0XHZW0VCPR]]; see [[this example|EHH5XEB6BG]].
- [[Bipartite graphs|0ZVQKTRKVQ]]: a graph is bipartite if and only if $\exists X \forall x \forall y\, (E(x, y) \to (X(x) \leftrightarrow \neg X(y)))$ holds. The set $X$ is one side of the bipartition.
- Hamiltonicity is $\mathrm{MSO}_2$-definable on graphs with at least three vertices. A Hamiltonian cycle is a set of edges with exactly two of its edges at each vertex, and the subgraph it forms is connected.

### Non-examples

- The language $\set{a^n b^n : n \geq 1}$ is not MSO-definable on words, because it is not regular; see [[this non-example|EHV16FB3Z8]].
- Over the empty vocabulary, "the domain has an even number of elements" is not MSO-definable on finite sets. A game argument with set moves shows that two pure sets with at least $2^k$ elements each satisfy the same MSO sentences of quantifier rank $k$.
- The same property is MSO-definable on finite linear orders, as in the even-length example. The order gives the alternating set something to follow.
- Hamiltonicity is not $\mathrm{MSO}_1$-definable, although it is $\mathrm{MSO}_2$-definable. So the two variants of MSO on graphs differ in power.
- Connectivity of finite graphs is not EMSO-definable, by a theorem of Fagin. Its complement, disconnectivity, is EMSO-definable: some set $X$ is nonempty, misses a vertex, and is closed under edges.

### Basic properties

- Expressive power: first-order logic is weaker than MSO, and MSO is weaker than full second-order logic. Even length separates the first pair; on finite pure sets, "even size" is definable in second-order logic by a fixed-point-free involution but not in MSO.
- The Büchi-Elgot-Trakhtenbrot theorem: a language of finite words is regular if and only if it is MSO-definable. Both directions are effective. The proof from automata to logic guesses the run with one set variable for each state. The proof from logic to automata uses the [[closure properties of regular languages|446KZ8HJ5F]] under union, complement and projection.
- On words, first-order logic with $<$ defines exactly the star-free languages, a theorem of McNaughton and Papert. So $\set{w : |w| \text{ even}}$ over a one-letter alphabet separates first-order logic from MSO.
- Satisfiability of MSO on finite words is decidable, since emptiness of finite automata is decidable. It has no algorithm of elementary time complexity.
- Infinite words: S1S is decidable, by Büchi's translation of MSO into [[Büchi automata|92DM43HQZT]]. The MSO-definable sets of infinite words are exactly the $\omega$-regular languages.
- Trees: on finite trees MSO defines exactly the sets recognised by [[tree automata|TQWGW9X8VF]], and Rabin proved that S2S is decidable. The topic [[automata on infinite words and trees|HQJP210CHQ]] treats these automata.
- Graphs: by Courcelle's theorem, each fixed $\mathrm{MSO}_2$ property is decidable in linear time on graphs of treewidth at most $k$, for each fixed $k$.
- On arbitrary structures MSO keeps the failures of second-order logic: satisfiability is undecidable, because first-order logic is a fragment.
- Under the Henkin semantics, MSO is a two-sorted first-order logic, and completeness and compactness hold again. All the results above use the full semantics.

### History

Büchi in 1960 and Elgot in 1961 proved that MSO on finite words defines exactly the regular languages, and Trakhtenbrot found the same result independently.
Büchi introduced Büchi automata in 1962 to decide S1S, and Rabin proved the decidability of S2S in 1969.
Thatcher and Wright extended the automata method to finite trees in 1968, and Courcelle proved his theorem on graphs of bounded treewidth in 1990.
Fagin showed in 1975 that connectivity is not in monadic NP, the class of properties defined by EMSO.

### Common errors

- To confuse MSO with the [[monadic predicate calculus|SERN6CRVWW]]. The monadic predicate calculus restricts the vocabulary to unary symbols and has no set quantifiers. MSO keeps every vocabulary and restricts only the quantified variables.
- To speak of "MSO on graphs" without saying $\mathrm{MSO}_1$ or $\mathrm{MSO}_2$. Hamiltonicity separates the two, and Courcelle's theorem is usually stated for $\mathrm{MSO}_2$.
- To think that MSO is decidable in general. Decidability holds for special classes, such as words, trees and graphs of bounded treewidth, and fails on the class of all finite graphs.

## Explanations

### L1 human

Ordinary logic talks about single objects: "there is a vertex", "every position".
Monadic second-order logic can also talk about groups of objects: "there is a set of vertices".
This is enough to say things that ordinary logic cannot say.
For example, a word has even length when we can mark every second letter, starting with the first, and the last letter stays unmarked.
For the word "abab" we mark the letters in positions 1 and 3, and position 4 is unmarked, so the length 4 is even.
On words, the properties this logic can express are exactly the properties that a machine with finitely many states can check.

### L2 human

We test the bipartiteness sentence $\beta = \exists X\, \forall x \forall y\, (E(x, y) \to (X(x) \leftrightarrow \neg X(y)))$ on two small graphs.

1. Take the 4-cycle with vertices $1, 2, 3, 4$ and edges $12$, $23$, $34$, $41$.
2. Choose $X = \set{1, 3}$. Each edge joins a vertex of $X$ to a vertex outside $X$, so the first-order part holds, and $\beta$ is true.
3. Take the triangle with vertices $1, 2, 3$ and edges $12$, $23$, $13$, and suppose that some set $X$ works.
4. The edges $12$ and $23$ give $X(1) \leftrightarrow \neg X(2)$ and $X(2) \leftrightarrow \neg X(3)$, so $X(1) \leftrightarrow X(3)$.
5. The edge $13$ gives $X(1) \leftrightarrow \neg X(3)$, which contradicts step 4. So no set $X$ works, and $\beta$ is false.

The typical use of MSO follows the pattern of $\beta$: guess one or more sets, then check a first-order condition on them.
Colourings, bipartitions, matchings and paths all fit this pattern.
A trap is to assume that every graph property of this kind is in EMSO.
Connectivity needs a universal set quantifier, and Fagin proved that no EMSO sentence defines it.

### L3 human

MSO sits between [[first-order logic|086QKPF0A6]] and full [[second-order logic|G6X7SZSNC5]], and it is the logic of choice when a structure is built from a finite skeleton such as a word, a tree or a tree decomposition.
On such structures the set quantifier corresponds to the projection of an automaton, and the Büchi-Elgot-Trakhtenbrot theorem, Büchi's theorem on S1S and Rabin's tree theorem are three stages of one correspondence between logic and automata.
Courcelle's theorem transfers the tree case to graphs of bounded treewidth, and [[Seese's theorem|RT898AFHWT]] gives a converse for decidability of $\mathrm{MSO}_2$ theories.
In [[finite model theory|4XRVJE0KAN]], EMSO is the monadic part of [[Fagin's theorem|BG8Q0BYSQ3]].
Fagin's proof that monadic NP differs from its complement is a proved analogue of the open question whether NP equals co-NP.
The [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]] extends to MSO by set moves, and this game proves the non-example on pure sets above.
Boolos read MSO as plural quantification over objects, a view treated in the page on plural quantification of this sub-area.
