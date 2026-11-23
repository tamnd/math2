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

An arbiter has the states $i$ (idle), $w$ (waiting) and $g$ (granted), with $L(i) = \emptyset$, $L(w) = \{\mathit{req}\}$ and $L(g) = \{\mathit{grant}\}$.
Its edges are $i \to i$, $i \to w$, $w \to g$ and $g \to i$, and it starts in $i$.
We check the [[CTL|1DA0Y6KDF8]] formula $\rho = AG(\mathit{req} \to AF\,\mathit{grant})$ at $i$.

1. The set $[\![ AF\,\mathit{grant} ]\!]$ is the least set $Z$ that contains the $\mathit{grant}$-states and every state all of whose successors are in $Z$.
2. Start with $Z_0 = \{g\}$.
   The only successor of $w$ is $g$, so $Z_1 = \{g, w\}$.
3. The state $i$ has the successor $i \notin Z_1$, so it is not added, and $[\![ AF\,\mathit{grant} ]\!] = \{g, w\}$.
4. The set $[\![ \mathit{req} \to AF\,\mathit{grant} ]\!]$ contains $w$, since $w \in \{g, w\}$, and the states $i$ and $g$, which have no request.
   So it is $\{i, w, g\}$.
5. Every state reachable from $i$ is in this set, so $i \models \rho$.

Now add the edge $w \to w$, so that a request may wait forever.

6. Then $w$ has the successor $w \notin Z_0$, so $w$ is not added, and $[\![ AF\,\mathit{grant} ]\!] = \{g\}$.
7. The reachable state $w$ has $\mathit{req}$ and fails $AF\,\mathit{grant}$, so $i \not\models \rho$.
   The path $i\,w\,w\,w \cdots$ is a counterexample.
8. The weaker formula $AG(\mathit{req} \to EF\,\mathit{grant})$ still holds, because $g$ is reachable from $w$.

## Remarks

The formula $\rho$ has an LTL twin, $G(\mathit{req} \to F\,\mathit{grant})$ read on all paths, and the two readings agree on every structure.
A [[model checker|VNY0VXVZ53]] reports the failure of step 7 as the lasso $i\,w^\omega$.
A fairness constraint, "if $w$ is visited infinitely often, then $w \to g$ is taken infinitely often", restores $\rho$ on fair paths.
The example shows the typical shape of a liveness bug: one self-loop at a waiting state is enough to break $AF$, while $EF$ does not notice it.

## Explanations

### L1 human

A server takes requests and grants them.
"Every request is surely granted later" is true when a waiting request always moves on to "granted".
If the server may also stay waiting forever, the sentence becomes false.
The weaker sentence "a grant is still possible" stays true.

### L2 human

Compute an $AF$ set from the goal states backwards, and add a state only when all its successors are already in the set.
Then check the implication at each reachable state.
In the arbiter, $w$ joins in the first round, and $i$ never joins, because of its own loop.
Watch out: $AG(\mathit{req} \to AF\,\mathit{grant})$ is not $AG\,\mathit{req} \to AG\,AF\,\mathit{grant}$, since the first is checked state by state.
