---
tag: BG9TYCJ7HP
kind: example
name: Muddy children puzzle
msc: ["03B42", "00A08"]
topics: [CQM9SRN8PM]
audience: ug3
instance_of: [EA34W4ERRE, 9465T2PWZT]
uses: [7BCMKF2P7X, RRRHWH9F6Y, VG7DWJBYB9, 0ASJVEFA9J, 8K0CMPQXXB]
sources:
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapters 1 and 2
  - url: https://en.wikipedia.org/wiki/Common_knowledge_(logic)
    locator: section Puzzle, section Solution, section Proof
---

## Example

Three children play outside, and children 1 and 2 get mud on their foreheads.
Each child sees the other two foreheads but not her own.
Their father says in public: "At least one of you is muddy."
Then he asks, round after round: "Does any of you know whether you are muddy?"
All children answer at the same time, truthfully, and they reason perfectly.

A world is a string $x \in \{0, 1\}^3$, where $x_i = 1$ means that child $i$ is muddy, so the actual world is $110$.
Child $i$ cannot tell $x$ from the string $x^i$ that differs from $x$ only at place $i$.
So at each world child $i$ considers exactly two worlds, $x$ and $x^i$, as long as both are still possible.
She knows whether she is muddy exactly when $x^i$ has been ruled out.

1. Before the father speaks, all 8 worlds are possible.
   His announcement deletes $000$, the only world where it is false, and leaves 7 worlds.
2. Round 1 at $110$: child 1 still considers $010$, child 2 still considers $100$, and child 3 still considers $111$.
   So all three say "no".
3. At $100$, $010$ and $001$ the muddy child's alternative is $000$, which is gone, so she would have said "yes".
   Everyone said "no", so those three worlds are deleted, and $\{110, 101, 011, 111\}$ remain.
4. Round 2 at $110$: child 1's alternative $010$ is gone, so she knows that she is muddy, and child 2 knows for the same reason.
   Child 3's alternative $111$ remains, so she says "no".

So the two muddy children say "yes" in round 2.
In general, with $k$ muddy children, every child says "no" in rounds $1$ to $k - 1$, and exactly the muddy children say "yes" in round $k$.

## Remarks

### The general argument

A world is now $x \in \{0, 1\}^n$, and $\lvert x \rvert$ counts its ones.
The worlds with the relations "differ at place $i$" form the [[hypercube graph|VG7DWJBYB9]].
Let $W_r$ be the set of worlds left after the announcement and $r$ rounds of "no".
Each announcement deletes worlds and keeps the relations on the rest, so child $i$ knows at $x \in W_r$ exactly when $x^i \notin W_r$.
We prove by [[induction|0ASJVEFA9J]] on $r$ that $W_r = \{x : \lvert x \rvert \ge r + 1\}$.

1. For $r = 0$, the father's announcement deletes only the all-zero world.
2. Assume the claim for $r$, and let $x \in W_r$.
   If $x_i = 0$, then $\lvert x^i \rvert = \lvert x \rvert + 1$, so $x^i \in W_r$ and child $i$ does not know.
3. If $x_i = 1$, then $\lvert x^i \rvert = \lvert x \rvert - 1$, so child $i$ knows exactly when $\lvert x \rvert = r + 1$.
4. So in round $r + 1$ somebody says "yes" at $x$ exactly when $\lvert x \rvert = r + 1$, and then it is exactly the muddy children.
   Deleting those worlds gives $W_{r + 1} = \{x : \lvert x \rvert \ge r + 2\}$.

If the actual world $a$ has $\lvert a \rvert = k$, step 4 says that rounds $1$ to $k - 1$ are silent and that the muddy children speak in round $k$.

### Why the father must speak

When $k \ge 2$, every child already sees mud, so everyone knows that someone is muddy before the father speaks.
Yet without the announcement the full cube stays, every alternative $x^i$ is present, and nobody ever knows.
What the announcement adds is [[common knowledge|7BCMKF2P7X]].
Before it, "someone is muddy" holds at $a$ as $E^{k-1}$ but not as $E^k$, because $000$ lies $k$ steps away along the cube.
So common knowledge, not mutual knowledge, starts the chain of reasoning.

### What changes

The rounds of silence carry information: each "no" is a public announcement that deletes a layer of the cube.
If the children answer one at a time, or some answers are private, the count of rounds changes, and [[action models|9465T2PWZT]] describe the update.
After round $k$ only $a$ is left, so in round $k + 1$ every child knows her state.

## Explanations

### L1 human

Suppose only one child is muddy.
She sees no mud on anyone else, so after the father speaks she knows that it is her.
Now suppose Ann and Bob are both muddy.
Ann sees Bob's mud and thinks: "If I am clean, Bob sees no mud and will say yes in round 1."
When Bob says "no" in round 1, Ann concludes that she is muddy, and Bob reasons the same way.
With three muddy children the same argument takes three rounds.

### L2 human

Take $n = 3$ and $a = 111$, so all three are muddy.
After the announcement 7 worlds remain, and in round 1 each child's alternative ($011$, $101$ or $110$) is still possible, so all say "no".
That deletes the three worlds with one $1$, leaving $\{110, 101, 011, 111\}$.
In round 2 the alternatives at $111$ are still there, so all say "no" again, and this deletes the three worlds with two ones.
Only $111$ remains, so in round 3 all three say "yes".
Watch out: it is tempting to say that the father's words are useless because each child already sees mud, and the run with $000$ kept shows that they are not.

### L3 human

The puzzle is a computation in [[public announcement logic|9465T2PWZT]] on the hypercube, and the induction above is induction on its layers.
The [[fixed point law for common knowledge|8K0CMPQXXB]] explains why one public sentence gives every level $E^m$ at once.
Fagin, Halpern, Moses and Vardi use the puzzle as the opening example of the knowledge-based analysis of distributed protocols.
