---
tag: WX2B2GTGJX
kind: proof
name: Proof that relations definable in Büchi arithmetic are automatic
msc: ["03B25", "03D05"]
topics: [E4AVTNWE9E]
audience: research
proves: NSTECGT93D
uses: [18WVBDCS38, W65B6BKZRY, SFMYM96C1B, DDVYP8RNG8, 446KZ8HJ5F, 1DQ1M6ZWS4, K7XDVK5854]
methods: [12MQ2NJ29A, 01XM7JEKHY, X5HG1RNWQX]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%BCchi_arithmetic
    locator: Büchi arithmetic and automata
  - url: https://en.wikipedia.org/wiki/Cobham%27s_theorem
    locator: Formulation in logic
---

## Proof

We use the notation of the [[statement|NSTECGT93D]]: $\Sigma_k = \set{0, \ldots, k-1}$, words over $\Sigma_k^m$ are read as $m$ tracks, least significant digit first, and $\operatorname{val}$ gives their values.
We write $\bar 0$ for the column of zeros.
Parts A to C prove that every definable relation is $k$-automatic, effectively, and that the theory is decidable.
Part D proves the converse direction only in outline.

**Part A: Three closure facts.**

1. Regular languages over one alphabet are closed under complement, intersection and union, by the [[closure properties of regular languages|446KZ8HJ5F]]. For the complement we first make the automaton deterministic by the [[powerset construction|DDVYP8RNG8]].
2. Let $h \colon \Gamma \to \Delta$ be a map of finite alphabets, applied to words letter by letter. If $L \subseteq \Delta^*$ is regular, then $h^{-1}(L)$ is regular. A [[deterministic automaton|W65B6BKZRY]] for $L$ that reads $h(a)$ whenever the input letter is $a$ recognizes $h^{-1}(L)$.
3. If $L \subseteq \Gamma^*$ is regular, then $h(L)$ is regular. Take a [[nondeterministic automaton|SFMYM96C1B]] for $L$ and replace each transition $(p, a, q)$ by $(p, h(a), q)$. An accepting run of the new automaton on $u$ uses letters $a_j$ with $h(a_j) = u_j$, so it is an accepting run of the old one on a word $v$ with $h(v) = u$. Conversely an accepting run on $v \in L$ becomes an accepting run on $h(v)$.
4. Zero closure. Let $A$ be a nondeterministic automaton for $L \subseteq \Delta^*$ and let $\bar 0 \in \Delta$. Let $F'$ be the set of states from which some path labelled $\bar 0^r$, with $r \ge 0$, reaches an accepting state. With $F'$ as the accepting set, $A$ recognizes $Z(L) = \set{u : u \bar 0^r \in L \text{ for some } r \ge 0}$. Indeed a run on $u$ ends in $F'$ exactly when it extends to an accepting run on some $u \bar 0^r$.
5. The set $F'$ is computable: it is the set of states that reach an accepting state in the graph of the $\bar 0$-transitions.

**Part B: Automata for the formulas.**

6. Unnesting. An atomic formula $\alpha$ that is not of the forms $x = y$, $x + y = z$, $V_k(x) = y$ contains a subterm $s$ of the form $u + v$ or $V_k(u)$ with variables $u, v$. Replace $\alpha$ by $\exists z \, (s = z \wedge \alpha[z/s])$ with a new variable $z$. This is equivalent, because $s$ has a value, and it lowers the number of function symbols in $\alpha$. Repeating gives an equivalent formula whose atomic formulas have the three basic forms.
7. Fix such a formula $\varphi$. Rename bound variables so that each variable is bound at most once and no variable is both free and bound. Let $x_1, \ldots, x_m$ be all variables of $\varphi$, with the free ones first.
8. A word $w$ over $\Sigma_k^m$ codes the assignment $s_w$ with $s_w(x_i) = $ the $i$-th component of $\operatorname{val}(w)$. For each subformula $\psi$ let $L_\psi = \set{w \in (\Sigma_k^m)^* : (\N, +, V_k) \models \psi[s_w]}$. We prove by [[structural induction|12MQ2NJ29A]] that each $L_\psi$ is regular, with an automaton that we construct.
9. Equality. The one-state automaton that accepts the columns $(a, a)$ recognizes the pairs of tracks with equal values. Two tracks of the same length $L$ have equal values exactly when their digits agree, because base-$k$ representations of fixed length are unique.
10. Addition. The states are the carries $0$ and $1$; the start state and the only accepting state is $0$. On the column $(a, b, d)$, carry $c$ goes to carry $c'$ when $a + b + c = d + kc'$, and there is no transition otherwise. Since $a + b + c \le 2k - 1$, the carry $c'$ is $0$ or $1$.
11. Let the input have values $x, y, z$ and length $L$, and suppose the run reads $j$ columns with carries $c_0 = 0, c_1, \ldots, c_j$. Adding the equations of step 10 times $k^i$ for $i < j$ gives $\sum_{i < j} (a_i + b_i) k^i = \sum_{i < j} d_i k^i + c_j k^j$.
12. If the run reads all $L$ columns and ends with $c_L = 0$, step 11 with $j = L$ gives $x + y = z$.
13. Conversely, let $x + y = z$. If the run stops at column $j$, then $d_j \not\equiv a_j + b_j + c_j \pmod k$. Reducing $x + y = z$ modulo $k^{j+1}$ with step 11 gives $a_j + b_j + c_j \equiv d_j \pmod k$, a contradiction. So the run reads all columns, and step 11 with $j = L$ gives $z = z + c_L k^L$, so $c_L = 0$ and the word is accepted.
14. The function $V_k$. Use the states $s_0$ (start), $s$, $t$ and $u$, with $t$ and $u$ accepting. The transitions on columns $(a, b)$, with $a$ on the track of $x$ and $b$ on the track of $y$, are: $s_0 \xrightarrow{(0,0)} s$, $s \xrightarrow{(0,0)} s$, $s_0 \xrightarrow{(a,1)} t$ and $s \xrightarrow{(a,1)} t$ for $a \ne 0$, $t \xrightarrow{(b,0)} t$ for every $b$, $s_0 \xrightarrow{(0,1)} u$ and $u \xrightarrow{(0,0)} u$.
15. A word accepted in $t$ is $(0,0)^p (a,1) w'$ with $a \ne 0$ and only zeros on the $y$-track of $w'$. Then the first nonzero digit of $x$ is at position $p$, so $V_k(x) = k^p = y$. A word accepted in $u$ is $(0,1)(0,0)^r$, so $x = 0$ and $y = 1 = V_k(0)$.
16. Conversely, let $V_k(x) = y$. If $x \ge 1$ and its first nonzero digit is at position $p$, then $y = k^p$ has the single digit $1$ at position $p$, and the word follows the path to $t$. If $x = 0$, then $y = 1$, and the word is $(0,1)(0,0)^r$, accepted in $u$. The empty word codes $(0, 0)$, and it is rejected because $V_k(0) = 1 \ne 0$.
17. Atomic formulas on $m$ tracks. Let $\alpha$ be $R(x_{i_1}, \ldots, x_{i_p})$ for one of the three basic relations $R$, with repetitions allowed. Let $h \colon \Sigma_k^m \to \Sigma_k^p$ keep the components $i_1, \ldots, i_p$. Then $\operatorname{val}(h(w)) = (s_w(x_{i_1}), \ldots, s_w(x_{i_p}))$, so $L_\alpha = h^{-1}(L_R)$, which is regular by step 2.
18. Negation and conjunction. Every word codes exactly one assignment, so $L_{\neg \psi}$ is the complement of $L_\psi$, and $L_{\psi \wedge \chi} = L_\psi \cap L_\chi$. Step 1 applies. The other connectives and $\forall$ are expressed by $\neg$, $\wedge$ and $\exists$.
19. Quantifier. Let $\psi' = \exists x_i \, \psi$. Let $g$ set the $i$-th component of a column to $0$, and let $M = g^{-1}(g(L_\psi))$. So $M$ is the set of words that agree off track $i$ with some word of $L_\psi$ of the same length. By steps 2 and 3, $M$ is regular.
20. We claim $L_{\psi'} = Z(M)$, the zero closure of step 4. This is the step that handles padding: a witness for $x_i$ may need more digits than the word $u$ has.
21. Let $u \in L_{\psi'}$. Then some $b \in \N$ gives $(\N, +, V_k) \models \psi[s_u[x_i \mapsto b]]$. Choose $r$ with $|u| + r$ at least the number of base-$k$ digits of $b$. Write the digits of $b$ on track $i$ of $u \bar 0^r$; the result $v$ codes $s_u[x_i \mapsto b]$, so $v \in L_\psi$. Since $v$ agrees with $u \bar 0^r$ off track $i$, we get $u \bar 0^r \in M$ and $u \in Z(M)$.
22. Let $u \in Z(M)$, so $u \bar 0^r \in M$ for some $r$. Some $v \in L_\psi$ agrees with $u \bar 0^r$ off track $i$. Appended zero columns do not change values, so $s_v = s_u[x_i \mapsto b]$ with $b$ the value of track $i$ of $v$. Hence $\psi$ holds under $s_u[x_i \mapsto b]$, and $u \in L_{\psi'}$.
23. By step 4, $Z(M)$ is regular. This completes the induction: $L_\varphi$ is regular.
24. Let $\varphi$ have the free variables $x_1, \ldots, x_n$ with $n \ge 1$, and let $X$ be the relation it defines. Let $e \colon \Sigma_k^n \to \Sigma_k^m$ add $m - n$ zero components. Truth of $\varphi$ depends only on its free variables, so $e(w) \in L_\varphi$ exactly when $\operatorname{val}(w) \in X$. Hence $L_X = e^{-1}(L_\varphi)$ is regular by step 2, and $X$ is $k$-automatic.

**Part C: Effectiveness and decidability.**

25. Each step above is an algorithm: unnesting, renaming, the fixed automata of steps 9 to 16, the powerset construction, products, relabelling of transitions and the graph search of step 5. So a [[proof by algorithm|X5HG1RNWQX]] turns $\varphi$ into an automaton for $L_X$. This proves part 2 of the theorem.
26. Let $\sigma$ be a sentence, and let $x$ be a variable that does not occur in $\sigma$. The formula $\sigma \wedge x = x$ defines $\N$ if $\sigma$ is [[true|K7XDVK5854]] in $(\N, +, V_k)$ and $\emptyset$ otherwise.
27. Build its automaton by step 25. Its language is nonempty exactly when $\sigma$ is true. An automaton has a nonempty language exactly when some accepting state is reachable from the start state, which a graph search decides. So $\operatorname{Th}(\N, +, V_k)$ is decidable.

**Part D: The converse direction, in outline.**

28. The formula $V_k(y) = y$ defines the set $P_k$ of powers of $k$. The order is defined by $x < y \Leftrightarrow \exists u \, (x + u = y \wedge \neg(u + u = u))$, and the number $1$ is the value $V_k(z)$ at the unique $z$ with $z + z = z$.
29. For a digit $j < k$, let $D_j(x, y)$ say: $y \in P_k$, and $x = z + jy + t$ for some $z < y$ and some $t$ with $t = 0$ or $y < V_k(t)$. Here $jy$ abbreviates $y + \cdots + y$. If $y = k^p$, then $y < V_k(t)$ means that $k^{p+1}$ divides $t$, so $D_j(x, y)$ says exactly that the digit of $x$ at position $p$ is $j$.
30. Let a deterministic automaton with states $q_0, \ldots, q_s$ recognize $L_X$. A formula says: there are a power $\ell$ of $k$ above all $x_i$ and numbers $r_{q_0}, \ldots, r_{q_s}$ whose digits are $0$ or $1$, such that at each position $y \le \ell$ exactly one $r_q$ has digit $1$, the run starts in $q_0$, the transitions match the digits $D_j(x_i, y)$, and the state at position $\ell$ is accepting.
31. The numbers $r_q$ code the run of the automaton on a representation of $(x_1, \ldots, x_n)$, and they are unique when they exist. So the formula defines $X$. We do not write out this check in detail; it follows the proof of the automaton-to-logic direction of the [[Büchi-Elgot-Trakhtenbrot theorem|AK66XQ59Z3]].

Parts A to C prove that every relation definable in $(\N, +, V_k)$ is $k$-automatic, effectively, and that $\operatorname{Th}(\N, +, V_k)$ is decidable; part D outlines the converse.

## Idea

Numbers are words of digits, and a formula about numbers becomes an automaton on tuples of words.
Atomic formulas need small automata, the carry automaton being the main one.
Negation is complement, conjunction is intersection, and an existential quantifier is projection, followed by the zero closure, because a witness may be longer than the other numbers.
Decidability then reduces to the emptiness test for finite automata.

## Variants

One can work only with the shortest representations; then projection must be followed by a step that removes or adds trailing zero columns, and the bookkeeping moves but does not disappear.
A second route reduces Büchi arithmetic to weak monadic second-order logic of one successor: a number is coded by the finite set of positions of its nonzero digits in base $2$, and in base $k$ by $k - 1$ such sets.
