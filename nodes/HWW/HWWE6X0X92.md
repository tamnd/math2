---
tag: HWWE6X0X92
kind: proof
name: Proof of Courcelle's theorem via tree automata
msc: ["03B25", "05C85", "05C83"]
topics: [E4AVTNWE9E]
audience: research
proves: DD4JB8XJ5A
uses: [AK66XQ59Z3, 3VSFM7K70Z, DDVYP8RNG8, FJ5E6FZVRJ, G6X7SZSNC5, 0JD5C82QMB]
methods: [12MQ2NJ29A, 01XM7JEKHY, X5HG1RNWQX]
sources:
  - url: https://en.wikipedia.org/wiki/Courcelle%27s_theorem
    locator: Proof strategy and complexity
  - url: https://en.wikipedia.org/wiki/Tree_automaton
    locator: Closure
  - url: https://en.wikipedia.org/wiki/Tree_automaton
    locator: Recognizability
---

## Proof

We turn the sentence into a tree automaton, and we turn the graph into a tree that the automaton reads.
We use the notation of the [[statement|DD4JB8XJ5A]] and of [[tree automata|3VSFM7K70Z]].
Part A proves in full that MSO sentences about finite labeled trees are equivalent to deterministic bottom-up tree automata, the theorem of Thatcher and Wright and of Doner.
Part B encodes graphs of treewidth at most $k$ as labeled trees.
It is an outline, and the linear-time computation of tree decompositions is cited.

### Part A: terms and set variables

Let $\mathcal{F}$ be a ranked alphabet with arities at most $r$.
A term $t \in T(\mathcal{F})$ is the structure whose domain is its set of nodes, with a predicate $P_f$ for the nodes labeled $f$ and relations $\operatorname{Ch}_i(x, y)$, "$y$ is the $i$-th child of $x$", for $1 \le i \le r$.
For set variables $X_1, \ldots, X_m$, an annotated term is a term over $\mathcal{F} \times \{0, 1\}^m$, where $(f, b)$ has the arity of $f$.
Track $j$ marks the nodes in $X_j$.

1. Replace each first-order variable $x$ by a set variable $X$ that is a singleton.
   The atomic formulas become $\operatorname{Sing}(X)$, $X \subseteq Y$, $X \subseteq P_f$ and $\operatorname{Ch}_i(X, Y)$.
   Here $x = y$ becomes $X \subseteq Y \wedge Y \subseteq X$, and $x \in Y$ becomes $X \subseteq Y$.
2. The quantifier $\exists x \, \psi$ becomes $\exists X \, (\operatorname{Sing}(X) \wedge \psi^*)$.
   By structural induction, $\psi$ holds for nodes $u_1, \ldots$ exactly when $\psi^*$ holds for $\{u_1\}, \ldots$, as in Part B of the [[proof of the Büchi-Elgot-Trakhtenbrot theorem|NT5RAK54G3]].
3. Claim: for every formula $\varphi(X_1, \ldots, X_m)$ of this form there is a deterministic bottom-up automaton $A_\varphi$, computable from $\varphi$, whose language is the set of annotated terms that satisfy $\varphi$.
   We prove it by structural induction on $\varphi$ in steps 4 to 14.

### Part A: deterministic automata and closure

4. A bottom-up automaton is deterministic when for each $f$ and states $q_1, \ldots, q_n$ there is exactly one rule $f(q_1, \ldots, q_n) \to q$.
   Then it reaches exactly one state on each term, computed from the leaves upwards in one pass.
5. Determinization: given a nondeterministic automaton with states $Q$, use the subsets of $Q$ as states.
   The rule $f(S_1, \ldots, S_n) \to S$ has for $S$ the set of $q$ with a rule $f(q_1, \ldots, q_n) \to q$ and all $q_i \in S_i$.
   By induction on terms, the new automaton reaches the set of all states that the old one reaches.
   The final states are the sets that contain a final state.
6. Complement: in a deterministic automaton, exchange final and non-final states.
   Union: run two deterministic automata in parallel on pairs of states, and accept when either accepts.

### Part A: letter maps

7. Let $h$ map letters to letters of the same arity, applied node by node.
   If $A$ recognizes $L$, the rules $h(f)(q_1, \ldots, q_n) \to q$, for the rules $f(q_1, \ldots, q_n) \to q$ of $A$, recognize $h(L)$.
   A run of $A$ on $s$ is a run of the new automaton on $h(s)$.
   Conversely, a run on $t$ uses at each node a rule that comes from some $f$ with $h(f)$ the label, and these letters $f$ form a term $s$ with $h(s) = t$.
8. The automaton with the rules $f(q_1, \ldots, q_n) \to q$, for each $f$ such that $h(f)(q_1, \ldots, q_n) \to q$ is a rule of $A$, recognizes $h^{-1}(L)$.
   Its runs on $s$ are the runs of $A$ on $h(s)$.
   This step adds unused tracks to an automaton.

### Part A: the simple atomic formulas

9. For $\operatorname{Sing}(X)$ the states are $0$, $1$ and $2$, the number of marked nodes in the subtree, capped at $2$.
   A node with bit $b$ and children in states $c_1, \ldots, c_n$ gets $\min(2, b + c_1 + \cdots + c_n)$.
   The final state is $1$.
10. For $X \subseteq Y$ and $X \subseteq P_f$ the states are "ok" and "bad".
    A node becomes bad when a child is bad, when it is marked in $X$ but not in $Y$, or when it is marked in $X$ and has a label other than $f$.
    The final state is "ok".

### Part A: the child relation

11. The formula $\operatorname{Ch}_i(X, Y)$ means $X = \{u\}$ and $Y = \{v\}$ with $v$ the $i$-th child of $u$.
    The states are $0$ (no marks below), $y$ (the root of the subtree is the only mark, and it is in $Y$ only), "done" and "bad".
12. An unmarked node with all children in $0$ gets $0$.
    A node marked in $Y$ only, with all children in $0$, gets $y$.
    A node marked in $X$ only, with $i$-th child in $y$ and the others in $0$, gets "done".
    An unmarked node with one child in "done" and the others in $0$ gets "done".
    All other cases give "bad", and "done" is final.
13. By induction on the term, the state $y$ marks exactly the subtrees whose only mark is a $Y$-mark at the root.
    The state "done" marks exactly the subtrees whose marks are a node $u$ in $X$ and its $i$-th child in $Y$.
    So the automaton is correct.

### Part A: induction, evaluation and emptiness

14. For the inductive step, bring the automata of the subformulas to the same tracks by step 8.
    Then $\neg$ is step 6, and $\wedge$ is the complement of the union of the complements.
    The quantifier $\exists X_{m+1}$ is step 7 for the map that erases track $m+1$, followed by step 5.
    This proves the claim of step 3.
15. Conversely, every tree automaton language is MSO-definable.
    Guess one set $X_q$ per state for the run, and say that the sets partition the nodes, that each node obeys a rule, and that the root lies in a final $X_q$.
    We do not need this direction below.
16. For a sentence $\varphi$, $A_\varphi$ is a deterministic automaton over $\mathcal{F}$.
    Deciding $t \models \varphi$ means running $A_\varphi$ on $t$, which takes time linear in the size of $t$ for fixed $\varphi$.
17. For emptiness, let $R$ be the least set of states closed under the rules: if $f(q_1, \ldots, q_n) \to q$ is a rule and all $q_i \in R$, then $q \in R$.
    It is computed by iteration in at most $|Q|$ rounds, and by induction it is the set of states reached on some term.
    So $L(A) \ne \emptyset$ exactly when $R$ contains a final state.

### Part B: decomposition and colors

18. For fixed $k$, Bodlaender's algorithm finds a [[tree decomposition|FJ5E6FZVRJ]] of width at most $k$ in time linear in $n$, or reports that none exists.
    We cite this result.
19. The decomposition is turned in linear time into a rooted one whose nodes are of five kinds.
    These are a leaf with an empty bag, "introduce vertex", "forget vertex", "introduce edge", which adds one edge between two vertices of the bag, and "join", with two children and the same bag.
    The root bag is empty, and each edge is introduced exactly once.
20. The vertices are colored with $k + 1$ colors so that the vertices of each bag have distinct colors.
    Going down from the root, a vertex receives a color when it is forgotten, and it takes a color that the other vertices of the bag at that node do not use.
    Those vertices are forgotten higher up, so their colors are already fixed, and there are at most $k$ of them.

### Part B: the term and the translation

21. The labels are $\mathrm{leaf}$ of arity $0$, $\mathrm{intro}_j$, $\mathrm{forget}_j$ and $\mathrm{edge}_{jl}$ of arity $1$ for colors $j, l \le k$, and $\mathrm{join}$ of arity $2$.
    This is a finite ranked alphabet $\mathcal{F}_k$, and the term $t_G$ has size linear in $n$.
22. Every vertex of $G$ is forgotten exactly once, so vertices correspond to the $\mathrm{forget}$ nodes, and edges correspond to the $\mathrm{edge}$ nodes.
    An $\mathrm{edge}_{jl}$ node is incident to the vertex of the nearest ancestor labeled $\mathrm{forget}_j$, and to that of the nearest ancestor labeled $\mathrm{forget}_l$.
    The ancestor relation is the least transitive relation that contains $\operatorname{Ch}_1$ and $\operatorname{Ch}_2$, which is MSO-definable, so incidence is MSO-definable in $t_G$.
23. Replace vertex and edge variables by node variables restricted to these labels, and replace $\operatorname{inc}$ by its definition.
    This turns each MSO₂ sentence $\varphi$ into an MSO sentence $\varphi_k$ over $\mathcal{F}_k$ with $G \models \varphi$ exactly when $t_G \models \varphi_k$.

### Part B: the algorithm and the decidable theory

24. Compute $t_G$ by steps 18 to 21 and run the automaton $A_{\varphi_k}$ of Part A on it.
    Each stage takes time linear in $n$ for fixed $\varphi$ and $k$, which proves the theorem.
25. One MSO sentence over $\mathcal{F}_k$ says that a term is well formed: colors are used consistently, the children of a join agree, and the root has no color.
    Every well-formed term encodes a graph of treewidth at most $k$.
    So $\varphi$ holds in some such graph exactly when the automaton for "well formed and $\varphi_k$" has a nonempty language, which step 17 decides.
    A sentence belongs to the MSO₂ theory of the class exactly when its negation holds in no such graph, so the theory is decidable.

So Part A is proved in full, step 18 is cited, and steps 19 to 25 are an outline.

## Idea

An MSO sentence about trees becomes a finite automaton that runs from the leaves to the root, by the same closure properties that work for words.
A graph of treewidth at most $k$ is built from a tree of small bags, so it can be written as a term over finitely many operations.
The sentence about the graph becomes a sentence about the term, and the automaton evaluates it in one pass.

## Variants

Courcelle's own proof is algebraic: graphs with $k$ distinguished vertices form an algebra under gluing, and MSO-definable sets are recognizable, that is, they have finitely many classes under a congruence.
A game-based proof uses Ehrenfeucht-Fraïssé games for MSO: the MSO type of a glued graph of fixed quantifier depth depends only on the types of its parts.
For clique-width, the same scheme works with terms over the operations of clique-width expressions, for MSO₁ only.
