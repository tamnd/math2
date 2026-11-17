---
tag: AJ2FDJJGTH
kind: concept
name: All horses are the same color
aliases: [all-horses-are-the-same-colour, equine-monochromaticity-theorem, horse-paradox]
msc: ["00A35", "03F30"]
topics: [EEH2F76CYQ]
audience: school
uses: [0ASJVEFA9J]
sources:
  - wikipedia: en:151912@r1369976011
    locator: All horses are the same color
    note: adapted
    mention: wikipedia://en/151912
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/All_horses_are_the_same_color
    locator: The argument
  - url: https://en.wikipedia.org/wiki/All_horses_are_the_same_color
    locator: Explanation
same_as:
  wikidata: Q1091396
  wikipedia: All horses are the same color
inventory: [VJPD9EGWGZ]
---

## Summary

"All horses are the same color" is a false proof by [[mathematical induction|0ASJVEFA9J]] of the claim in its name.
The claim $P(n)$ is "in every set of $n$ horses, all the horses have the same color".
The base case $P(1)$ is true.
The induction step compares two overlapping subsets of $n$ horses inside a set of $n + 1$ horses.
The step fails for $n = 1$, because two sets of one horse each do not overlap.
The argument matters as the standard warning that an induction step must hold for every $n$ from the base case on, including the smallest.

## Motivation

The argument looks like a correct induction: it has a true base case and a step that works for almost every $n$.
Its conclusion is false: a black horse and a white horse form a set of $2$ horses with two colors.
So the argument forces a reader to find the exact place where an induction can break.

## Remarks

### The false proof

1. Base case: in a set of $1$ horse, all the horses have the same color. So $P(1)$ holds.
2. Step: assume $P(n)$, and take a set of $n + 1$ horses $h_1, h_2, \ldots, h_{n+1}$.
3. The set $\{h_1, \ldots, h_n\}$ has $n$ horses, so they all have the same color, by $P(n)$.
4. The set $\{h_2, \ldots, h_{n+1}\}$ also has $n$ horses, so they all have the same color.
5. The two sets share the horses $h_2, \ldots, h_n$. So the two colors are equal, and all $n + 1$ horses have the same color.
6. By induction, $P(n)$ holds for every $n \ge 1$.

### Where the step fails

1. For $n + 1 = 2$, the two sets in steps 3 and 4 are $\{h_1\}$ and $\{h_2\}$. They share no horse, because the list $h_2, \ldots, h_n$ is empty. So step 5 fails, and $P(1)$ does not imply $P(2)$.
2. For $n \ge 2$, the two sets share at least the horse $h_2$, and the step is correct.
3. So the argument proves that $P(2)$ implies $P(n)$ for every $n \ge 2$. All the content of the claim is in $P(2)$, and $P(2)$ is false.

### Examples

1. Pólya's form: "any $n$ numbers are equal". The same overlap step fails from $1$ number to $2$ numbers.
2. "Any $n$ points in the plane lie on one line." The base cases $n = 1$ and $n = 2$ are true. The step needs two shared points to fix the line, and for $n + 1 = 3$ the two sets of $2$ points share only one point.

### Non-examples

1. "In a set of horses in which any two have the same color, all have the same color." The same proof with the base case $n = 2$ is correct, because for $n \ge 2$ the sets overlap.
2. "If any $3$ of $n \ge 3$ points lie on a line, then all $n$ points lie on a line." The same proof with the base case $n = 3$ is correct, because for $n \ge 3$ the two sets share $n - 1 \ge 2$ points.

### Basic properties

1. The base case and all steps from $P(n)$ to $P(n + 1)$ with $n \ge 2$ are correct, and still the conclusion is false. Induction needs a chain with no broken link.
2. The repair of an overlap argument is a base case that covers every $n$ for which the overlap is too small.

### History

George Pólya gave the argument in 1954, in his book Induction and Analogy in Mathematics.
His form asks whether any $n$ numbers are equal, as an exercise on induction.
The version with horses is due to Joel Cohen, who used it in a satirical article in 1961.

### Common errors

1. A student checks the step with a picture of many horses, and never writes out the case $n = 1$.
2. A student says that the base case is wrong. The base case $P(1)$ is true, and the error is in the step from $1$ to $2$.

## Explanations

### L1 human

Here is a joke "proof" that all horses have the same color.
One horse alone has one color.
For a group of horses, take out one horse; the rest have one color.
Put it back and take out another horse; again the rest have one color.
The two groups overlap, so all the horses have the same color.
The joke fails for a group of two horses.
After we take out one horse, only one horse is left each time, and the two leftover horses are different.
There is no overlap to compare their colors.

### L2 human

We check the step of the false proof for $n + 1 = 3$ and for $n + 1 = 2$.

1. For $n + 1 = 3$, the sets are $\{h_1, h_2\}$ and $\{h_2, h_3\}$. By $P(2)$, $h_1$ and $h_2$ have the same color, and $h_2$ and $h_3$ have the same color. So all three do. This step is correct.
2. For $n + 1 = 2$, the sets are $\{h_1\}$ and $\{h_2\}$. By $P(1)$, each set has one color. Nothing links the color of $h_1$ to the color of $h_2$.
3. So the step $P(1) \Rightarrow P(2)$ is missing. The chain $P(1), P(2), P(3), \ldots$ breaks at its first link.

The typical use of this argument is as a test for an induction step: the step must hold for each $n$ from the base case on.
A trap is to check the step only for large $n$.
In a correct proof with a similar overlap, the base case must cover every $n$ for which the overlap can be empty.
More errors of this kind are listed in [[errors in induction proofs|V52HDTMPV5]].

### L3 human

In logical terms, the argument proves $P(1)$ and $P(n) \Rightarrow P(n + 1)$ for every $n \ge 2$.
These two facts do not imply $P(n)$ for every $n \ge 1$, because the implication $P(1) \Rightarrow P(2)$ is missing.
A two-horse herd with two colors is a model in which both facts hold and $P(2)$ fails.
The same gap appears in proofs by induction on the size of a graph or a set, when the step needs several elements and the small cases are skipped.
