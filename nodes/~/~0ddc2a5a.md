---
tag: ~0ddc2a5a
kind: example
name: A Herbrand disjunction for a common upper bound of two elements
msc: ["03F07", "03B10"]
topics: [8XY7JYZKFW]
audience: research
instance_of: [~22b3510a]
uses: [~22b3510a, VZ21F10WRS, 0WCP0PVET6, MVCH6N9SNW]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand%27s_theorem
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Herbrand%27s_theorem
    locator: Generalizations of Herbrand's theorem
---

## Example

Let the language have a binary relation symbol $\le$ and two constant symbols $a$ and $b$.
Let $T$ be the universal theory with the two axioms
$$\forall x \, (x \le x), \qquad \forall x \, \forall y \, (x \le y \lor y \le x).$$
Let $\psi(z)$ be the quantifier-free formula $a \le z \land b \le z$.
The theorem is $T \vdash \exists z \, \psi(z)$: the elements $a$ and $b$ have a common upper bound.

For pure logic, [[Herbrand's theorem|VZ21F10WRS]] gives the following form of [[Herbrand analysis|~22b3510a]].
For a universal theory $T$ and a quantifier-free $\psi$, $T \vdash \exists z \, \psi(z)$ holds exactly when there are closed terms $t_1, \ldots, t_n$ and finitely many instances of the axioms of $T$ that imply $\psi(t_1) \lor \cdots \lor \psi(t_n)$ by propositional logic alone.
The disjunction $\psi(t_1) \lor \cdots \lor \psi(t_n)$ is a *Herbrand disjunction*.

Here the closed terms are $a$ and $b$, and we check that the Herbrand disjunction
$$(a \le a \land b \le a) \lor (a \le b \land b \le b)$$
follows from the three axiom instances $a \le a$, $b \le b$ and $a \le b \lor b \le a$.

1. Assume the three instances. The third one gives two cases.
2. Case $b \le a$. With the instance $a \le a$, the first disjunct $a \le a \land b \le a$ holds.
3. Case $a \le b$. With the instance $b \le b$, the second disjunct $a \le b \land b \le b$ holds.
4. In both cases the disjunction holds. The argument uses only the truth values of the atomic sentences $a \le a$, $b \le b$, $a \le b$ and $b \le a$, so the implication is a tautology.
5. So $T \vdash \exists z \, \psi(z)$, with the Herbrand terms $a$ and $b$.

No single term is enough.

6. Let $\mathcal M_1$ be the [[model|MVCH6N9SNW]] with domain $\{0, 1\}$, the usual order $\le$, $a = 0$ and $b = 1$. It satisfies both axioms, and $\psi(a)$ fails in it, since $b \le a$ means $1 \le 0$.
7. Let $\mathcal M_2$ be the same structure with $a = 1$ and $b = 0$. Here $\psi(b)$ fails, since $a \le b$ means $1 \le 0$.
8. By soundness, $T$ proves neither $\psi(a)$ nor $\psi(b)$.

The witness is given by cases: $z = b$ if $a \le b$, and $z = a$ otherwise.
This is the definition by cases of the witnessing step, written as a disjunction.

## Remarks

The example shows the base case of Herbrand analysis: in pure logic without induction, the witnesses are terms, and a [[proof by cases|0WCP0PVET6]] in the derivation turns into a disjunction of instances.
In a theory with induction, such as $\mathrm{I}\Sigma_1$, the disjunction is replaced by a function defined by cases and by recursion.

If we add a function symbol $\max$ with the axioms $\forall x \, \forall y \, (x \le \max(x, y))$ and $\forall x \, \forall y \, (y \le \max(x, y))$, then the single term $\max(a, b)$ is a witness, and the Herbrand disjunction has one member.
The definition by cases has moved into the new function symbol.

If we add a third constant $c$, the theorem $\exists z \, (a \le z \land b \le z \land c \le z)$ is no longer provable from the two axioms.
In the structure $\{a, b, c\}$ with $a \le b$, $b \le c$, $c \le a$ and $x \le x$ for each $x$, both axioms hold, but no element is above all three.
With the transitivity axiom it becomes provable, and its Herbrand disjunction uses the three terms $a$, $b$ and $c$ and instances of transitivity.

## Explanations

### L1 human

Take two numbers $a$ and $b$.
We know that one of them is at least as large as the other.
So one of them is at least as large as both, but which one depends on the numbers.
For $a = 3$ and $b = 5$ it is $5$, and for $a = 5$ and $b = 3$ it is again $5$, which is now $a$.
Herbrand's theorem says that the proof gives a short list of candidates, here "$a$ or $b$", and that one of them always works.

### L2 human

We check the Herbrand disjunction in all possible cases, with a truth table of the two atoms $p := (a \le b)$ and $q := (b \le a)$.
The axiom instances make $a \le a$ and $b \le b$ true, and they require $p \lor q$.

1. $p$ true, $q$ true: both disjuncts hold.
2. $p$ true, $q$ false: the first disjunct fails, since it needs $b \le a$. The second holds.
3. $p$ false, $q$ true: the first disjunct holds. The second fails, since it needs $a \le b$.
4. $p$ false, $q$ false: the axiom instance $p \lor q$ is false, so this row is excluded.

The typical use is in automated theorem proving: a prover searches for the Herbrand terms and then checks a propositional formula.
A trap is to look for one term that works in every model; Herbrand's theorem promises only a finite disjunction.
