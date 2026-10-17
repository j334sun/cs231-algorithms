# Source mapping and preparation notes

## Original exercise locations

| Original folder and file | Organized file |
| --- | --- |
| `a0/sumofthree.py` | `sumofthree.py` |
| `a1/numlocations.py` | `numlocations.py` |
| `a1/ancestorcolours.py` | `ancestorcolours.py` |
| `a1/clusterexhaustive.py` | `clusterexhaustive.py` |
| `assignment 4/clusterbacktrack.py` | `clusterbacktrack.py` |

## Changes made during portfolio preparation

- Removed the student number from source headers; retained the author's name.
- Consolidated identical copies of `graphs.py`, `equiv.py`, and `check.py` from Assignment 1 and Assignment 4.
- Used the supplied February 2022 course checker for all exercises, replacing the older warm-up copy. The warm-up uses only `check.expect`; the consolidated checker passes that exercise.
- Corrected the warm-up's expected answer from 71 to 72 for `27 + 42 + 3`, corrected its test description, and removed an unused variable. Its function was unchanged.
- Added a runner for the existing checks, a README, and `.gitignore`.
- Left all algorithm implementations and the other original checks unchanged.
- Omitted Python bytecode caches and macOS metadata.

The instructor Assignment 1 and final-assessment solution PDFs were copied into a separate local reference folder with readable names. They are not part of this GitHub repository. All original course files remain untouched.

## Ownership and scope

The five exercise headers identify Jialu Sun as their author. Helper modules carry CS 231 course-download headers and retain that attribution. The sample graph files are course materials retained from the original folder. This private archive makes no claim of authorship or redistribution rights over those materials.

These exercises support a portfolio's programming foundations. They do not demonstrate a completed AI-safety research project. Possible future extensions, not implemented here, include search pruning, performance measurements, broader property checks, and a separate model-evaluation project.
