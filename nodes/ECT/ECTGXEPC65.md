---
tag: ECTGXEPC65
kind: example
name: An action proof with counters that the sum of two odd numbers is even
msc: ["97E50", "97F30"]
topics: [VHGA6J4NZK]
audience: school
instance_of: [SG9XA69J64]
uses: [SG9XA69J64]
sources:
  - url: https://doi.org/10.1007/BF00555722
    locator: pages 183-203
---

## Example

The claim is that the sum of two odd numbers is even.
A class of eight-year-olds has agreed that a number is even if its counters can be put in pairs with none left over, and odd if one counter is left over.
A student argues with counters.

1. She lays out $7$ counters in pairs: three pairs and one single counter.
2. She lays out $5$ counters in pairs: two pairs and one single counter.
3. She pushes the two sets together.
   The pairs stay pairs, and the two single counters form a new pair.
4. Now all $12$ counters are in pairs with none left over, so $7 + 5$ is even.
5. She says: "Every odd number is pairs and one more. When you put two together, the two extra ones make a pair."

We check that the argument is a [[pre-formal proof|SG9XA69J64]] by action.
Her sentence in step 5 states the general structure, "pairs and one", which is the class's definition of odd.
The push in step 3 does not depend on how many pairs each pile has, so it works for any two odd numbers.
The conclusion uses the class's definition of even.
So the argument is an action proof, and a valid proof for the class.

## Remarks

The action matches the symbolic proof line by line.
"Pairs and one" is $2a + 1$, pushing the piles together is $(2a + 1) + (2b + 1)$, the two single counters forming a pair is $1 + 1 = 2$, and "all in pairs" is
$$(2a + 1) + (2b + 1) = 2(a + b + 1).$$
The numbers $7$ and $5$ play no role in the steps, and that is what makes the action generic.
If she had stopped after step 4, the argument would only check the single case $7 + 5$; step 5 is what makes it a proof.

## Explanations

### L1 human

An odd number of counters can be put in pairs with one left over.
If two children each have an odd number of counters and put them together, the two left-over counters make a pair.
So the total can be put in pairs with nothing left over, which means it is even.
This works no matter how many counters each child has.

### L2 human

An action proof has four parts.
First the class fixes its definitions: even means "all in pairs" and odd means "pairs and one".
Then the student performs the action on one case and says what happens to the pairs and to the single counters.
Next the student says why the action works for any odd numbers.
Finally, when the class is ready, the teacher translates the action into $(2a + 1) + (2b + 1) = 2(a + b + 1)$.
Watch out for stopping after the action itself: without the third part, the action is a check of one case and not a proof.
