---
tag: MKDZSQM3KE
kind: example
name: Extension variables for the carries of binary addition
msc: ["03F20", "94C11"]
topics: [CBAF7J051K]
audience: research
instance_of: [5YSE04SHFH]
uses: [5YSE04SHFH, NDPRFZGZ9M]
sources:
  - url: https://en.wikipedia.org/wiki/Frege_system
    locator: Extended Frege system
---

## Example

Add two binary numbers $x = x_{n-1} \dots x_0$ and $y = y_{n-1} \dots y_0$, with $x_0$ and $y_0$ the lowest bits.
The carry $c_i$ into position $i$ has $c_0 = 0$ and $c_{i+1} = \mathrm{MAJ}(x_i, y_i, c_i)$, where the majority function is
$$\mathrm{MAJ}(u, v, w) = (u \land v) \lor (u \land w) \lor (v \land w).$$
We compare two ways to write the carries: as formulas, and with extension variables.

*Unfolded formulas.*
Define $C_1 = x_0 \land y_0$ and $C_{i+1} = (x_i \land y_i) \lor (x_i \land C_i) \lor (y_i \land C_i)$, and count variables and connectives as symbols.

1. $\lvert C_1 \rvert = 3$.
2. $C_{i+1}$ has two copies of $C_i$ and $9$ other symbols, so $\lvert C_{i+1} \rvert = 2 \lvert C_i \rvert + 9$.
3. Adding $9$ to both sides gives $\lvert C_{i+1} \rvert + 9 = 2 (\lvert C_i \rvert + 9)$, and $\lvert C_1 \rvert + 9 = 12$.
   So by induction
   $$\lvert C_i \rvert = 12 \cdot 2^{i-1} - 9 \ge 2^i.$$

*Extension variables.*
An [[extended Frege|5YSE04SHFH]] proof can instead write the extension axioms
$$q_1 \leftrightarrow (x_0 \land y_0), \qquad q_{i+1} \leftrightarrow (x_i \land y_i) \lor (x_i \land q_i) \lor (y_i \land q_i),$$
for $i = 1, \dots, n - 1$, in this order.

1. Each $q_{i+1}$ is new when it appears, and its definition uses only $x_i$, $y_i$ and the earlier $q_i$.
2. The first axiom has $5$ symbols and each later one has $2 + 9 + 2 = 13$, so all $n$ axioms together have at most $13 n$ symbols.
3. The sum bit at position $i \ge 1$ is then the short formula $x_i \oplus y_i \oplus q_i$.

## Remarks

The extension variables $q_i$ are the gates of a [[Boolean circuit|NDPRFZGZ9M]] for addition.
So an EF-proof can reason about a circuit of size $O(n)$, while a proof that writes the unfolded $C_i$ must handle formulas of size $2^i$ or more.

The example does not separate Frege from EF, for the following reason.
The carry also has the carry-lookahead formula
$$c_i = \bigvee_{j < i} \Bigl( x_j \land y_j \land \bigwedge_{j < k < i} (x_k \lor y_k) \Bigr),$$
which says that some position $j < i$ generates a carry and every position between $j$ and $i$ passes it on.
It has size $O(i^2)$, and Frege proofs about addition use formulas of this kind.
Watch out: one long formula for a function does not show that every formula for that function is long.

## Explanations

### L1 human

When we add two numbers by hand, we write each carry once, above its column.
A formula cannot do this: each time it needs a carry, it must write the whole expression for it again.
The expression for the next carry contains the previous one twice, so its length roughly doubles at each column.
Extended Frege lets the proof write each carry once and give it a name.

### L2 human

We compute $\lvert C_3 \rvert$ by the recursion.

1. $\lvert C_1 \rvert = 3$, for $x_0 \land y_0$.
2. $\lvert C_2 \rvert = 2 \cdot 3 + 9 = 15$.
3. $\lvert C_3 \rvert = 2 \cdot 15 + 9 = 39$.

Check: the closed form gives $12 \cdot 2^2 - 9 = 39$.
With extension variables, the third carry is $q_3$, of size $1$, and its definition has $13$ symbols.
The typical use of this example is as the model for translating a polynomial-time computation into an EF-proof, one extension variable for each gate.
