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

"All horses are the same color" is a false proof by [[mathematical induction|0ASJVEFA9J]] that looks almost right, and finding its mistake teaches more about induction than many correct proofs.
The claim $P(n)$ is "in every set of $n$ horses, all the horses have the same color".
The base case $P(1)$ is true, and the induction step compares two overlapping groups of $n$ horses inside a group of $n + 1$.
The step is correct for every $n \ge 2$ and fails for $n = 1$, because two groups of one horse each do not overlap.
So the argument is the standard warning that an induction step must work for every $n$ from the base case on, the smallest included.

## Motivation

The conclusion is false: a black horse and a white horse form a set of $2$ horses with two colors.
The argument still has a true base case and a step that works for almost every $n$.
So something must break, and the reader has to find the exact link of the chain where it breaks.
That search is the skill the example trains, and it is the same skill you need when checking your own induction proofs.

## Remarks

### The false proof

Here is the argument as it is usually told.

1. Base case: in a set of $1$ horse, all the horses have the same color, so $P(1)$ holds.
2. Step: assume $P(n)$, and take a set of $n + 1$ horses $h_1, h_2, \ldots, h_{n+1}$.
3. The group $\{h_1, \ldots, h_n\}$ has $n$ horses, so by $P(n)$ they all have one color.
4. The group $\{h_2, \ldots, h_{n+1}\}$ also has $n$ horses, so they all have one color too.
5. The two groups share the horses $h_2, \ldots, h_n$, so the two colors are equal, and all $n + 1$ horses have the same color.
6. By induction, $P(n)$ holds for every $n \ge 1$.

### Where the step fails

Run the step for $n + 1 = 3$ first.
The groups are $\{h_1, h_2\}$ and $\{h_2, h_3\}$, and they share $h_2$, so $h_1$ and $h_3$ both have the color of $h_2$.
That step is correct.

Now run it for $n + 1 = 2$.
The groups are $\{h_1\}$ and $\{h_2\}$, and the shared list $h_2, \ldots, h_n$ is empty because $n = 1$.
Nothing links the color of $h_1$ to the color of $h_2$, so step 5 fails, and $P(1)$ does not imply $P(2)$.
For every $n \ge 2$ the groups share at least $h_2$, and the step is correct.
So the argument proves that $P(2)$ implies $P(n)$ for every $n \ge 2$: all the content of the claim sits in $P(2)$, and $P(2)$ is false.

### The same trap elsewhere

Any overlap argument has this weak point.
"Any $n$ numbers are equal" has the same false proof, and it breaks at the same step from $1$ number to $2$.
"Any $n$ points in the plane lie on one line" is true for $n = 1$ and $n = 2$.
Its step needs two shared points to fix the line, and for $n + 1 = 3$ the two groups of $2$ points share only one point, so the step breaks from $2$ to $3$.

### When the same argument is correct

Move the base case up to the size where the overlap is large enough, and the argument becomes a real proof.
"If any two horses in a set have the same color, then all of them do" is correct by the same step with base case $n = 2$, since for $n \ge 2$ the groups overlap.
"If any $3$ of $n \ge 3$ distinct points lie on a line, then all $n$ points do" is correct with base case $n = 3$, since for $n \ge 3$ the two groups share $n - 1 \ge 2$ points, and two distinct points fix one line.
The repair is always the same: the base cases must cover every $n$ for which the overlap is too small.

### Watch out

A common slip is to say that the base case is wrong.
The base case $P(1)$ is true, and the error is in the step from $1$ to $2$.
Another slip is to check the step with a picture of many horses and never write out the smallest case.
The correct check is to run the step by hand for the first value of $n$ that it must cover, here $n = 1$.
More errors of this kind are collected in [[errors in induction proofs|V52HDTMPV5]].

### History

George Pólya gave an argument of this kind in his 1954 book Induction and Analogy in Mathematics, as an exercise on induction.
The version with horses is now the standard form of the paradox.

### Try it

First, a "proof" shows that any $n$ lines in the plane, no two parallel, pass through one point, with base case $n = 2$ and an overlap step.
Where does it break?
For $n + 1 = 3$ the two groups of $2$ lines share one line, and one line does not fix a point, so the step from $2$ to $3$ fails.

Second, what is the smallest base case that makes the horse argument correct for "if every two horses agree, all agree"?
It is $n = 2$, because the step from $n$ to $n + 1$ then always has at least one shared horse.

## Explanations

### L1 human

Here is a joke "proof" that all horses have the same color.
One horse alone has one color.
For a group of horses, take out one horse, and the rest have one color.
Put it back and take out another horse, and again the rest have one color.
The two groups overlap, so all the horses have the same color.
The joke fails for a group of two horses.
After you take out one horse, only one horse is left each time, and the two leftover horses are different horses.
There is no overlap to compare their colors.

### L2 human

Treat the argument as an audit of an induction step, and test each link of the chain $P(1) \Rightarrow P(2) \Rightarrow P(3) \Rightarrow \cdots$.
For $P(2) \Rightarrow P(3)$, the groups $\{h_1, h_2\}$ and $\{h_2, h_3\}$ share $h_2$, so $P(2)$ would give one color to all three, and the link holds.
For $P(1) \Rightarrow P(2)$, the groups $\{h_1\}$ and $\{h_2\}$ share nothing:
$$\{h_1\} \cap \{h_2\} = \emptyset.$$
So the first link is missing, and the chain breaks at its start.

The lesson for every induction proof is to run the step by hand for the first value that it must cover.
Watch out: a step that "works for large $n$" proves nothing about the small values, and in an overlap argument the base cases must cover every $n$ for which the overlap can be empty.

### L3 human

In logical terms the argument proves $P(1)$ and $P(n) \Rightarrow P(n + 1)$ for every $n \ge 2$.
These two facts do not imply $P(n)$ for every $n \ge 1$, because the implication $P(1) \Rightarrow P(2)$ is missing.
A herd of two horses with two colors is a model in which both facts hold and $P(2)$ fails.
The same gap appears in [[induction on size|B2D8PTFNN1]] for graphs and sets, whenever the step needs several elements and the small cases are skipped, and in [[strong induction|0KMVFSHFGZ]] with too few base cases.
