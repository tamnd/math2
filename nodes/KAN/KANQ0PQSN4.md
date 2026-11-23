---
tag: KANQ0PQSN4
kind: proof
name: Proof of McNaughton's theorem by truncation and max-min representation
msc: ["03B50", "06D35"]
topics: [WZP584JQ06]
audience: research
proves: E11A9H8Z7Q
uses: [JQ713VVD0G, DG496EV8FE]
methods: [12MQ2NJ29A, 0ASJVEFA9J, 0J0XBKG64S, 01XM7JEKHY]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 3. Łukasiewicz logic
  - book: isbn:9780792360094
---

## Proof

We prove the easy direction by induction on formulas, and the hard direction by clipping each linear piece to $[0, 1]$ and gluing the pieces with $\max$ and $\min$.
Write $\tau(t) = \max(0, \min(1, t))$ for $t \in \mathbb{R}$, and $g^\# = \tau \circ g$.
In $[0, 1]$ we have $x \oplus y = \min(1, x + y)$, $\neg x = 1 - x$ and $x \odot y = \max(0, x + y - 1)$.
"Definable" means "equal to $f_\varphi$ for some formula $\varphi$".

### Part 1: definable functions are McNaughton functions

1. We use induction on $\varphi$.
   A variable $p_i$ gives $x_i$, and the constant $0$ gives the zero function.
2. If $f$ is continuous with integer pieces $g_j$, then $1 - f$ is continuous with the integer pieces $1 - g_j$.
3. If $f$ and $g$ are as in step 2, with pieces $g_j$ and $h_k$, then $\min(1, f + g)$ is continuous.
   Its pieces are $1$ and the sums $g_j + h_k$, which have integer coefficients.
4. The connectives $\to$, $\land$, $\lor$ and $\odot$ are defined from $\oplus$ and $\neg$, so the induction covers every formula.

### Part 2: truncations are definable

For an affine $g$ with integer coefficients, let its size be $\lvert m_1 \rvert + \dots + \lvert m_n \rvert$, leaving out the constant $m_0$.
We show that $g^\#$ is definable, by induction on the size.

5. Size $0$: $g = m_0$ is constant, and $g^\#$ is $0$ or $1$, defined by $0$ or $\neg 0$.
6. For real $a$ and $x \in [0, 1]$ we claim $\tau(a + x) = \min(1, \tau(a) + x) \odot \tau(a + 1)$.
   We check it in four cases.
7. If $a \ge 1$, both sides are $1$.
   If $a \le -1$, the left side is $0$, and the right side is $x \odot 0 = \max(0, x - 1) = 0$.
8. If $0 \le a \le 1$, then $\tau(a + 1) = 1$, and both sides are $\min(1, a + x)$.
   If $-1 \le a \le 0$, then $a + x \le 1$, and both sides are $\max(0, a + x)$.
9. For real $t$ we have $1 - \tau(t) = \tau(1 - t)$, by the three cases $t \le 0$, $0 \le t \le 1$ and $t \ge 1$.
10. Size $s > 0$ with some $m_i > 0$: put $q = g - x_i$.
    Then $q$ and $q + 1$ have size $s - 1$, so $q^\#$ and $(q + 1)^\#$ are definable.
11. By step 6 with $a = q(x)$, we get $g^\# = (q^\# \oplus x_i) \odot (q + 1)^\#$, which is definable.
12. Size $s > 0$ with all nonzero $m_i < 0$: then $1 - g$ has size $s$ and a positive coefficient.
    So $(1 - g)^\#$ is definable by steps 10 and 11, and $g^\# = \neg (1 - g)^\#$ by step 9.

### Part 3: a lemma on pieces

Let $D \subseteq \mathbb{R}^n$ be convex, and let $f \colon D \to \mathbb{R}$ be continuous with affine $g_1, \dots, g_k$ such that $f(x) \in \{g_1(x), \dots, g_k(x)\}$ for all $x$.
We claim that for all $x, y \in D$ some $j$ has $g_j(y) \ge f(y)$ and $g_j(x) \le f(x)$.

13. For $s \in [0, 1]$ put $\varphi(s) = f(y + s(x - y))$ and $h_j(s) = g_j(y + s(x - y))$.
    Each $h_j$ is affine in $s$, and $\varphi(s)$ is one of the values $h_j(s)$.
14. Let $J = \{j : h_j(0) \ge \varphi(0)\}$ and $\psi = \min_{j \in J} h_j$.
    The set $J$ is not empty, $\psi$ is concave, and $\psi(0) = \varphi(0)$, because some $h_j$ equals $\varphi$ at $0$.
15. It is enough to show $\psi(1) \le \varphi(1)$, since then the $j \in J$ with $h_j(1) = \psi(1)$ proves the claim.
    Assume, for contradiction, that $\psi(1) > \varphi(1)$.
16. Let $s_0 = \sup \{s \in [0, 1] : \varphi(s) \ge \psi(s)\}$.
    By continuity $s_0 < 1$, $\varphi(s_0) = \psi(s_0)$, and $\varphi < \psi$ on $(s_0, 1]$.

### Part 3, continued

17. Two different affine functions of $s$ agree at most at one point.
    So some interval $(s_0, s_0 + \delta)$ contains no point where two different $h_j$ agree.
18. On that interval the sets $\{s : \varphi(s) = h_i(s)\}$, one for each different function $h_i$, are closed, disjoint and cover it.
    The interval is connected, so $\varphi = h_i$ on all of it, for one $i$.
19. By continuity $h_i(s_0) = \psi(s_0)$, and $h_i < \psi$ just above $s_0$, by step 16.
20. The function $h_i - \psi$ is convex, is $0$ at $s_0$ and is negative just above $s_0$.
    By convexity it is positive on $[0, s_0)$, so in every case $h_i(0) \ge \psi(0) = \varphi(0)$.
21. Hence $i \in J$, so $\psi \le h_i$ everywhere, which contradicts step 19.

### Parts 4 and 5: the max-min form and the end

22. For $y \in D$ let $S_y = \{j : g_j(y) \ge f(y)\}$ and $F_y = \min_{j \in S_y} g_j$.
    Then $F_y(y) = f(y)$, since some $g_j$ equals $f$ at $y$.
23. By Part 3, for each $x$ some $j \in S_y$ has $g_j(x) \le f(x)$, so $F_y(x) \le f(x)$.
24. So $f = \max_{y \in D} F_y$, a maximum over the finitely many different sets $S_y$.
25. Now let $f$ be a McNaughton function with pieces $g_j$, and use step 24 with $D = [0, 1]^n$.
26. The map $\tau$ is non-decreasing, so it commutes with $\max$ and $\min$.
    Since $f$ has values in $[0, 1]$, we get $f = \tau \circ f = \max_y \min_{j \in S_y} g_j^\#$.
27. Each $g_j^\#$ is definable by Part 2.
    The maximum is defined by $(p \to q) \to q$, by [[the max example|DG496EV8FE]], and $\min(x, y) = 1 - \max(1 - x, 1 - y)$.

So every McNaughton function is definable, and with Part 1 this proves the theorem.

## Idea

Cut the function into its affine pieces.
Each piece, clipped to $[0, 1]$, is given by a formula that is built one unit of slope at a time, using the identity of step 6.
A continuous function made of affine pieces is a maximum of minima of those pieces, by the lemma of Part 3.
Łukasiewicz logic has both $\max$ and $\min$, so the glued function is a formula too.

## Variants

The proof above is constructive: from the list of pieces it computes a formula, although a long one.
Another constructive route, due to Mundici, triangulates the cube into unimodular simplices and writes $f$ through the hat functions of the triangulation.
