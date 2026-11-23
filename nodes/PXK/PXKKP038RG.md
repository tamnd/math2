---
tag: PXKKP038RG
kind: statement
role: theorem
name: Rabin's tree theorem
aliases: [rabins-tree-theorem, decidability-of-s2s]
msc: ["03B25", "03D05"]
topics: [E4AVTNWE9E]
audience: research
about: [3VSFM7K70Z, QXECDPAYTN, G6X7SZSNC5]
uses: [YPDXVTH5JR, G6X7SZSNC5, 3VSFM7K70Z, 92DM43HQZT, QXECDPAYTN, HWC687ES0Q, 5BXYE8REDN]
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

The theorem says that S2S, the monadic theory of the infinite binary tree, is decidable, because its formulas match tree automata.

Let $T = \{0, 1\}^*$, viewed as the nodes of the infinite binary tree with root $\varepsilon$.
The successor functions are $s_0(w) = w0$ and $s_1(w) = w1$.
S2S is the theory of $(T, s_0, s_1)$ in which first-order variables range over nodes, set variables range over all subsets of $T$, and the atomic formulas are $s_0(x) = y$, $s_1(x) = y$, $x = y$ and $x \in X$.

For a finite alphabet $\Sigma$, a $\Sigma$-tree is a map $t \colon T \to \Sigma$.
A [[tree automaton|3VSFM7K70Z]] on infinite trees is $A = (Q, \Sigma, q_{\mathrm{in}}, \Delta, \mathrm{Acc})$ with finitely many states $Q$, an initial state $q_{\mathrm{in}}$, transitions $\Delta \subseteq Q \times \Sigma \times Q \times Q$ and an acceptance condition $\mathrm{Acc}$.
A run on $t$ is a map $\rho \colon T \to Q$ with $\rho(\varepsilon) = q_{\mathrm{in}}$ and $(\rho(w), t(w), \rho(w0), \rho(w1)) \in \Delta$ for every node $w$.
For an infinite path from the root, $\operatorname{Inf}$ is the set of states that $\rho$ takes infinitely often on the path.
In a Rabin condition, $\mathrm{Acc}$ is a finite list of pairs $(E_j, F_j)$ of sets of states, and a path is good when some $j$ has $\operatorname{Inf} \cap E_j = \emptyset$ and $\operatorname{Inf} \cap F_j \ne \emptyset$.
The run is accepting when every path is good, and $L(A)$ is the set of trees with an accepting run.

1. For every S2S formula $\varphi(X_1, \ldots, X_m)$, a Rabin tree automaton computable from $\varphi$ accepts exactly the $\{0,1\}^m$-trees that code satisfying assignments.
   Conversely, every language of a Rabin tree automaton is S2S-definable.
2. These languages are effectively closed under complement.
3. Emptiness of a Rabin tree automaton is decidable, and every nonempty language contains a regular tree, that is, a tree with only finitely many distinct subtrees.
4. S2S is [[decidable|HWC687ES0Q]].

## Remarks

### A first tree automaton

Take $\Sigma = \{a, b\}$ and the property "some node is labeled $a$".
An automaton with states $g$ ("go on searching") and $d$ ("done") checks it.
In state $g$ at a node labeled $b$, it sends $g$ to one child and $d$ to the other, and it may choose which.
In state $g$ at a node labeled $a$, it sends $d$ to both children, and in state $d$ it sends $d$ to both children whatever the label.
A path is good when it ends in $d$, which is a Rabin condition with the one pair $(\{g\}, \{d\})$.
So an accepting run is a guessed path from the root down to an $a$.
The automaton needs its freedom of choice, and we see below that no deterministic automaton does the job.

### Parity conditions and games

A parity condition is a priority map $\Omega \colon Q \to \mathbb{N}$, and a path is good for it when the largest priority in $\Omega(\operatorname{Inf})$ is even.
Rabin automata and parity automata recognize the same tree languages, by effective translations.
The modern proof rests on positional [[determinacy|QXECDPAYTN]] of parity games: in a parity game on a graph, from each vertex one of the two players has a winning strategy that depends only on the current vertex.
The [[proof|8YEEVRR5JY]] proves positional determinacy on finite graphs and the decidability of emptiness in full, cites complementation, and gives the translation of formulas in outline.

### Why the acceptance condition matters

Büchi tree automata ask for an accepting state infinitely often on every path, and they are strictly weaker.
Rabin showed in 1970 that the trees over $\{a, b\}$ in which every path has only finitely many $a$'s form a language that no Büchi tree automaton recognizes.
Its complement, "some path has infinitely many $a$'s", is Büchi-recognizable, so Büchi tree automata are not closed under complement.

### Why the logic must be monadic

Full second-order logic over $(T, s_0, s_1)$ can quantify over relations.
It then interprets arithmetic with addition and multiplication, so its theory is undecidable.

### Why the automata must be nondeterministic

No deterministic parity tree automaton accepts the trees with at least one $a$.
In a deterministic run, the state at a node depends only on the labels of its proper ancestors.
Take any path $\pi$ and a node $w$ off $\pi$.
The tree with a single $a$ at $w$ is accepted, and along $\pi$ it carries the same states as the all-$b$ tree, so $\pi$ is good in the all-$b$ tree.
Since $\pi$ was any path, every path of the all-$b$ tree is good, and the all-$b$ tree is accepted too, which is wrong.
So complementation, the step that determinism would make easy, is the hard part.

### What it gives you in logic

S1S is the theory of one branch of the binary tree, so [[Büchi's theorem on S1S|YPDXVTH5JR]] is a special case.
The monadic theory of the tree with countably many successors, SωS, is interpretable in S2S, and so it is decidable.
The monadic theory of $(\mathbb{Q}, <)$ is decidable, because $(\mathbb{Q}, <)$ is isomorphic to a definable subset of the tree with the left-to-right order.
Every countable linear order embeds in $(\mathbb{Q}, <)$, so a sentence holds in all countable linear orders exactly when it holds relativized to every subset $X$ of $\mathbb{Q}$.
Hence the monadic theory of the countable linear orders is decidable too.

### What it gives you in verification

Satisfiability of the [[modal mu-calculus|5BXYE8REDN]], of propositional dynamic logic and of CTL*, the extension of [[computation tree logic|1DA0Y6KDF8]], is decidable.
These logics are invariant under bisimulation, a satisfiable formula has a tree model of bounded branching, and statements about such trees translate into S2S.
Direct automata constructions give much better bounds than the route through S2S.
Satisfiability is EXPTIME-complete for the modal mu-calculus and 2EXPTIME-complete for CTL*.
Model checking the modal mu-calculus on a finite [[Kripke structure|NGHWZ9Y7ZV]] is equivalent to solving a finite parity game.

### The converse and its limits

Part 1 is an equivalence: the S2S-definable tree languages are exactly the languages of Rabin tree automata.
Decidability does not survive natural extensions.
Adding the relation "$x$ and $y$ are at the same depth" lets formulas interpret grids, whose monadic theory is undecidable, as in the [[proof of Seese's theorem|AW5XA4GYGH]].

### Generalizations

Gurevich and Harrington (1982) gave a proof of complementation by games.
Emerson and Jutla (1991) and, independently, Mostowski (1991) proved positional determinacy of parity games, which gives the shortest route to complementation.
Zielonka (1998) gave a recursive proof of positional determinacy that is also an algorithm for finite parity games.
Many decidable theories come from S2S by interpretation, and so do the decidable MSO theories of graphs of bounded treewidth in [[Courcelle's theorem|DD4JB8XJ5A]].

### Watch out

Do not expect the Büchi condition to be enough on trees, as it is on words.
"Every path has only finitely many $a$'s" needs a parity condition, for example with $\Omega(q_a) = 1$ and $\Omega(q_b) = 0$ in the automaton of the L2 explanation.
Then a path with infinitely many $a$'s sees priority $1$ infinitely often and is bad, and a path with finitely many sees only $0$ in the end and is good.

### Try it

Does the language of the first automaton contain a regular tree?
Yes: the tree with $a$ at the root and $b$ everywhere else has only two distinct subtrees, itself and the all-$b$ tree.

Why does S2S decide the monadic theory of $(\mathbb{N}, S)$?
Because the set $\{0\}^*$ is S2S-definable and $s_0$ restricted to it is a copy of the successor on $\mathbb{N}$, so every S1S sentence becomes an S2S sentence.

## History

Michael Rabin proved the theorem in 1969, in a long paper on second-order theories and automata on infinite trees.
His complementation proof was hard to read, and simpler proofs used infinite games: Gurevich and Harrington in 1982, and Emerson and Jutla and Mostowski in 1991 with parity games.
Many later decidability results in logic and verification come from an interpretation of a theory in S2S.

## Explanations

### L1 human

Picture a tree that starts at a root and splits in two at every node, forever.
Every node carries a letter, for example $a$ or $b$.
A tree automaton walks down all branches at the same time and keeps a finite memory on each branch.
Rabin showed that such automata check every property of these trees that we can write with "for every node", "there is a set of nodes", "left child" and "right child".
He also showed how to decide whether any tree at all has the property, so the logic of the infinite binary tree is decidable.

### L2 human

We build a parity tree automaton for "every path has infinitely many $a$'s" over $\{a, b\}$, and we test it on two trees.

1. The states are $q_{\mathrm{in}}$, $q_a$ and $q_b$, with $\Omega(q_{\mathrm{in}}) = 0$, $\Omega(q_a) = 2$ and $\Omega(q_b) = 1$.
   A state $q_c$ at a node claims that the node has label $c$.
2. The transitions are $(q, c, q_{c'}, q_{c''})$ for all $c', c'' \in \{a, b\}$, where $q$ is $q_{\mathrm{in}}$ or $q_c$.
   So the automaton guesses the labels of the two children and checks each guess one level lower.
3. In an accepting run every node $w \ne \varepsilon$ has the state $q_{t(w)}$.
   Along a path, $q_a$ occurs infinitely often exactly when $a$ does, and then the largest priority seen infinitely often is $2$, which is even.
   Otherwise it is $1$, which is odd.
4. The tree with $t(w) = a$ for $|w|$ even and $t(w) = b$ for $|w|$ odd is accepted, because on every path the labels alternate.
5. The tree with $t(w) = a$ exactly for $w \in \{0\}^*$ is rejected, because on the path $1, 11, 111, \ldots$ every label is $b$.

The typical use is a decision procedure: write a property of trees, or of programs unfolded into trees, as an automaton and test emptiness.

### L3 human

Rabin's theorem completes the correspondence between monadic second-order logic and automata, from finite words through infinite words to infinite trees.
The modern proof is a game: acceptance of a tree is a game between the automaton and a pathfinder, complementation follows from positional determinacy of parity games, and emptiness becomes the solution of a finite parity game.
The same games give the semantics of the modal mu-calculus.
Solving finite parity games is a central open problem of algorithms: it is in NP and in co-NP, and quasi-polynomial algorithms are known, but no polynomial algorithm is known.
