# Python Algorithms: Grids, Trees, and Graph Search

A curated collection of CS 231 coursework by **[Jialu Sun](https://github.com/j334sun)**. These exercises demonstrate Python programming, data-structure traversal, recursive search, and checking results on small examples.

## Start here

| Exercise | What it does | Skill demonstrated |
| --- | --- | --- |
| [Grid search](numlocations.py) | Counts occurrences of an item in a grid | Traversal and indexing |
| [Ancestor colours](ancestorcolours.py) | Collects node colours while following parents to a tree's root | Tree navigation and iterative reasoning |
| [Exhaustive cluster search](clusterexhaustive.py) | Finds the minimum total edge weight of a complete subgraph of a requested size | Combinations, exhaustive search, and feasibility checks |
| [Maximum-cluster search](clusterbacktrack.py) | Recursively searches vertex subsets for a largest complete subgraph | Recursive state and combinatorial search |
| [Python warm-up](sumofthree.py) | Adds two fixed constants to an input | Basic function contracts and checking |

For the two graph exercises, a **cluster** means a complete subgraph, also called a clique. This is a graph-theory task, not an implementation of machine-learning clustering.

## Why these exercises matter

The exercises provide foundations for implementing and evaluating more complex computational methods: representing data, translating a problem into code, tracking recursive state, checking edge cases, and recognizing the cost of exhaustive search. They complement the statistical modelling and cross-validation in my [life-expectancy project](https://github.com/j334sun/life-expectancy-mixed-effects).

This repository contains coursework, not AI-safety research or an ML model. The transferable skills are Python implementation and algorithmic reasoning.

## Run the checks

Requires Python 3. No external packages are needed; the original course support modules are included in this private archive.

```bash
python3 run_checks.py
```

The runner executes each exercise in a separate process from the correct working directory. It detects the course checker's printed failures as well as Python errors, and exits unsuccessfully if an exercise fails. All **20 existing checks** pass after correcting one arithmetic test expectation. These examples are not a comprehensive correctness proof or a performance benchmark.

To inspect a single exercise, run it from this folder:

```bash
python3 clusterexhaustive.py
python3 clusterbacktrack.py
```

## Implementation limits

- The exhaustive search materializes all size-k combinations before checking them, so memory and runtime grow quickly.
- The recursive maximum-cluster search explores subsets without pruning an invalid partial cluster or using a size bound. It is an educational exhaustive recursive search, not an optimized clique solver.
- Tests are embedded in the exercise files and run when those modules are imported.
- One original grid check constructs a 0-by-0 grid even though the supplied Grid class documents positive dimensions. It passes with this implementation but lies outside that class's stated contract.
- Original headers contain both Spring 2024 and Spring 2025 dates; they are preserved rather than assigning an unverified common date.

## Organization and attribution

The five exercise files retain their original names. One shared copy of each course helper sits alongside them so the original imports still work. Three sample graph files are retained for the exercises and further exploration.

`graphs.py`, `trees.py`, `grids.py`, `equiv.py`, and `check.py` are **course-provided support code**, not my implementations. Their original headers remain intact. The repository is private because it includes assignment solutions and course code with no redistribution license identified in the supplied folder. Instructor solution PDFs are kept outside the repository.

See [COURSE_NOTES.md](COURSE_NOTES.md) for source-file mapping and the small preparation changes. No license is granted here for the course-provided material.
