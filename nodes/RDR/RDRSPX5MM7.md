---
tag: RDRSPX5MM7
kind: example
name: AG EF p is not expressible in LTL
msc: ["03B44", "68Q60"]
topics: [CQM9SRN8PM]
audience: grad
not_instance_of:
  - target: RMJ56ZPA63
    note: the branching property AG EF p is not equivalent to any LTL formula, because two structures with the same set of paths disagree on it
uses: [8S64VZ6A1S, F6JA5C5BJX, RFQ8DJZNQT]
sources:
  - url: https://en.wikipedia.org/wiki/Computation_tree_logic
    locator: section Relations with other logics
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 6
---

## Example

The [[CTL|F6JA5C5BJX]] formula $AG\,EF p$ says that from every reachable state some $p$-state is reachable.
It is a reset property: the system can always return to a good state.
We show that no [[LTL|RMJ56ZPA63]] formula $\varphi$ is equivalent to it on [[Kripke structures|RFQ8DJZNQT]].

1. Let $M_1$ have states $s_0$ and $s_1$, edges $s_0 \to s_0$, $s_0 \to s_1$ and $s_1 \to s_1$, and $p$ true only at $s_1$.
2. Let $M_2$ be $M_1$ plus a state $s_2$, with edges $s_0 \to s_2$ and $s_2 \to s_2$, and $p$ false at $s_2$.
3. The paths of $M_1$ from $s_0$ have the label words $\emptyset^\omega$ (stay at $s_0$) and $\emptyset^n \{p\}^\omega$ for $n \ge 1$ (move to $s_1$ after $n$ steps).
4. The new paths of $M_2$ go from $s_0$ to $s_2$ and stay there, and their label words are $\emptyset^\omega$ again.
   So both structures have the same set of label words from $s_0$.
5. By [[the definition|8S64VZ6A1S]], whether $s_0$ satisfies an LTL formula depends only on this set.
   So $s_0$ satisfies $\varphi$ in $M_1$ exactly when it does in $M_2$.
6. In $M_1$ the reachable states are $s_0$ and $s_1$, and each of them reaches $s_1$, so $s_0 \models AG\,EF p$.
7. In $M_2$ the state $s_2$ is reachable and reaches only itself, so $s_2 \not\models EF p$ and $s_0 \not\models AG\,EF p$.
8. If $\varphi$ were equivalent to $AG\,EF p$, steps 5 to 7 would give a contradiction.
   So no such $\varphi$ exists.

## Remarks

The argument shows that LTL sees only the set of paths, not the places where they branch.
Together with [[the non-example for CTL|NCE59DW7ZA]], which gives an LTL formula with no CTL equivalent, it shows that LTL and CTL are incomparable.
Both formulas are expressible in [[CTL*|Y4XZ94GRXV]].
If we give $s_2$ an edge to $s_1$, then $s_2$ reaches a $p$-state and $M_2$ satisfies $AG\,EF p$ again, so the extra state alone is not the problem: its dead end is.

## Explanations

### L1 human

Two machines start in a waiting state.
In the first, you may wait or move to a good state, and then you stay good forever.
The second has an extra trap state that also looks like "waiting" from outside.
Every run of either machine looks like "wait, wait, and maybe good forever".
So a logic of single runs cannot tell them apart, but only the first machine can always get back to a good state.

### L2 human

The method has three steps.
List the label words of the paths from the initial state in both structures, check that the two lists are the same set, and find a branching property on which the structures differ.
Watch out: $AG\,F p$, which is $GFp$ in LTL, is not the same as $AG\,EF p$.
In $M_1$ the path that stays at $s_0$ forever violates $GFp$, although $AG\,EF p$ holds.
