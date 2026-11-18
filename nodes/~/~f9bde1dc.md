---
tag: ~f9bde1dc
kind: definition
name: Cutting planes
msc: ["03F20", "90C10"]
topics: [CBAF7J051K]
audience: research
defines: PR7VMJN5BH
uses: [~8ae21f34, T3SXVH3ZZC, 0B3D4C8YF2, 7NERHHWBWR, ~586b5042]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Feasible interpolation
  - url: https://en.wikipedia.org/wiki/Cutting-plane_method
    locator: Gomory's cut
---

## Definition

Fix propositional variables $x_1, \dots, x_n$, and read the value $1$ as true and $0$ as false.
A *line* is a linear inequality $\sum_{i=1}^n a_i x_i \geq \gamma$ with integer coefficients $a_1, \dots, a_n$ and an integer $\gamma$.
A $0$-$1$ assignment *satisfies* a line when the inequality holds at that assignment.

A [[clause|T3SXVH3ZZC]] $C$ translates to the line
$$\sum_{x \in C} x + \sum_{\neg x \in C} (1 - x) \geq 1,$$
with the constants then moved to the right side.
A $0$-$1$ assignment satisfies this line exactly when it makes some literal of $C$ true.
For example, $x \vee \neg y \vee z$ translates to $x - y + z \geq 0$.
A [[CNF formula|0B3D4C8YF2]] $F$ translates to the set of the lines of its clauses.

The *cutting-planes proof system* has the following axioms and rules.

1. **Clause axioms.** The lines of the clauses of $F$.
2. **Boolean axioms.** The lines $x_i \geq 0$ and $-x_i \geq -1$ for $i = 1, \dots, n$.
3. **Linear combination.** From $\sum_i a_i x_i \geq \gamma$ and $\sum_i b_i x_i \geq \delta$, derive $\sum_i (\alpha a_i + \beta b_i) x_i \geq \alpha \gamma + \beta \delta$, for integers $\alpha, \beta \geq 0$.
4. **Division with rounding.** From $\sum_i a_i x_i \geq \gamma$, derive $\sum_i (a_i / c) x_i \geq \ceil{\gamma / c}$, for an integer $c \geq 1$ that divides every $a_i$.

A *cutting-planes derivation* from $F$ is a finite sequence of lines in which each line is an axiom or follows from earlier lines by a rule.
A *cutting-planes refutation* of $F$ is a derivation whose last line is $0 \geq 1$.

The measures of a derivation $\pi$ are these.

- The *length* of $\pi$ is the number of its lines.
- The *size* of $\pi$ is the total number of bits of the coefficients and constants of its lines, written in binary.
- The *rank* of a line is $0$ for an axiom, the larger rank of the premises for a linear combination, and one more than the rank of the premise for a division. The rank of $\pi$ is the largest rank of its lines.

## Notation

We write CP for the cutting-planes proof system.
A line is often written as $a^{\mathsf T} x \geq \gamma$, with $a \in \mathbb{Z}^n$.
We also write $\sum a_i x_i \leq \gamma$ for the line $\sum (-a_i) x_i \geq -\gamma$, and an equation for the pair of its two inequalities.
Division with rounding is also called the *Chvátal-Gomory rule*, and its conclusion is a *Chvátal-Gomory cut*.
In the $\leq$ form, division rounds the right side down: from $\sum a_i x_i \leq \gamma$ it derives $\sum (a_i / c) x_i \leq \floor{\gamma / c}$.

## Remarks

### Soundness and completeness

Each rule keeps every $0$-$1$ solution of its premises.
For linear combination, this holds because $\alpha, \beta \geq 0$, so the sum of two true inequalities with these weights is true.
For division, the left side $\sum (a_i / c) x_i$ is an integer at every integer point, since each $a_i / c$ is an integer.
It is at least $\gamma / c$, so it is at least $\ceil{\gamma / c}$.
The line $0 \geq 1$ has no solution, so a CNF with a refutation is unsatisfiable.

CP p-simulates [[resolution|~586b5042]].
Let a resolution step derive $E$ from $C \vee x$ and $D \vee \neg x$, where $E = C \cup D$.
Write $L_E = \sum_{y \in E} y + \sum_{\neg y \in E} (1 - y)$, so the line of $E$ is $L_E \geq 1$.
Add the Boolean axioms $y \geq 0$ or $1 - y \geq 0$ for the literals of $E$ that are not in $C$, and obtain $L_E + x \geq 1$ from the line of $C \vee x$.
In the same way, obtain $L_E + (1 - x) \geq 1$ from the line of $D \vee \neg x$.
The sum of the two lines is $2 L_E \geq 1$.
If $E$ has $k$ negative literals, this line is $2 \sum_{y \in E} y - 2 \sum_{\neg y \in E} y \geq 1 - 2k$.
Division by $2$ gives the right side $\ceil{(1 - 2k)/2} = 1 - k$, and this is the line $L_E \geq 1$ of $E$.
So a resolution refutation with $S$ clauses on $n$ variables gives a CP refutation with $O(nS)$ lines.
In particular, every unsatisfiable CNF has a CP refutation, so CP is complete.

### The two main facts

- [[The pigeonhole formulas have polynomial-size CP refutations|~d332f763]] (Cook, Coullard and Turán). By [[Haken's theorem|~dd16430c]], they need exponential size in resolution, so CP is exponentially stronger than resolution.
- [[Pudlák's lower bound|~8976ef2c]]: the clique-colouring formulas need CP refutations of exponential length. The proof goes through [[feasible interpolation|~afa24e9d]] and monotone real circuits.

### Relation to integer programming

CP is the proof-theoretic form of the cutting-plane method of [[integer programming|7NERHHWBWR]].
Every line derived by linear combination alone is valid for the polytope of the linear relaxation, in which each $x_i$ ranges over the interval $[0, 1]$.
Division cuts off parts of that polytope that contain no integer point.
The [[Gomory fractional cut|AZJMC8A93H]] of the simplex method is a cut of this kind.

### Examples on separate pages

- [[A CP refutation of the four clauses on two variables|~a30f1786]], which needs division.
- [[A Chvátal-Gomory cut for three pairwise exclusions|~103a4786]], which removes the point $(1/2, 1/2, 1/2)$.
- [[Rounding without divisibility is unsound|~0d8f2e9f]], a rule that is not a CP rule.

### Coefficients

The size of a CP refutation counts the bits of the coefficients, and the coefficients can be large.
Bonet, Pitassi and Raz (1997) proved lower bounds for CP refutations whose coefficients are bounded by a polynomial in $n$.
Impagliazzo, Pitassi and Urquhart (1994) studied tree-like CP, in which each line is used at most once as a premise.

## Explanations

### L1 human

Write "true" as $1$ and "false" as $0$.
Then the clause "$x$ or $y$" says $x + y \geq 1$.
Cutting planes reasons with such inequalities: it adds them, multiplies them by positive whole numbers, and divides them.
The division step uses that a sum of whole numbers is a whole number.
For example, $2x \geq 1$ with $x \in \set{0, 1}$ forces $x \geq 1$, because $x$ cannot be $1/2$.
A refutation ends with $0 \geq 1$, which shows that the clauses cannot all be true.

### L2 human

We refute the clauses $x$ and $\neg x \vee y$ and $\neg y$.

1. The lines are $x \geq 1$, $-x + y \geq 0$ and $-y \geq 0$.
2. Linear combination of the first two lines with $\alpha = \beta = 1$ gives $y \geq 1$.
3. Linear combination of $y \geq 1$ and $-y \geq 0$ gives $0 \geq 1$.

This refutation uses no division, and its length is $5$.
A typical use of CP is to count: the pigeonhole formulas say that $n + 1$ ones fit into a sum that is at most $n$.
A trap is to measure CP proofs by their length only: the size also counts the bits of the coefficients, and the two measures can differ.
A second trap is to divide when $c$ does not divide every coefficient, which is unsound.

### L3 human

CP refutations describe a sequence of polytopes $P = P_0 \supseteq P_1 \supseteq \cdots$, where $P$ is the linear relaxation of the formula and each division removes non-integral parts.
The rank of a refutation counts the rounds of division, and it is related to the Chvátal rank of $P$: the number of rounds of all possible cuts that reach the integer hull.
The lower bounds for CP use the interpolation method: a short refutation gives a small monotone real circuit, as in [[feasible interpolation|~afa24e9d]].
Stronger semialgebraic systems, such as the [[sum-of-squares system|~57cdb980]], reason with polynomial inequalities instead of linear ones.
A lower bound for CP says nothing about [[Frege systems|~3f0577bc]], which p-simulate CP.
