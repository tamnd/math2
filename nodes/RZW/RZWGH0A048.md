---
tag: RZWGH0A048
kind: example
name: The length of a concatenation of lists
msc: ["00A35", "68P05"]
topics: [EEH2F76CYQ]
audience: ug1
instance_of: [12MQ2NJ29A]
uses: [12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_induction
    locator: Examples
---

## Example

A list is either the empty list $[\,]$, or $a :: xs$, an element $a$ in front of a list $xs$.
So $[1, 2]$ is short for $1 :: (2 :: [\,])$.
The length and the concatenation $\mathbin{+\!\!+}$ are defined by recursion on the first list:
$$\operatorname{len}([\,]) = 0, \qquad \operatorname{len}(a :: xs) = 1 + \operatorname{len}(xs),$$
$$[\,] \mathbin{+\!\!+} ys = ys, \qquad (a :: xs) \mathbin{+\!\!+} ys = a :: (xs \mathbin{+\!\!+} ys).$$
We prove that $\operatorname{len}(xs \mathbin{+\!\!+} ys) = \operatorname{len}(xs) + \operatorname{len}(ys)$ for all lists $xs$ and $ys$, by [[structural induction|12MQ2NJ29A]] on $xs$.
For a list $xs$, let $P(xs)$ be the claim "$\operatorname{len}(xs \mathbin{+\!\!+} ys) = \operatorname{len}(xs) + \operatorname{len}(ys)$ for every list $ys$".

1. Case $[\,]$.
   Let $ys$ be a list.
   The first rule for $\mathbin{+\!\!+}$ and the first rule for $\operatorname{len}$ give
   $$\operatorname{len}([\,] \mathbin{+\!\!+} ys) = \operatorname{len}(ys) = 0 + \operatorname{len}(ys) = \operatorname{len}([\,]) + \operatorname{len}(ys).$$
   So $P([\,])$ holds.
2. Case $a :: xs$.
   The induction hypothesis is $P(xs)$.
   Let $ys$ be a list.
3. The second rule for $\mathbin{+\!\!+}$ gives $(a :: xs) \mathbin{+\!\!+} ys = a :: (xs \mathbin{+\!\!+} ys)$.
4. The second rule for $\operatorname{len}$, then the hypothesis $P(xs)$, then the second rule for $\operatorname{len}$ again give
   $$\operatorname{len}(a :: (xs \mathbin{+\!\!+} ys)) = 1 + \operatorname{len}(xs \mathbin{+\!\!+} ys) = 1 + \operatorname{len}(xs) + \operatorname{len}(ys) = \operatorname{len}(a :: xs) + \operatorname{len}(ys).$$
5. Steps 3 and 4 give $\operatorname{len}((a :: xs) \mathbin{+\!\!+} ys) = \operatorname{len}(a :: xs) + \operatorname{len}(ys)$, which is $P(a :: xs)$.
6. Both cases hold, so $P(xs)$ holds for every list $xs$, by structural induction.

Check on a small case, by the rules for $\mathbin{+\!\!+}$:
$$[1, 2] \mathbin{+\!\!+} [3] = 1 :: ([2] \mathbin{+\!\!+} [3]) = 1 :: (2 :: ([\,] \mathbin{+\!\!+} [3])) = 1 :: (2 :: [3]) = [1, 2, 3],$$
and the length is $3 = 2 + 1$.

## Remarks

The induction is on $xs$ because both functions are defined by recursion on their first list.
Then each line of the proof applies one rule of a definition.
An induction on $ys$ gets stuck: its step needs $\operatorname{len}(xs \mathbin{+\!\!+} (b :: ys))$, and no rule for $\mathbin{+\!\!+}$ applies while $xs$ is unknown.

The list $ys$ never changes in the step, so the same proof works with one fixed $ys$.
For other claims, such as properties of a reverse function that carries a second list along, the hypothesis must hold for every second list, as $P(xs)$ here is stated.

A corollary is $\operatorname{len}(xs \mathbin{+\!\!+} ys) = \operatorname{len}(ys \mathbin{+\!\!+} xs)$, although the two lists can differ: $[1, 2] \mathbin{+\!\!+} [3] = [1, 2, 3]$ but $[3] \mathbin{+\!\!+} [1, 2] = [3, 1, 2]$.
The Lean 4 core library states the result as `List.length_append`, and its proof is this induction on the first list.

## Explanations

### L1 human

Joining two lists gives a list that holds the first list and then the second.
Its length is the sum of the two lengths, and we prove this from the rules for joining and for length.
Joining takes the first element of the first list, joins the rest, and puts the element back in front.
So the proof walks through the first list one element at a time.
Each element adds $1$ to the length on both sides of the equation.

### L2 human

Let us follow the step for $a :: xs = [1, 2]$, so $a = 1$ and $xs = [2]$, with $ys = [3]$.
The hypothesis $P([2])$ says that $\operatorname{len}([2] \mathbin{+\!\!+} [3]) = 1 + 1 = 2$.
Step 3 gives $[1, 2] \mathbin{+\!\!+} [3] = 1 :: ([2] \mathbin{+\!\!+} [3])$, and step 4 gives its length:
$$1 + \operatorname{len}([2] \mathbin{+\!\!+} [3]) = 1 + 2 = 3.$$
The right side is $\operatorname{len}([1, 2]) + \operatorname{len}([3]) = 2 + 1 = 3$, so the two sides agree.
The typical use of this pattern is a property of a recursive function on lists, proved by induction on the argument that the recursion takes apart.
Watch out: the same proof on the second argument fails, as the remarks show.
