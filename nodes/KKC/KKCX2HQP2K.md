---
tag: KKCX2HQP2K
kind: definition
name: Cutting planes
msc: ["03F20", "90C10"]
topics: [CBAF7J051K]
audience: research
defines: PR7VMJN5BH
uses: [3V24CYWDT6, T3SXVH3ZZC, 0B3D4C8YF2, 7NERHHWBWR, 6JSH907W5R]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Feasible interpolation
  - url: https://en.wikipedia.org/wiki/Cutting-plane_method
    locator: Gomory's cut
---

## Definition

Cutting planes is the proof system that refutes a CNF by adding integer linear inequalities and rounding the results.

In the [[pigeonhole formulas|RJ571F7FF0]], let $x, y, z$ say that pigeons $1$, $2$ and $3$ sit in hole $1$.
The clauses $\neg x \vee \neg y$, $\neg y \vee \neg z$ and $\neg x \vee \neg z$ become the inequalities $x + y \leq 1$, $y + z \leq 1$ and $x + z \leq 1$.
Add the three inequalities:
$$2x + 2y + 2z \leq 3.$$
At a $0$-$1$ point the left side is even, so we may divide by $2$ and round the right side down:
$$x + y + z \leq \lfloor 3/2 \rfloor = 1.$$
So at most one pigeon sits in hole $1$, and one line now says what three clauses said.

Fix variables $x_1, \dots, x_n$ with values in $\{0, 1\}$.
A *line* is an inequality $\sum_{i} a_i x_i \geq \gamma$ with integers $a_1, \dots, a_n$ and $\gamma$.
A [[clause|T3SXVH3ZZC]] $C$ becomes the line
$$\sum_{x \in C} x + \sum_{\neg x \in C} (1 - x) \geq 1,$$
with the constants moved to the right side, and a [[CNF formula|0B3D4C8YF2]] $F$ becomes the set of the lines of its clauses.
The *cutting-planes system* has these axioms and rules.

1. The clause axioms are the lines of the clauses of $F$.
2. The Boolean axioms are $x_i \geq 0$ and $-x_i \geq -1$ for each $i$.
3. Linear combination derives $\sum_i (\alpha a_i + \beta b_i) x_i \geq \alpha \gamma + \beta \delta$ from $\sum_i a_i x_i \geq \gamma$ and $\sum_i b_i x_i \geq \delta$, for integers $\alpha, \beta \geq 0$.
4. Division derives $\sum_i (a_i / c) x_i \geq \lceil \gamma / c \rceil$ from $\sum_i a_i x_i \geq \gamma$, for an integer $c \geq 1$ that divides every $a_i$.

A *derivation* from $F$ is a sequence of lines, each an axiom or the result of a rule applied to earlier lines.
A *refutation* of $F$ is a derivation whose last line is $0 \geq 1$.
The *length* of a derivation is its number of lines.
Its *size* is the total number of bits of all coefficients and constants, written in binary.

## Notation

We write CP for cutting planes.
A line is often written $a^{\mathsf T} x \geq \gamma$ with $a \in \mathbb{Z}^n$.
We write $\sum a_i x_i \leq \gamma$ for the line $\sum (-a_i) x_i \geq -\gamma$.
In the $\leq$ form the division rule rounds the right side down, and in the $\geq$ form it rounds up.
The division rule is also called the *Chvátal-Gomory rule*, and its result is a *Chvátal-Gomory cut*.
The *rank* of a derivation counts the divisions on the longest chain of premises.

## Remarks

### Why each rule is sound

Each rule keeps every $0$-$1$ point that satisfies its premises, so a CNF with a refutation has no satisfying assignment.
Linear combination needs $\alpha, \beta \geq 0$.
With $\alpha = -1$ the true line $x \geq 0$ would give $-x \geq 0$, which fails at $x = 1$.
Division needs that $c$ divides every $a_i$.
Then the left side $\sum (a_i / c) x_i$ is an integer at every integer point, and an integer that is at least $\gamma / c$ is at least $\lceil \gamma / c \rceil$.
[[Rounding without divisibility|3619VP5J7J]] shows a rule that drops this condition and derives a false line.

### Two worked refutations

The CNF with the four clauses $x \vee y$, $x \vee \neg y$, $\neg x \vee y$, $\neg x \vee \neg y$ has a [[refutation with 9 lines|Q0XHSP88VD]].
The lines of the first two clauses are $x + y \geq 1$ and $x - y \geq 0$, and their sum is $2x \geq 1$.
Division by $2$ gives $x \geq \lceil 1/2 \rceil = 1$.
In the same way the last two clauses give $-x \geq 0$, and the sum of the two results is $0 \geq 1$.
The point $x = y = 1/2$ satisfies all four clause lines, so no refutation can avoid division.

The opening computation is worked out in [[a Chvátal-Gomory cut for three pairwise exclusions|6RA1FTFWYR]].
It removes the point $(1/2, 1/2, 1/2)$, which satisfies all three pairwise lines but has $x + y + z = 3/2$.

### Resolution inside cutting planes

CP p-simulates [[resolution|6JSH907W5R]].
Let a resolution step derive $E = C \cup D$ from $C \vee x$ and $D \vee \neg x$.
Write $L_E = \sum_{y \in E} y + \sum_{\neg y \in E} (1 - y)$, so that the line of $E$ is $L_E \geq 1$.
Adding Boolean axioms for the missing literals turns the two premises into these lines:
$$L_E + x \geq 1, \qquad L_E + (1 - x) \geq 1.$$
Their sum is $2 L_E + 1 \geq 2$, that is, $2 L_E \geq 1$.
If $E$ has $k$ negative literals, the left side of $2 L_E \geq 1$ carries the constant $2k$, and moving it gives the right side $1 - 2k$.
Division by $2$ gives the right side $\lceil 1/2 - k \rceil = 1 - k$, which is exactly the line $L_E \geq 1$.
So a resolution refutation with $S$ clauses on $n$ variables becomes a CP refutation with $O(nS)$ lines, and CP is complete.

### What cutting planes can and cannot prove

The [[pigeonhole formulas have CP refutations of polynomial size|40KJ0VKNG7]], by a counting argument built from the opening step.
By [[Haken's theorem|4PCEYEW3JG]], resolution refutations of the same formulas need exponential size.
So CP is exponentially stronger than resolution.

[[Pudlák's theorem|5RYPXFF0G2]] gives the other side: the clique-coloring formulas need CP refutations of exponential length.
The measure here is the number of lines, so the bound holds even when the coefficients are huge.
The proof goes through [[feasible interpolation|59GJCM8C66]] and monotone real circuits.

### Relation to integer programming

CP is the proof form of the cutting-plane method of [[integer programming|7NERHHWBWR]].
A line derived by linear combination alone holds on the whole linear relaxation, where each $x_i$ ranges over $[0, 1]$.
Division cuts away parts of that polytope that contain no integer point.
The [[Gomory fractional cut|AZJMC8A93H]] of the simplex method is a cut of this kind.

### Watch out

In the $\geq$ form the right side rounds up.
So division of $-2x - 2y \geq -3$ by $2$ gives $-x - y \geq \lceil -3/2 \rceil = -1$, and not $-2$.
Rounding the wrong way gives a weaker line, which is sound but loses the cut.
A second slip is to read a lower bound for CP as a lower bound for stronger systems.
[[Frege systems|J2BAR09TPF]] p-simulate CP, and no superpolynomial lower bound is known for Frege.
A third slip is to mix the measures: a bound on length is stronger than a bound on size, since a line may have many bits.

### History

Chvátal related the rounding cuts to proofs in combinatorics in 1973.
Cook, Coullard and Turán studied CP as a propositional proof system in 1987, and they gave polynomial-size refutations of the pigeonhole formulas.
Pudlák proved the exponential lower bound on length in 1997.
In the same year Bonet, Pitassi and Raz proved lower bounds for CP refutations whose coefficients are bounded by a polynomial.

### Try it

First, derive a line from $x + y \geq 1$ and $x - y \geq 0$ that has only the variable $x$.
The sum is $2x \geq 1$, and division by $2$ gives $x \geq 1$.

Second, is the step from $3x + 3y \geq 2$ to $x + y \geq 1$ a CP step?
Yes: $3$ divides both coefficients, and $\lceil 2/3 \rceil = 1$.

## Explanations

### L1 human

Write true as $1$ and false as $0$.
Then the clause "$x$ or $y$" says $x + y \geq 1$.
Cutting planes reasons with such inequalities: it adds them, multiplies them by positive whole numbers, and divides them.
The division step uses the fact that a sum of whole numbers is a whole number.
For example, $2x \geq 1$ forces $x \geq 1$, because $x$ cannot be $1/2$.
A refutation ends with $0 \geq 1$, which shows that the clauses cannot all be true.

### L2 human

We refute the three clauses $x$, $\neg x \vee y$ and $\neg y$.
Their lines are $x \geq 1$, $-x + y \geq 0$ and $-y \geq 0$.
Add the first two lines:
$$x + (-x + y) \geq 1 + 0, \quad \text{that is,} \quad y \geq 1.$$
Add $-y \geq 0$ to this line, and the result is $0 \geq 1$.
The refutation has $5$ lines and needs no division.
Division is needed only when the clauses have a fractional solution, as in the four clauses on two variables.
The typical use of CP is counting: the pigeonhole formulas say that $n + 1$ ones fit into a sum that is at most $n$, and CP can add up both sides.

### L3 human

A CP refutation describes a chain of polytopes $P = P_0 \supseteq P_1 \supseteq \cdots$, where $P$ is the linear relaxation of the formula and each round of division removes non-integral parts.
The rank of a refutation is related to the Chvátal rank of $P$, the number of rounds of all cuts that reach the integer hull.
The lower bounds for CP use interpolation: a short refutation gives a small monotone real circuit, as in [[feasible interpolation|59GJCM8C66]].
Semialgebraic systems such as [[sum of squares|ZERBQSTZB5]] reason with polynomial inequalities instead of linear ones.
