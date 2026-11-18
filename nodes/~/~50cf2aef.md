---
tag: ~50cf2aef
kind: example
name: Muddy children puzzle
msc: ["03B42", "00A08"]
topics: [CQM9SRN8PM]
audience: ug3
instance_of: [~8b9604fb, ~0c910f5d]
uses: [7BCMKF2P7X, RRRHWH9F6Y, VG7DWJBYB9, 0ASJVEFA9J, ~2e0d432a]
sources:
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapters 1 and 2
  - url: https://en.wikipedia.org/wiki/Common_knowledge_(logic)
    locator: section Puzzle, section Solution, section Proof
---

## Example

The puzzle.
There are $n$ children, and $k \ge 1$ of them have mud on their foreheads.
Each child sees every forehead except her own.
The father says in public: "At least one of you is muddy."
Then he asks again and again: "Does any of you know whether you are muddy?"
In each round all children answer at the same time and truthfully, and all are perfect reasoners.
Claim: in rounds $1, \dots, k - 1$ every child answers "no", and in round $k$ exactly the muddy children answer "yes".

The model.
A world is a vector $x \in \set{0, 1}^n$, where $x_i = 1$ means "child $i$ is muddy".
Write $|x|$ for the number of ones.
Child $i$ sees every coordinate but $x_i$, so $x \sim_i y$ iff $x$ and $y$ agree outside coordinate $i$.
So $x$ has exactly one other $\sim_i$-neighbour, the vector $x^i$ with coordinate $i$ flipped, and the worlds form the [[hypercube graph|VG7DWJBYB9]].
Let $W_r$ be the set of worlds still possible after the father's announcement and $r$ rounds in which everyone said "no".
A public announcement deletes the worlds where it is false, and keeps the relations on the remaining worlds.

Lemma: at $x \in W_r$, child $i$ knows whether she is muddy iff $x^i \notin W_r$.

1. The worlds child $i$ considers possible at $x$ are those of $\set{x, x^i}$ that lie in $W_r$.
2. Her status differs between $x$ and $x^i$. So she knows it iff $x^i$ is gone.

Proof of the claim, by [[induction|0ASJVEFA9J]] on $k$.
We prove $S(k)$: $W_{k-1} = \set{x : |x| \ge k}$.

3. Base $k = 1$. Before the announcement every world is possible. The announcement deletes the one world $0 \cdots 0$ where it is false, so $W_0 = \set{x : |x| \ge 1}$.
4. Step. Assume $W_{k-1} = \set{x : |x| \ge k}$, and take $x \in W_{k-1}$.
5. Let $x_i = 1$. Then $|x^i| = |x| - 1$, so $x^i \notin W_{k-1}$ iff $|x| = k$.
6. Let $x_i = 0$. Then $|x^i| = |x| + 1 > k$, so $x^i \in W_{k-1}$, and child $i$ does not know.
7. By the lemma, in round $k$ some child says "yes" at $x$ iff $|x| = k$, and then exactly the muddy children say "yes".
8. "Everyone said no in round $k$" is true at $x \in W_{k-1}$ iff $|x| \ge k + 1$. So $W_k = \set{x : |x| \ge k + 1}$, which is $S(k + 1)$.

Now let the actual world $a$ have $|a| = k$.

9. For $r \le k - 2$, step 7 for $S(r + 1)$ shows that nobody says "yes" in round $r + 1$ at $a$, since $|a| \ne r + 1$.
10. So $a \in W_{k-1}$, and by step 7 for $S(k)$, exactly the muddy children say "yes" in round $k$.

## Remarks

Role of the announcement.
For $k \ge 2$, every child already knows that someone is muddy before the father speaks.
But in the full hypercube every world has all its neighbours.
So by the lemma nobody ever knows, and the "no" rounds delete nothing.
The announcement deletes $0 \cdots 0$, which is at distance $k$ from $a$ along hypercube edges.
Before it, "someone is muddy" holds as $E_G^{k-1}$ but not as $E_G^k$; after it, it is [[common knowledge|7BCMKF2P7X]].
So the puzzle shows that common knowledge, not mutual knowledge, starts the reasoning.

In round $k$ the answers at $a$ name exactly the muddy children of $a$.
In $W_{k-1}$ no other world gives the same answers, by step 7.
So after round $k$ only $a$ remains, and in round $k + 1$ every child knows.

## Explanations

### L1 human

Suppose only one child is muddy.
She sees no mud on anyone else, so after the father says "someone is muddy", she knows it is her.
Now suppose two are muddy, Ann and Bob.
Ann sees only Bob's mud, and thinks: "if I am clean, Bob sees no mud and will say yes in round 1."
When Bob says "no" in round 1, Ann concludes that she is muddy, and Bob reasons the same way.
With $k$ muddy children the same argument takes $k$ rounds.

### L2 human

We follow $n = 3$ children with $a = 110$: children 1 and 2 are muddy.

1. The cube has 8 worlds. The announcement deletes $000$, so $W_0$ has the 7 worlds with at least one $1$.
2. Round 1: at $a = 110$, child 1 considers $010$, which is in $W_0$. Child 2 considers $100$, also in $W_0$. Child 3 considers $111$. So all say "no".
3. The worlds where someone says "yes" in round 1 are $100$, $010$ and $001$. Deleting them leaves $W_1 = \set{110, 101, 011, 111}$.
4. Round 2: at $110$, child 1's alternative $010$ is gone, so child 1 says "yes", and so does child 2. Child 3's alternative $111$ remains, so child 3 says "no".

The typical use is to model reasoning by elimination of worlds, which [[public announcement logic|~0c910f5d]] formalizes.
A trap: "no" answers carry information; each round of silence is a public announcement.

### L3 human

The puzzle is a public announcement logic computation on the hypercube: the father's announcement and each round of answers delete a layer of the cube.
The induction on $k$ is induction on the layers $\set{x : |x| = k}$.
If the children answer one at a time, or some answers are private, the analysis changes, and action models handle such variants.
