---
tag: ~5d6edbff
kind: statement
role: theorem
name: Rabin's tree theorem
aliases: [rabins-tree-theorem, decidability-of-s2s]
msc: ["03B25", "03D05"]
topics: [E4AVTNWE9E]
audience: research
about: [3VSFM7K70Z, QXECDPAYTN, G6X7SZSNC5]
uses: [~fe9d17e9, G6X7SZSNC5, 3VSFM7K70Z, 92DM43HQZT, QXECDPAYTN, HWC687ES0Q, 5BXYE8REDN]
sources:
  - url: https://en.wikipedia.org/wiki/S2S_(mathematics)
    locator: Decidability of S2S
  - url: https://en.wikipedia.org/wiki/Infinite-tree_automaton
    locator: Acceptance condition
  - url: https://en.wikipedia.org/wiki/Parity_game
    locator: Relation with logic and automata theory
history:
  first_stated: "1969"
  notes: "Rabin, Decidability of second-order theories and automata on infinite trees, Transactions of the AMS, 1969."
---

## Statement

Let $T = \set{0, 1}^*$ be the set of finite words over $\set{0,1}$, viewed as the nodes of the infinite binary tree with root $\varepsilon$.
The successor functions are $s_0(w) = w0$ and $s_1(w) = w1$.
S2S is the monadic second-order theory of $(T, s_0, s_1)$: first-order variables range over nodes, set variables range over all subsets of $T$, and the atomic formulas are $s_0(x) = y$, $s_1(x) = y$, $x = y$ and $x \in X$.

For a finite alphabet $\Sigma$, a $\Sigma$-tree is a map $t \colon T \to \Sigma$.
A nondeterministic [[tree automaton|3VSFM7K70Z]] on infinite trees is $A = (Q, \Sigma, q_{\mathrm{in}}, \Delta, \mathrm{Acc})$ with a finite set $Q$ of states, an initial state $q_{\mathrm{in}}$, transitions $\Delta \subseteq Q \times \Sigma \times Q \times Q$, and an acceptance condition $\mathrm{Acc}$.
A run on $t$ is a map $\rho \colon T \to Q$ with $\rho(\varepsilon) = q_{\mathrm{in}}$ and $(\rho(w), t(w), \rho(w0), \rho(w1)) \in \Delta$ for every node $w$.
For an infinite path from the root, $\operatorname{Inf}$ is the set of states that $\rho$ takes infinitely often on the path.

In a Rabin condition, $\mathrm{Acc}$ is a finite list of pairs $(E_j, F_j)$ of sets of states, and a path is good when some $j$ has $\operatorname{Inf} \cap E_j = \emptyset$ and $\operatorname{Inf} \cap F_j \ne \emptyset$.
The run is accepting when every path is good, and $L(A)$ is the set of trees with an accepting run.

1. For every S2S formula $\varphi(X_1, \ldots, X_m)$ a Rabin tree automaton, computable from $\varphi$, accepts exactly the $\set{0,1}^m$-trees that code satisfying assignments. Conversely every language of a Rabin tree automaton is S2S-definable.
2. The languages of Rabin tree automata are closed under complement, effectively.
3. Emptiness of a Rabin tree automaton is decidable, and every nonempty language contains a regular tree, that is, a tree with only finitely many distinct subtrees.
4. S2S is [[decidable|HWC687ES0Q]].

## Remarks

### About the proof

A parity condition is a priority map $\Omega \colon Q \to \N$.
A path is good for it when the largest priority in $\Omega(\operatorname{Inf})$ is even.
Rabin and parity tree automata recognize the same tree languages, by effective translations.
The modern proof rests on positional determinacy of parity games: in a parity game on a graph, from each vertex one of the two players has a winning strategy that depends only on the current vertex.

The [[proof|~a89d767e]] proves positional determinacy of parity games on finite graphs and the decidability of emptiness for parity tree automata in full; it cites complementation and gives the translation of formulas in outline.

### Why each hypothesis is needed

- The acceptance condition. Büchi tree automata, which ask for an accepting state infinitely often on every path, are strictly weaker. Rabin showed in 1970 that the trees over $\set{a, b}$ in which every path has only finitely many $a$ form a language that no Büchi tree automaton recognizes, although its complement is Büchi-recognizable.
- Monadic quantifiers. Full second-order logic over $(T, s_0, s_1)$ interprets arithmetic with addition and multiplication, so its theory is undecidable.
- Nondeterminism. No deterministic parity tree automaton accepts the trees over $\set{a, b}$ with at least one $a$. So the theorem needs nondeterministic automata, and complementation is the hard part.

For the claim on determinism: in a deterministic run the state at a node depends only on the labels of its proper ancestors.
Take any path $\pi$ and a node $w$ off $\pi$.
The tree with a single $a$ at $w$ is accepted, and $\pi$ carries the same states there as in the all-$b$ tree.
So every path of the all-$b$ tree is good, and the all-$b$ tree is accepted too.

### Consequences

1. S1S is the theory of one branch of the binary tree, so [[Büchi's theorem on S1S|~fe9d17e9]] is a special case.
2. The monadic theory of the tree with countably many successors, SωS, is interpretable in S2S, and so it is decidable.
3. The monadic second-order theory of $(\mathbb{Q}, <)$ is decidable, because $(\mathbb{Q}, <)$ is isomorphic to a definable subset of the tree with the left-to-right order. Every countable linear order embeds in $(\mathbb{Q}, <)$, so a sentence holds in all countable linear orders exactly when it holds relativized to every subset $X$ of $\mathbb{Q}$. Hence the monadic theory of the countable linear orders is decidable too.
4. Satisfiability of the [[modal mu-calculus|5BXYE8REDN]], of propositional dynamic logic and of [[CTL|1DA0Y6KDF8]]* is decidable. These logics are invariant under bisimulation, a satisfiable formula has a tree model of bounded branching, and statements about such trees translate into S2S.
5. Direct automata constructions give much better bounds than the route through S2S: satisfiability is EXPTIME-complete for the modal mu-calculus and 2EXPTIME-complete for CTL*.
6. Model checking the modal mu-calculus on a finite [[Kripke structure|NGHWZ9Y7ZV]] is equivalent to solving a finite parity game.

### Converse

Part 1 is an equivalence: the S2S-definable tree languages are exactly the languages of Rabin tree automata.
Decidability does not survive natural extensions: adding the relation "$x$ and $y$ are at the same depth" lets one interpret grids, whose monadic theory is undecidable (see the [[proof of Seese's theorem|~af9f53a2]]).

### Generalizations

1. Gurevich and Harrington (1982) gave a proof of complementation by games. Emerson and Jutla (1991) and, independently, Mostowski (1991) proved positional determinacy of parity games, which gives the shortest route to complementation.
2. Zielonka (1998) gave a recursive proof of positional determinacy that also yields an algorithm for finite parity games.
3. The decidability of S2S is the source of many decidable theories obtained by interpretation, and of the decidable MSO theories of graphs of bounded treewidth ([[Courcelle's theorem|~2cb7df7c]]).

## History

Michael Rabin proved the theorem in 1969, in a long paper on second-order theories and automata on infinite trees.
His complementation proof was hard to read, and simpler proofs used infinite games: Gurevich and Harrington in 1982, and Emerson and Jutla and Mostowski in 1991 with parity games.
Many later decidability results in logic and verification are obtained by interpreting a theory in S2S.

## Explanations

### L1 human

Picture a tree that starts at a root and splits in two at every node, forever.
Every node carries a letter, for example $a$ or $b$.
A tree automaton walks down all branches at the same time and keeps a finite memory on each branch.
Rabin showed that every property of such trees that one can write with "for every node", "there is a set of nodes", and "left child" and "right child" can be checked by such an automaton.
He also showed how to decide whether any tree at all has the property.
So the logic of the infinite binary tree is decidable.

### L2 human

We build a parity tree automaton for "every path has infinitely many $a$" over $\set{a, b}$, and we test it on two trees.

1. States: $q_{\mathrm{in}}$, $q_a$, $q_b$, with $\Omega(q_{\mathrm{in}}) = 0$, $\Omega(q_a) = 2$, $\Omega(q_b) = 1$. A state $q_c$ at a node claims that the node has label $c$.
2. Transitions: $(q, c, q_{c'}, q_{c''})$ for all $c', c'' \in \set{a, b}$, where $q$ is $q_{\mathrm{in}}$ or $q_c$. So the automaton guesses the labels of the two children and checks each guess one level lower.
3. In an accepting run every node $w \ne \varepsilon$ has state $q_{t(w)}$. Along a path, $q_a$ occurs infinitely often exactly when $a$ does. Then the largest priority seen infinitely often is $2$, which is even; otherwise it is $1$.
4. The tree with $t(w) = a$ for $|w|$ even and $b$ for $|w|$ odd is accepted: on every path the labels alternate.
5. The tree with $t(w) = a$ exactly for $w \in \set{0}^*$ is rejected: on the path $1, 11, 111, \ldots$ every label is $b$.

The typical use is a decision procedure: write a property of trees, or of programs unfolded into trees, as an automaton and test emptiness.
A trap is to expect Büchi acceptance to suffice on trees: "every path has only finitely many $a$" needs the parity condition, here with $\Omega(q_a) = 1$ and $\Omega(q_b) = 0$.

### L3 human

Rabin's theorem completes the correspondence between monadic second-order logic and automata, from finite words through infinite words to infinite trees.
The modern proof is game-theoretic: acceptance of a tree is a two-player game between the automaton and a pathfinder, complementation follows from positional determinacy of parity games, and emptiness becomes the solution of a finite parity game.
The same games are the semantics of the modal mu-calculus, and solving finite parity games is a central open problem of algorithmics: it is in NP and in co-NP, and quasi-polynomial algorithms are known, but no polynomial algorithm is known.
