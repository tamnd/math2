---
tag: X1GJ1JS06Y
kind: example
name: The response property AG(req → AF grant) on a small arbiter
msc: ["03B44", "68Q60"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [F6JA5C5BJX]
uses: [1DA0Y6KDF8, RFQ8DJZNQT, VNY0VXVZ53]
sources:
  - url: https://en.wikipedia.org/wiki/Computation_tree_logic
    locator: section Examples
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 6
---

## Example

An arbiter has the states $i$ (idle), $w$ (waiting) and $g$ (granted), with $L(i) = \emptyset$, $L(w) = \set{\mathit{req}}$, $L(g) = \set{\mathit{grant}}$.
Its edges are $i \to i$, $i \to w$, $w \to g$ and $g \to i$, and it starts in $i$.
We check the [[CTL|1DA0Y6KDF8]] formula $\rho = AG(\mathit{req} \to AF\,\mathit{grant})$ at $i$.

1. $[\![ AF\,\mathit{grant} ]\!]$ is the least set $Z$ that contains the $\mathit{grant}$-states and every state all of whose successors are in $Z$.
2. Start with $Z_0 = \set{g}$. The only successor of $w$ is $g$, so $Z_1 = \set{g, w}$.
3. The state $i$ has the successor $i \notin Z_1$, so it is not added. So $[\![ AF\,\mathit{grant} ]\!] = \set{g, w}$.
4. $[\![ \mathit{req} \to AF\,\mathit{grant} ]\!]$ contains $w$, since $w \in \set{g, w}$, and the states without $\mathit{req}$. So it is $\set{i, w, g}$.
5. Every state reachable from $i$ is in this set, so $i \models \rho$.

Now add the edge $w \to w$, so a request may wait forever.

6. Then $w$ has the successor $w \notin Z_0$, and $w$ is not added. So $[\![ AF\,\mathit{grant} ]\!] = \set{g}$.
7. The reachable state $w$ has $\mathit{req}$ and fails $AF\,\mathit{grant}$, so $i \not\models \rho$. The path $i\,w\,w\,w \cdots$ is a counterexample.
8. The weaker formula $AG(\mathit{req} \to EF\,\mathit{grant})$ still holds, because $g$ is reachable from $w$.

## Remarks

The formula $\rho$ is also an LTL formula, read on all paths, and both readings agree.
A [[model checker|VNY0VXVZ53]] returns the lasso $i\,(w)^\omega$ as the counterexample in step 7.
A fairness constraint "$w \to g$ is taken infinitely often if $w$ is visited infinitely often" restores $\rho$ on fair paths.

## Explanations

### L1 human

A server takes requests and grants them.
"Every request is surely granted later" is true when a waiting request always moves to "granted".
If the server may also stay waiting forever, the sentence becomes false.
The weaker sentence "a grant is still possible" stays true.

### L2 human

1. Compute $AF$ sets from the goal states backwards.
2. Add a state only when all its successors are already in the set.
3. Then check the implication at each reachable state.

A trap: $AG(\mathit{req} \to AF\,\mathit{grant})$ is not $AG\,\mathit{req} \to AG\,AF\,\mathit{grant}$; the first is checked state by state.
