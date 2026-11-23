---
tag: MD3MRG90W4
kind: concept
name: Extremal principle
aliases: [extremal-principle]
msc: ["00A35", "05D99"]
topics: [G9JFJGY4TQ, GB14W4SYPK]
audience: school
uses: [01BX15HSRR, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester%E2%80%93Gallai_theorem
    locator: Kelly's proof
  - url: https://en.wikipedia.org/wiki/Well-ordering_principle
    locator: Example applications
  - url: https://en.wikipedia.org/wiki/Oskar_Perron
    locator: lead section
---

## Summary

The extremal principle says: when you need an object with a special property, look at an object that is largest or smallest for a well-chosen quantity.
Such an object often has the property, because an object without it could be improved, and nothing beats the extreme one.

Here is a first problem.
Put $n$ red points and $n$ blue points in the plane, with no three of the $2n$ points on one line.
Can you join each red point to its own blue point by $n$ segments so that no two segments cross?
Among the $n!$ ways to pair the colors, take one with the least total length.
If two of its segments $R_1 B_1$ and $R_2 B_2$ crossed, the triangle inequality would make the swap to $R_1 B_2$ and $R_2 B_1$ strictly shorter.
So the shortest pairing has no crossings, and [[the red-blue matching example|H58TWAEXBW]] gives every step.

In general, a proof by the extremal principle has two parts.
First, prove that an object with the largest or smallest value of the quantity exists.
Second, show that if this object lacked the property, a change would give an object of the same family with a strictly better value, against the choice.
In a finite nonempty family the first part is automatic.
In an infinite family it needs a proof, for example by the [[well-ordering principle|01BX15HSRR]].

## Motivation

Existence problems often ask for a needle in a haystack: a line through exactly two points of a set, a long cycle in a graph, a pairing without crossings.
A search over all candidates is long, and in an infinite family it never ends.
The extremal principle replaces the search by one candidate, chosen to be as constrained as possible.
Nothing in the family beats it, so every small improvement is forbidden, and these forbidden improvements often force the property.

The idea runs through mathematics.
In number theory, a least counterexample is the extremal form of induction.
In graph theory, a longest path or a largest set with some property starts many proofs.
In analysis and optimization, a proof often starts with a minimizer, and compactness gives its existence.
[[Monovariants|TP3GC5J08D]] put the same idea in motion: a process that strictly improves a quantity must stop at an extreme state.

## Notation

The method has no symbols of its own.
Books write "choose $x$ with $f(x)$ maximal", "let $x$ minimize $f$" or "consider an extreme case", and problem books also call it the extremal method.
Read the word "maximal" with care.
In a partial order, a [[maximal element|072G59HW59]] has nothing strictly above it, while a greatest element lies above everything, and the two can differ.
Many extremal proofs need only a maximal object, such as a path that cannot be extended.

## Remarks

### Choosing the quantity

The skill of the method is the choice of the quantity.
A good quantity has two features: it takes a best value on the family, and every failure of the property allows a change that improves it strictly.
For the red-blue pairing, the total length works.
The number of crossings looks more natural, but it is a poor choice.
One swap removes one crossing and can create new crossings with other segments, so the count need not drop.
The total length drops at every uncrossing swap, so one swap gives the contradiction.
Typical quantities are the length of a path, the number of elements of a set, a distance, an area, a sum of values and the size of a counterexample.

### A longest path in a tree

Claim: a finite [[tree|062D9KXJB1]] with at least two vertices has at least two [[leaves|EA8S0JHXMP]].
A path in a finite graph visits each vertex at most once, so there are finitely many paths, and a longest path $v_0 v_1 \cdots v_k$ exists, with $k \ge 1$.
Suppose $v_0$ had a neighbor $w \ne v_1$.
If $w$ is off the path, then $w v_0 \cdots v_k$ is longer, against the choice.
If $w = v_j$ with $j \ge 2$, then $v_0 v_1 \cdots v_j v_0$ is a cycle, and a tree has none.
So $v_0$ is a leaf, and by the same steps $v_k$ is a second leaf.

The same start gives a [[cycle of length at least d + 1|NT7GFT7H6T]] in every finite graph of minimum degree $d \ge 2$.
A longest trail gives the [[proof of Euler's theorem on Eulerian circuits|JSB2RB25Y8]].
In each case the ends of the extreme object have all their neighbors inside it.

### A smallest distance: Sylvester-Gallai

The [[Sylvester-Gallai theorem|T3GGJN70P2]] says: a finite set $S$ of points in the plane, not all on one line, has a line through exactly two of its points.
Kelly's proof is extremal.
Look at the pairs $(P, L)$ where $L$ is a line through at least two points of $S$ and $P \in S$ is off $L$.
There are finitely many pairs, and at least one, since $S$ is not on one line.
Choose a pair with the least distance from $P$ to $L$, and let $F$ be the foot of the perpendicular from $P$ to $L$.
If $L$ held three points of $S$, two of them, $A$ and $B$, would lie on one side of $F$, with $A$ between $F$ and $B$ or $A = F$.
Put $L$ on the $x$-axis with $P = (0, h)$, $A = (a, 0)$ and $B = (b, 0)$, where $0 \le a < b$.
The distance from $A$ to the line $PB$ is
$$\frac{h(b - a)}{\sqrt{h^2 + b^2}} \le \frac{h b}{\sqrt{h^2 + b^2}} < h,$$
so the pair $(A, PB)$ beats $(P, L)$, a contradiction.
Check: with $h = 1$, $a = 0$ and $b = 1$, the distance is $1/\sqrt{2} \approx 0.71 < 1$.

### A least counterexample

Claim: every integer $n \ge 2$ is a product of [[primes|0SN0MAEKYX]].
If not, the set of integers $n \ge 2$ that are not products of primes is nonempty, so it has a least element $n$ by the well-ordering principle.
This $n$ is not prime, so $n = ab$ with $1 < a, b < n$.
Both $a$ and $b$ are smaller than $n$, so they are products of primes, and then so is $n = ab$, a contradiction.
A least counterexample and [[infinite descent|0EFYCFHYFG]] are two forms of one idea: the first shows that a least counterexample would have a smaller one, and the second shows that every counterexample has a smaller one.

The [[Erdős-Szekeres theorem|0SNJM8HSD3]] mixes the method with counting.
Its [[proof by the pigeonhole principle|22G1VPJW6Y]] labels each term with the length of the longest increasing subsequence that ends there, which is an extremal label.

### When the extreme does not exist

Perron's paradox is the standard warning.
"Let $N$ be the largest positive integer; if $N > 1$, then $N^2 > N$, so $N = 1$."
Every step after the first is correct, and the conclusion is false, because no largest positive integer exists; [[Perron's paradox|HJ3C7DFQBK]] takes it apart.

The integer lattice $\mathbb{Z}^2$ shows the same failure in geometry.
Every line through two lattice points holds infinitely many, so the Sylvester-Gallai conclusion fails, and Kelly's proof breaks at its first step.
The line $x - ny = 1$ passes through the lattice points $(1, 0)$ and $(n + 1, 1)$, and its distance from $(0, 0)$ is $1/\sqrt{1 + n^2}$.
These distances shrink toward $0$, so no least positive distance exists.

In analysis, the function $f(x) = x$ on the open interval $(0, 1)$ has no largest value.
The [[extreme value theorem|0WS1A8E2P9]] needs a closed and bounded interval, and more generally a nonempty [[compact space|0TVJZYB6SH]].

### Watch out

Three slips break extremal proofs.
The first is to take an extreme object in an infinite family without a proof that it exists, as in Perron's paradox.
The second is a change that is only as good as the extreme object.
If the swap gives a tie, no contradiction appears, which is why the red-blue proof needs the strict triangle inequality and the hypothesis that no three points are collinear.
The third is a change that leaves the family.
In $\{1, 2, \ldots, 10\}$ the largest element $10$ exists, but $10^2 = 100$ is not in the set, so "$N^2 > N$" does not contradict the choice of $N$.

### History

James Joseph Sylvester posed the problem of ordinary lines in 1893, and Tibor Gallai published a proof in 1944.
Leroy Milton Kelly found the short proof by least distance.
Paul Erdős and George Szekeres proved their theorem on monotone subsequences in 1935.
Oskar Perron gave his paradox as a warning that an extremal problem may have no solution, so a proof must not assume one.

### Try it

First, prove that every finite graph in which every vertex has degree at least $2$ contains a cycle.
Take a longest path $v_0 \cdots v_k$; the vertex $v_0$ has a neighbor other than $v_1$, maximality puts it on the path as some $v_j$ with $j \ge 2$, and $v_0 v_1 \cdots v_j v_0$ is a cycle.

Second, finitely many points in the plane are not all on one line.
Show that some triangle with vertices among them has no other of the points inside it or on its sides.
Take a nondegenerate triangle $ABC$ of least area; a further point inside or on side $AB$ would give a smaller nondegenerate triangle, such as $ABQ$ or $AQC$.

Third, is this proof correct: "among all ways to write a positive rational as $p/q$ with positive integers, choose one with $q$ least; if $d = \gcd(p, q) > 1$, then $(p/d)/(q/d)$ has a smaller denominator"?
Yes, since the denominators are positive integers, the well-ordering principle gives the least one, and the proof shows that every positive rational has a form in lowest terms.

## Explanations

### L1 human

To prove that something exists, look at the most extreme candidate: the longest, the shortest, the largest or the closest.
Suppose this candidate lacked the property you want.
Often you could then change it a little and get an even more extreme candidate.
That is impossible, because you chose the most extreme one.
So the extreme candidate has the property.
There is one catch: the most extreme candidate must exist, and in an endless family it may not.

### L2 human

Here is a typical problem.
In a finite group of people, each person has at most three enemies, and being enemies is mutual.
Show that you can split the people into two rooms so that each person has at most one enemy in the same room.

There are only finitely many splits, $2^n$ for $n$ people, so choose a split that makes the number $E$ of enemy pairs inside a room as small as possible.
Suppose some person $x$ has at least two enemies in the same room.
Since $x$ has at most three enemies, $x$ has at most one enemy in the other room.
Move $x$ to the other room.
The pairs that do not contain $x$ keep their status, so the change in $E$ is
$$\Delta E = (\text{enemies of } x \text{ in the other room}) - (\text{enemies of } x \text{ in its room}) \le 1 - 2 = -1.$$
So the new split has a smaller $E$, against the choice.
Therefore every person has at most one enemy in the same room.

Check with four people who are all enemies of each other: put two people in each room, and each person has exactly one enemy in the same room.
The problem shows the usual pattern: a total count of defects as the quantity, a local move that strictly lowers it, and finiteness for the existence of the minimum.

### L3 human

The extremal principle rests on the existence of extrema in an ordered set.
For finite sets this is induction on the size, for the natural numbers it is the well-ordering principle, and for continuous functions it is compactness.
In set theory, [[Zorn's lemma|04RXTQA5ZA]] gives maximal elements in partial orders where every chain has an upper bound, and many existence proofs of algebra rest on it, such as the existence of a basis of a vector space.
In analysis, the direct method of the calculus of variations first proves that a minimizer exists and only then uses it, which is the lesson of Perron's paradox.

In combinatorics, extremal choices start many proofs in graph theory and discrete geometry, and the field of extremal combinatorics asks for the largest object that avoids a given structure.
The method sits beside [[invariants|8NQ190278Y]], [[monovariants|TP3GC5J08D]] and [[parity arguments|H9JT1XNDKQ]] as a standard tool for existence and impossibility, and the [[averaging argument|HXP9VMXV8S]] is its cousin that compares an object with the mean instead of with the best.
