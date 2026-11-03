---
tag: M81NRAZVH0
kind: concept
name: Neighbor joining
msc: [92B10, 92-08]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Neighbor_joining
same_as:
  wikidata: Q1935806
  wikipedia: Neighbor joining
---

## Summary

Neighbor joining is a distance-based [[algorithm|9DMSG5HAQX]] that builds an unrooted [[phylogenetic tree|RK58WSHJSG]] from a matrix of pairwise distances between taxa.
It repeatedly joins the pair of taxa that minimises a corrected distance, replaces them by a new node, and updates the distances.
It runs in polynomial time and does not assume a molecular clock.
It recovers the correct tree when the distances come exactly from a tree with positive edge lengths.

## Explanations

### L1 human

Start with all taxa in a star, all linked to one centre.
Find the two taxa that are best explained as neighbours, join them through a new node, and treat that node as a new taxon.
The choice is not simply the closest pair: the method corrects for taxa that are far from everyone because they evolve fast.
Repeat until the tree is fully resolved.
