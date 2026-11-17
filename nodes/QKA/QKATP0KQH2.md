---
tag: QKATP0KQH2
kind: example
name: Converse well-foundedness is not a geometric frame rule
msc: ["03F05", "03B45", "03C07"]
topics: [R10RMQCJQX]
audience: grad
not_instance_of:
  - target: F46GV42XCE
    note: the frame condition of provability logic GL, transitivity with converse well-foundedness, is not first-order, so it is not a geometric implication and gives no geometric frame rule
uses: [VW8XP95XCB, WJK0YA4GP2, 0DQPNJNPYK, 1NR3HAWG9D]
sources:
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Compactness_theorem
    locator: lead section
---

## Example

[[Provability logic|WJK0YA4GP2]] GL is K with the axiom $\Box(\Box A \to A) \to \Box A$.
A frame validates this axiom exactly when $R$ is transitive and *converse well-founded*: there is no infinite chain $w_0 R w_1 R w_2 R \cdots$.
The frame rules of the [[definition of labelled sequent calculus|VW8XP95XCB]] come from geometric implications, which are first-order sentences in the language with one binary relation $R$.
We show that no set of first-order sentences defines the class of GL frames, so no set of geometric frame rules captures GL in this way.

**Claim.** There is no set $T$ of first-order sentences such that a frame satisfies $T$ exactly when it is transitive and converse well-founded.

1. Suppose that $T$ is such a set.
2. Add new constants $c_0, c_1, c_2, \dots$ to the language, and let $T'$ be $T$ together with the sentences $c_i R c_{i+1}$ for all $i \ge 0$.
3. Take a finite subset $F$ of $T'$. Let $n$ be larger than every index $i$ with $c_i$ in $F$.
4. Let $W = \{0, 1, \dots, n\}$, let $R$ be the strict order $<$, and interpret $c_i$ as $i$ for $i \le n$ and as $n$ for $i > n$.
5. The relation $<$ is transitive. It is converse well-founded, because a chain $w_0 < w_1 < \cdots$ in a set of $n + 1$ elements has at most $n + 1$ terms.
6. So $(W, <)$ satisfies $T$. It also satisfies each $c_i R c_{i+1}$ in $F$, because $i + 1 \le n$ and $i < i + 1$.
7. Every finite subset of $T'$ has a model, so the [[compactness theorem|1NR3HAWG9D]] gives a model $(W', R')$ of all of $T'$.
8. This model satisfies $T$, so $R'$ is converse well-founded by step 1.
9. It also satisfies $c_i R' c_{i+1}$ for all $i$, so the interpretations of $c_0, c_1, \dots$ form an infinite chain. This contradicts step 8.

So the claim holds.

**Consequence.** A geometric implication is a first-order sentence, so a set of geometric frame rules corresponds to a first-order class of frames.
By the claim, no such class equals the class of GL frames.
So GL is not of the form G3K$S$ for a set $S$ of geometric implications, read as the logic of the frames that satisfy $S$.

## Remarks

The condition that fails is the geometric form of the frame condition.
Converse well-foundedness says "every nonempty set of worlds has an $R$-maximal element", which quantifies over sets of worlds, not over worlds.
The claim shows that no first-order sentence can replace it.

A stronger statement holds: no class of frames defined by first-order sentences has GL as its logic.
If all frames of such a class validate GL, they are transitive and converse well-founded.
GL does not prove $\Box^{n+1}\bot$, since the strict order on $\{0, \dots, n+1\}$ refutes it at $0$.
If no frame of the class had an $R$-chain of $n + 1$ steps, then $\Box^{n+1}\bot$ would be valid on the class, and so it would be in GL.
So the class contains, for each $n$, a frame with an $R$-chain of $n + 1$ steps.
The compactness argument of steps 2 to 9 then gives a frame of the class with an infinite chain, a contradiction.

Negri gives a labelled calculus for GL by changing the rule ${\Box}$R instead of adding a frame rule.
The new rule infers $\Gamma \Rightarrow \Delta, x : \Box A$ from $x R y, y : \Box A, \Gamma \Rightarrow \Delta, y : A$, with $y$ fresh, and the calculus keeps Trans.
We check its soundness on a transitive, converse [[well-founded|0DQPNJNPYK]] frame.

10. Suppose that the conclusion fails, so some world $w$ with $\rho(x) R w$ refutes $A$.
11. The set $U$ of worlds $w$ with $\rho(x) R w$ that refute $A$ is nonempty. By converse well-foundedness, $U$ has an element $w_0$ with no $R$-successor in $U$.
12. Every successor $v$ of $w_0$ satisfies $\rho(x) R v$ by transitivity. Since $v \notin U$, $v$ satisfies $A$. Hence $\Box A$ holds at $w_0$.
13. With $\rho(y) = w_0$, the premise fails, so the rule is sound.

## Explanations

### L1 human

Labelled calculi turn properties of the reachability relation into proof rules.
This works for properties that talk about worlds one at a time, such as "every world reaches itself".
Provability logic needs the property "there is no endless chain of steps", and that talks about infinite chains.
The argument above shows that no list of simple properties of worlds can express it.
So this logic needs a different kind of rule, not a frame rule.

### L2 human

The proof is a compactness argument.

1. Assume that some first-order theory $T$ defines the frames without infinite ascending chains.
2. Add names $c_0, c_1, \dots$ and ask for $c_0 R c_1 R c_2 R \cdots$.
3. Each finite part has a finite model, a finite strict order.
4. Compactness gives one model of everything, and it has an infinite chain, which is a contradiction.

The typical use of this argument is to show that a property of structures is not first-order.
A trap is to think that GL has no cut-free labelled calculus at all: it has one, with a modified box rule.
