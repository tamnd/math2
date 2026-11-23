---
tag: GF8VBT1R3N
kind: proof
name: Proof of Church's theorem by encoding Turing machines
msc: ["03B25", "03D35"]
topics: [E4AVTNWE9E]
audience: ug2
proves: VA6BNNY2YC
uses: [758EYCN27B, TC69PEHAX7, Z7TN2B35B0, 5SDS9T8E7J, 983GZBQYT4, JTAH37JTHD]
methods: [6F55216R53, 0ASJVEFA9J, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Entscheidungsproblem
    locator: Negative answer
  - url: https://builds.openlogicproject.org/
    locator: Undecidability
  - book: isbn:9780521701464
---

## Proof

We reduce the [[halting problem|Z7TN2B35B0]] to validity: for each input $w$ we write a sentence $\varphi_w$ that is valid exactly when the machine halts on $w$.

### The machine

Let $M$ be a [[Turing machine|758EYCN27B]] with states $q_0, \ldots, q_m$, start state $q_0$, and tape symbols $a_0, \ldots, a_k$, where $a_0$ is the blank.
The tape has cells $0, 1, 2, \ldots$, and the head starts at cell $0$.
The instruction table is a partial map $\delta(q, a) = (r, b, D)$ with $D \in \{ \mathrm{L}, \mathrm{R} \}$, which means: write $b$, move in direction $D$, and enter state $r$.
A move to the left at cell $0$ leaves the head at cell $0$.
$M$ halts when it is in state $q$ reading $a$ and $\delta(q, a)$ is undefined.
An input word $w = b_0 b_1 \cdots b_{n-1}$ stands in cells $0$ to $n - 1$, and all other cells are blank.

We take $M$ to be a [[universal Turing machine|TC69PEHAX7]].
Then the set of words $w$ on which $M$ halts is not computable, because $M$ halts on a code of $(e, x)$ exactly when the machine with number $e$ halts on $x$.

### The signature

The signature $L_M$ has a constant $0$, a unary function symbol $'$, a binary relation symbol $<$, and binary relation symbols $Q_q$ and $C_a$ for each state $q$ and each symbol $a$.
The intended meaning of $Q_q(x, t)$ is "at time $t$ the machine is in state $q$ with the head at cell $x$".
The intended meaning of $C_a(x, t)$ is "at time $t$ cell $x$ contains $a$".
The numeral $\bar{n}$ is the term $0'' \cdots '$ with $n$ strokes.

### The sentence

Let $\varphi_w$ be $(\pi \wedge \iota_w \wedge \tau) \to \eta$, with the four parts below.
For a variable $z$, let $F(z)$ be $\forall y \, (y \neq z \to \bigwedge_{c} (C_c(y, t) \to C_c(y, t')))$, which says that the cells other than $z$ keep their symbols from time $t$ to time $t'$.

- $\pi$ is the conjunction of $\forall x \, \forall y \, \forall z \, (x < y \wedge y < z \to x < z)$, $\forall x \, (x < x')$ and $\forall x \, \neg (x < x)$.
- $\iota_w$ is $Q_{q_0}(0, 0) \wedge \bigwedge_{i < n} C_{b_i}(\bar{i}, 0) \wedge \forall y \, (y \neq \bar{0} \wedge \cdots \wedge y \neq \overline{n-1} \to C_{a_0}(y, 0))$.
- $\tau$ has, for each $\delta(q, a) = (r, b, \mathrm{R})$, the axiom $\forall x \, \forall t \, (Q_q(x, t) \wedge C_a(x, t) \to Q_r(x', t') \wedge C_b(x, t') \wedge F(x))$, and for each $\delta(q, a) = (r, b, \mathrm{L})$, the two axioms $\forall x \, \forall t \, (Q_q(x', t) \wedge C_a(x', t) \to Q_r(x, t') \wedge C_b(x', t') \wedge F(x'))$ and $\forall t \, (Q_q(0, t) \wedge C_a(0, t) \to Q_r(0, t') \wedge C_b(0, t') \wedge F(0))$.
- $\eta$ is $\exists x \, \exists t \, \bigvee (Q_q(x, t) \wedge C_a(x, t))$, where the disjunction runs over the pairs $(q, a)$ with $\delta(q, a)$ undefined.

The map $w \mapsto \varphi_w$ is computable, since $\varphi_w$ is written down directly from $w$ and the table of $M$.

### Part 1: if $M$ halts on $w$, then $\varphi_w$ is valid

1. Let $q_t$, $h_t$ and $c_t(y)$ be the state, the head position and the symbol in cell $y$ after $t$ steps of $M$ on $w$.
   Let $T$ be the step at which $M$ halts.
2. Let $\mathcal{A}$ be an $L_M$-[[structure|983GZBQYT4]] that satisfies $\pi \wedge \iota_w \wedge \tau$.
   We show that $\mathcal{A} \models \eta$.
3. In $\mathcal{A}$ the numerals are distinct.
   For $i < j$, the axiom $\forall x \, (x < x')$ and transitivity give $\bar{i} < \bar{j}$, and irreflexivity then gives $\bar{i} \neq \bar{j}$.
4. We prove by [[induction|0ASJVEFA9J]] on $t \le T$ the claim $P(t)$: $\mathcal{A} \models Q_{q_t}(\bar{h}_t, \bar{t})$, and $\mathcal{A} \models C_{c_t(y)}(\bar{y}, \bar{t})$ for every $y \in \mathbb{N}$.
5. $P(0)$ holds by $\iota_w$.
   For a cell $y \ge n$, step 3 gives $\bar{y} \neq \bar{i}$ for each $i < n$, so the last conjunct of $\iota_w$ gives $C_{a_0}(\bar{y}, 0)$.

### Part 1, continued: the induction step

6. Assume $P(t)$ with $t < T$.
   Then $\delta(q_t, c_t(h_t)) = (r, b, D)$ is defined, since $M$ does not halt at step $t$.
7. Case $D = \mathrm{R}$.
   The axiom of $\tau$ for this instruction, with $x = \bar{h}_t$ and $t = \bar{t}$, gives $Q_r(\overline{h_t + 1}, \overline{t + 1})$ and $C_b(\bar{h}_t, \overline{t + 1})$, which are the new state, head and symbol.
8. Case $D = \mathrm{L}$ and $h_t \ge 1$.
   The first axiom, with $x = \overline{h_t - 1}$ so that $x' = \bar{h}_t$, gives $Q_r(\overline{h_t - 1}, \overline{t + 1})$ and $C_b(\bar{h}_t, \overline{t + 1})$.
9. Case $D = \mathrm{L}$ and $h_t = 0$.
   The second axiom gives $Q_r(0, \overline{t + 1})$ and $C_b(0, \overline{t + 1})$, and the head of $M$ stays at cell $0$.
10. In each case the conjunct $F$ holds at the old head position $\bar{h}_t$.
    For $y \neq h_t$, step 3 gives $\bar{y} \neq \bar{h}_t$, so $F$ and $P(t)$ give $C_{c_t(y)}(\bar{y}, \overline{t + 1})$.
    Since $c_{t+1}(y) = c_t(y)$, this proves $P(t + 1)$.
11. By $P(T)$, $\mathcal{A} \models Q_{q_T}(\bar{h}_T, \bar{T}) \wedge C_{c_T(h_T)}(\bar{h}_T, \bar{T})$.
    The pair $(q_T, c_T(h_T))$ has no instruction, because $M$ halts at step $T$.
12. So $\eta$ holds in $\mathcal{A}$ with $x = \bar{h}_T$ and $t = \bar{T}$.
    Since $\mathcal{A}$ was arbitrary, $\varphi_w$ is valid.

### Part 2: if $M$ does not halt on $w$, then $\varphi_w$ is not valid

13. Let $\mathcal{N}$ be the structure with domain $\mathbb{N}$, with $0$, $x' = x + 1$ and the usual order $<$.
    Let $Q_q(x, t)$ hold when $q_t = q$ and $h_t = x$, and let $C_a(x, t)$ hold when $c_t(x) = a$.
    These are defined for every $t$, because $M$ runs forever.
14. $\mathcal{N} \models \pi$, because the usual order on $\mathbb{N}$ is transitive and irreflexive, and $x < x + 1$.
15. $\mathcal{N} \models \iota_w$, because at time $0$ the state is $q_0$, the head is at cell $0$, the word $w$ fills cells $0$ to $n - 1$, and the other cells are blank.
16. $\mathcal{N} \models \tau$.
    If $Q_q(x, t) \wedge C_a(x, t)$ holds, then at time $t$ the machine is in state $q$ at cell $x$ reading $a$.
    One step of $M$ then makes the conclusion of the matching axiom true, including $F$, since only the cell under the head changes.
17. $\mathcal{N} \not\models \eta$.
    At each time $t$, $Q_q(x, t) \wedge C_a(x, t)$ holds only for $q = q_t$, $x = h_t$ and $a = c_t(h_t)$, and $\delta(q_t, c_t(h_t))$ is defined, since $M$ never halts.
18. So $\mathcal{N}$ satisfies the premises of $\varphi_w$ and not its conclusion, and $\varphi_w$ is not valid.

### Conclusion

19. By parts 1 and 2, $M$ halts on $w$ if and only if $\varphi_w$ is valid.
    So $w \mapsto \varphi_w$ is a computable [[many-one reduction|JTAH37JTHD]] of the halting set of $M$ to the set of [[valid|5SDS9T8E7J]] $L_M$-sentences.
20. If validity were computable, we could decide whether $M$ halts on $w$ by computing $\varphi_w$ and testing its validity.
    This contradicts the choice of $M$.
21. So the set of valid $L_M$-sentences is not computable, and the signature $L_M$ is finite.
    This proves the theorem.

## Idea

A run of a machine is a sequence of configurations indexed by time.
The relations $Q_q(x, t)$ and $C_a(x, t)$ describe the configurations, and universal axioms describe one step.
If the machine halts, every structure that obeys the axioms contains a copy of the finite run, and so a halting configuration.
If it does not halt, the run itself is a structure on $\mathbb{N}$ in which no halting configuration occurs.
Notice the asymmetry: Part 1 must handle every structure, while Part 2 needs only one.

## Variants

Turing's proof of 1936 uses the same idea with a different coding of configurations.
You can also use a binary relation $S(x, y)$ for successor in place of a function symbol, and then the axioms must also say that every element has a successor.
With more work, the relations $Q_q$ and $C_a$ can be coded by one binary relation symbol, so validity is undecidable for a signature with one binary relation symbol.

A proof through arithmetic is the [[proof of Church's theorem from Robinson arithmetic|7PV025KTPE]].
With finite structures in place of $\mathbb{N}$, the same encoding proves [[Trakhtenbrot's theorem|XP6FW2WDWT]].
