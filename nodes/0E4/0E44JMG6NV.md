---
tag: 0E44JMG6NV
kind: example
name: Base rate fallacy
aliases: [base-rate-neglect, false-positive-paradox]
msc: [62F15]
uses: [0NM6E9VW04, 0W62TKMW7V]
sources:
  - url: https://en.wikipedia.org/wiki/Base_rate_fallacy
    locator: False positive paradox
same_as:
  wikidata: Q1859747
  wikipedia: Base rate fallacy
---

## Example

A disease affects $1\%$ of a population. A test is positive for $90\%$ of the sick people and for $9\%$ of the healthy people.
Let $S$ be the event "sick" and $T$ the event "positive test". Then $P(S) = 0.01$, $P(T \mid S) = 0.9$ and $P(T \mid S^c) = 0.09$.
By the [[law of total probability|0W62TKMW7V]], $P(T) = 0.9 \cdot 0.01 + 0.09 \cdot 0.99 = 0.0981$.
By [[Bayes' theorem|0NM6E9VW04]], $P(S \mid T) = 0.009 / 0.0981 \approx 0.092$.
So only about $9\%$ of the people with a positive test are sick.
This is true although the test is right for $90\%$ of the sick and for $91\%$ of the healthy.

## Remarks

The base rate fallacy is the error to ignore the base rate $P(S)$ and to take $P(S \mid T)$ to be close to $P(T \mid S)$.
When the condition is rare, most positive results are false positives, even for a good test.

## Explanations

### L1 human

Among $10000$ people, $100$ are sick and $90$ of them test positive. Of the $9900$ healthy people, $891$ also test positive.
So of the $981$ positive tests, only $90$ come from sick people.
