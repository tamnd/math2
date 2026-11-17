---
tag: XWY34NHQ58
kind: example
name: No graph on nine vertices has all degrees equal to 3
msc: ["00A35", "05C07"]
topics: [GB14W4SYPK]
audience: school
instance_of: [H9JT1XNDKQ]
uses: [H9JT1XNDKQ, 0XAP8WHNES, 0KS0KRDV4Y, 0Q70YFB6ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Handshaking_lemma
    locator: Regular graphs
---

## Example

We show that no finite simple [[graph|00C0BR7D7H]] has exactly $9$ vertices, each of [[degree|0KS0KRDV4Y]] $3$.
In words: nine people cannot be arranged so that each person knows exactly three of the others, if "knows" is mutual.

1. Suppose that such a graph $G$ exists, with vertex set $V$ and edge set $E$. So $|V| = 9$ and $\deg(v) = 3$ for each $v \in V$.
2. We compute the sum of the degrees: $\sum_{v \in V} \deg(v) = 9 \cdot 3 = 27$.
3. The [[handshaking lemma|0XAP8WHNES]] gives $\sum_{v \in V} \deg(v) = 2|E|$. The number $2|E|$ is even, because it is $2$ times an integer.
4. Steps 2 and 3 give $27 = 2|E|$. But $27 = 2 \cdot 13 + 1$ is odd.
5. An integer cannot be both even and odd, so the assumption of step 1 is false. No such graph exists.

## Remarks

The example shows the pattern of a [[parity argument|H9JT1XNDKQ]]: one quantity, the degree sum, has a parity fixed by a theorem, and the target needs the other parity.
The same steps prove a general fact.
A [[regular graph|0Q70YFB6ZM]] of odd degree $d$ on $n$ vertices has degree sum $dn$, and $dn$ is even only when $n$ is even.
So every $3$-regular graph has an even number of vertices.

When the number of vertices changes from $9$ to $10$, the parity obstruction disappears.
The degree sum is $30 = 2 \cdot 15$, and a $3$-regular graph on $10$ vertices exists: the [[Petersen graph|0NR95CTFCZ]] is one.
For $9$ vertices and degree $4$, the sum is $36$, which is even, and the cycle $1, 2, \ldots, 9$ with each vertex also joined to the vertices two steps away is $4$-regular.
So the obstruction depends only on the parity of the product $dn$.

## Explanations

### L1 human

Nine people meet, and we want each person to know exactly three of the others.
Count the friendships from each person's side: $9$ people times $3$ friends gives $27$.
But each friendship is counted twice, once by each of the two friends.
So this count must be an even number, and $27$ is odd.
Hence the plan is impossible, however we try to arrange the friendships.

### L2 human

We test the same idea on the list of degrees $3, 3, 2, 2, 2, 1$ for a graph on six vertices.

1. The sum of the list is $3 + 3 + 2 + 2 + 2 + 1 = 13$.
2. By the handshaking lemma the sum must equal $2|E|$, an even number.
3. The sum $13$ is odd, so no graph has these degrees.
4. Equivalently, the list has three odd entries ($3$, $3$ and $1$), but every graph has an even number of vertices of odd degree.

The typical use is a quick test of a degree list before any attempt to draw the graph.
The trap is the converse: an even degree sum does not guarantee a graph.
The list $3, 3, 1, 1$ has the even sum $8$, but a vertex of degree $3$ in a simple graph on four vertices is joined to all three others, so two such vertices give both remaining vertices degree at least $2$.
