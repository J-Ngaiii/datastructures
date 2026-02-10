---
layout: default
title: "Problem Solving Approaches"
date: 2026-02-10
categories: DSA
---
# Problem Solving Cues

## Cues for Pointers & Hashing
- Value/Index Tracks & Updates: Have to track values or indices in multiple places in an array that update based on new information as more of the array is explored
- Memory of Many Values: Have to retain memory of and match many unique values. 
    - If just need to track that they've been seen => hashset
    - If need to track some arbitrary score quantity $s$ per unique value -> hashmap

## Cues for Binary Search
- Sorted Equi-Match: Your search space is a sorted list of values AND the value you're looking for is something your matching exactly 

## Cues for Backtracking
- Permutations: Trying all permutations of something, no way around it => usually backtracking
- Anchor & Remove: State space can be traversed via pattern of anchoring in a certain value --> recursively exploring permutations given that anchor then removing that anchor

## Cues for DP
- Non-Memoryless Iterative Problems: You have to iterate through some values and at an arbitrary value i, you have to make k choices --> but which choice to make depends on info prpopgating from ALL previous steps
    - Opposite of a memoryless markov chain in the long run

# Learning with AI
- Try work through the problem first:
    - breakdown the problem (Data 140 mixed opener + CS88 highlighting words)
    - define a conceptual approach
    - implement (conceptual then TDD testing for edgecases)
    - adjust & debug

- Prompt AI to breakdown problem when u need help --> try to solve with it
- If you really don't get it, ask for answer --> it can be something you would've never thought of if you're tackling a problem you have no foundation for (no conceptual or no knowledge library)