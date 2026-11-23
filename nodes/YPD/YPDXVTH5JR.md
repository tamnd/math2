---
tag: YPDXVTH5JR
kind: statement
role: theorem
name: Büchi's theorem on S1S
aliases: [buchis-theorem-s1s, decidability-of-s1s]
msc: ["03B25", "03D05"]
topics: [E4AVTNWE9E]
audience: research
about: [92DM43HQZT, G6WP8B6NGD, G6X7SZSNC5]
uses: [AK66XQ59Z3, G6X7SZSNC5, 0MWKJ44V5A, 92DM43HQZT, G6WP8B6NGD, HWC687ES0Q, RJ3MCAAZSV]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%BCchi_automaton
    locator: Complementation
  - url: https://en.wikipedia.org/wiki/S2S_(mathematics)
    locator: Models of S1S and S2S
  - url: https://en.wikipedia.org/wiki/Monadic_second-order_logic
    locator: Decidability and complexity of satisfiability
history:
  first_stated: "1962"
  notes: "Büchi, in the proceedings of the 1960 International Congress for Logic, Methodology and Philosophy of Science, published in 1962."
---

## Statement

The theorem says that monadic second-order logic on infinite words matches Büchi automata, and so S1S is decidable.

S1S is the monadic second-order theory of the [[natural numbers|0MWKJ44V5A]] with the successor relation $S = \{ (i, i+1) : i \in \mathbb{N} \}$.
Its formulas are built as in [[monadic second-order logic on words|AK66XQ59Z3]]: first-order variables range over $\mathbb{N}$, set variables range over all subsets of $\mathbb{N}$, and the atomic formulas are $S(x, y)$, $x = y$ and $x \in X$.
For a finite alphabet $\Sigma$, an infinite word $\alpha = a_0 a_1 a_2 \cdots \in \Sigma^\omega$ is the structure $(\mathbb{N}, S, (P_a)_{a \in \Sigma})$ with $P_a = \{ i : a_i = a \}$.

A nondeterministic [[Büchi automaton|92DM43HQZT]] is $A = (Q, \Sigma, \Delta, I, F)$ with a finite set $Q$ of states, transitions $\Delta \subseteq Q \times \Sigma \times Q$, initial states $I \subseteq Q$ and accepting states $F \subseteq Q$.
A run of $A$ on $\alpha$ is a sequence $r_0 r_1 r_2 \cdots$ with $r_0 \in I$ and $(r_i, a_i, r_{i+1}) \in \Delta$ for all $i$.
The run is accepting when some state of $F$ occurs in it infinitely often, and $L(A)$ is the set of infinite words with an accepting run.

**Theorem (Büchi).**

1. A language $L \subseteq \Sigma^\omega$ is definable by an MSO sentence over $(\mathbb{N}, S, (P_a)_{a \in \Sigma})$ if and only if $L = L(A)$ for some Büchi automaton $A$, that is, if and only if $L$ is [[omega-regular|G6WP8B6NGD]].
   Both translations are effective.
2. For every Büchi automaton $A$ over $\Sigma$ there is a Büchi automaton $B$, computable from $A$, with $L(B) = \Sigma^\omega \setminus L(A)$.
3. $L(A) \ne \emptyset$ if and only if some accepting state is reachable from an initial state and lies on a cycle, and this condition is decidable.
4. S1S is [[decidable|HWC687ES0Q]].
5. S1S is not [[elementary recursive|RJ3MCAAZSV]]: no decision procedure for it runs in time bounded by a tower of exponentials of fixed height.

## Remarks

### A first property in two languages

Take the alphabet $\{a, b\}$ and the property "the letter $a$ occurs infinitely often".
With the order $<$, which S1S can define, the sentence is $\forall x \, \exists y \, (x < y \wedge P_a(y))$.
A Büchi automaton for the same property has states $q_a$ and $q_b$, both initial, with $q_a$ accepting, and each letter $c$ leads from every state to $q_c$.
On $(ab)^\omega$ the run visits $q_a$ at every second step, so the word is accepted, and the sentence is true in it.
On $a b^\omega$ the run stays in $q_b$ from the third state on, so the word is rejected, and the sentence is false in it.
The [[proof|5809DBA7MW]] turns every sentence into such an automaton and back.

### Why the logic must be monadic

Full second-order logic over $(\mathbb{N}, S)$ can quantify over ternary relations.
It can then define addition and multiplication by their recursion equations, so its theory contains true arithmetic.
True arithmetic is undecidable by [[Gödel's incompleteness theorems|X9WYNYE29C]], so the theorem fails without the word "monadic".

### Why the automata must be nondeterministic

Deterministic Büchi automata are strictly weaker.
The language of words over $\{a, b\}$ with only finitely many $a$'s has a nondeterministic Büchi automaton, which guesses the last $a$, but no deterministic one.
So complementation cannot work by exchanging accepting and rejecting states, as it does for finite automata on finite words.

### Why "infinitely often"

Suppose a run is called accepting when it visits $F$ at least once.
Then "finitely many $a$'s" is still recognized: the automaton guesses the last $a$, enters an accepting state, and then loops on $b$ only.
Its complement "infinitely many $a$'s" is not recognized under the weaker condition, so this condition gives a class that is not closed under complement.

### What it gives you

The monadic second-order theory of $(\mathbb{N}, <)$ is decidable, because $x < y$ is S1S-definable: $x \ne y$, and every set that contains $x$ and is closed under successor contains $y$.
WS1S reduces to S1S, because "$X$ is finite" is S1S-definable as $\exists y \, \forall z \, (z \in X \to z < y)$.
Satisfiability of [[linear temporal logic|RMJ56ZPA63]] is decidable, because each formula translates into an S1S formula whose free set variables stand for the atomic propositions.
In practice one builds a Büchi automaton for the temporal formula directly.

Part 3 also shows that every nonempty omega-regular language contains an ultimately periodic word $u v^\omega$.
Take for $u$ the label of a path to the accepting state, and for $v$ the label of a cycle through it.

### The converse and other forms

Part 1 is an equivalence, so its converse is a part of it.
The omega-regular languages are also exactly the finite unions of sets $U V^\omega$ with $U$ and $V$ regular languages of finite words, and the proof of complementation gives this as a by-product.

### Generalizations

McNaughton's theorem (1966) says that every omega-regular language is recognized by a deterministic automaton with a Muller acceptance condition.
Safra (1988) gave a determinization of $n$-state Büchi automata with $2^{O(n \log n)}$ states.
For infinite trees, the monadic theory of two successors, S2S, is decidable by [[Rabin's tree theorem|PXKKP038RG]].
Elgot and Rabin (1966) showed that S1S stays decidable when a unary predicate for the set of powers of $2$ is added.

### Watch out

Do not complement a Büchi automaton by exchanging accepting and rejecting states.
In the automaton for "infinitely many $a$'s", the swap makes $q_b$ accepting, and the new automaton accepts "infinitely many $b$'s".
On $(ab)^\omega$ both automata accept, so the swap is not the complement.

### Try it

Write an S1S sentence with $<$ for "after some point, only $b$ occurs".
One answer is $\exists x \, \forall y \, (x < y \to P_b(y))$.

Does the language of "infinitely many $a$'s" contain an ultimately periodic word?
Yes: $(ab)^\omega = \varepsilon \, (ab)^\omega$ is one, with $u$ empty and $v = ab$.

## History

Julius Richard Büchi proved the theorem in a paper presented at the 1960 International Congress for Logic, Methodology and Philosophy of Science, published in 1962.
He introduced the automata now named after him for this purpose, and he proved complementation with Ramsey's theorem.
Robert McNaughton proved the determinization theorem in 1966, and Shmuel Safra gave his determinization construction in 1988.

## Explanations

### L1 human

Imagine a machine that reads an endless sequence of letters, such as $a b a b a b \ldots$, and never stops.
It cannot wait for the end, so it accepts when it passes through a "good" state again and again forever.
Büchi showed that such machines check exactly the properties of endless sequences that a simple logic of positions and sets of positions can express.
For example, "the letter $a$ appears infinitely often" is such a property.
Because a machine can be inspected, every sentence of this logic can be decided true or false.

### L2 human

We decide the sentence $\exists x \, \forall y \, (x < y \to P_b(y))$ on the word $(ab)^\omega$ in two ways.
By hand, every position $x$ has a later odd position $y = 2x + 1$ with $a_y = b$, and a later even position $y = 2x + 2$ with $a_y = a$.
So no $x$ works, and the sentence is false in $(ab)^\omega$.
With automata, the sentence says "finitely many $a$'s", and its automaton guesses a point after which it reads only $b$'s.
On $(ab)^\omega$ every such guess fails at the next $a$, so no run is accepting.
The two methods agree, and the automaton method works for every sentence and every ultimately periodic word.
This is the typical use of the theorem: specifications of programs that never stop are checked against automata.
Watch out: the automaton for "finitely many $a$'s" must be nondeterministic, since no deterministic Büchi automaton recognizes this language.

### L3 human

Büchi's theorem extends the [[Büchi-Elgot-Trakhtenbrot theorem|AK66XQ59Z3]] from finite to infinite words, and the only new difficulty is complementation.
Büchi's proof uses Ramsey's theorem to cut every infinite word into a prefix and infinitely many blocks of the same type.
Modern proofs use determinization (McNaughton, Safra) or ranking functions on run graphs.
The same scheme, with games in place of Ramsey's theorem, gives [[Rabin's tree theorem|PXKKP038RG]], and it is the theoretical base of model checking with automata.
