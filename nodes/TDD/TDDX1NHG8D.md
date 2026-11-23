---
tag: TDDX1NHG8D
kind: statement
role: theorem
name: De Jongh-Sambin fixed-point theorem
msc: ["03F45", "03B45"]
topics: [3E7M66WW6Q]
audience: research
uses: [61THBNS8WE, QQ6PZFGGB3, WJK0YA4GP2, 1ZRWVDYPX0, 3PRW76471J, SBMQ5QHG9W, 4NBAX3VRQ7, HACXBCM7SS]
about: [WJK0YA4GP2]
proofs: [6T82THKX5M]
history:
  notes: "Existence proved independently by de Jongh and by Sambin; uniqueness proved independently by Bernardi, de Jongh and Sambin."
sources:
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: History
  - book: isbn:9780521701464
---

## Statement

Every self-referential equation built from provability has a solution without self-reference, and the solution is unique up to provable equivalence.

Let $A(p)$ be a modal formula in which the variable $p$ is modalized: every occurrence of $p$ lies in the scope of some $\square$.
$A$ may contain other variables $q_1, \dots, q_k$.
For a formula $H$, $A(H)$ is the result of replacing every $p$ by $H$.
Write $\boxdot X := X \wedge \square X$, and let $r$ be a variable that does not occur in $A$.

1. Existence: there is a formula $H$ whose variables are among $q_1, \dots, q_k$ such that $\mathsf{GL} \vdash H \leftrightarrow A(H)$.
2. Uniqueness: $\mathsf{GL} \vdash \boxdot(p \leftrightarrow A(p)) \wedge \boxdot(r \leftrightarrow A(r)) \to (p \leftrightarrow r)$.
   Hence, if $\mathsf{GL} \vdash H \leftrightarrow A(H)$ and $\mathsf{GL} \vdash H' \leftrightarrow A(H')$, then $\mathsf{GL} \vdash H \leftrightarrow H'$.
3. Explicit form for one box: let $A(p) = B(\square C(p))$, where $B(x)$ is a formula in a new variable $x$ without $p$, and $C(p)$ is any formula.
   Then $H = B(\square C(B(\top)))$ is a fixed point.
4. Arithmetical form: let $*$ be a realization of $q_1, \dots, q_k$ for $\mathsf{PA}$, and write $A^*(\sigma)$ for the realization of $A$ with $p^* = \sigma$.
   If $\mathsf{PA} \vdash \sigma \leftrightarrow A^*(\sigma)$, then $\mathsf{PA} \vdash \sigma \leftrightarrow H^*$.

Here $\mathsf{GL}$ is the logic of the [[definition of provability logic|61THBNS8WE]].
The [[proof of the de Jongh-Sambin theorem|6T82THKX5M]] proves parts 2, 3 and 4 in full and cites the reduction of part 1 to part 3.

## Remarks

### A first computation

The first case to know is $A(p) = \neg \square p$, the equation of the Gödel sentence.
Part 3 with $B(x) = \neg x$ and $C(p) = p$ gives $B(\top) = \neg \top$, which is equivalent to $\bot$, and then $H = \neg \square \neg \top$, which is equivalent to $\neg \square \bot$.
So the equation is solved by the consistency statement:

$$\mathsf{GL} \vdash \neg \square \bot \leftrightarrow \neg \square \neg \square \bot.$$

Check: after negation this is $\square \bot \leftrightarrow \square(\square \bot \to \bot)$, and Löb's axiom gives the hard direction.

### Why each hypothesis is needed

The variable $p$ must be modalized.
For $A(p) = \neg p$, no formula $H$ has $\mathsf{GL} \vdash H \leftrightarrow \neg H$, because $\mathsf{GL}$ is consistent.
For $A(p) = p$, every formula is a fixed point, so uniqueness fails.

Löb's axiom is needed, and $\mathsf{K4}$ alone is not enough.
No formula $H$ has $\mathsf{K4} \vdash H \leftrightarrow \square \neg H$.
To see this, take the one-world frame with $a R a$, which validates $\mathsf{K4}$.
At $a$, $\square \neg H$ is true exactly when $\neg H$ is true, so $H \leftrightarrow \square \neg H$ fails at $a$.

The boxes in part 2 are needed too.
Without $\boxdot$, the formula $(p \leftrightarrow A(p)) \wedge (r \leftrightarrow A(r)) \to (p \leftrightarrow r)$ is not a theorem for $A(p) = \square p$.
Take two worlds with $1 R 2$, with $p$ true at both and $r$ false at both.
At $1$, both $p \leftrightarrow \square p$ and $r \leftrightarrow \square r$ hold, but $p \leftrightarrow r$ fails.
The box rules this model out, because $r \leftrightarrow \square r$ fails at the dead end $2$.

### What it gives you

The theorem computes what a self-referential sentence says.
We saw that the Gödel equation $p \leftrightarrow \neg \square p$ has the solution $\neg \square \bot$.
By part 4, every sentence $G$ with $\mathsf{PA} \vdash G \leftrightarrow \neg \mathrm{Prov}(\ulcorner G \urcorner)$ is equivalent in $\mathsf{PA}$ to the [[consistency statement|4NBAX3VRQ7]].

The [[Henkin sentences|SBMQ5QHG9W]] solve $p \leftrightarrow \square p$.
Part 3 with $B(x) = x$ gives $H = \square \top$, which is equivalent to $\top$.
So every sentence that says "I am provable" is provable, which is Löb's answer to Henkin.

In the same way, $A(p) = \square \neg p$ gives $H = \square \neg \top$, which is equivalent to $\square \bot$.
A sentence that says "my negation is provable" is equivalent to the inconsistency of $\mathsf{PA}$.
For $A(p) = \square p \to q$, part 3 gives $\square q \to q$.
This is the sentence of the usual proof of [[Löb's theorem|3HD30YG3DG]].

The [[diagonal lemma|3PRW76471J]] gives fixed points in arithmetic, but it does not say what they mean.
Part 4 shows that, for modal $A$, all of them are equivalent to one explicit sentence.

### The converse

The converse of part 2 holds.
If $\mathsf{GL} \vdash H \leftrightarrow H'$ and $H$ is a fixed point, then $H'$ is a fixed point, by replacement of equivalents.
So the fixed points of $A$ are exactly the formulas that are equivalent to $H$.

### Generalizations

Part 4 holds for every theory to which [[Solovay's theorem|1ZRWVDYPX0]] applies, because its proof uses only realizations of theorems of $\mathsf{GL}$.
For the same reason, parts 1 to 3 hold in every extension of $\mathsf{GL}$ that is closed under the same rules.
Algebraically, the theorem says that in a [[Magari algebra|YTA4C8QCB0]] every term in which the variable is under the operator has a unique fixed point, and the fixed point is a term.

### Watch out

The formula $B(\top)$ is a step in the recipe, not the answer.
For $A(p) = \neg \square p$ we get $B(\top) = \bot$, and $\bot$ is not a fixed point.
Indeed $\bot \leftrightarrow \neg \square \bot$ would need $\mathsf{GL} \vdash \square \bot$, which fails at any world with no successor.
The correct move is to put $B(\top)$ back under the box: $H = B(\square C(B(\top)))$, here $\neg \square \bot$.

### Try it

1. Find the fixed point of $p \leftrightarrow q \wedge \square p$.
   Answer: $B(x) = q \wedge x$ and $B(\top)$ is equivalent to $q$, so $H = q \wedge \square q$.
   Check: $\square(q \wedge \square q)$ is equivalent to $\square q$ by axiom 4.
2. Find the fixed point of $p \leftrightarrow \neg \square \neg p$.
   Answer: $B(x) = \neg x$ and $C(p) = \neg p$, so $H = \neg \square \neg \bot$, which is equivalent to $\bot$.
3. Show that $p \leftrightarrow p \wedge \square p$ has two fixed points that are not equivalent.
   Answer: both $\top$ and $\bot$ solve it, which is allowed because $p$ is not modalized.

## History

Dick de Jongh and Giovanni Sambin found explicit fixed points independently, around 1975.
Claudio Bernardi, de Jongh and Sambin proved the uniqueness independently in the same years.

## Explanations

### L1 human

Some famous sentences of logic talk about themselves, such as "I am not provable" or "I am provable".
The theorem says that such a sentence, built from provability, can be rewritten without talking about itself.
For example, "I am not provable" says the same thing as "arithmetic is consistent".
It also says that two sentences with the same self-referential description say the same thing.

### L2 human

We find the fixed point of $A(p) = \neg \square p$ with part 3, and then we check it by hand.
First write $A(p) = B(\square C(p))$ with $B(x) = \neg x$ and $C(p) = p$.
Then $B(\top) = \neg \top$, and the recipe gives $H = \neg \square \neg \top$, which is equivalent to $\neg \square \bot$.

To check $H \leftrightarrow A(H)$, negate both sides.
We must prove:

$$\mathsf{GL} \vdash \square \bot \leftrightarrow \square \neg \square \bot.$$

From left to right, $\bot \to \neg \square \bot$ is a tautology, so its boxed form gives $\square \bot \to \square \neg \square \bot$.
From right to left, $\neg \square \bot$ is $\square \bot \to \bot$.
So $\square \neg \square \bot$ is the antecedent of Löb's axiom for $\bot$, and the axiom gives $\square \bot$.

The problem shows the typical use: the recipe gives a candidate, and Löb's axiom confirms it.
The theorem needs $p$ under a box, and "I am false" has no fixed point at all.

### L3 human

Self-reference through provability adds no expressive power.
Every such fixed point is already a Boolean and modal combination of the parameters.
The theorem is related to the Beth definability property.
Part 2 says that $\boxdot(p \leftrightarrow A(p))$ defines $p$ implicitly, and part 1 gives an explicit definition.
Löb's axiom enters through Löb's rule in both halves, and this is why the theorem fails for $\mathsf{K4}$.
