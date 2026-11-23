---
tag: NT5RAK54G3
kind: proof
name: Proof of the Büchi-Elgot-Trakhtenbrot theorem by automata for formulas
msc: ["03B25", "03D05"]
topics: [E4AVTNWE9E]
audience: grad
proves: AK66XQ59Z3
uses: [18WVBDCS38, W65B6BKZRY, SFMYM96C1B, DDVYP8RNG8, 446KZ8HJ5F, K7XDVK5854]
methods: [12MQ2NJ29A, 0ASJVEFA9J, 01XM7JEKHY, X5HG1RNWQX]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%BCchi%E2%80%93Elgot%E2%80%93Trakhtenbrot_theorem
    locator: Proof overview
  - url: https://en.wikipedia.org/wiki/Monadic_second-order_logic
    locator: Decidability and complexity of satisfiability
---

## Proof

We turn automata into sentences by writing their runs as sets, and sentences into automata by induction on the formula.
We use the notation of the [[statement|AK66XQ59Z3]].
Part A proves that regular languages are MSO-definable, Part B proves the converse, Part C proves part 3 and Part D proves the decidability of WS1S.

### Part A: from an automaton to a sentence

1. Let $L \subseteq \Sigma^+$ be regular.
   Then a [[deterministic finite automaton|W65B6BKZRY]] $A = (Q, \Sigma, \delta, q_{\mathrm{in}}, F)$ recognizes $L$.
2. Write $\operatorname{first}(x)$ for $\neg \exists z \, (z < x)$, $\operatorname{last}(x)$ for $\neg \exists z \, (x < z)$, and $S(x, y)$ for $x < y \wedge \neg \exists z \, (x < z \wedge z < y)$.
   These formulas say "first position", "last position" and "$y = x + 1$".
3. Take one set variable $X_q$ for each $q \in Q$, read as "the state after the letter at this position is $q$".
   Let $\varphi_A$ be $\exists (X_q)_{q \in Q} \, (\mathrm{Part} \wedge \mathrm{Init} \wedge \mathrm{Trans} \wedge \mathrm{Acc})$, with the four parts of steps 4 to 7.
4. $\mathrm{Part}$ says that every position lies in exactly one $X_q$, so it is $\forall x \, \bigl( \bigvee_q x \in X_q \wedge \bigwedge_{q \ne q'} \neg(x \in X_q \wedge x \in X_{q'}) \bigr)$.
5. $\mathrm{Init}$ is $\forall x \, \bigl( \operatorname{first}(x) \to \bigwedge_{a \in \Sigma} (P_a(x) \to x \in X_{\delta(q_{\mathrm{in}}, a)}) \bigr)$.
6. $\mathrm{Trans}$ is $\forall x \, \forall y \, \bigl( S(x, y) \to \bigwedge_{q \in Q, \, a \in \Sigma} ((x \in X_q \wedge P_a(y)) \to y \in X_{\delta(q, a)}) \bigr)$.
7. $\mathrm{Acc}$ is $\forall x \, \bigl( \operatorname{last}(x) \to \bigvee_{q \in F} x \in X_q \bigr)$.

### Part A: the sentence defines the language

8. Let $w = a_0 \cdots a_{n-1}$, and let $r_0 = q_{\mathrm{in}}$, $r_{i+1} = \delta(r_i, a_i)$ be the run of $A$ on $w$.
   Then $w \in L$ if and only if $r_n \in F$.
9. Suppose $r_n \in F$, and put $X_q = \{ i : r_{i+1} = q \}$.
   Each position $i$ lies only in $X_{r_{i+1}}$, so $\mathrm{Part}$ holds.
   $\mathrm{Init}$ and $\mathrm{Trans}$ hold by the definition of the run.
   $\mathrm{Acc}$ holds because $n - 1 \in X_{r_n}$ and $r_n \in F$, so $\underline{w} \models \varphi_A$.
10. Conversely, let sets $X_q$ satisfy the four conjuncts.
    We show $i \in X_{r_{i+1}}$ by [[induction|0ASJVEFA9J]] on $i$.
    For $i = 0$ this is $\mathrm{Init}$ with $a = a_0$.
    If $i \in X_{r_{i+1}}$, then $\mathrm{Trans}$ with $q = r_{i+1}$ and $a = a_{i+1}$ gives $i + 1 \in X_{r_{i+2}}$.
11. By $\mathrm{Part}$, the position $n - 1$ lies in $X_{r_n}$ and in no other $X_q$.
    By $\mathrm{Acc}$, it lies in some $X_q$ with $q \in F$, so $r_n \in F$ and $w \in L$.
12. Hence $\varphi_A$ defines $L$, and $\varphi_A$ is computed from $A$.

### Part B: only set variables

13. Let $\mathrm{MSO}_0$ have only set variables and the atomic formulas $\operatorname{Sing}(X)$ ("$X$ has exactly one element"), $X \subseteq Y$, $X \subseteq P_a$, and $X \prec Y$ ("some element of $X$ is smaller than some element of $Y$").
14. We translate each MSO formula $\psi$ into a formula $\psi^*$ of $\mathrm{MSO}_0$, and we replace each first-order variable $x$ by a new set variable $X_x$.
    Put $(x < y)^* = X_x \prec X_y$, $(x = y)^* = X_x \subseteq X_y \wedge X_y \subseteq X_x$, $P_a(x)^* = X_x \subseteq P_a$, and $(x \in Y)^* = X_x \subseteq Y$.
    Let $*$ commute with the connectives and with $\exists Y$, and put $(\exists x \, \psi)^* = \exists X_x \, (\operatorname{Sing}(X_x) \wedge \psi^*)$.
15. For an assignment $s$, let $s^*$ send $X_x$ to $\{ s(x) \}$ and keep the set variables.
    We claim that $\underline{w} \models \psi[s]$ if and only if $\underline{w} \models \psi^*[s^*]$, and we prove it by [[structural induction|12MQ2NJ29A]] on $\psi$.
16. In the atomic cases, $\{i\} \prec \{j\}$ holds if and only if $i < j$, and $\{i\}$ and $\{j\}$ include each other if and only if $i = j$.
    Also $\{i\} \subseteq P_a$ holds if and only if $a_i = a$, and $\{i\} \subseteq Y$ holds if and only if $i \in Y$.
17. The connectives and $\exists Y$ pass through the induction unchanged.
    For $\exists x \, \psi$, the variable $X_x$ ranges over the singletons $\{i\}$ exactly as $x$ ranges over the positions $i$, so the induction hypothesis gives the claim.

### Part B: words with extra tracks

18. Fix a sentence $\varphi$, rename its bound variables apart, and list the set variables $X_1, \ldots, X_m$ of $\varphi^*$.
    A word over $\Gamma = \Sigma \times \{0,1\}^m$ is a word $w$ over $\Sigma$ together with sets $U_1, \ldots, U_m$ of positions, where $U_j$ is the set of positions whose $j$-th bit is $1$.
    This is a bijection between $\Gamma^+$ and such tuples.
19. For a subformula $\psi$ of $\varphi^*$, let $L_\psi$ be the set of $u \in \Gamma^+$ whose tuple $(w, U_1, \ldots, U_m)$ gives $\underline{w} \models \psi[X_j \mapsto U_j]$.
    We show by structural induction that each $L_\psi$ is regular.
20. For $\operatorname{Sing}(X_j)$, two states $0$ and $1$ count the bits $1$ on track $j$.
    A second bit $1$ has no transition, and the accepting state is $1$.
21. For $X_i \subseteq X_j$, one accepting state suffices, with no transition on letters whose bit $i$ is $1$ and whose bit $j$ is $0$.
    The automaton for $X_i \subseteq P_a$ is the same, with "bit $j$ is $0$" replaced by "the letter is not $a$".
22. For $X_i \prec X_j$, take states $0, 1, 2$, with $2$ accepting, and let every letter loop on each state.
    A letter with bit $i$ equal to $1$ may also go from $0$ to $1$, and a letter with bit $j$ equal to $1$ may also go from $1$ to $2$.
    An accepting run makes these two moves at positions $p < q$ with $p \in U_i$ and $q \in U_j$, and such positions give an accepting run.

### Part B: connectives and quantifiers

23. By step 18 every word of $\Gamma^+$ codes exactly one tuple, so $L_{\neg \psi} = \Gamma^+ \setminus L_\psi$ and $L_{\psi \wedge \chi} = L_\psi \cap L_\chi$.
    These languages are regular by the [[closure properties|446KZ8HJ5F]], with the [[powerset construction|DDVYP8RNG8]] for the complement.
24. Let $g_j$ set bit $j$ of a letter to $0$.
    Then $L_{\exists X_j \, \psi} = g_j^{-1}(g_j(L_\psi))$, because a word lies in the right side exactly when some change of track $j$ gives a word of $L_\psi$, that is, when some set $U_j$ is a witness.
25. The image $g_j(L_\psi)$ is regular, because we can relabel the transitions of a [[nondeterministic automaton|SFMYM96C1B]].
    The preimage is regular, because a deterministic automaton can read $g_j(c)$ for each letter $c$.
26. Let $e(a) = (a, 0, \ldots, 0)$.
    Since the truth of the sentence $\varphi^*$ does not depend on the sets, step 15 gives $\{ w \in \Sigma^+ : \underline{w} \models \varphi \} = e^{-1}(L_{\varphi^*})$, and this language is regular.
    Each step is a construction, so the automaton is computed from $\varphi$.

### Part C: satisfiability and validity over finite words

27. Let $\varphi$ be an MSO sentence and let $A$ be the automaton of step 26.
    Then $\varphi$ is true in some nonempty word if and only if $L(A) \ne \emptyset$, and it is true in every nonempty word if and only if $\Sigma^+ \setminus L(A) = \emptyset$.
28. Emptiness of a finite automaton is decided by a search for a path from the start state to an accepting state.
    So both sets of part 3 are decidable.

### Part D: finite sets of natural numbers

29. For WS1S we use the translation of step 14 with $S(x, y)^* = \operatorname{Succ}(X_x, X_y)$, where $\operatorname{Succ}(X, Y)$ says that $X = \{p\}$ and $Y = \{p+1\}$ for some $p$.
    Step 15 holds in $(\mathbb{N}, S)$ with finite sets by the same induction, since singletons are finite.
30. A tuple of finite sets $U_1, \ldots, U_m \subseteq \mathbb{N}$ is coded by every word $u$ over $\{0,1\}^m$ whose length $\ell$ gives $U_j \subseteq \{0, \ldots, \ell - 1\}$ for all $j$.
    Every word codes exactly one tuple, and the tuple coded by $u$ is also coded by each word $u \bar 0^r$, where $\bar 0$ is the zero column.
31. Let $L_\psi$ be the set of all words whose tuple satisfies $\psi$ in $(\mathbb{N}, S)$.
    The automata of steps 20 and 21 work without change.
    For $\operatorname{Succ}(X_i, X_j)$ take states $0, 1, 2$ with $2$ accepting.
    Letters with bits $(0,0)$ on tracks $i, j$ loop on $0$ and on $2$, bits $(1,0)$ go from $0$ to $1$, and bits $(0,1)$ go from $1$ to $2$.
32. Negation and conjunction work as in step 23, with $(\{0,1\}^m)^*$ in place of $\Gamma^+$, because every word codes exactly one tuple.

### Part D: the quantifier and the decision

33. For $\exists X_j \, \psi$, a finite witness may contain positions beyond the end of the word.
    Let $M = g_j^{-1}(g_j(L_\psi))$, and we claim that $L_{\exists X_j \psi} = \{ u : u \bar 0^r \in M \text{ for some } r \ge 0 \}$.
34. If a finite witness $U_j$ exists, choose $r$ with $U_j \subseteq \{0, \ldots, |u| + r - 1\}$.
    Writing $U_j$ on track $j$ of $u \bar 0^r$ gives a word of $L_\psi$, so $u \bar 0^r \in M$.
    Conversely, a word of $L_\psi$ that agrees with $u \bar 0^r$ off track $j$ gives a finite witness, since $u$ and $u \bar 0^r$ code the same sets.
35. The right side of step 33 is regular.
    In an automaton for $M$, we declare accepting every state from which an accepting state is reachable by reading zero columns only, and a graph search finds these states.
36. For a sentence $\varphi$, the language $L_{\varphi^*}$ is either all words or empty, according to the truth of $\varphi$ in $(\mathbb{N}, S)$.
    The emptiness test of step 28 decides which case holds.

Parts A and B prove part 1, their constructions prove part 2, and Parts C and D prove parts 3 and 4.

## Idea

An automaton becomes a sentence when we guess its run: one set of positions for each state, with local checks of the transitions.
A sentence becomes an automaton by induction on the formula.
The free variables become extra tracks of the alphabet, negation becomes complement, conjunction becomes intersection, and an existential set quantifier becomes the projection that forgets a track.
First-order variables are first replaced by singleton set variables, so that only one kind of variable remains.
For WS1S the sets live in $\mathbb{N}$, so the projection must also allow extra zero columns at the end of the word.

## Variants

We can keep the first-order variables and use the alphabet $\Sigma \times \{0,1\}^m$, with the condition that the track of each first-order variable has exactly one bit $1$.
This is the same construction without the translation of step 14.

An algebraic proof replaces automata by finite monoids.
It uses the composition method of Feferman, Vaught and Shelah, which splits a word into two parts and combines the MSO types of the parts.

A third proof uses an Ehrenfeucht-Fraïssé game for MSO.
The game shows that the MSO types of quantifier depth $q$ form a congruence of finite index on words, and the Myhill-Nerode theorem then gives regularity.
