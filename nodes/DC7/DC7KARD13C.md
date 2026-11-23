---
tag: DC7KARD13C
kind: proof
name: Proof that LTL satisfiability and model checking are PSPACE-complete
msc: ["03B44", "68Q17", "68Q60"]
topics: [CQM9SRN8PM]
audience: grad
proves: RD9B213GJ5
uses: [BYMYN6GN8E, 92DM43HQZT, PFKWV5SFF5, 758EYCN27B, JWC9CE07Q2, 5XY87RKYJ4, V0K79AD81V]
methods: [0NTF6DMVAP, 01XM7JEKHY]
sources:
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapters 4 and 5
---

## Proof

We search the Büchi automaton of the formula without building it for the upper bounds, and we encode a Turing machine in a formula for the lower bounds.
We prove [[the complexity theorem|RD9B213GJ5]] with [[the translation theorem|BYMYN6GN8E]], [[Savitch's theorem|PFKWV5SFF5]] and a lasso lemma.
For the lower bound we give the construction of Sistla and Clarke and cite their check of correctness.

### Upper bound for satisfiability

1. A Büchi automaton has an accepting run if and only if it has a path from an initial state to an accepting state $q$ and a cycle through $q$.
   An accepting run visits some accepting $q$ infinitely often, because there are finitely many states, and two visits to $q$ give the cycle.
   Conversely, the path followed by the cycle forever is an accepting run.
2. If the automaton has $n$ states, the path and the cycle can be chosen of length at most $n$, by removing repeated states.
3. Let $\mathcal{A}_\varphi$ be the automaton of the translation theorem, with $n = 2^{O(\lvert\varphi\rvert)}$ states.
   The algorithm guesses $q$, and then guesses the path and the cycle one state at a time.
4. At each moment it stores the current state, the previous one, $q$ and a step counter up to $n$.
   Each takes $O(\lvert\varphi\rvert)$ bits, by part 3 of the translation theorem.
5. Each guessed step is checked against the rules of $\mathcal{A}_\varphi$ in polynomial time, without building $\mathcal{A}_\varphi$.
   So satisfiability is in NPSPACE, and NPSPACE equals PSPACE by Savitch's theorem.

### Upper bounds for model checking

6. A state $s$ fails $\varphi$ if and only if some path from $s$ has a label word that satisfies $\neg\varphi$.
7. Form the product of $M$ with $\mathcal{A}_{\neg\varphi}$.
   Its states are pairs $(m, B)$, and $(m, B) \to (m', B')$ when $m \to m'$ in $M$ and $\mathcal{A}_{\neg\varphi}$ moves from $B$ to $B'$ on the label of $m$.
8. A product state is accepting when $B$ is.
   Its accepting runs from $(s, B_0)$, with $B_0$ initial, correspond to the paths from $s$ whose label words satisfy $\neg\varphi$.
9. Apply steps 3 to 5 to the product.
   A product state needs $O(\log\lvert M \rvert + \lvert\varphi\rvert)$ bits, so "$s$ fails $\varphi$" is in PSPACE, and so is its complement.
10. The product has $\lvert M \rvert \cdot 2^{O(\lvert\varphi\rvert)}$ states and edges.
    A reachable accepting state on a cycle is found in linear time with [[strongly connected components|5XY87RKYJ4]], which gives part 3.

### Lower bound for satisfiability

11. Let $T$ be a deterministic Turing machine that runs in space $N = p(\lvert x \rvert)$ on input $x$, and that repeats its accepting configuration forever once it accepts.
    Every language in PSPACE is decided by such a machine.
    For fixed $T$, we build from $x$ in polynomial time a formula $\varphi_{T,x}$ that is satisfiable exactly when $T$ accepts $x$.
12. There is one atomic proposition for each tape symbol, one for each pair of a state and a symbol, and one for the separator $\#$.
    A word codes the configurations of $T$ in blocks of length $N + 1$, each ended by $\#$.
13. The formula is a conjunction.
    One conjunct says $G$("exactly one letter proposition is true"), and one says that the first block is the initial configuration on $x$, using $X^i$ for $i \le N$.

### Lower bound, continued

14. The content of a cell in the next configuration is a function $f$ of the three cells around it now.
    For all letters $a$, $b$, $c$, the window conjunct states the following:
$$G\big((a \wedge Xb \wedge X^2 c) \to X^{N+2} f(a, b, c)\big).$$
15. Read at the position of $a$, the operator $X^{N+2}$ reaches the position of $b$ in the next block, because $b$ is one step on and a block has length $N + 1$.
    The conjunct has $O(N)$ symbols for each triple, so the formula has polynomial size.
16. The last conjunct is $F\,\mathit{acc}$, where $\mathit{acc}$ is the disjunction of the letters with an accepting state.
17. Sistla and Clarke check that the models of $\varphi_{T,x}$ are exactly the codes of the accepting computations of $T$ on $x$, and we cite this check.
    So satisfiability is PSPACE-hard, which completes part 1.
18. Let $M_T$ have one state for each letter, all edges between them, and a start state $s$ with an empty label and edges to all letter states.
    The label words of paths from $s$ are $\emptyset$ followed by any word with exactly one letter at each position.
19. So $s$ fails $\neg X\varphi_{T,x}$ if and only if $\varphi_{T,x}$ is satisfiable.
    $M_T$ has polynomial size, so the complement of model checking is PSPACE-hard, and model checking is PSPACE-hard because PSPACE is closed under complement.
    This completes part 2.

## Idea

An LTL formula is equivalent to an automaton with exponentially many states, but each state is small.
So a nondeterministic search can walk through the automaton in polynomial space, keeping only the current state.
For hardness, the operator $X$ iterated $N + 2$ times links each tape cell to the same cell one configuration later.

## Variants

The upper bound can also be proved without automata.
One guesses an ultimately periodic model one position at a time and stores only the set of subformulas true there, which is the same search seen from the formula side.
